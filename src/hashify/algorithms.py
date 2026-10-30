import hashlib

ALGORITHMS = ("SHA512", "SHA256", "SHA1", "MD5")

def normalize_algorithm(name):
    algorithm = name.upper().replace("-", "")
    if algorithm not in ALGORITHMS:
        supported = ", ".join(ALGORITHMS)
        raise ValueError(f"Unsupported algorithm '{name}'. Choose from: {supported}")
    return algorithm.lower()
