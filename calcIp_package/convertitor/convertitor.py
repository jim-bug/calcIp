# Definizione della funzione generatrice
def dec_to_bin(num: int):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while num != 0:
        result[i] = (num % 2)
        num //= 2
        i += 1
    result = result[::-1]
    for i in result:
        yield i     # creo un generatore

def bin_to_dec(sequence: str) -> int:
    num = 0
    sequence = sequence[::-1]
    for i in range(len(sequence)):
        num += (2**i)*int(sequence[i])
    return num
