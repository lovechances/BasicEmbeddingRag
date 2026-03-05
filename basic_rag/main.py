from app.index_build import ensure_index
from app.answer import answer_question

def main():
    index = ensure_index()

    while True:
        q = input("Ask a question (or 'q' to quit): ").strip()
        if q.lower() == "q":
            break

        response = answer_question(q, index)
        print(f"-- ANSWER --")
        print(response)

if __name__ == "__main__":
    main()