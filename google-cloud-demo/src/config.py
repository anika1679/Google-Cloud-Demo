from dotenv import load_dotenv
import os
from pathlib import Path

# Links the env to the config file
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
# Gets the environment variables from the env file and configures them
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

