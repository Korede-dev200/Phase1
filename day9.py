import streamlit as st
import pandas as pd

st.title("Book Data Dashboard")

df = pd.read_csv(("books_cleaned.csv"))
st.dataframe(df)

subjects = st.selectbox("Filter by price range", ["All", "Under £30", "£30-£50", "Over £50"])


if subjects == "Under £30":
    filtered = df[df["Price"] < 30]
elif subjects == "£30-£50":
    filtered = df[(df["Price"] >= 30) & (df["Price"] <= 50)]
elif subjects == "Over £50":
    filtered = df[df["Price"] > 50]
else:
    filtered = df

st.dataframe(filtered)
st.bar_chart(filtered.set_index("Title")["Price"])

df.to_csv("dashboard_source.csv", index=False)    # optional - just marks this as your final dashboard dataset