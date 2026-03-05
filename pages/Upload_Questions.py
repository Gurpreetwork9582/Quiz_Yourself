import streamlit as st
import pandas as pd

class Upload:
    def __init__(self):
        pass

    def Upload_Files(self):
# let the user upload either a CSV or an Excel workbook
        self.file_types = ["csv", "xlsx", "xls"]
        self.uploaded = st.file_uploader("Upload questionnaire file", type=self.file_types)

        if self.uploaded is not None:
            try:
                name = self.uploaded.name.lower()
                if name.endswith(".csv"):
                    # try to infer delimiter and encoding
                    try:
                        df = pd.read_csv(self.uploaded, sep=None, engine="python")
                    except Exception:
                        # fallback to common options
                        df = pd.read_csv(self.uploaded, encoding="ISO-8859-1", sep=";")
                else:
                    # treat as Excel workbook
                    df = pd.read_excel(self.uploaded)
            except Exception as e:
                st.error(f"Could not read the file: {e}")
            else:
                st.data_editor(df)
                return df


U1 =Upload()
U1.Upload_Files()