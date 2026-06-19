import torch

def transcribe_batch(audio_files, model='base', language=None):
    """Transcribe multiple audio files."""
    results = []
    for f in audio_files:
        results.append({'file': f, 'text': '', 'segments': []})
    return results
