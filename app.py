import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Rupesh | Sales Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Analytics Dashboard")
st.write("Welcome, Rupesh! Analyze sales performance with interactive insights.")

# Sample sales dataset
data = {
    "Product": [
        "Laptop", "Mobile", "Headphones", "Laptop",
        "Mobile", "Headphones", "Tablet", "Tablet",
        "Laptop", "Mobile", "Headphones", "Tablet"
    ],
    "Region": [
        "North", "South", "East", "West",
        "North", "South", "East", "West",
        "South", "East", "North", "West"
    ],
    "Sales": [
        50000, 25000, 5000, 60000,
        30000, 7000, 20000, 22000,
        55000, 28000, 6000, 18000
    ],
    "Profit": [
        8000, 4000, 1000, 10000,
        5000, 1500, 3500, 4000,
        9000, 4500, 1200, 3000
    ],
    "Month": [
        "January", "January", "January", "February",
        "February", "February", "March", "March",
        "March", "April", "April", "April"
    ]
}

df = pd.DataFrame(data)

# Upload your own sales dataset
st.sidebar.header("Upload Your Data")

uploaded_file = st.sidebar.file_uploader(
    "Upload an Excel or CSV file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        required_columns = [
            "Product", "Region", "Sales", "Profit", "Month"
        ]

        missing_columns = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing_columns:
            st.sidebar.error(
                f"Missing columns: {', '.join(missing_columns)}"
            )

            st.stop()

        st.sidebar.success("Dataset uploaded successfully!")

    except Exception as e:
        st.sidebar.error(f"Could not read the file: {e}")
        st.stop()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

products = st.sidebar.multiselect(
    "Select Product",
    options=sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

filtered_df = df[
    df["Region"].isin(regions)
    & df["Product"].isin(products)
]

# KPI metrics
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_sales:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Total Orders", total_orders)

st.divider()

# Sales by product
st.subheader("📦 Sales by Product")

product_sales = (
    filtered_df.groupby("Product", as_index=False)["Sales"]
    .sum()
)

if not product_sales.empty:
    fig_product = px.bar(
        product_sales,
        x="Product",
        y="Sales",
        color="Product",
        title="Revenue by Product",
        text_auto=True
    )
    st.plotly_chart(fig_product, use_container_width=True)
else:
    st.info("No data available for the selected filters.")

# Regional analysis
st.subheader("🌍 Regional Sales Analysis")

region_sales = (
    filtered_df.groupby("Region", as_index=False)["Sales"]
    .sum()
)

if not region_sales.empty:
    fig_region = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        hole=0.45,
        title="Revenue Distribution by Region"
    )
    st.plotly_chart(fig_region, use_container_width=True)
else:
    st.info("No regional data available.")

# Monthly sales trend
st.subheader("📈 Monthly Sales Trend")

month_order = ["January", "February", "March", "April"]

monthly_sales = (
    filtered_df.groupby("Month")["Sales"]
    .sum()
    .reindex(month_order, fill_value=0)
    .reset_index()
)

if not filtered_df.empty:
    fig_monthly = px.line(
        monthly_sales,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Revenue Trend"
    )
    st.plotly_chart(fig_monthly, use_container_width=True)

# Data table
st.subheader("📋 Sales Records")
st.dataframe(filtered_df, use_container_width=True)

# Download filtered data
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv_data,
    file_name="rupesh_sales_data.csv",
    mime="text/csv"
)

st.success("Dashboard loaded successfully!")