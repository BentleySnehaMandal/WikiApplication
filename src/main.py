from wiki_utils import get_wikipedia_summary, set_language
from languages import SUPPORTED_LANGUAGES

def choose_language():
    print("Select a language for Wikipedia search:")
    for code, name in SUPPORTED_LANGUAGES.items():
        print(f"{code}: {name}")
    while True:
        lang = input("Enter language code (default 'en'): ").strip().lower()
        if not lang:
            lang = "en"
        if lang in SUPPORTED_LANGUAGES:
            set_language(lang)
            return
        print("Invalid language code. Try again.")

def main():
    choose_language()
    while True:
        topic = input("\nEnter a topic to search on Wikipedia (or type 'exit' to quit): ").strip()
        if topic.lower() == 'exit':
            print("Goodbye!")
            break
        summary, options = get_wikipedia_summary(topic)
        if options:
            print("\nTopic is ambiguous. Please choose one of the following options:")
            for idx, opt in enumerate(options, 1):
                print(f"{idx}. {opt}")
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(options):
                    summary, _ = get_wikipedia_summary(options[choice-1])
                else:
                    print("Invalid choice. Skipping.")
                    continue
            except ValueError:
                print("Invalid input. Skipping.")
                continue
        print("\nSummary:\n")
        print(summary)

if __name__ == "__main__":
    main()