import json

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "club_members"

client = QdrantClient(path="./qdrant_db")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open(
    "data/members.json",
    "r"
) as f:

    members = json.load(f)

points = []

for member in members:

    text = f"""
    Name: {member['name']}
    Role: {member['role']}
    Skills: {', '.join(member['skills'])}
    Achievements: {', '.join(member['achievements'])}
    Participation: {', '.join(member['participation'])}
    Responsibilities: {', '.join(member['responsibilities'])}
    """

    vector = model.encode(text).tolist()

    points.append(
        PointStruct(
            id=member["id"],
            vector=vector,
            payload=member
        )
    )

client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print(f"Inserted {len(points)} members")