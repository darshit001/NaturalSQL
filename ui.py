import streamlit as st

from langchain_DB import get_few_shot_db_chain

st.set_page_config(page_title="SQL Query Generator", page_icon="📊", layout="wide")

with st.sidebar:
    st.title("🗄️ Database Connection")
    db_user = st.text_input("Username", value="root")
    db_password = st.text_input("Password", type="password", value="Root")
    db_host = st.text_input("Host", value="localhost")
    db_name = st.text_input("Database Name", value="atliq_tshirts")
    connect_db = st.button("Connect to Database")

st.title("🔍 SQL Query Generator")
st.write("Welcome to the SQL Query Generator! Ask your question, and we'll generate the SQL query to fetch the relevant data from the database.")

question = st.text_area("Enter your question here:")

chain = None

if connect_db:
    try:
        chain = get_few_shot_db_chain(db_user, db_password, db_host, db_name)
        st.success("🌐 Connected to the database successfully!")
    except Exception as e:
        st.error(f"❌ Error connecting to the database: {e}")

if chain and question:
    try:
        response = chain.run(question)
        st.header("🔍 Answer for the given text query from DB:")
        st.header(response)
    except Exception as e:
        st.error(f"❌ Error executing the query: {e}")