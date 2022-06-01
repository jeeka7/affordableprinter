import streamlit as st
import pandas as pd
import random

scoredict = {
  "Player":0,"Computer":0,
}
def listToString(s): 
    
    str1 = " " 
    
    return (str1.join(s))
  
if st.button("Rock"):
  Computerguess = random.sample(["Scissors","Paper"],1)
  st.write(type(listToString(Computerguess)))
  st.write(Computerguess)
  st.write('Computer used {}'.format(Computerguess))
  if Computerguess
scoredf = pd.DataFrame(scoredict,index=[0])
st.write(scoredf)
