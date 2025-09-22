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
company_name = input("Name of a company:")

# Prompt to be used by the AI client
prompt = f"""Think of yourself as a business analyst for {company_name}. Give:
- Overview and key stats
- SWOT analysis, listing their strenghts, weaknesses, opportunities, and risks (each on a different slide)
- Strategic recommendations for {company_name}
- Implications
Format your output as JSON, with each topic as a new slide section. Make content concise and actionable"""

# Gets the response from the client
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt)
response_text = response.text

# Creates the data from AI response into a json that can be parsed
analysis_json = parseResponseData(response_text)
analysis_json = json.dumps(analysis_json, indent=2)
print(analysis_json)

if not analysis_json:
    print("Error: could not parse data")
    exit()


def createPowerPoints():
    prs = Presentation()


