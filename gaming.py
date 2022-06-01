import streamlit as st
import pandas as pd

scoredict = {
  "Player":0,"Computer":0
}
scoredf = pd.DataFrame(scoredict)

score = [["Player","Computer" ],[0,0]]

st.write(score)
st.write(scoredf)
st.write(scoredict)
