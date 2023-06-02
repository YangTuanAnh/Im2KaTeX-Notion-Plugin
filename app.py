import streamlit as st
import requests, json, os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('NOTION_KEY')
headers = {
    "Authorization": "Bearer " + key,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def uploadKaTeX(pageID, equation):
    updateUrl = f"https://api.notion.com/v1/blocks/{pageID}/children"
    updateData = {
        "children": [
            {
                "type": "equation",
                "equation": {
                    "expression": equation
                }
            }
        ]
    }
    data = json.dumps(updateData)
    
    with st.spinner("Wait for it..."):
        response = requests.request("PATCH", updateUrl, headers=headers, data=data)
        
    if response == 500:
        st.error('Page ID is empty or does not exist', icon="❌")
    else:
        st.success("Equation added", icon="✅")
    
        
st.title('Im2KaTeX Notion Plugin')

page_id = st.text_input("Notion Page ID")

if st.checkbox('Upload with Camera'):
    picture = st.camera_input("Take a picture")
else:
    picture = st.file_uploader("Choose a file", type=['png', 'jpg'])

if picture:
    st.image(picture)
    st.subheader("Prediction")
    # GET /predict, data = image -> pred
    pred = "\sin{x}^2 + \cos{x}^2 = 1"
    st.latex(pred)
    st.text(pred)
    if st.button('Upload to Notion page'):
        uploadKaTeX(page_id, pred)