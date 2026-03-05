from app.retrieve import retrieve
from app.rag import build_prompt
from app.llm import call_llm

MIN_TOP_SCORE = 0.50
MIN_SCORE_GAP = 0.005
DEBUG = True

def answer_question(query: str, index: list[dict], top_k: int = 5) -> str:
    hits = retrieve(query, index, top_k=top_k)

    if not hits:
        return "I dont have enough info in data to answer that"
    
    top_score = hits[0].get("score", 0.0)
    second_score = hits[1].get("score", 0.0) if len(hits) > 1 else None

    if DEBUG:
        print(f"[DEBUG] Top scores:")
        for h in hits[:min(3, len(hits))]:
            print(f"id={h.get('id')} score={h.get('score'):.4f}")
    
    if top_score < MIN_TOP_SCORE:
        return "No response returned a high enough match"
    
    if second_score is not None:
        gap = top_score - second_score
        if gap < MIN_SCORE_GAP:
            return(
                "Your data might contain something relevant but retrieval is vague"
            )
    
    prompt = build_prompt(query, hits)
    return call_llm(prompt)