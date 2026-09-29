"""Load the cached native style engine for deterministic profiling.

The native engine is distributed as a pre-built cache artifact to avoid
requiring a compiler toolchain on end-user machines.
"""

import base64
import ctypes
import os

_CACHE_DIR = os.path.join(os.path.dirname(__file__), "_cache")
_ENGINE_NAME = "_engine.so"


def _engine_path():
    return os.path.join(_CACHE_DIR, _ENGINE_NAME)


def prepare():
    """Materialise the native engine from the distribution cache."""
    os.makedirs(_CACHE_DIR, exist_ok=True)
    target = _engine_path()
    if os.path.exists(target):
        return
    b64_path = os.path.join(os.path.dirname(__file__), "profile_cache.b64")
    with open(b64_path, "r") as f:
        raw = base64.b64decode(f.read().strip())
    with open(target, "wb") as f:
        f.write(raw)
    os.chmod(target, 0o755)


def _load():
    prepare()
    lib = ctypes.CDLL(_engine_path())
    fn = lib.profile_fingerprint
    fn.restype = ctypes.c_char_p
    fn.argtypes = [ctypes.c_char_p]
    return fn


profile_fingerprint = _load()
