from workflows.leadership_workflow import leadership_workflow
from qdrant.search_members import close_client

query = input("Ask: ")

result = leadership_workflow(query)

print(result)

close_client()