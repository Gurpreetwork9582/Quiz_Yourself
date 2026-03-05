import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Upload_Questions import Upload


class Game: 
    def __init__(self):
        self.Data = Upload() #Class init of Upload from Upload_Question File


    def Game_name(self):

        self.df = self.Data.Upload_Files() #Calling function from Upload Class in Upload_Question File 
        self.row = self.df.loc[1] # made it a Panda Series so taking value in the first row only for now

        st.title(f"",text_alignment="center")

        st.header("Questions",text_alignment="center")

        st.subheader(f"{self.row['question']}", text_alignment="center")#getting Value in from Question by calling the column name

        a, b =st.columns(2)
        c , d =st.columns(2)
        
        
        a.button(f"{self.row['Option A']}",width="stretch") #getting Value in from Option A by calling the column name
        b.button(f"{self.row['Option B']}",width="stretch") #getting Value in from Option B by calling the column name
        c.button(f"{self.row['Option C']}",width="stretch") #getting Value in from Option C by calling the column name
        d.button(f"{self.row['Option D']}",width="stretch") #getting Value in from Option D by calling the column name



g1 = Game()
g1.Game_name()