import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))




class Game: 
    def __init__(self):
       # self.Data = Upload() #Class init of Upload from Upload_Question File
        pass

    def Upload_Files(self):
        # let the user upload either a CSV or an Excel workbook
        self.file_types = ["csv", "xlsx", "xls"]
        self.uploaded = st.file_uploader("Upload questionnaire file", type=self.file_types)

        if self.uploaded is not None:
            try:
                self.name = self.uploaded.name.lower()
                if self.name.endswith(".csv"):
                    # try to infer delimiter and encoding
                    try:
                        self.df = pd.read_csv(self.uploaded, sep=None, engine="python")
                    except Exception:
                        # fallback to common options
                        self.df = pd.read_csv(self.uploaded, encoding="ISO-8859-1", sep=";")
                else:
                    # treat as Excel workbook
                   self.df = pd.read_excel(self.uploaded)
            except Exception as e:
                st.error(f"Could not read the file: {e}")
            else:
                st.data_editor(self.df)
                return self.df




    def Game_name(self):
        #self.df =  #Calling function from Upload Class in Upload_Question File 
            self.df = self.Upload_Files() # made it a Panda Series so taking value in the first row only for now
            if self.df is not None:
                self.row = self.df.iloc[0]
                st.title(f"",text_alignment="center")

                st.header("Questions",text_alignment="center")

                st.subheader(f"{self.row['question']}", text_alignment="center")#getting Value in from Question by calling the column name

                a, b =st.columns(2)
                c , d =st.columns(2)
                
                
                a.button(f"{self.row['option A']}",width="stretch") #getting Value in from Option A by calling the column name
                b.button(f"{self.row['option B']}",width="stretch") #getting Value in from Option B by calling the column name
                c.button(f"{self.row['option C']}",width="stretch") #getting Value in from Option C by calling the column name
                d.button(f"{self.row['option D']}",width="stretch") #getting Value in from Option D by calling the column name
            

            if st.button():
                st.success("Thats Correct")

g1 = Game()
g1.Game_name()