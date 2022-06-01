import streamlit as st
import pandas as pd
import random

scoredict = {
  "Player":0,"Computer":0,
}

if st.button("Rock"):
  Computerguess = random.sample(["Scissors","Paper"],1)
  st.write("Computer guess is",Computerguess)
  st.write(type(Computerguess))

scoredf = pd.DataFrame(scoredict,index=[0])
st.write(scoredf)
