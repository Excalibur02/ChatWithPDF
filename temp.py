import pathlib
import textwrap
import os
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

from dotenv import load_dotenv

load_dotenv()

os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.0-pro-001')


def to_markdown(text):
    formatted_text = text.replace("**", "").replace("*", "")

    # Split the text into sections based on headings
    sections = formatted_text.split("**")

    # Define a dictionary to store the converted text
    converted_text = {}

    # Process each section
    for section in sections:
        lines = section.strip().split("\n")
        if lines:
            heading = lines[0].strip().replace(":", "")
            content = "\n".join(lines[1:]).strip()

            # Convert bullet points to "- "
            content = content.replace("* ", "- ")

            # Add the section to the converted text dictionary
            converted_text[heading] = content

    # Construct the converted text
    converted_output = ""
    for heading, content in converted_text.items():
        converted_output += f"{heading}:\n{content}\n\n"

    return converted_output


def gemini_general_reply(text):
    response = model.generate_content(str(text))
    return to_markdown(response.text)


# ques = input("What do you want to know ? ")
#
#
# print(gemini_general_reply(ques))




