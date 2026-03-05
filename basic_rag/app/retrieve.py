import json
from app.embedder import embed_text
from app.similarity import cosine_sim

def load_index(path: str = "data/index.json") -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load()
    
def retrieve(query: str, index: list[dict], top_k: int = 5) -> list[dict]:
    qvec = embed_text(query)
    scored: list[tuple[float, dict]] = []

    for item in index:
        score = cosine_sim(qvec, item["embedding"])
        scored.append((score, item))

    scored.sort(key=lambda x:x[0], reverse=True)

    out: list[dict] = []
    for score, item in scored[:top_k]:
        enriched = dict(item)
        enriched["score"] = float(score)
        out.append(enriched)

    return out 