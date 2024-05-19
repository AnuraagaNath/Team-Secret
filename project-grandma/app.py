# @Team Secret: Anuraaga Nath


import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

GEMINI_API_KEY = st.secrets['GEMINI_API_KEY']

genai.configure(api_key=GEMINI_API_KEY)

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

# Set up the model
generation_config = {
  "temperature": 0.95,
  "top_p": 0.95
}

st.set_page_config(page_title='project-grandma', page_icon='download.jpeg')

def get_story(prompt):
    model = genai.GenerativeModel(model_name='gemini-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    response = model.generate_content(prompt)   
    return response.text


st.header('Hello Grandma!')

st.text('Tell us some stories')

prompt = "You are a grandmother telling stories to her grandchildren. Tell them stories based on their desire. The topic is given at the end after the \"&\" sign. Make it sound more human and greet grandchildren more in between the stories. Sound like \'first person\' to telling the story and no intermediate conversations or drama sequence included. Make the vocabulary as easy as understandable by 6th grade. & "

input = st.text_input("Enter your topic here: ")

submit = st.button("Tell me the story")

if submit:
    response = get_story(prompt+input)
    st.write(response)