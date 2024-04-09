import sys
from calcIp_package.IPv4 import IPv4

def extract_argument():
    return False if len(sys.argv)-1 <= 1 else sys.argv[1:]   # ritorno una lista shiftata di 1 da sinistra, questo -1 è dovuto al fatto che dentro la lista sys.argv è presente anche il nome dle file dato che son parametri da CLI


def filter_argument():
    """
    Alla posizione:

    0 -> IPv4 + subnet mask in CIDR.
    1 -> Nuova subnet per il subnetting,  se impostata a X non viene effettuato.
    2 -> Nuova subnet maask per il supernetting, se impostata a X non viene effettuato.

    Questa funzione filtra gli argomenti passati da CLI, seguendo lo schema riportato qui in alto
    :return:
    """
    input_argument = extract_argument()

    if not input_argument:
        print("MANCANZA DI ARGOMENTI")
        exit(0)
    else:
            ip = input_argument[0]
            subnemask_subnetting = input_argument[1]
            subnemask_supernetting = input_argument[2]
    return ip, subnemask_subnetting, subnemask_supernetting

def run_calcip():
    ip, subnetmask_subnetting, subnetmask_supernetting = filter_argument()
    ipv4 = IPv4(ip)
    if subnetmask_subnetting != 'X' and subnetmask_supernetting != 'X':
        ipv4.subnetting(int(subnetmask_subnetting))
        ipv4.supernetting(int(subnetmask_supernetting))
    ipv4.to_string()


if __name__ == "__main__":
    run_calcip()
