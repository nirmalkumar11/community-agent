from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def recommend_candidate(query, analysis):

    prompt = f"""
    User Query:
    {query}

    Analysis:
    {analysis}

    Choose ONE best candidate.

    Return:

    Winner:
    Confidence:
    Reason:
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
