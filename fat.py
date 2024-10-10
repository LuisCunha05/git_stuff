
def fat(n: int):
    """Calculates the Fatortial of N, Raises TypeError if N is different than Int"""
    if( type(n) != int): 
        raise TypeError

    if( n == 1):
        return 1
    return n * fat(n - 1)
