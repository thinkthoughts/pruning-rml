"""Helpers for reasoning about surviving capabilities after pruning."""


def residue_delta(before, after):
    """Compute metric changes after pruning or revision."""
    keys = set(before) | set(after)
    return {k: after.get(k, 0) - before.get(k, 0) for k in sorted(keys)}


def retention_ratio(before, after):
    """Compute after / before for each metric where before is nonzero."""
    ratios = {}
    for key, value in before.items():
        if value != 0:
            ratios[key] = after.get(key, 0) / value
    return ratios
