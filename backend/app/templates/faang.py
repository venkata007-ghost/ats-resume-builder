FAANG_TEMPLATE = {
    "header": "Software Engineer",
    "sections": ["Summary", "Experience", "Projects", "Education", "Skills"]
}


def render(data: dict) -> str:
    # Very small example template renderer
    out = [data.get('name', 'Candidate'), data.get('summary', '')]
    return "\n\n".join(out)
