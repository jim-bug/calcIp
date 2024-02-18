class IPv4:
    def __init__(self, ip: str):
        self.__ip = {
            'bin': 0,
            'dec': ip
        }
        self.__subnet_mask = {
            'bin': 0,
            'dec': 0,
            'cidr': 0
        }
        self.__wild_card = {
            'bin': 0,
            'dec': 0
        }
        self.__class = None

    def __divided_ip_subnet_mask(self):
        for i in range(len(self.__ip)):
            if self.__ip[i] == '/':
                self.__subnet_mask['cidr'] = int(self.__ip['dec'][i + 1:])     # estraggo la subnet mask in notazione CIDR, sommo 1 all'indice così parto dalla prima cifra della subnet mask fino alla fine di essa.
                self.__ip = self.__ip['dec'][:i]   # estraggo tutto quello che c'è prima dello / quindi solamente l'ip.
                break
        return self.__ip, self.__subnet_mask['cidr']

    def convert_address_to_bin(self, byte, subnet_mask_cidr=0):
        sequence = [i for i in range(8)]    # preparo il byte
        i = 0
        while byte != 0:
            sequence[i] = byte % 2
            byte //= 2
            i += 1
        return sequence
