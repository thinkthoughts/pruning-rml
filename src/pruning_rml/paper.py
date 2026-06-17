"""Load paper and statement metadata."""

from pathlib import Path
import yaml


def load_yaml(path):
    """Load a YAML file as a Python dictionary."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing YAML file: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or {}


def paper_summary_table(paper):
    """Return a compact table-friendly summary from paper metadata."""
    return {
        "identifier": paper.get("identifier", "—"),
        "title": paper.get("paper_title", paper.get("title", "—")),
        "category": paper.get("category", "—"),
        "status": paper.get("status", "—"),
    }
