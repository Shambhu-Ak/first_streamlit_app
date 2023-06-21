import streamlit
import pandas
streamlit.title('my parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry oatmel')
streamlit.text(' 🥗 Kale, spinach& rocket smoothie')
streamlit.text(' 🐔 Hard boiled free-range egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
