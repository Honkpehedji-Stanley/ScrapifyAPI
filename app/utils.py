def clean_text(text: str) -> str:
    """Nettoie une chaîne de texte : supprime les espaces et sauts de ligne inutiles."""
    return text.strip().replace("\n", "")
