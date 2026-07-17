import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="TourismPulse",
    page_icon="🌍",
    layout="wide"
)


@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/cleaned_tourism_data.csv"
    )


data = load_data()


st.title("🌍 TourismPulse")
st.subheader("Travel Analytics Engine")

st.write(
    "Understand destinations through tourism data and analytics."
)


st.sidebar.title("TourismPulse")

page = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Overview",
        "Seasonal Analysis",
        "Peak Travel Analysis",
        "Visitor Preferences",
        "Destination Popularity",
        "Demand Forecast",
        "Destination Comparison",
        "Emerging Hotspots"
    ]
)


if page == "Overview":

    st.header("Tourism Overview")

    total_tourists = data["total_tourists"].sum()
    domestic_tourists = data["domestic_tourists"].sum()
    foreign_tourists = data["foreign_tourists"].sum()

    total_revenue = data[
        "tourism_revenue_inr_crore"
    ].sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Tourists",
        f"{total_tourists / 1_000_000:.2f} M"
    )

    col2.metric(
        "Domestic Tourists",
        f"{domestic_tourists / 1_000_000:.2f} M"
    )

    col3.metric(
        "Foreign Tourists",
        f"{foreign_tourists / 1_000_000:.2f} M"
    )

    col4.metric(
        "Tourism Revenue",
        f"₹{total_revenue:,.2f} Cr"
    )

    st.subheader("Top Tourist Destinations")

    top_states = (
        data.groupby("state")["total_tourists"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_states)


elif page == "Seasonal Analysis":

    st.header("Seasonal Visitor Analysis")

    seasonal_data = (
        data.groupby("season")[
            [
                "domestic_tourists",
                "foreign_tourists",
                "total_tourists"
            ]
        ]
        .sum()
    )

    st.dataframe(
        seasonal_data,
        use_container_width=True
    )

    st.subheader("Tourists Across Seasons")

    st.bar_chart(
        seasonal_data["total_tourists"]
    )

    popular_season = (
        seasonal_data["total_tourists"].idxmax()
    )

    lowest_season = (
        seasonal_data["total_tourists"].idxmin()
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Most Popular Season",
        popular_season
    )

    col2.metric(
        "Lowest Visitor Season",
        lowest_season
    )


elif page == "Peak Travel Analysis":

    st.header("Peak and Off-Peak Travel Analysis")

    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    monthly_data = (
        data.groupby("month")["total_tourists"]
        .sum()
        .reindex(month_order)
    )

    st.subheader("Monthly Tourist Trend")

    st.line_chart(monthly_data)

    peak_month = monthly_data.idxmax()
    offpeak_month = monthly_data.idxmin()

    col1, col2 = st.columns(2)

    col1.metric(
        "Peak Travel