# # app.py

# from qdrant.search_members import search_members

# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# query = input("Ask: ")

# members = search_members(query)

# prompt = f"""
# Question:
# {query}

# Candidates:
# {members}

# Rank the candidates.

# Evaluate:
# 1. Leadership
# 2. Technical Skills
# 3. Achievements
# 4. Participation
# 5. Responsibilities

# Provide:
# - Rank
# - Candidate Name
# - Reason
# """

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=prompt
# )

# print(response.text)


# from adk.orchestrator import run
# from qdrant.search_members import close_client

# query = input("Ask: ")

# result = run(query)

# print(result)

# close_client()


from adk.orchestrator import run

while True:
    query = input("\nAsk: ")

    if query.lower() == "exit":
        break

    result = run(query)

    print("\n")
    print(result)