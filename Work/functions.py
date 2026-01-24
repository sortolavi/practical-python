
def sumcount_using_range(n):
    """Returns the sum of all integers from 1 to n and the count of those integers."""
    if n < 1:
        return 0, 0
    total_sum = sum(range(1, n + 1))
    count = n
    return total_sum, count

print(sumcount_using_range(100))  # Output: (5050, 100)

def sumcount_using_formula(n):
    """Returns the sum of all integers from 1 to n and the count of those integers using formulas."""
    if n < 1:
        return 0, 0
    total_sum = n * (n + 1) // 2 # floor division to ensure an integer result
    count = n
    return total_sum, count

print(sumcount_using_formula(100))  # Output: (5050, 100)


