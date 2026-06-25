"""
FILTER MODULE
━━━━━━━━━━━━
Decides which scraped jobs are worth alerting on.
Edit INCLUDE_KEYWORDS / EXCLUDE_KEYWORDS to tune signal vs noise.
"""

# ── Tune these ────────────────────────────────────────────────────────────────
INCLUDE_KEYWORDS = [
    "genai", "gen ai", "generative ai", "generative artificial",
    "llm", "large language model",
    "ai engineer", "ml engineer", "machine learning engineer",
    "langchain", "langgraph", "rag", "retrieval augmented",
    "openai", "anthropic", "hugging face", "vector", "embedding",
    "nlp", "natural language processing",
    "prompt engineer", "foundation model",
    "multimodal", "diffusion", "transformer",
]

EXCLUDE_KEYWORDS = [
    "senior principal",   # adjust seniority if needed
    "staff engineer",
    "vp of", "director of",
    "data entry", "sales", "marketing",
    "unpaid", "volunteer",
]
# ──────────────────────────────────────────────────────────────────────────────


def is_relevant(job: dict) -> bool:
    """Return True if the job matches our filter criteria."""
    haystack = f"{job['title']} {job['company']}".lower()

    # Must match at least one include keyword
    if not any(kw in haystack for kw in INCLUDE_KEYWORDS):
        return False

    # Must not match any exclude keyword
    if any(kw in haystack for kw in EXCLUDE_KEYWORDS):
        return False

    return True


def filter_jobs(jobs: list[dict]) -> list[dict]:
    return [j for j in jobs if is_relevant(j)]
