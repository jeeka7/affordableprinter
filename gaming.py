import streamlit as st
import pandas as pd
import random


if "player" not in st.session_state:
  st.session_state.player = 0
if "computer" not in st.session_state:
  st.session_state.computer = 0

def AddPlayer():
 st.session_state.player += 1
def AddComputer():
 st.session_state.computer += 1 
  
if st.button("Rock"):
  Computerguess = random.choice(('Scissors','Paper'))

  st.write('Computer used {}'.format(Computerguess))
  if (Computerguess == "Scissors"):
    AddPlayer()
  else:
    AddComputer()
st.write('Player score is {}'.format(player))
st.write('Computer score is {}'.format(computer))

