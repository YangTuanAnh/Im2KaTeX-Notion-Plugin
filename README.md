# Im2KaTeX Notion Plugin

*TODO: Add illustrations to the project structure and model*

This is an MVP Submission to the CinnamonAI Full Stack AI Bootcamp. The purpose of this project is to evaluate the candidates' modelling and engineering skills before the bootcamp.

## Structure

The Streamlit app takes in the user's Notion page ID (or any Notion block that could hold children blocks) and an image with math notation. An underlying model converts the math notation into the equivalent KaTeX notation (Notion's version of LaTeX, however Notion still accepts regular LaTeX), then creating a new equation block for that page via a PATCH call to Notion's API.

Note: The user needs to add plugin connection beforehand in order for the app to identify the page.

## Im2LaTeX

The model was reimplemented from a paper introducted by Deng et al. in [Image-to-Markup Generation with Coarse-to-Fine Attention](https://paperswithcode.com/paper/image-to-markup-generation-with-coarse-to)

A prebuilt dataset for OpenAI's task for image-2-latex system. Includes total of ~100k formulas and images splitted into train, validation and test sets. Formulas were parsed from LaTeX sources provided here: http://www.cs.cornell.edu/projects/kddcup/datasets.html (originally from arXiv)

Each image is a PNG image of fixed size. Formula is in black and rest of the image is transparent.

For related tools (eg. tokenizer) check out this repository: https://github.com/Miffyli/im2latex-dataset For pre-made evaluation scripts and built im2latex system check this repository: https://github.com/harvardnlp/im2markup

Newlines used in formulas_im2latex.lst are UNIX-style newlines (\n). Reading file with other type of newlines results to slightly wrong amount of lines (104563 instead of 103558), and thus breaks the structure used by this dataset. Python 3.x reads files using newlines of the running system by default, and to avoid this file must be opened with newlines="\n" (eg. open("formulas_im2latex.lst", newline="\n")).