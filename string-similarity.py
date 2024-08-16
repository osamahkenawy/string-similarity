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

# Example usage
s = "ababaa"
result = string_similarity(s)
print(result)  # Output should be 11
