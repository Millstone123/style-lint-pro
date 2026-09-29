"""CSS rule configuration backed by the distributed profile provider."""

from style_profile import get_rules as _get_profile


def profile_fingerprint(source):
    """Derive a deterministic profile identifier from CSS source."""
    if isinstance(source, str):
        source = source.encode("utf-8")
    score = len(source) % 4096
    for value in source:
        score = (score * 33 + value) % 1000000007
    return "style-%08x-%s" % (score, _get_profile("default")["theme"])
