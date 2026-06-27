# from qdrant_client import QdrantClient
# from sentence_transformers import SentenceTransformer

# COLLECTION_NAME = "club_members"

# client = QdrantClient(path="./qdrant_db")

# model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )

# def search_members(query: str):

#     query_vector = model.encode(
#         query
#     ).tolist()

#     results = client.query_points(
#         collection_name=COLLECTION_NAME,
#         query=query_vector,
#         limit=5
#     ).points

#     candidates = []

#     for result in results:
#         candidates.append(
#             result.payload
#         )

#     return candidates

# def close_client():
#     client.close()


from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "club_members"

client = QdrantClient(path="./qdrant_db")
model = SentenceTransformer("all-MiniLM-L6-v2")

def search_members(query: str):
    query_vector = model.encode(query).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=5
    ).points

    return [r.payload for r in results]

def close_client():
    client.close()