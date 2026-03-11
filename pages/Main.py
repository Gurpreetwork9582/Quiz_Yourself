import streamlit as st
import pandas as pd
import time
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
                        self.df = self.df.reset_index(drop=True)
                    except Exception:
                        # fallback to common options
                        self.df = pd.read_csv(self.uploaded, encoding="ISO-8859-1", sep=";")
                        self.df = self.df.reset_index(drop=True)
                else:
                    # treat as Excel workbook
                   self.df = pd.read_excel(self.uploaded)
                   self.df = self.df.reset_index(drop=True)
            except Exception as e:
                st.error(f"Could not read the file: {e}")
            else:
                st.data_editor(self.df)
                return self.df

    @st.dialog("Come Back agaain!")
    def modal_dialog(self):
        st.write("Quiz completed! 🎉")

    

        
    def Game_name(self):
        #self.df =  #Calling function from Upload Class in Upload_Question File 
            self.df = self.Upload_Files()# made it a Panda Series so taking value in the first row only for now
            st.header("Questions",text_alignment="center")
           
            if self.df is not None:
                   
                     

                        if "Number" not in st.session_state:
                            st.session_state.Number =0               

                        # Prevent going outside dataframe
                        if st.session_state.Number >= len(self.df):
                            st.success("Quiz Finished!")
                            self.modal_dialog()
                            st.session_state.Number = 0
                            st.rerun()
                            
                        st.subheader(f"{self.df.loc[st.session_state.Number,'question']}", text_alignment="center")#getting Value in from Question by calling the column name
                        
                        a, b =st.columns(2)
                        c , d =st.columns(2)
                        
                        
                        self.a_click=a.button(f"{self.df.loc[st.session_state.Number,'option A']}",width="stretch",key=f"A") #getting Value in from Option A by calling the column name
                        self.b_click=b.button(f"{self.df.loc[st.session_state.Number,'option B']}",width="stretch",key=f"B") #getting Value in from Option B by calling the column name
                        self.c_click=c.button(f"{self.df.loc[st.session_state.Number,'option C']}",width="stretch",key=f"C") #getting Value in from Option C by calling the column name
                        self.d_click=d.button(f"{self.df.loc[st.session_state.Number,'option D']}",width="stretch",key=f"D") #getting Value in from Option D by calling the column name
                    
                        self.correct = self.df.loc[st.session_state.Number,"answer"]

                        if self.a_click:
                            if self.correct == "A":
                                st.success("Thats Correct")
                                st.session_state.Number +=1
                                
                            else:
                                st.error("Not Correct")
                        elif self.b_click:
                            if self.correct == "B":
                    
                                st.session_state.Number +=1
                
                            else:
                                st.error("Not Correct")
                        elif self.c_click:
                            if self.correct == "C":
                                st.success("Thats Correct")
                                st.session_state.Number +=1
                            else:
                                st.error("Not Correct")
                        elif self.d_click:
                            if self.correct == "D":
                                st.success("Thats Correct")
                                st.session_state.Number +=1
                            else:
                                st.error("Not Correct")


                        with st.container(horizontal= True, horizontal_alignment="distribute"):
                            if st.button("Back",icon_position="left",width="content",help="Move to the Previous question"):
                                st.session_state.Number = max(0, st.session_state.Number - 1)
                                
                            if st.button("forward",icon_position="right",width="content",help="Move to the next question"):
                                st.session_state.Number +=1
                                
                        
            
                 
                            
                            
g1 = Game()
g1.Game_name()