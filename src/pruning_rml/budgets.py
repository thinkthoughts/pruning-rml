"""Utilities for comparing token budgets."""


def token_efficiency(score, tokens):
    """Return score per million tokens."""
    if tokens <= 0:
        raise ValueError("tokens must be positive")
    return score / (tokens / 1_000_000)


def budget_ratio(a_tokens, b_tokens):
    """Return a_tokens / b_tokens with validation."""
    if b_tokens <= 0:
        raise ValueError("b_tokens must be positive")
    return a_tokens / b_tokens
