import sys
import calcip_package as cp
from calcip_package.IPv4 import IPv4


class CLI:
    """
    Classe che si occupa di formattare l'input da riga di comando per istanziare un oggetto IPv4.
    """
    @staticmethod
    def extract_argument():
        args = ['x' for i in range(5)]
        if len(sys.argv)-1 < 1:
            return False    # ritorno una lista shiftata di 1 da sinistra, questo -1 è dovuto al fatto che dentro la lista sys.argv è presente anche il nome del file dato che son parametri da CLI
        for i in range(1, len(sys.argv)):
            args[i-1] = sys.argv[i]     # l'indice di sys.argv deve partire da 1 così da evitare di comprendere il nome del file.
        return args


    @staticmethod
    def filter_argument():
        """
        Alla posizione:

        0 -> IPv4 + subnet mask in CIDR.
        1 -> Nuova subnet per il subnetting
        2 -> Nuova subnet maask per il supernetting

        Questa funzione filtra gli argomenti passati da CLI, seguendo lo schema riportato qui in alto
        :return:
        """
        input_argument = CLI.extract_argument()
        try:
            if not input_argument:
                print("MANCANZA DI ARGOMENTI, CODE ERROR 101")
                raise Exception
            else:
                for i in input_argument:
                    if i == '-h' or i == '--help':      # se è presente la richiesta di visualizzare l'help interrompo il processo.
                        CLI.help_calcip()
                        # input_argument.remove(i)
                        raise Exception
            return input_argument[1], input_argument[2], input_argument[0]
        except:
            exit(0)


    @staticmethod
    def run_calcip():
        ip, new_subnet_mask, option = CLI.filter_argument()
        ipv4 = IPv4(ip)
        try:
            if option == '-s':
                ipv4.subnetting(int(new_subnet_mask))
            elif option == '-S':
                ipv4.supernetting(int(new_subnet_mask))
        except:
            print(f"Input del subentting o supernetting invalido, CODE ERROR: 102")
        ipv4.to_string()

    @staticmethod
    def help_calcip():
        help_message = """
Usage: python3 Main.py [OPTIONS] [IP] [SUBNETS] [SUPERNETS]

Options:
-h, --help Show this message and exit
-s, Used for making subnetting from the new subnet mask
-S, Used for making supernetting from the new subnet mask

IP: ip address along with subnet information (CIDR notation)
SUBNETS: new subnet mask for subnetting (less than subnet)
SUPERNETS: new supernet mask for supernetting (greater than subnet)
        """
        print(help_message)
        cp.print_calcip_information()


