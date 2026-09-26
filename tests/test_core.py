from tts_utils import chunk_text, estimate_duration_sec, wrap_ssml_speak

def test_chunk():
    t = "Hello world. " * 50
    c = chunk_text(t, max_chars=80)
    assert len(c) > 1

def test_dur():
    assert estimate_duration_sec("one two three four", wpm=120) > 0

def test_ssml():
    assert "speak" in wrap_ssml_speak("hi")
