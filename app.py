import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import sys, os
sys.path.append(os.path.dirname(__file__))
from utils.data_loader import load_salary_data
from modules.linear_algebra import vector_operations, matrix_operations
from modules.calculus import derivative_example, gradient_descent_example
from modules.probability_stats import gaussian_example, expectation_variance
from modules.optimization import gradient_descent, regularization_example
from sklearn.linear_model import LinearRegression

st.title("AI/ML Math Foundation with Real Data")

# Load Dataset
df = load_salary_data()
st.subheader("Salary Dataset")
st.dataframe(df)

# Exploratory Data Analysis
st.subheader("EDA")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="YearsExperience", y="Salary", ax=ax)
st.pyplot(fig)

# Linear Regression Example
st.subheader("Linear Regression")
X = df[["YearsExperience"]]
y = df["Salary"]
model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)
st.write("Regression Coefficient:", model.coef_[0])
st.write("Regression Intercept:", model.intercept_)

fig2, ax2 = plt.subplots()
ax2.scatter(X, y, color='blue')
ax2.plot(X, pred, color='red')
st.pyplot(fig2)

# Math Demonstrations
st.subheader("Math Demonstrations")

st.write("**Vector Operations:**", vector_operations())
st.write("**Matrix Operations:**", matrix_operations())
st.write("**Derivative Example:**", derivative_example())
st.write("**Gradient Descent Example:**", gradient_descent_example())
x_vals, pdf_vals = gaussian_example()
st.line_chart(pd.DataFrame({"x": x_vals, "pdf": pdf_vals}))
st.write("**Gradient Descent Optimization Result:**", gradient_descent())
st.write("**Regularization Example:**", regularization_example(pd.Series([1.0, 2.0, 3.0])))
