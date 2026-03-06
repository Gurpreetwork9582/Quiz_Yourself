import streamlit as st
import pandas as pd

class Manual:

    def __init__(self):
        pass

    def Manual_Que(self):

        st.title("Create Quiz Question")

        #Initializing the Session to store the data in rerun
        if 'key' not in st.session_state:
            st.session_state.key = []

        # User inputs
        self.question_text = st.text_input("Enter Question")
        self.option_a = st.text_input("Option A")
        self.option_b = st.text_input("Option B")
        self.option_c = st.text_input("Option C")
        self.option_d = st.text_input("Option D")

        self._answer = st.selectbox("Correct Answer",["A", "B", "C", "D"])

        if st.button("Save Question", key="Save_button"):

            self.question = {
                "question": self.question_text,
                "option A": self.option_a,
                "option B": self.option_b,
                "option C": self.option_c,
                "option D": self.option_d,
                "answer": self._answer 
                }
            
            st.session_state.key.append(self.question)
            st.success("Question saved!")
            
            

        if st.session_state.key:
            df = pd.DataFrame(st.session_state.key)
            st.dataframe(df)
            
        st.button("Done",key="Done_key")
            
            
        if st.session_state['Done_key']:
            df = pd.DataFrame(st.session_state.key)
            csv = df.to_csv(index = False)
            st.download_button("Download you excel sheet", data=csv ,file_name= "Question_File.csv")




M1 = Manual()
M1.Manual_Que()