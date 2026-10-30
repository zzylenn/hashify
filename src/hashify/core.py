import hashlib
import hmac

from .algorithms import normalize_algorithm


def hash_file(path, algorithm="SHA256", chunk_size=1024 * 1024):
    algorithm = normalize_algorithm(algorithm)
    digest = hashlib.new(algorithm)

    with open(path, "rb") as file:
        while chunk := file.read(chunk_size):
            digest.update(chunk)

    return digest.hexdigest()


def verify_file(path, expected_hash, algorithm="SHA256"):
    actual_hash = hash_file(path, algorithm)
    return hmac.compare_digest(actual_hash.lower(), expected_hash.strip().lower()), actual_hash


def compare_files(first_path, second_path, algorithm="SHA256"):
    first_hash = hash_file(first_path, algorithm)
    second_hash = hash_file(second_path, algorithm)
    return first_hash == second_hash, first_hash, second_hash
