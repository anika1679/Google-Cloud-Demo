from google import genai
import os
from .config import GEMINI_API_KEY, GOOGLE_API_KEY, PROJECT_ID
import json
import re
from pptx import Presentation
from pptx.util import Inches

# Helper Method to create Json responses from the AI API response
def parseResponseData(response):
    json_text_match = re.search(r"\{.*\}", response, re.DOTALL)
    if json_text_match:
        json_text = json_text_match.group(0)
        try:
            data = json.loads(json_text)
            print("Parsed Successfully")
            return data
        except json.JSONDecodeError as e:
            print("Warning: Not valid JSON", e) 
            return None
        
# Initializes the ai client being used.
client = genai.Client(vertexai=True, project=PROJECT_ID, location="global")
# Gets the information of the company and its compeitors from the user
company_name = input("Name of your company:")
description = input("Please give a description of your companies operations:")
competitors = input("Enter the names of your competitors:")
# Prompt to be used by the AI client
prompt = f"""Think of yourself as a business analyst for {company_name}. Their description is: {description}. Create a side-by-side competitve benchmark analysis for these competitors: {competitors}
For each competitor be sure to list their strengths, weaknesses, opportunities, and risks. Format as JSON with competitor names as keys. """
# Gets the response from the client
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt)
response_text = response.text

# Creates the data from AI response into a json that can be parsed
competitor_json = None
json_text_match = re.search(r"\{.*\}", response_text, re.DOTALL)
if json_text_match:
    json_text = json_text_match.group(0)
    try:
        competitor_json=json.loads(json_text)
        print("Parsed Successfully")
    except json.JSONDecodeError as e:
        print("Warning: Not valid JSON", e)

competitor_json = parseResponseData(response_text)
competitor_json = json.dumps(competitor_json, indent=2)
print(competitor_json)

if not competitor_json:
    print("Error: could not parse data")
    exit()

# Second prompt to compare the competitors to the user's company
prompt2 = f"""Think of yourself as a business analyst for {company_name}. Their description is: {description}.
Start first with a company overview and their key stats. Then using this competitor data in JSON format: {competitor_json}
For each competitor, give:
- Overview and key stats
- SWOT analysis
- Strategic recommendations for {company_name}
- Implications
Format your output as JSON, with each topic as a new slide section. Make content concise and actionable"""

response2 = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt2
)

response_text2 = response2.text

analysis_json = parseResponseData(response_text2)
analysis_json = json.dumps(analysis_json, indent=2)
print(analysis_json)

if not analysis_json:
    print("Error: could not parse data")
    exit()


def createPowerPoints():
    prs = Presentation()


