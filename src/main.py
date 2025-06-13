from wiki_utils import get_wikipedia_summary

def main():
    topic = input("Enter a topic to search on Wikipedia: ")
    try:
        summary = get_wikipedia_summary(topic)
        print("\nSummary:\n")
        print(summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()