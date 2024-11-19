"""An example of recursive functions"""


def factorial(n: int) -> int:
    """Compute the factorial of n."""
    if n < 0:
        raise ValueError("Can't use negative numbers.")
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)


print(factorial(n=5))
