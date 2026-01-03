import streamlit as st
import pandas as pd
from apyori import apriori

st.title("🛒 Apriori Association Rule Miner")

uploaded_file = st.file_uploader("Upload your Groceries CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    cust_level = df[['Member_number','itemDescription']].sort_values(by="Member_number")
    cust_level['itemDescription'] = cust_level['itemDescription'].str.strip()
    transactions = [a[1]['itemDescription'].tolist() for a in list(cust_level.groupby(["Member_number"]))]

    min_support = st.slider("Minimum Support", 0.01, 0.1, 0.02)
    min_confidence = st.slider("Minimum Confidence", 0.1, 1.0, 0.3)
    min_lift = st.slider("Minimum Lift", 1.0, 5.0, 1.2)

    if st.button("Run Apriori"):
        rules = apriori(transactions=transactions,
                        min_support=min_support,
                        min_confidence=min_confidence,
                        min_lift=min_lift,
                        min_length=2)
        results = list(rules)

        lhs, rhs, supports, confidences, lifts = [], [], [], [], []
        for result in results:
            for ordered_stat in result[2]:
                lhs.append(tuple(ordered_stat[0])[0] if ordered_stat[0] else '')
                rhs.append(tuple(ordered_stat[1])[0] if ordered_stat[1] else '')
                supports.append(result[1])
                confidences.append(ordered_stat[2])
                lifts.append(ordered_stat[3])

        df_rules = pd.DataFrame({
            'Left Hand Side': lhs,
            'Right Hand Side': rhs,
            'Support': supports,
            'Confidence': confidences,
            'Lift': lifts
        })

        st.write("### Top Rules by Confidence", df_rules.nlargest(10, 'Confidence'))
        st.bar_chart(df_rules.nlargest(10, 'Confidence')[['Confidence']])
