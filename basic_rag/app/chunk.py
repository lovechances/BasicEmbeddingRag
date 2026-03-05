from typing import List, Dict

def chunk_text(text: str, chunk_size: int = 700, overlap: int = 120) -> List[Dict]:
    chunks = []
    start = 0

    if overlap < 0:
        overlap = 0
    if overlap >= chunk_size:
        overlap = chunk_size // 3  # safety

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append({"text": chunk})


        start = end - overlap

    return chunks