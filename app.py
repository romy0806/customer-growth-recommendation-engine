import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Customer Growth Recommendation Assistant",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("recommendation_bundle.csv")

recommendation_bundle = load_data()

st.title("🛍️ Customer Growth Recommendation Assistant")

st.markdown(
    """
    Use this app to generate **next-best product recommendations**, estimate 
    **incremental revenue opportunity**, and identify potential cross-sell actions.
    """
)

st.divider()

# Sidebar
st.sidebar.header("Recommendation Input")

product_list = sorted(recommendation_bundle["Product_A"].dropna().unique())

selected_product = st.sidebar.selectbox(
    "Select purchased product",
    product_list
)

rec = recommendation_bundle[
    recommendation_bundle["Product_A"] == selected_product
]

if not rec.empty:
    row = rec.iloc[0]

    st.subheader("Purchased Product")
    st.markdown(f"### **{row['Product_A']}**")

    st.divider()

    # KPI row
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Co-Purchase Count",
        f"{int(row['Total_CoPurchase_Count']):,}"
    )

    col2.metric(
        "Estimated Revenue Opportunity",
        f"£{row['Total_Incremental_Revenue_Potential']:,.0f}"
    )

    col3.metric(
        "Recommendations Generated",
        "3"
    )

    st.divider()

    st.subheader("Next Best Product Recommendations")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown("#### Recommendation 1")
        st.success(row["Recommendation_1"])

    with r2:
        st.markdown("#### Recommendation 2")
        st.success(row["Recommendation_2"])

    with r3:
        st.markdown("#### Recommendation 3")
        st.success(row["Recommendation_3"])

    st.divider()

    st.subheader("Business Recommendation")

    st.markdown(
        f"""
        Customers who purchased **{row['Product_A']}** also frequently purchased 
        **{row['Recommendation_1']}**, **{row['Recommendation_2']}**, and 
        **{row['Recommendation_3']}**.

        This indicates a strong cross-sell opportunity. These recommendations can be used for:
        
        - Website product recommendations
        - Checkout cross-sell suggestions
        - Personalized coupons
        - Targeted email campaigns
        - Bundle promotions
        """
    )

    st.info(
        f"Estimated incremental revenue opportunity: "
        f"£{row['Total_Incremental_Revenue_Potential']:,.0f}"
    )

else:
    st.warning("No recommendation available for this product.")