KEYWORD_LINKS = [
    {
        "keywords": ["intent"],
        "links": [{"title": "LearnTeachMaster - Intent-Driven Engineering", "url": "https://learnteachmaster.org"}],
    },
    {
        "keywords": ["anthropic"],
        "links": [{"title": "Anthropic Documentation", "url": "https://docs.anthropic.com"}],
    },
    {
        "keywords": ["fastapi"],
        "links": [{"title": "FastAPI Docs", "url": "https://fastapi.tiangolo.com"}],
    },
    {
        "keywords": ["react"],
        "links": [{"title": "React Documentation", "url": "https://react.dev"}],
    },
]


def enrich(message: str, response: str) -> list[dict]:
    combined = (message + " " + response).lower()
    seen_urls = set()
    references = []
    for entry in KEYWORD_LINKS:
        if any(kw in combined for kw in entry["keywords"]):
            for link in entry["links"]:
                if link["url"] not in seen_urls:
                    seen_urls.add(link["url"])
                    references.append(link)
    return references
