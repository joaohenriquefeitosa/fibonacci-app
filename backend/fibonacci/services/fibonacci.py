from fibonacci.models import FibonacciData
from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
        Generate a Fibonacci sequence of length `n`.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def check_fibonacci(n: int) -> List[int]:
    """
    Check if the Fibonacci sequence of length n exists in the database.
    """
    fibonacci_data = FibonacciData.objects.filter(value=n).first()

    if fibonacci_data:
        return fibonacci_data.serie
    
    serie = generate_fibonacci(n)
    FibonacciData.objects.create(value=n, serie=serie)
    
    return serie