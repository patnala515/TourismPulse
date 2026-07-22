import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TourismPulse",
    page_icon="🌍",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_tourism_data.csv")

df = load_data()

st.title("🌍 TourismPulse")
st.subheader("Travel Analytics Engine")
st.write("Understand destinations through tourism data.")

st.sidebar.title("🌍 TourismPulse")
st.sidebar.write("Travel Analytics Dashboard")
st.sidebar.markdown("---")

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

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Tourists",
        f"{df['total_tourists'].sum()/1_000_000:.2f} M"
    )

    col2.metric(
        "Domestic Tourists",
        f"{df['domestic_tourists'].sum()/1_000_000:.2f} M"
    )

    col3.metric(
        "Foreign Tourists",
        f"{df['foreign_tourists'].sum()/1_000_000:.2f} M"
    )

    col4.metric(
        "Revenue",
        f"₹{df['tourism_revenue_inr_crore'].sum()/1000:.2f}K Cr"
    )

    st.subheader("Top 10 Tourist States")

    top = (
        df.groupby("state")["total_tourists"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top)
elif page == "Seasonal Analysis":
    
    st.header("Seasonal Analysis")

    seasonal = (
        df.groupby("season")["total_tourists"]
        .sum()
        .sort_values(ascending=False)
    )

    st.dataframe(seasonal)

    st.bar_chart(seasonal)

    st.success(f"Most Popular Season: {seasonal.idxmax()}")


elif page == "Peak Travel Analysis":

    st.header("Peak and Off-Peak Travel")

    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    monthly = (
        df.groupby("month")["total_tourists"]
        .sum()
        .reindex(month_order)
    )

    st.line_chart(monthly)

    c1, c2 = st.columns(2)

    c1.metric(
        "Peak Travel Month",
        monthly.idxmax()
    )

    c2.metric(
        "Off-Peak Month",
        monthly.idxmin()
    )


elif page == "Visitor Preferences":

    st.header("Visitor Preferences")

    purpose = (
        df.groupby("purpose_of_visit")["total_tourists"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(purpose)

    st.dataframe(purpose)
elif page == "Destination Popularity":
    
    st.header("Destination Popularity")

    popularity = (
        df.groupby("state")["total_tourists"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(popularity)

    st.dataframe(popularity)


elif page == "Demand Forecast":

    st.header("Demand Forecast")

    monthly_forecast = (
        df.groupby("month")["total_tourists"]
        .mean()
    )

    st.line_chart(monthly_forecast)

    st.info("This forecast is based on the average monthly tourist count.")


elif page == "Destination Comparison":

    st.header("Destination Comparison")

    states = sorted(df["state"].unique())

    state1 = st.selectbox("Select State 1", states)

    state2 = st.selectbox(
        "Select State 2",
        states,
        index=1 if len(states) > 1 else 0
    )

    comparison = (
        df[df["state"].isin([state1, state2])]
        .groupby("state")["total_tourists"]
        .sum()
    )

    st.bar_chart(comparison)

    st.dataframe(comparison)
elif page == "Emerging Hotspots":
    
    st.header("Emerging Hotspots")

    hotspots = (
        df.groupby("state")["growth_%_approx."]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(hotspots)

    st.dataframe(
        hotspots.rename("Average Growth (%)")
    )

    st.success(
        f"Top Emerging Destination: {hotspots.idxmax()}"
    )
    

st.sidebar.markdown("---")
st.sidebar.subheader("About")
st.sidebar.write(
    "TourismPulse is a travel analytics dashboard developed using Python, Pandas, and Streamlit."
)

st.markdown("---")
st.caption("Developed by Sowmya Patnala | TourismPulse © 2026")