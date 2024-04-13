import sys
from calcIp_package.IPv4 import IPv4

class CLI:
    """
    Classe che si occupa di formattare l'input da riga di comando per istanziare un oggetto IPv4.
    """
    @staticmethod
    def extract_argument():
        return False if len(sys.argv) - 1 <= 1 else sys.argv[1:]  # ritorno una lista shiftata di 1 da sinistra, questo -1 è dovuto al fatto che dentro la lista sys.argv è presente anche il nome dle file dato che son parametri da CLI

    @staticmethod
    def filter_argument():
        """
        Alla posizione:

        0 -> IPv4 + subnet mask in CIDR.
        1 -> Nuova subnet per il subnetting,  se impostata a X non viene effettuato.
        2 -> Nuova subnet maask per il supernetting, se impostata a X non viene effettuato.

        Questa funzione filtra gli argomenti passati da CLI, seguendo lo schema riportato qui in alto
        :return:
        """
        input_argument = CLI.extract_argument()

        if not input_argument:
            print("MANCANZA DI ARGOMENTI, CODE ERROR 101")
            exit(0)
        else:
            ip = input_argument[0]
            subnemask_subnetting = input_argument[1]
            subnemask_supernetting = input_argument[2]
        return ip, subnemask_subnetting, subnemask_supernetting

    @staticmethod
    def run_calcip():
        ip, subnetmask_subnetting, subnetmask_supernetting = CLI.filter_argument()
        ipv4 = IPv4(ip)
        try:
            if subnetmask_subnetting != 'X':
                ipv4.subnetting(int(subnetmask_subnetting))
            if subnetmask_supernetting != 'X':
                ipv4.supernetting(int(subnetmask_supernetting))
        except:
            print("Input del subentting o supernetting invalido, CODE ERROR: 102")
        ipv4.to_string()

