# class IPv4:
#     BYTE = 4
#     bit = 32
#     def __init__(self, ip: str):
#         self.__ip = {
#             'bin': [],
#             'dec': ip
#         }
#         self.__subnet_mask = {
#             'bin': [],
#             'dec': [],
#             'cidr': 0
#         }
#         self.__wild_card = {
#             'bin': 0,
#             'dec': 0
#         }
#         self.__class = None
#         self.__divided_ip_subnet_mask()
#
#     def __divided_ip_subnet_mask(self):
#         for i in range(len(self.__ip['dec'])):
#             if self.__ip['dec'][i] == '/':
#                 self.__subnet_mask['cidr'] = int(self.__ip['dec'][i + 1:])     # estraggo la subnet mask in notazione CIDR, sommo 1 all'indice così parto dalla prima cifra della subnet mask fino alla fine di essa.
#                 self.__ip['dec'] = self.__ip['dec'][:i]   # estraggo tutto quello che c'è prima dello / quindi solamente l'ip.
#                 break
#
#     def __convert_dec_byte_to_bin(self, address, subnet_mask_cidr=0):
#         sequence = [0 for i in range(8)]    # preparo il byte
#         i = 0
#         while address != 0:
#             sequence[i] = address % 2
#             address //= 2
#             i += 1
#         sequence = sequence[::-1]
#         for i in sequence:
#             yield i     # uso il generatore per evitare di avere l'address come una lista di liste.
#
#     def __convert_address_to_bin(self, address):
#         bytes = address.split('.')
#         binary_ip = []
#         for i in range(IPv4.BYTE):
#             for j in self.__convert_dec_byte_to_bin(int(bytes[i])):
#                 binary_ip.append(j)
#             if i != IPv4.BYTE - 1:
#                 binary_ip.append('.')
#         return binary_ip
#
#     def __find_occurrence(self, iterable, key):
#         all_possible_occurrence = []
#         for i in range(len(iterable)):
#             if iterable[i] == key:
#                 all_possible_occurrence.append(i)
#         return all_possible_occurrence
#
#
#     def __convert_address_to_dec(self, address):
#         position_point_address = self.__find_occurrence(address, '.')
#         start = 0
#         end = 0
#         decimal_number = 0
#         decimal_address = []
#         for i in range(IPv4.BYTE):
#             if i == IPv4.BYTE - 1:  # l'ultimo byte non prevede un . alla fine, perciò se sono arrivato all'ultima iterazione devo estrarlo diversamente l'ultimo byte
#                 byte = address[end + 1:][::-1]
#             else:
#                 end = position_point_address[i]
#                 byte = address[start : end][::-1]      # faccio il reverse del i-esimo byte
#             for j in range(len(byte)):
#                 decimal_number += (2**j)*byte[j]
#             decimal_address.append(decimal_number)
#             decimal_number = 0
#             start = end + 1
#         return decimal_address
#
#     def ipv4_to_bin(self):
#         self.__ip['bin'] = self.__convert_address_to_bin(self.__ip['dec'])
#         return self.__ip['bin']
#
#     def subnet_mask_to_bin(self):
#         subnet_mask_bin = []
#         for i in range(IPv4.bit):
#             if i % 8 == 0 and i != 0:
#                 subnet_mask_bin.append('.')
#             if i < self.__subnet_mask['cidr']:
#                 subnet_mask_bin.append(1)
#             else:
#                 subnet_mask_bin.append(0)
#         self.__subnet_mask['bin'] = subnet_mask_bin
#         return subnet_mask_bin
#
#     def subnet_mask_to_dec(self):
#         try:
#             self.__subnet_mask['dec'] = self.__convert_address_to_dec(self.__subnet_mask['bin'])
#         except:
#             self.subnet_mask_to_bin()
#             self.__subnet_mask['dec'] = self.__convert_address_to_dec(self.__subnet_mask['bin'])
#         return self.__subnet_mask
#
#     def wild_card_to_bin(self):
#
#
#
#
#
#
#
# ip = IPv4("192.168.1.5/24")
# print(ip.subnet_mask_to_dec())
print(~0b1010)