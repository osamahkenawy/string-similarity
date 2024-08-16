

# string-similarity

This Python script solves the "String Similarity" problem by efficiently calculating the sum of similarities between a given string and all its suffixes using the Z-algorithm. The problem is to determine the total number of characters in common between the string and each of its suffixes.

## Problem Description

Given a string s, the task is to calculate the sum of similarities between s and all of its suffixes. The similarity between two strings is defined as the length of the longest common prefix between them.

### Input

- A single string s consisting of lowercase English letters.

### Output

- A single integer representing the sum of similarities between the string s and all its suffixes.

## Implementation

The string_similarity function leverages the Z-algorithm to efficiently compute the sum of similarities in linear time. The process involves calculating the Z-array, which stores the lengths of the longest common prefixes between the string and its suffixes.

### Functions

 **string_similarity(s)**:
   - Computes the sum of similarities between the string s and all of its suffixes using the Z-algorithm.


### Example

```python
def string_similarity(s):
    n = len(s)
    Z = [0] * n

    # Initialize variables
    L, R, K = 0, 0, 0

    for i in range(1, n):
        if i > R:
            L, R = i, i
            while R < n and s[R] == s[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            K = i - L
            if Z[K] < R - i + 1:
                Z[i] = Z[K]
            else:
                L = i
                while R < n and s[R] == s[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
    
    return sum(Z) + n

# Example usage:
s = "ababaa"
print(string_similarity(s))  # Output should be 11
```

### Output

For an input like:

```
ababaa
```

The output will be:

```
11
```

## https://www.hackerrank.com/challenges/string-similarity/problem