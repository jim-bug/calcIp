# Autore: Ignazio Leonardo Calogero Sperandeo
# Data 03/01/2024
# Nome progetto: CalcIp
# by jim_bug :)
from sys import path
from argparse import ArgumentParser
from os import getcwd
from calcIp_package import binary_ipv4, decimal_ipv4, print_ip_bin, which_class, wild_card_calculation
path.append(getcwd()+'\\calcIp_package')
# path.append("C:\\Users\\Ignazio\\Desktop\\coding\\project_python\\project\\calcip\\calcIp_package")



LENGHT_BYTE_IP = 4
LENGHT_BIT_IP = 32
parser = ArgumentParser()
parser.add_argument('ipv4', type=str, help='ipv4 concatenato alla subnet mask in notazione CIDR')
args = parser.parse_args()
ip_address_dec = args.ipv4
subnet_mask_dec = []
wild_card_dec = []
network_address_dec = []
broadcast_address_dec = []
subnet_mask_cidr = 0
point_pos = []
ip_address_bin = []
subnet_mask_bin = []
wild_card_bin = []
network_address_bin = []
broadcast_address_bin = []
max_host = 0
start = 0

# divido ip da subnet mask in notazione CIDR
for i in range(len(ip_address_dec)):
    if ip_address_dec[i] == '/':
        subnet_mask_cidr = ip_address_dec[i + 1:]
        subnet_mask_cidr = int(subnet_mask_cidr)
        ip_address_dec = ip_address_dec[:i]     # in questa maniera lascio solo l'ip_address_dec senza la subnet mask in notazione CIDR
        break

j = 0
for i in range(LENGHT_BIT_IP):   # ricavo la subnetmask in binario
    if j < subnet_mask_cidr:
        subnet_mask_bin.append('1')
        j += 1
    else:
        subnet_mask_bin.append('0')

max_host = 2 ** (32 - subnet_mask_cidr) - 2
ip_address_dec = ip_address_dec.split('.')          # rendo l'ip una lista di stringhe con omessi i punti
ip_address_bin = binary_ipv4(ip_address_dec)      # trasformo in binario l'ip
subnet_mask_dec = decimal_ipv4(subnet_mask_bin)  # trasformo in decimale la subnet mask
wild_card_bin = wild_card_calculation(subnet_mask_bin)  # calcolo la wild card in binario
wild_card_dec = decimal_ipv4(wild_card_bin)     # trasformo la wild card in decimale

for i in range(LENGHT_BYTE_IP):
    network_address_dec.append(str(int(ip_address_dec[i]) & int(subnet_mask_dec[i])))       # operazione and bit a bit tra ip e subnet mask
network_address_bin = binary_ipv4(network_address_dec)

j = 0
for i in range(LENGHT_BIT_IP):
    if j < subnet_mask_cidr:    # finche sono nei bit della rete copio ogni bit
        broadcast_address_bin.append(str(ip_address_bin[i]))
        j += 1
    else:
        broadcast_address_bin.append('1')   # nei bit dell'host invece li pongo tutti a 1
broadcast_address_dec = decimal_ipv4(broadcast_address_bin)

print(f"IP: {'.'.join(ip_address_dec)}\nSubnet mask: {'.'.join(subnet_mask_dec)}\nSubnet mask in notazione CIDR: /{subnet_mask_cidr}\nIP rete: {'.'.join(network_address_dec)}\nIP broadcast: {'.'.join(broadcast_address_dec)}\nWild card: {'.'.join(wild_card_dec)}\nHost massimi: {max_host}\nClasse di indirizzo: {which_class(ip_address_dec, subnet_mask_cidr)}")
print("---------------------")
print_ip_bin(ip_address_bin, "IP binario", subnet_mask_cidr=subnet_mask_cidr)
print_ip_bin(subnet_mask_bin, "Subnet mask binaria", subnet_mask_cidr=subnet_mask_cidr)
print_ip_bin(wild_card_bin, "Wild Card binaria")
print_ip_bin(network_address_bin, "IP rete binario", subnet_mask_cidr=subnet_mask_cidr)
print_ip_bin(broadcast_address_bin, "IP broadcast binario", subnet_mask_cidr=subnet_mask_cidr)
