# BasicEmbeddingRag
REQUIREMENTS: OPENAI, REQUESTS, NUMPY

DESCRIPTION:
A minimal Retrieval-Augmented Generation (RAG) project built from scratch:

chunks text files
builds an embedding index
retrieves top relevant chunks using cosine similarity
assembles a RAG prompt
calls an OpenAI chat model (4omini) to answer using only retrieved context
built in scoring system for responses
INSTRUCTIONS:

add your api key in app/llm.py
add text or data into data/sample.txt (books, scraped data, tweets, ect)
run main.py
type questions into cli, type q to quit
ai will respond only off of your sample text
NOTES:

app/chunk.py contains the chunking params. (more specific data = lower chunk size and overlap)
app/answer.py contains the scoring system. (more specific data = higher score and gap threshold)
