from google import genai

val = input("Enter the names of your competitors:")


client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=""
)