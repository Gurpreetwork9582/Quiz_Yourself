import streamlit as st
import pandas as pd


st.title("Create Quiz Question")

#Initializing the Session to store the data in rerun
if 'key' not in st.session_state:
    st.session_state.key = []

# User inputs
question_text = st.text_input("Enter Question")
option_a = st.text_input("Option A")
option_b = st.text_input("Option B")
option_c = st.text_input("Option C")
option_d = st.text_input("Option D")

answer = st.selectbox("Correct Answer",["A", "B", "C", "D"])

if st.button("Save Question"):

    question = {
        "question": question_text,
        "option A": option_a,
        "option B": option_b,
        "option C": option_c,
        "option D": option_d,
        "answer": answer 
        }
    
    st.session_state.key.append(question)
    st.success("Question saved!")
    

if st.session_state.key:
    df = pd.DataFrame(st.session_state.key)
    st.dataframe(df)

    
if st.button("Done"):
    df = pd.DataFrame(st.session_state.key)
    csv = df.to_csv(index = False)
    st.download_button("Download you excel sheet", data=csv ,file_name= "Question_File.csv")
