from __future__ import annotations
import re

def chunk_text(text: str, max_chars: int = 400) -> list[str]:
    text = re.sub(r"\s+", " ", text.strip())
    if len(text) <= max_chars:
        return [text] if text else []
    parts = re.split(r"(?<=[.!?])\s+", text)
    chunks, cur = [], ""
    for p in parts:
        if not cur:
            cur = p
        elif len(cur) + 1 + len(p) <= max_chars:
            cur = cur + " " + p
        else:
            chunks.append(cur)
            cur = p
    if cur:
        chunks.append(cur)
    return chunks

def estimate_duration_sec(text: str, wpm: float = 150.0) -> float:
    words = len(text.split())
    return float(words / max(wpm, 1.0) * 60.0)

def wrap_ssml_speak(text: str, rate: str = "medium") -> str:
    safe = text.replace("&", "&amp;").replace("<", "&lt;")
    return f'<speak><prosody rate="{rate}">{safe}</prosody></speak>'
