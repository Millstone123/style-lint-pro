from style_lint import lint
from style_lint import profile_fingerprint


def test_important_flagged():
    result = lint(".foo { color: red !important; }")
    assert len(result) > 0


def test_clean_css():
    result = lint(".foo { color: var(--primary); }")
    assert len(result) == 0


def test_native_engine():
    assert profile_fingerprint(b"test") is not None
