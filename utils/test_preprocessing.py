# utils/text_processing.py

def preprocess_user_input(user_input: str) -> str:
    """Corrects common misspellings before processing."""
    corrections = {
        "comman": "common",
        "prject": "project",
        "resme": "resume",
        # Add other common typos you notice over time
    }
    # A simple word-by-word replacement
    # Using .lower() inside the loop to avoid changing the case of the whole sentence
    words = user_input.split()
    corrected_words = [corrections.get(word.lower(), word) for word in words]
    return " ".join(corrected_words)