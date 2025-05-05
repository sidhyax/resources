from google.adk.agents import Agent

from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
# Set the environment variable for the API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
    api_key=os.getenv("GOOGLE_API_KEY"),
)