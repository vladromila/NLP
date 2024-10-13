import numpy as np

S1 = "The man saw a car in the park"
S2 = "I saw the man park the car"

S1_tokens = S1.lower().split()
S2_tokens = S2.lower().split()

print("Tokens of S1:", S1_tokens)
print("Tokens of S2:", S2_tokens)

vocabulary = sorted(set(S1_tokens + S2_tokens))
print("Vocabulary:", vocabulary)

def vectorize(sentence_tokens, vocabulary):
    return np.array([sentence_tokens.count(word) for word in vocabulary])

S1_vector = vectorize(S1_tokens, vocabulary)
S2_vector = vectorize(S2_tokens, vocabulary)

print("S1 vector:", S1_vector)
print("S2 vector:", S2_vector)

euclidean_distance = np.linalg.norm(S1_vector - S2_vector)
euclidean_similarity = 1 / (1 + euclidean_distance)

cosine_similarity = np.dot(S1_vector, S2_vector) / (np.linalg.norm(S1_vector) * np.linalg.norm(S2_vector))

S1_set = set(S1_tokens)
S2_set = set(S2_tokens)

jaccard_similarity = len(S1_set.intersection(S2_set)) / len(S1_set.union(S2_set))

overlap_similarity = len(S1_set.intersection(S2_set)) / min(len(S1_set), len(S2_set))

print(f"Euclidean Similarity: {euclidean_similarity}")
print(f"Cosine Similarity: {cosine_similarity}")
print(f"Jaccard Similarity: {jaccard_similarity}")
print(f"Overlap Similarity: {overlap_similarity}")