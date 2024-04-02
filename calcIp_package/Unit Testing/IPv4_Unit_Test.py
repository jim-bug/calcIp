import unittest
from calcIp_package.IPv4 import IPv4
# Autore: Ignazio Leonardo Calogero Sperandeo
# Data: 02/04/2024
# by jim_bug :)


class MyTestCase(unittest.TestCase):
    def test_ipv4_to_bin(self):
        test_input = [
            "192.168.1.0/24",
            "210.47.206.46/19",
            "410.5.0.1/-3",
            "192.167.1.78/-10",
            "192.170.3000.1/13"
        ]
        test_output = [
            [1, 1, 0, 0, 0, 0, 0, 0, '.', 1, 0, 1, 0, 1, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 1, '.', 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 1, 0, '.', 0, 0, 1, 0, 1, 1, 1, 1, '.', 1, 1, 0, 0, 1, 1, 1, 0, '.', 0, 0, 1, 0, 1, 1, 1, 0],
            None,
            None,
            None
        ]

        for i in range(len(test_input)):
            ip = IPv4(test_input[i])
            if test_output[i] is None:
                self.assertIsNone(ip.ipv4_to_bin())
            else:
                self.assertEqual(ip.ipv4_to_bin(), test_output[i])

    def test_network_address_to_bin(self):
        test_input = [
            "192.168.1.0/24",
            "210.47.206.46/19",
            "410.5.0.1/-3",
            "192.167.1.78/-10",
            "192.170.30.1/13"
        ]
        test_output = [
            [1, 1, 0, 0, 0, 0, 0, 0, '.', 1, 0, 1, 0, 1, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 1, '.', 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 1, 0, '.', 0, 0, 1, 0, 1, 1, 1, 1, '.', 1, 1, 0, 0, 0, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 0],
            None,
            None,
            [1, 1, 0, 0, 0, 0, 0, 0, '.', 1, 0, 1, 0, 1, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        for i in range(len(test_input)):
            ip = IPv4(test_input[i])
            if test_output[i] is None:
                self.assertIsNone(ip.network_address_to_bin())
            else:
                self.assertEqual(ip.network_address_to_bin(), test_output[i])

    def test_broadcast_address_to_bin(self):
        test_input = [
            "192.168.1.0/24",
            "210.47.206.46/19",
            "410.5.0.1/-3",
            "255.255.255.255/10",
            "192.170.30.1/13"
        ]
        test_output = [
            [1, 1, 0, 0, 0, 0, 0, 0, '.', 1, 0, 1, 0, 1, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 0, 0, 1, 0, '.', 0, 0, 1, 0, 1, 1, 1, 1, '.', 1, 1, 0, 1, 1, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1],
            None,
            [1, 1, 1, 1, 1, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, '.', 1, 0, 1, 0, 1, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        for i in range(len(test_input)):
            ip = IPv4(test_input[i])
            if test_output[i] is None:
                self.assertIsNone(ip.broadcast_address_to_bin())
            else:
                self.assertEqual(ip.broadcast_address_to_bin(), test_output[i])

    def test_wild_card_to_bin(self):
        test_input = [
            "97.56.88.1/13",
            "45.78.1.67/24",
            "76.55.120.4/33",
            "55.340.1.5/1",
            "192.168.1.0/20"
        ]

        test_output = [
            [0, 0, 0, 0, 0, 0, 0, 0, '.', 0, 0, 0, 0, 0, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 0, '.', 1, 1, 1, 1, 1, 1, 1, 1],
            None,
            None,
            [0, 0, 0, 0, 0, 0, 0, 0, '.', 0, 0, 0, 0, 0, 0, 0, 0, '.', 0, 0, 0, 0, 1, 1, 1, 1, '.', 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        for i in range(len(test_input)):
            ip = IPv4(test_input[i])
            if test_output[i] is None:
                self.assertIsNone(ip.wild_card_to_bin())
            else:
                self.assertEqual(ip.wild_card_to_bin(), test_output[i])

    def test_class(self):
        test_input = [
            "192.168.1.0/24",
            "10.0.0.1/8",
            "173.6.56.88/16",
            "23.11.65.88/11",
            "55.123.200.1/31"
        ]

        test_output = [
            'C',
            'A',
            'B',
            None,
            None
        ]

        for i in range(len(test_input)):
            ip = IPv4(test_input[i])
            if test_output[i] is None:
                self.assertIsNone(ip.which_class())
            else:
                self.assertEqual(ip.which_class(), test_output[i])


if __name__ == '__main__':
    unittest.main()
