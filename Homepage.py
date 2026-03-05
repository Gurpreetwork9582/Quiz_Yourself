import streamlit as st


Main_Page= st.Page("pages/Main.py",title="Main Questions")
Upload_Page= st.Page("pages/Upload_Questions.py",title="Upload File")
Manual_Page = st.Page("pages/Manual_Que.py",title="Enter Question Manually")

pg =st.navigation([Main_Page,Upload_Page,Manual_Page])

pg.run()