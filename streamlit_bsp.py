# streamlit beispiel

# streamlit in positron


# !uv pip install streamlit
# !uv pip install plotly.express
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



st.set_page_config(page_title="Umfrage Demo", layout="wide")
st.title("Streamlit Schnellbeispiel")
st.caption("Läuft in Positron über den Data-App-Play-Button oder `streamlit run streamlit_bsp.py`")

np.random.seed(42)
gruppen = ["18-25", "26-35", "36-50", "51+"]
n = 200
df = pd.DataFrame({
    "Altersgruppe": np.random.choice(gruppen, n),
    "Zufriedenheit": np.random.randint(1, 8, n),
    "Nutzungsdauer_Monate": np.random.randint(1, 36, n),
})

min_zufriedenheit = st.slider("Minimale Zufriedenheit", 1, 7, 1)
gefiltert = df[df["Zufriedenheit"] >= min_zufriedenheit]

col1, col2 = st.columns(2)
with col1:
    st.metric("Anzaaaahl Antworten", len(gefiltert))
    st.dataframe(gefiltert.head(10))

with col2:
    fig = px.scatter(
        gefiltert,
        x="Nutzungsdauer_Monate",
        y="Zufriedenheit",
        color="Altersgruppe",
        title="Zufriedenheit vs. Nutzungsdauer",
    )
    st.plotly_chart(fig, width="stretch")

##################################
# im terminal ausführen mit:
# streamlit run streamlit_bsp.py --server.runOnSave true
