import streamlit
streamlit.title('My parents healthy dinner')
streamlit.header('Breakfast Favourties')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥙 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.header('🍹🍌🍊🍉 Build your own fruit smoothies 🥭🍎🍇🥤')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
my_fruit_selected=streamlit.multiselect("Pick Fruits You Like :",list(my_fruit_list.index),['Avocado','Strawberries'])
##streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[my_fruit_selected]
streamlit.dataframe[fruits_to_show]
                    
