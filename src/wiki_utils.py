import wikipedia

def set_language(lang_code):
    """
    Sets the language for Wikipedia queries.
    """
    wikipedia.set_lang(lang_code)

def get_wikipedia_summary(topic, sentences=5):
    """
    Fetches the summary of a topic from Wikipedia.
    Returns (summary, options) where options is a list if ambiguous, else None.
    """
    try:
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary, None
    except wikipedia.DisambiguationError as e:
        return None, e.options[:5]
    except wikipedia.PageError:
        return "No Wikipedia page found for this topic.", None
    except Exception as e:
        return f"An error occurred: {e}", None