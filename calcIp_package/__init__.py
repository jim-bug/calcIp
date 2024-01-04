from calcIp_package.convertitor.convertitor import dec_to_bin, bin_to_dec
from calcIp_package.colors.color import Colors

# funzione che trasforma l'ip_address_dec in binario bit per bit:
def binary_ipv4(ip, lenght_ip=4):
    ip_result = []
    for i in range(lenght_ip):
        generator = dec_to_bin(int(ip[i]))
        for k in generator:
            ip_result.append(k)
    return ip_result


# funzione che trasforma la subnetmask da binaria a decimale:
def decimal_ipv4(subnet_mask, lenght_ip=4):
    subnet = []
    start = 0
    for i in range(lenght_ip):
        subnet.append(str(bin_to_dec(subnet_mask[start: start+8])))
        start += 8      # mi sposto di 8 perchè sto estrando byte
    return subnet

# funzione che determina la classe di indirizzo di quell'ipv4
def which_class(ip):
    if 0 < ip[0] < 127:
        return 'A'
    elif 128 < ip[0] < 191:
        return 'B'
    elif 192 < ip[0] < 223:
        return 'C'


# funzione che manda a video un indirizzo ip binario con la suddivisione dei bit dedicati alla rete e all'host
def print_ip_bin(ip_bin, subnet_mask_cidr, message, lenght_byte_ip=32):
    i = 0
    print(f"{message}: ", end='')
    for j in range(lenght_byte_ip):
        if j % 8 == 0 and j != 0:
            print('.', end='')
        if i < subnet_mask_cidr:
            print(Colors.GREEN + str(ip_bin[i]), end='')      # i bit dedicati alla rete li mando a video in verde
            i += 1
        else:
            print(Colors.RED + str(ip_bin[j]), end='')     # i bit dedicati agli host li mando a video in rosso
    print(Colors.RESET)
