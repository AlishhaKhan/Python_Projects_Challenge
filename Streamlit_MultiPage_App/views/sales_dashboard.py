import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Title ---
st.title("📊Sales Dashboard")
st.write("Analyze sales performance, track revenue, and gain business insights.")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("assets/sales_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Data")
region = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())
product = st.sidebar.multiselect("Select Product", options=df["Product"].unique(), default=df["Product"].unique())

filtered_df = df[(df["Region"].isin(region)) & (df["Product"].isin(product))]

# --- KPIs ---
total_sales = filtered_df["Sales"].sum()
total_units = filtered_df["Units"].sum()
avg_price = round(filtered_df["Sales"].sum() / filtered_df["Units"].sum(), 2)

st.metric("💰 Total Sales", f"${total_sales:,.2f}")
st.metric("📦 Units Sold", f"{total_units}")
st.metric("💲 Average Price", f"${avg_price}")

# --- Sales Over Time ---
sales_by_date = filtered_df.groupby("Date")["Sales"].sum().reset_index()
fig1 = px.line(sales_by_date, x="Date", y="Sales", title="Sales Over Time", markers=True)
st.plotly_chart(fig1, use_container_width=True)

# --- Sales by Region ---
sales_by_region = filtered_df.groupby("Region")["Sales"].sum().reset_index()
fig2 = px.bar(sales_by_region, x="Region", y="Sales", title="Sales by Region", color="Region")
st.plotly_chart(fig2, use_container_width=True)

# --- Sales by Product ---
sales_by_product = filtered_df.groupby("Product")["Sales"].sum().reset_index()
fig3 = px.pie(sales_by_product, names="Product", values="Sales", title="Sales Distribution by Product")
st.plotly_chart(fig3, use_container_width=True)
