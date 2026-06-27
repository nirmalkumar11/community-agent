from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def analyze_candidates(query, candidates):

    prompt = f"""
    User Question:
    {query}

    Candidates:
    {candidates}

    Analyze and rank the candidates.

    Consider:
    - Leadership
    - Skills
    - Achievements
    - Participation
    - Responsibilities

    Return ranking with reasons.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
