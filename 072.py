# This implementation of the solution adapted from JitteryWombat on the project euler forums.
def totients_up_to(limit):
    """
    Totient sieve.
    >>> from utility import totient
    >>> limit = 10000
    >>> assert [totient(i) for i in range(limit)] == totients_up_to(limit)
    """
    totients = list(range(limit))
    for i in range(2, limit):
        if totients[i] == i: # Prime, as it hasn't been divided by anything lower.
            totients[i] -= 1 # Primes are coprime to everything below them.
            # Factor i into the totients of its multiples.
            for j in range(i + i, limit, i):
                totients[j] -= totients[j] // i
    return totients

print(sum(totients_up_to(1000000)))
