import streamlit as st
import pandas as pd

@st.cache_data
def load_and_modify_data(url):
    lm_df = pd.read_csv(url, encoding="latin-1")
    # rovaniemi_df["vuosi"] = rovaniemi_df["Kuukausi"].str.split("M")[0]
    lm_df[["Vuosi", "Kuukausinumero"]] = lm_df["Kuukausi"].str.split("M", expand=True)
    return lm_df

rovaniemi_df = load_and_modify_data("https://pxdata.stat.fi/PxWeb/sq/b3a8bb82-5d4c-431c-b7c3-710dec0c1b44")

# Load one municipality via saved-query CSV URL (PxWeb).
# Show a data table for that municipality.
st.dataframe(rovaniemi_df)

# Simple overall trend (line chart) for a chosen metric.
huone_aste_roi_df = rovaniemi_df[["Kuukausi", "Huonekäyttöaste, % Rovaniemi"]]
# st.dataframe(huone_aste_roi_df)
st.line_chart(huone_aste_roi_df, x="Kuukausi", y="Huonekäyttöaste, % Rovaniemi")

# Yearly totals (bar chart) for nights spent.
# "Yöpymiset, lkm Rovaniemi"
vuosi_yo_roi_df = rovaniemi_df[["Vuosi", "Yöpymiset, lkm Rovaniemi"]].groupby(by="Vuosi").sum()
# st.dataframe(vuosi_yo_roi_df)
# st.bar_chart(vuosi_yo_roi_df, x="Vuosi", y="Yöpymiset, lkm Rovaniemi")
st.bar_chart(vuosi_yo_roi_df)