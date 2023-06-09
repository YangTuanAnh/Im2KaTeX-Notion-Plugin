# Im2KaTeX Notion Plugin

*TODO: Add illustrations to the project structure and model*

This is an MVP Submission to the CinnamonAI Full Stack AI Bootcamp. The purpose of this project is to evaluate the candidates' modelling and engineering skills before the bootcamp.

[Youtube Demo](https://www.youtube.com/watch?v=g54oVOdBtSY)

## Structure

The Streamlit app takes in the user's Notion page ID (or any Notion block that could hold children blocks) and an image with math notation. An Pix2Tex model converts the math notation into the equivalent KaTeX notation (Notion's version of LaTeX, however Notion still accepts regular LaTeX), then creating a new equation block for that page via a PATCH call to Notion's API.

Note: The user needs to add the Notion plugin connection beforehand in order for the app to identify the page.

## Pix2Tex

The model comes from the Pix2Tex package, authored by Lukas Blecher from the [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) repository. The model consist of a ViT encoder with a ResNet backbone and a Transformer decoder.

## Installation

To run the app on Streamlit, follow along the [installation](https://docs.streamlit.io/library/get-started/installation) steps according to your OS

After you've set up a Python environment with Anaconda Terminal, perform these lines to run the app

```py
pip install python-dotenv pix2tex
streamlit run app.py
```

In development, you need to have a `/.streamlit/secrets.toml` file and replace with your Notion integration key as such

```
NOTION_KEY = "secret_123abc"
```

In deployment, you may need to paste the contents of `/.streamlit/secrets.toml` into the Secret settings for environment variables to work

## Struggles

There was an attempt to reimplement [Sujay et al.](https://sujayr91.github.io/Im2Latex/) and [Deng et al.](https://paperswithcode.com/dataset/im2latex-100k)'s papers, yet proven to be unsuccessful due to constraints. Future iterations of this project will include a seperate API for the model, as well as higher accuracy for handwritten math notations.

OAuth Authorization may be unstable, and will be revisioned in the future.

