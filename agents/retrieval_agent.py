from google.adk.agents import Agent

from qdrant.search_members import search_members

retrieval_agent = Agent(
    name="retrieval_agent",
    model="gemini-2.5-flash",
    description="Retrieve relevant club members",
    instruction="""
    Use search_members tool.

    Retrieve the most relevant
    members for the user query.

    Return member details.
    """,
    tools=[
        search_members
    ]
)