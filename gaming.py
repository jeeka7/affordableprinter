import streamlit as st
import pandas as pd
import random


if "player" not in st.session_state:
  st.session_state.player = 0
st.write(st.session_state.player)
st.metric(label="YOU", value=player, delta=None, delta_color="normal")
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
    if st.button("Paper"):
      Computerguess = random.choice(('Rock','Scissor'))

      st.write('Computer used {}'.format(Computerguess))
      if (Computerguess == "Rock"):
        AddPlayer()
      else:
        AddComputer()
with col3:
    if st.button("Scissors"):
      Computerguess = random.choice(('Rock','Paper'))

      st.write('Computer used {}'.format(Computerguess))
      if (Computerguess == "Paper"):
        AddPlayer()
      else:
        AddComputer()

