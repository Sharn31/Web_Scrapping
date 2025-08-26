import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("books_data.csv")

# Clean price column (remove £ if present and convert to float)
df["price"] = df["price"].astype(str).str.replace("£", "", regex=False)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

st.title("📚 Book Price Tracker")
st.write("Track book prices from BooksToScrape.com")

# Book selection
book_choice = st.selectbox("Choose a Book", df["title"].unique())
filtered = df[df["title"] == book_choice]

st.write("### Selected Book Details")
st.dataframe(filtered)

# 📊 Bar Chart - Average price per rating
st.write("### Average Price by Rating")
st.bar_chart(df.groupby("rating")["price"].mean())
