import streamlit as st
import pandas as pd

scoredict = {
  "Player":0,"Computer":0,
}
scoredf = pd.DataFrame(scoredict)
st.write(scoredf)
