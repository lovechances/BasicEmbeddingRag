from typing import List, Dict

def build_prompt(query: str, chunks: list[dict]) -> str:
    context = "\n\n".join(
        [f"[chunk {c.get('id')} | score={c.get('score', 0):.3f}]\n{c['text']}" for c in chunks]
    )

    return f"""You must answer ONLY using the context below.
    If the answer is not in the context, say: "I don't have sufficient information in the provided data."

    QUESTION:
    {query}

    CONTEXT:
    {context}

    ANSWER:"""