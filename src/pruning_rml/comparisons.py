"""Reset versus revision comparisons."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Comparison:
    """A simple result record for comparing methods."""
    method: str
    score: float
    tokens: int
    mode: str = "unspecified"


def winner(a, b):
    """Return the better-performing comparison by score."""
    return a if a.score >= b.score else b


def label_mode(method):
    """Map method language to reset/revision vocabulary."""
    lower = method.lower()
    if "scratch" in lower or "random" in lower or "reset" in lower:
        return "reset"
    if "prun" in lower or "revision" in lower or "inherited" in lower:
        return "revision"
    return "observe"
