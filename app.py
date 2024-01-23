from dotenv import load_dotenv


import streamlit as st
import os 
from PIL import Image 
import io 
import PyPDF2 as pdf
import base64
import google.generativeai as genai

load_dotenv()


genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))


def get_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_setup(pdf_file):
    reader=pdf.PdfReader(pdf_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


st.set_page_config(page_title="ATS Resume Application")
st.header("Application Tracking System")
input_text=st.text_area("Job Description: ",key="input")
pdf_file=st.file_uploader("Upload your resume(Only PDF Format)...",type=["pdf"])


if pdf_file is not None:
    st.write('PDF File Uploaded Successfully')



submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("Percentage match")

submit3 = st.button("How Can I Improvise my Resume and skills")

submit4 = st.button('what are the keywords that are Missing in the Resume')
                    



input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt3 = """
As a skilled ATS (Applicant Tracking System) scanner with expertise in data science and ATS functionality, 
your task is to provide insights on how to improve a resume. What suggestions do you have for enhancing my resume?
"""

input_prompt4 = """
As a Technical Human Resource Manager, you are responsible for optimizing candidate resumes to match job requirements. 
Your task is to identify and provide insights on the keywords that are missing in the provided resume. 
Highlight the crucial terms or skills that are essential for the specified job role but are not adequately represented in the candidate's resume.
"""


if submit1:
    if pdf_file is not None:
        pdf_content=input_setup(pdf_file)
        response=get_response(input_prompt1)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if pdf_file is not None:
        pdf_content=input_setup(pdf_file)
        response=get_response(input_prompt2)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")


elif submit3:
    if pdf_file is not None:
        pdf_content=input_setup(pdf_file)
        response=get_response(input_prompt3)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")


elif submit4:
    if pdf_file is not None:
        pdf_content=input_setup(pdf_file)
        response=get_response(input_prompt4)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")





