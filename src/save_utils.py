def save_summary_to_file(topic, summary, filename="wikipedia_summaries.txt"):
    """
    Appends the topic and its summary to a local text file.
    """
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Topic: {topic}\n")
            f.write(f"Summary:\n{summary}\n")
            f.write("-" * 60 + "\n")
        print(f"Summary saved to {filename}")
    except Exception as e:
        print(f"Failed to save summary: {e}")