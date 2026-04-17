def parse_resume(file_bytes: bytes) -> dict:
    """Extract text and structured fields from a resume file."""
    # TODO: add PDF/DOCX parsing
    return {"text": file_bytes.decode('utf-8', errors='ignore')}
