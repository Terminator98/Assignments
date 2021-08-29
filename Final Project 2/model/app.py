import streamlit as st
import joblib
import random
import pandas as pd
import numpy as np

df = pd.read_csv('kc_house_data.csv')
model = joblib.load('model.h5')
scaler = joblib.load("scaler.h5")
price_opt = ["< 90000","90000 - 150000" , "150000 - 300000" , "> 300000"]

st.set_page_config("House price predictor","⛪",
layout="centered",initial_sidebar_state="expanded")

st.write("""
# House Price Prediction App
**You can check some of prices of houses in our dataset from the figure below with many options**
""")
st.sidebar.text("View prices in range")
check_price = st.sidebar.selectbox("",options=price_opt)

if check_price == "< 90000":
    st.line_chart(df[df['price']< 90000]['price'])
    st.write(f"There're about {len(df[df['price']< 90000]['price'])} houses in our data")
    st.write(f"The average price is {round(df.query(f'price < {90000}')['price'].mean(),2)}")

elif check_price == "90000 - 150000":
    st.line_chart(df.query(f'price >= {90000} & price < {150000}')['price'])
    st.write(f"There're about {len(df.query(f'price >= {90000} & price < {150000}')['price'])} houses in our data")
    st.write(f"The average price is {round(df.query(f'price >= {90000} & price < {150000}')['price'].mean(),2)}")

elif check_price == "150000 - 300000":
    st.line_chart(df.query(f'price >= {150000} & price < {300000}')['price'])
    st.write(f"There're about {len(df.query(f'price >= {150000} & price < {300000}')['price'])} houses in our data")
    st.write(f"The average price is {round(df.query(f'price >= {150000} & price < {300000}')['price'].mean(),2)}")

else:
    st.line_chart(df.query(f'price >= {300000}')['price'])
    st.write(f"There're about {len(df.query(f'price >= {300000}')['price'])} houses in our data")
    st.write(f"The average price is {round(df.query(f'price >= {300000}')['price'].mean(),2)}")




options = [1,2,3,4,5,6,7,8,9,"10+"]
dec = ["Yes","No"]
cond_opt = ["Poor","Not bad",'Good','Very good','Excellent']
grade_opt = ["Normal","Good","Excellent"]

bedrooms_con = st.empty()
bedrooms_con = bedrooms_con.selectbox("How many bedrooms do you have?",options)
if bedrooms_con == "10+":
    bedrooms_con = st.empty().number_input("How many bedrooms do you have?",step=1)

bathrooms = st.slider("How many bathrooms do you have ?",min_value=1,max_value=5)

area_living = st.number_input("Area of the living space in sqft",step=1)


floors = st.number_input("How many floors is your house ?",step=1)

waterfront = st.selectbox("Does it have waterfront?",options=["Yes",'No'])

view = st.slider("How good is your view ?",min_value=0,max_value=4)

cond = st.selectbox("How good is its condition ?",options=cond_opt)

grade = st.selectbox("How good is the building and its design ?",options=grade_opt)
if grade == "Normal":
    grade = random.randrange(1,3)
elif grade == "Good":
    grade = random.randrange(4,10)

else:
    grade = random.randrange(11,13)

base = st.number_input("Area of basement in sqft (0 if no basement)",step=1)

pred = st.button("Predict")


data = [bedrooms_con,bathrooms,area_living,floors,
dec.index(waterfront), view, cond_opt.index(cond), grade, base]

if pred :
    if (bathrooms == 0 or area_living == 0  or floors == 0):
        st.write("Please enter the missing values")
    else:
        data = scaler.transform([data])
        result = model.predict(data)[0]
        st.write(f"Predicted price is {round(result,2)}")


