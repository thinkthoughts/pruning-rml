from pathlib import Path

def repo_root():
    current = Path.cwd().resolve()
    for path in [current, *current.parents]:
        if (path / "paper.yaml").exists():
            return path
    return current

def ensure_dir(path):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path
