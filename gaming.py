import streamlit as st
import pandas as pd
import random


if "computer" not in st.session_state:
  st.session_state.computer = 0
if "player" not in st.session_state:
  st.session_state.player = 0
if "x" not in st.session_state:
  st.session_state.x = 0
if "y" not in st.session_state:
  st.session_state.y = 0
cl1, cl2 = st.columns(2)

with cl1:
  st.metric(label="You", value=st.session_state.player, delta=st.session_state.x, delta_color="normal")

with cl2:
  st.metric(label="Computer", value=st.session_state.computer, delta=st.session_state.y, delta_color="normal")


def AddPlayer():
 st.session_state.player += 1
 st.session_state.x = 1
 st.session_state.y = 0
def AddComputer():
 st.session_state.computer += 1
 st.session_state.x = 0
 st.session_state.y = 1

st.write("Choose from 3 weapons to play against Computer AI")
st.write("********RULES OF THE GAME*********")
st.write("Rock is strong against Scissors but weak against Paper")
st.write("Paper is strong against Rock but weak against Scissors")
st.write("Scissors is strong against Paper but weak against Rock")

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

        
if st.button("Reset Score"):
  st.session_state.player = 0
  st.session_state.computer = 0

if st.button("Finish Game"):
  if ( st.session_state.player > st.session_state.computer ):
   st.write("YOU WON !! :)")
  elif(st.session_state.player < st.session_state.computer):
   st.write("YOU Lost !! :(")
  else:
   st.write("It is a Draw")
  
arr = [st.session_state.player,st.session_state.computer]

