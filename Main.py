import sys
from calcIp_package.IPv4 import IPv4

def extract_argument():
    return sys.argv[1:]     # ritorno una lista shiftata di 1 da sinistra.


def filter_argument():
    """
    Alla posizione:

    0 -> IPv4 + subnet mask in CIDR.
    1 -> Nuova subnet per il subnetting,  se impostata a X non viene effettuato.
    2 -> Nuova subnet maask per il supernetting, se impostata a X non viene effettuato.
    :return:
    """
    input_argument = extract_argument()
    if len(input_argument) == 0:
        return 'X', 'X', 'X'
    else:
        ip = input_argument[0]
        subnemask_subnetting = input_argument[1]
        subnemask_supernetting = input_argument[2]
    return ip, subnemask_subnetting, subnemask_supernetting

def run_calcip():
    ip, subnetmask_subnetting, subnetmask_supernetting = filter_argument()
    if ip == 'X' and subnetmask_subnetting == 'X' and subnetmask_supernetting == 'X':
        print("DATI INSUFFICENTI")
    else:
        ipv4 = IPv4(ip)
        if subnetmask_subnetting != 'X' and subnetmask_supernetting != 'X':
            ipv4.subnetting(int(subnetmask_subnetting))
            ipv4.supernetting(int(subnetmask_supernetting))
        ipv4.to_string()


if __name__ == "__main__":
    run_calcip()
