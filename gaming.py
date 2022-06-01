import streamlit as st
import pandas as pd
import random

scoredict = {
  "Player":0,"Computer":0,
}

def AddPlayer():
 scoredict["Player"] += 1 
def AddComputer():
 scoredict["Computer"] += 1 
  
if st.button("Rock"):
  Computerguess = random.choice('Scissors','Paper')
  st.write(Computerguess)
  st.write('Computer used {}'.format(Computerguess))
  if (Computerguess == "Scissors"):
    Addplayer()
  else:
    AddComputer()
scoredf = pd.DataFrame(scoredict,index=[0])
st.write(scoredf)
