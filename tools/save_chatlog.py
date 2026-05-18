from datetime import datetime
from pathlib import Path
from typing import List, Optional

def save_chatlog(
    text: str,
    title: str = "chat",
    module: Optional[str] = None,
    tags: Optional[List[str]] = None,
    source: str = "Copilot"
):
    """
    Lagrer en chatlog i chat_logs/-mappen med auto-metadata.
    Metadata legges i toppen av filen som YAML-lignende header.
    """

    folder = Path("chat_logs")
    folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M")

    safe_title = title.replace(" ", "_").replace("/", "-")
    filename = folder / f"{timestamp}_{safe_title}.md"

    # Metadata-blokk
    metadata = [
        "---",
        f"title: {title}",
        f"date: {date}",
        f"time: {time}",
        f"module: {module if module else 'none'}",
        f"tags: {', '.join(tags) if tags else 'none'}",
        f"source: {source}",
        "---",
        "",
    ]

    with filename.open("w", encoding="utf-8") as f:
        f.write("\n".join(metadata))
        f.write(text.strip() + "\n")

    print(f"Chatlog lagret som: {filename}")
    return filename
