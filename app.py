from chatbot import create_qa_chain

def main():
    print("=" * 60)
    print(" Domain-Specific RAG Chatbot (Local & Offline)")
    print(" Ask questions based on the content of your JSON file")
    print(" Type 'exit' to quit")
    print("=" * 60)

    try:
        qa_chain = create_qa_chain()
    except Exception as e:
        print(f" Failed to initialize chatbot: {e}")
        return

    while True:
        try:
            query = input("\nYou: ")
            if query.lower() in ["exit", "quit"]:
                print(" Exiting chatbot. Goodbye!")
                break

            response = qa_chain.invoke({"query": query})
            print(f"\n Bot: {response['result']}")
        except KeyboardInterrupt:
            print("\n Chatbot interrupted. Goodbye!")
            break
        except Exception as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()
