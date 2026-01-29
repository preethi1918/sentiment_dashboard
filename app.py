import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Market Trends & Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f4f7fb;
}
.kpi-card {
    padding: 20px;
    border-radius: 16px;
    color: white;
    font-weight: bold;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}
.blue {background: linear-gradient(135deg, #4facfe, #00f2fe);}
.green {background: linear-gradient(135deg, #43e97b, #38f9d7);}
.red {background: linear-gradient(135deg, #fa709a, #fee140);}
.purple {background: linear-gradient(135deg, #667eea, #764ba2);}
.orange {background: linear-gradient(135deg, #f7971e, #ffd200);}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📈 Market Dashboard")
st.sidebar.markdown("AI-powered insights")
menu = st.sidebar.radio(
    "Navigation",
    ["Overview", "Market Trends", "Sentiment Analysis", "Reports"]
)

st.sidebar.markdown("---")
st.sidebar.write("📅 Year: 2024")

# ---------------- TITLE ----------------
st.title("📊 Market Trends & Consumer Sentiment Analysis")
st.caption("Real-time insights on market movement and customer emotions")

# ---------------- KPI SECTION ----------------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("<div class='kpi-card blue'>📈<br>Market Trend Score<br><h2>82</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='kpi-card green'>😊<br>Positive Sentiment<br><h2>68%</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='kpi-card orange'>😐<br>Neutral Sentiment<br><h2>20%</h2></div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='kpi-card red'>😠<br>Negative Sentiment<br><h2>12%</h2></div>", unsafe_allow_html=True)

with col5:
    st.markdown("<div class='kpi-card purple'>🔥<br>Trending Products<br><h2>24</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- CHART DATA ----------------
sentiment_df = pd.DataFrame({
    "Sentiment": ["Positive", "Neutral", "Negative"],
    "Value": [68, 20, 12]
})

trend_df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Trend Score": [60, 65, 70, 75, 80, 82]
})

product_df = pd.DataFrame({
    "Product": ["iPhone 15", "Samsung S24", "OnePlus 12", "Pixel 8", "Nothing Phone"],
    "Sentiment Score": [87, 82, 78, 74, 69]
})

# ---------------- VISUALIZATION ROW 1 ----------------
c1, c2 = st.columns(2)

with c1:
    st.subheader("💬 Sentiment Distribution")
    pie = px.pie(
        sentiment_df,
        names="Sentiment",
        values="Value",
        color="Sentiment",
        color_discrete_map={
            "Positive": "#2ecc71",
            "Neutral": "#f1c40f",
            "Negative": "#e74c3c"
        },
        hole=0.4
    )
    st.plotly_chart(pie, use_container_width=True)

with c2:
    st.subheader("📈 Market Trend Over Time")
    line = px.area(
        trend_df,
        x="Month",
        y="Trend Score",
        markers=True,
        color_discrete_sequence=["#667eea"]
    )
    st.plotly_chart(line, use_container_width=True)

# ---------------- VISUALIZATION ROW 2 ----------------
c3, c4 = st.columns(2)

with c3:
    st.subheader("🏆 Top Products by Sentiment")
    bar = px.bar(
        product_df,
        x="Sentiment Score",
        y="Product",
        orientation="h",
        color="Sentiment Score",
        color_continuous_scale="greens"
    )
    st.plotly_chart(bar, use_container_width=True)

with c4:
    st.subheader("🗣️ Recent Customer Feedback")
    st.success("✔️ Delivery was super fast and smooth!")
    st.warning("⚠️ UI is good but payment page is confusing.")
    st.error("❌ Refund process took too long.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2024 AI Market Intelligence Dashboard")
# ---------------- CSV UPLOAD ----------------
st.sidebar.markdown("### Upload Your CSV Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("✅ File uploaded successfully!")
        st.write("Preview of your CSV data:")
        st.dataframe(df.head())

        # Example: dynamically use CSV if it has specific columns
        if {"Sentiment", "Value"}.issubset(df.columns):
            sentiment_df = df[["Sentiment", "Value"]]
        if {"Month", "Trend Score"}.issubset(df.columns):
            trend_df = df[["Month", "Trend Score"]]
        if {"Product", "Sentiment Score"}.issubset(df.columns):
            product_df = df[["Product", "Sentiment Score"]]

    except Exception as e:
        st.sidebar.error(f"❌ Error reading CSV: {e}")
else:
    st.sidebar.info("Upload a CSV to replace the default data")
