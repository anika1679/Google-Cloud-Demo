from google import genai
import os
from .config import GEMINI_API_KEY, GOOGLE_API_KEY, GOOGLE_APPLICATION_CREDENTIALS, PROJECT_ID

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

client = genai.Client(vertexai=True, project=PROJECT_ID, location="global")

val = input("Enter the names of your competitors:")

prompt = f"""Think of yourself as a business analyst for a company. Create a side-by-side competitve benchmark analysis for these competitors: {val}
For each competitor be sure to list their strengths, weaknesses, opportunities, and risks. Format everything in a clear and readable table"""

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt)

print(response.text, end="")
