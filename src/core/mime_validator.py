import os

# Default to 250 MB if not specified in environment
_default_max_mb = 250
try:
    MAX_OOXML_UNCOMPRESSED_MB = int(os.getenv("MAX_OOXML_UNCOMPRESSED_MB", _default_max_mb))
except (TypeError, ValueError):
    MAX_OOXML_UNCOMPRESSED_MB = _default_max_mb

# Convert MB to bytes for size checks
MAX_OOXML_TOTAL_UNCOMPRESSED_SIZE = MAX_OOXML_UNCOMPRESSED_MB * 1024 * 1024