import google.generativeai as genai
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import (
    ChatPromptTemplate, 
    FewShotChatMessagePromptTemplate, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate, 
    AIMessagePromptTemplate
)
import re
import json
import os
import asyncio
from config import examples, prompt, prompt2
import unicodedata

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize LLM and parser
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17", google_api_key=API_KEY)
parser = StrOutputParser()

# Alternative approach using FewShotChatMessagePromptTemplate properly
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=ChatPromptTemplate.from_messages([
        ("human", "Please extract the clean job description from this raw text:\n{Raw_Text}"),
        ("ai", "{Output}")
    ]),
    examples=examples
)

chain = prompt | llm | parser  
chain2 = prompt2 | llm

def extract_job_description(text):
    try:
        result = chain.invoke({"Raw_Text": text})
        return result
    except Exception as e:
        print(f"[ERROR] Failed to extract job description: {e}")
        return None

# def remove_trailing_commas(json_str):
#     json_str = re.sub(r',\s*(\]|\})', r'\1', json_str)
#     return json_str

# def json_file_create(job_text):
#     result_str = chain2.invoke({"text": job_text})
#     cleaned_output = result_str.content.strip()

#     if cleaned_output.startswith("```json"):
#         cleaned_output = cleaned_output[len("```json"):].strip()
#     if cleaned_output.endswith("```"):
#         cleaned_output = cleaned_output[:-3].strip()

#     cleaned_output = (
#         cleaned_output
#         .replace("“", '"')
#         .replace("”", '"')
#         .replace("’", "'")
#         .replace("None", "null")  
#     )

#     cleaned_output = remove_trailing_commas(cleaned_output)

#     try:
#         return json.loads(cleaned_output)
#     except json.JSONDecodeError as e:
#         print("Error parsing JSON:", e)
#         print("Failed JSON content:\n", cleaned_output)
#         return None


def remove_trailing_commas(text):
    import re
    return re.sub(r',\s*([}\]])', r'\1', text)

def normalize_quotes(text):
    return unicodedata.normalize("NFKC", text)

def json_file_create(job_text):
    result_str = chain2.invoke({"text": job_text})
    cleaned_output = result_str.content.strip()

    if cleaned_output.startswith("```json"):
        cleaned_output = cleaned_output[len("```json"):].strip()
    if cleaned_output.endswith("```"):
        cleaned_output = cleaned_output[:-3].strip()

    cleaned_output = normalize_quotes(cleaned_output)
    cleaned_output = cleaned_output.replace("None", "null")
    cleaned_output = remove_trailing_commas(cleaned_output)

    try:
        return json.loads(cleaned_output)
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        print("Failed JSON content:\n", cleaned_output)
        return None
