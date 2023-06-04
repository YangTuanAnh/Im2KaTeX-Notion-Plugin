import streamlit as st
import requests, json, os
from PIL import Image

# from dotenv import load_dotenv
# load_dotenv()
# key = os.getenv('NOTION_KEY')

from pix2tex import cli as pix2tex

headers = {
    "Authorization": "Bearer " + st.secrets['NOTION_KEY'],
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

model = pix2tex.LatexOCR()

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
        
    if response == 200 or response == 400:
        st.success("Equation added", icon="✅")
    else:
        st.error('Page ID is empty, unathorized, or does not exist', icon="❌")
        
    
def getPrediction(picture):
    img = Image.open(picture)
    output = model(img)
    return output

def redirect_button(url: str, text: str= None, color="#FD504D"):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

        
st.title('Im2KaTeX Notion Plugin')
url = "https://api.notion.com/v1/oauth/authorize?client_id=abf6a6f6-1369-488e-8f23-18ee7ad157b2&response_type=code&owner=user&redirect_uri=https%3A%2F%2Fyangtuananh-im2katex-notion-plugin-app-qucmyk.streamlit.app%2F"

redirect_button(url,"Authorize Integration to Notion account")

page_id = st.text_input("Notion Page ID")
st.write("https://www.notion.so/Personal-Home- **6b241a4133ba4db18f5bd9fbc76e6856** 👈 Example Page ID")
if st.checkbox('Upload with Camera'):
    picture = st.camera_input("Take a picture")
else:
    picture = st.file_uploader("Choose a file", type=['png', 'jpg'])

if picture is not None:
    st.image(picture)
    st.subheader("Prediction")
    pred = getPrediction(picture)
    #pred = "\sin{x}^2 + \cos{x}^2 = 1"
    #output = st.text_area("Edit KaTeX here", pred)
    st.latex(st.text_area("Edit KaTeX here", pred))
    if st.button('Upload to Notion page'):
        uploadKaTeX(page_id, pred)