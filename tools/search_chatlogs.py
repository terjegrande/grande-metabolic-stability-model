from pathlib import Path

def search_chatlogs(query: str, folder: str = "chat_logs"):
    """
    Søk etter tekst i alle .md-filer i chat_logs-mappen.
    Viser filnavn, linjenummer og selve linjen.
    """
    base = Path(folder)
    if not base.exists():
        print(f"Mappen '{folder}' finnes ikke.")
        return

    query_lower = query.lower()
    results = []

    for file in base.glob("*.md"):
        with file.open("r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                if query_lower in line.lower():
                    results.append((file.name, lineno, line.strip()))

    if not results:
        print(f"Ingen treff for '{query}'.")
        return

    print(f"\nTreff for '{query}':\n")
    for filename, lineno, line in results:
        print(f"- {filename} (linje {lineno}): {line}")

    print(f"\nTotalt {len(results)} treff.")
