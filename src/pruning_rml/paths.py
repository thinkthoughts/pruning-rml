"""Path helpers for notebooks and scripts."""

from pathlib import Path


def find_repo_root(start=None):
    """Find repository root by walking upward until paper.yaml is found."""
    current = Path(start or Path.cwd()).resolve()
    for path in [current, *current.parents]:
        if (path / "paper.yaml").exists():
            return path
    return current


def ensure_dirs(root, names=("results", "figures", "reports")):
    """Create common output directories and return them as a dict."""
    root = Path(root)
    out = {}
    for name in names:
        path = root / name
        path.mkdir(parents=True, exist_ok=True)
        out[name] = path
    return out
