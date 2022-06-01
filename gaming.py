import streamlit as st
import pandas as pd
import random

if "scoredict" not in st.session_state:
  st.session_state.scoredict["Player"] = 0
  st.session_state.scoredict["Computer"] = 0
scoredict={
"Player":0,"Computer":0
}


def AddPlayer():
 st.session_state.scoredict["Player"] += 1
def AddComputer():
 st.session_state.scoredict["Computer"] += 1 
  
if st.button("Rock"):
  Computerguess = random.choice(('Scissors','Paper'))

  st.write('Computer used {}'.format(Computerguess))
  if (Computerguess == "Scissors"):
    AddPlayer()
  else:
    AddComputer()
scoredf = pd.DataFrame(scoredict,index=[0])
st.write(scoredf)
