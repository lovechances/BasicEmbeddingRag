from openai import OpenAI

client = OpenAI() #YOUR API KEY HERE 

EMBED_MODEL = "text-embedding-3-small"

def embed_text(text:str) -> list[float]:
    text = text.strip()
    if not text:
        return []
    
    res = client.embeddings.create(
        model=EMBED_MODEL,
        input=text
    )
    return res.data[0].embedding