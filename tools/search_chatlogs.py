import os

def search_chatlogs(term):
    base_dir = os.path.join(os.path.dirname(__file__), "..", "chat_logs")
    base_dir = os.path.abspath(base_dir)

    print(f"Søker i: {base_dir}\n")

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        for lineno, line in enumerate(f, start=1):
                            if term.lower() in line.lower():
                                print(f"{path}:{lineno}: {line.strip()}")
                except Exception as e:
                    print(f"Kunne ikke lese {path}: {e}")

if __name__ == "__main__":
    term = input("Enter search term: ")
    search_chatlogs(term)
