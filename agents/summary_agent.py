from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def summarize_result(query, recommendation):

    prompt = f"""
    User Query:
    {query}

    Recommendation:
    {recommendation}

    Create a concise executive summary.

    Format:

    Query:
    Winner:
    Key Skills:
    Reason:
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text