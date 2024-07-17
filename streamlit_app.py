# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Streamlit App :balloon:")

name_on_order = st.text_input("name on smoothie")
st.write("name on smoothie will be :",name_on_order)
cnx=st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
INGREDIENT_LIST = st.multiselect('choose upto 5 ingredients:',my_dataframe,max_selections =5)
if INGREDIENT_LIST :
    # st.write(INGREDIENT_LIST)
    # st.text(INGREDIENT_LIST)

    ingredient_string =''
    for fruit in INGREDIENT_LIST :
        ingredient_string +=fruit  + ' '
    # st.write(ingredient_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredient_string + """','""" + name_on_order + """')"""
    

    st.write(my_insert_stmt)
    time_tp_insert = st.button("Submit order")
    
    if time_tp_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())
fv_Df= st.dataframe(data=fruityvice_response.json(),use_container_Width=True)

        


    























