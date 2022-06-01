import streamlit as st
import pandas as pd
import random


if "player" not in st.session_state:
  st.session_state.player = 0
st.write(st.session_state.player)
if "computer" not in st.session_state:
  st.session_state.computer = 0
st.write(st.session_state.computer)

if st.button("Reset Score"):
  st.session_state.player = 0
  st.session_state.computer = 0

def AddPlayer():
 st.session_state.player += 1
def AddComputer():
 st.session_state.computer += 1 


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Rock"):
      Computerguess = random.choice(('Scissors','Paper'))

  st.write('Computer used {}'.format(Computerguess))
  if (Computerguess == "Scissors"):
    AddPlayer()
  else:
    AddComputer()

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


