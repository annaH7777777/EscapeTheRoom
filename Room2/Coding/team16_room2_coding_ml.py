#For Machine Learning: Write a function that calculates the cosine similarity between two NumPy vectors.
import numpy as np

def cosine_similarity(vec1, vec2):
    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        raise ValueError("Input vectors must not be zero-vectors.")
    return dot_product / (norm1 * norm2)


def test_cosine_similarity():
    # Test with two identical vectors
    v1 = np.array([1, 2, 3])
    v2 = np.array([1, 2, 3])
    result1 = cosine_similarity(v1, v2)
    print(f"\ncosine_similarity({v1},{v2}) = {result1}")
    assert np.isclose(result1, 1.0), "Identical vectors should have similarity 1.0"

    # Test with orthogonal vectors
    v3 = np.array([1, 0])
    v4 = np.array([0, 1])
    result2 = cosine_similarity(v3, v4)
    print(f"cosine_similarity({v3},{v4}) = {result2}")
    assert np.isclose(result2, 0.0), "Orthogonal vectors should have similarity 0.0"

    # Test with opposite vectors
    v5 = np.array([1, 0])
    v6 = np.array([-1, 0])
    result3 = cosine_similarity(v5, v6)
    print(f"cosine_similarity({v5},{v6}) = {result3}")
    assert np.isclose(result3, -1.0), "Opposite vectors should have similarity -1.0"

    # Test with non-normalized vectors
    v7 = np.array([2, 0])
    v8 = np.array([1, 0])
    result4 = cosine_similarity(v7, v8)
    print(f"cosine_similarity({v7},{v8}) = {result4}")
    assert np.isclose(result4, 1.0), "Colinear vectors should have similarity 1.0"

    # Test with zero vector (should raise ValueError)
    v9 = np.array([0, 0])
    v10 = np.array([1, 2])
    try:
        cosine_similarity(v9, v10)
        print(f"cosine_similarity({v9},{v10}) did not raise ValueError as expected")
        assert False, "Zero vector should raise ValueError"
    except ValueError:
        print(f"cosine_similarity({v9},{v10}) correctly raised ValueError")

    print("All tests passed.")


if __name__ == "__main__":
    test_cosine_similarity()
