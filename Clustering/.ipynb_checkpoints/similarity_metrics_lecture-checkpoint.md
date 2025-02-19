# Understanding Vectors

## Definition of a Vector
A **vector** has both **magnitude** and **direction**. It can be represented as:

- **2D**: \( v = (x, y) \)
- **3D**: \( v = (x, y, z) \)
- **N-dimensional**: \( v = (v_1, v_2, ..., v_n) \)

## Magnitude (Length) of a Vector
```
||v|| = sqrt(x1^2 + x2^2 + ... + xn^2)
```

## Vector Operations
- **Addition**: `A + B = (a1 + b1, a2 + b2)`
- **Subtraction**: `A - B = (a1 - b1, a2 - b2)`
- **Scalar Multiplication**: `k · v = (k · x, k · y)`
- **Dot Product**: `A · B = a1 b1 + a2 b2`

## Applications of Vectors
- **Physics**: velocity, acceleration
- **Computer Graphics**: 3D transformations
- **Machine Learning**: feature vectors
- **NLP**: word embeddings

---


# Similarity Metrics in Data Science and Machine Learning

## Introduction
Similarity metrics help determine how similar or different two data points are. These metrics are widely used in clustering, recommendation systems, and information retrieval. 

### Metrics Covered:
1. **Euclidean Distance**
2. **Manhattan Distance**
3. **Minkowski Distance**
4. **Cosine Similarity**
5. **Jaccard Similarity**

---

## 1. Euclidean Distance
**Definition**: The straight-line distance between two points in an N-dimensional space.

**Formula:**
```
d(P, Q) = sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

**Example:**
For two points \( P(1,2,3) \) and \( Q(4,6,7) \):
```
d(P, Q) = sqrt((4-1)^2 + (6-2)^2 + (7-3)^2) = sqrt(41) ≈ 6.4
```

**Use Cases:**
- Clustering algorithms (K-Means)
- Nearest neighbor search (K-Nearest Neighbors)
- Image recognition

---

## 2. Manhattan Distance
**Definition**: The sum of absolute differences between coordinates.

**Formula:**
```
d(P, Q) = sum(|q_i - p_i|)
```

**Example:**
For two points \( P(1,2,3) \) and \( Q(4,6,7) \):
```
d(P, Q) = |4-1| + |6-2| + |7-3| = 11
```

---

## 3. Minkowski Distance
**Definition**: A generalization of Euclidean and Manhattan distances, controlled by parameter p.

**Formula:**
```
d(P, Q) = (sum(|q_i - p_i|^p))^(1/p)
```

---

## 4. Cosine Similarity
**Definition**: Measures the cosine of the angle between two vectors.

**Formula:**
```
cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)
```

**Example:**
For vectors \( A = (1,2,3) \) and \( B = (4,6,7) \):
```
cosine_similarity ≈ 0.97
```

---

## 5. Jaccard Similarity
**Definition**: Measures how similar two sets are by comparing their intersection and union.

**Formula:**
```
J(A, B) = |A ∩ B| / |A ∪ B|
```

---

## Comparison Table

| Metric        | Best for                         | Weaknesses |
|--------------|--------------------------------|------------|
| **Euclidean** | Continuous space, clustering  | Affected by scale |
| **Manhattan** | Grid-like structures         | Ignores diagonal movement |
| **Minkowski** | Flexible for tuning          | Requires selecting p |
| **Cosine**    | Text similarity, high-dimensional | Ignores magnitude |
| **Jaccard**   | Set-based comparison         | Not useful for numeric data |

---

