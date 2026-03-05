import json
from pathlib import Path
from app.embedder import embed_text
from app.chunk import chunk_text

def build_index(book_text: str, out_path: str = "data/index.json") -> int:
    chunks = chunk_text(book_text, chunk_size=900, overlap=150) 
    index = []

    for i, c in enumerate(chunks):
        vec = embed_text(c["text"])
        index.append({
            "id": i,
            "text": c["text"],
            "embedding": vec,
        })

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f)

    return len(index) 

def ensure_index(
    text_path: str = "data/sample.txt",
    out_path: str = "data/index.json",
) -> list[dict]:

    if Path(out_path).exists():
        with open(out_path, "r", encoding="utf-8") as f:
            return json.load(f)


    with open(text_path, "r", encoding="utf-8") as f:
        book_text = f.read()

    build_index(book_text, out_path=out_path)

    with open(out_path, "r", encoding="utf-8") as f:
        return json.load(f)