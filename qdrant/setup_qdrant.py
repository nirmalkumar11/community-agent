from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(path="./qdrant_db")

COLLECTION_NAME = "club_members"

collections = client.get_collections().collections

existing = [c.name for c in collections]

if COLLECTION_NAME not in existing:

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

print("Qdrant collection ready")