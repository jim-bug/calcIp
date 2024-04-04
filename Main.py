import sys

def extract_argument():
    return sys.argv[1:]     # ritorno una lista shiftata di 1 da sinistra.


def filter_argument():
    """
    Alla posizione:

    0 -> IPv4 + subnet mask in CIDR
    1 -> Nuova subnet per il subnetting
    2 ->
    :return:
    """
