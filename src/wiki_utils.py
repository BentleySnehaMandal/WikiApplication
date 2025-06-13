import wikipedia

def get_wikipedia_summary(topic):
    """
    Fetches the summary of a topic from Wikipedia.
    """
    try:
        summary = wikipedia.summary(topic, sentences=5)
        return summary
    except wikipedia.DisambiguationError as e:
        return f"Topic is ambiguous. Options: {e.options[:5]}"
    except wikipedia.PageError:
        return "No Wikipedia page found for this topic."
    except Exception as e:
        return f"An error occurred: {e}"