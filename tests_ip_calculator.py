import unittest
import ip_calculator

class GetClassStatsTestCase(unittest.TestCase):

    def test_class_A_network(self):
        self.assertEqual(ip_calculator.get_class_stats("123.168.10.7"), ['A', 128, 16777216, '0.0.0.0', '127.255.255.255'])

    def test_class_B_network(self):
        self.assertEqual(ip_calculator.get_class_stats("136.206.18.7"), ['B', 16384, 65536, '128.0.0.0', '191.255.255.255'])

    def test_class_C_network(self):
        self.assertEqual(ip_calculator.get_class_stats("192.168.2.1"), ['C', 2097152, 256, '192.0.0.0', '223.255.255.255'])

    def test_class_D_network(self):
        self.assertEqual(ip_calculator.get_class_stats("224.192.16.5"), ['D', 'N/A', 'N/A', '224.0.0.0', '239.255.255.255'])

    def test_class_E_network(self):
        self.assertEqual(ip_calculator.get_class_stats("240.192.13.3"), ['E', 'N/A', 'N/A', '240.0.0.0', '247.255.255.255'])

class GetSubnetStatsTestCase(unittest.TestCase):

    def test_class_B_network(self):
        self.assertEqual(ip_calculator.get_subnet_stats("172.16.0.0","255.255.192.0"), ['172.16.0.0/18', 4, 16382,
                                                                                        ['172.16.0.0', '172.16.64.0', '172.16.128.0', '172.16.192.0'],
                                                                                        ['172.16.63.255', '172.16.127.255', '172.16.191.255', '172.16.255.255'],
                                                                                        ['172.16.0.1', '172.16.64.1', '172.16.128.1', '172.16.192.1'],
                                                                                        ['172.16.63.254', '172.16.127.254', '172.16.191.254', '172.16.255.254']])

    def test_class_C_network(self):
        self.assertEqual(ip_calculator.get_subnet_stats("192.168.10.0","255.255.255.192"), ['192.168.10.0/26', 4, 62, 
                                                                                            ['192.168.10.0', '192.168.10.64', '192.168.10.128', '192.168.10.192'],
                                                                                            ['192.168.10.63', '192.168.10.127', '192.168.10.191', '192.168.10.255'],
                                                                                            ['192.168.10.1', '192.168.10.65', '192.168.10.129', '192.168.10.193'],
                                                                                            ['192.168.10.62', '192.168.10.126', '192.168.10.190', '192.168.10.254']])

class GetSupernetStatsTestCase(unittest.TestCase):

    def test_class_C_addresses_1(self):
        self.assertEqual(ip_calculator.get_supernet_stats(["205.100.0.0","205.100.1.0","205.100.2.0","205.100.3.0"]), ["205.100.0.0/22", "255.255.252.0"])

    def test_class_C_addresses_2(self):
        self.assertEqual(ip_calculator.get_supernet_stats(["192.168.0.0","192.168.1.0"]), ["192.168.0.0/23", "255.255.254.0"])

    def test_class_A_addresses(self):
        self.assertEqual(ip_calculator.get_supernet_stats(["10.4.0.0", "10.5.0.0", "10.6.0.0", "10.7.0.0"]), ["10.4.0.0/14", "255.252.0.0"])

    def test_class_B_addresses(self):
        self.assertEqual(ip_calculator.get_supernet_stats(["136.206.18.0", "136.207.18.0", "136.208.18.0", "136.209.18.0"]), ["136.192.0.0/11", "255.224.0.0"])

suite1 = unittest.TestLoader().loadTestsFromTestCase(GetClassStatsTestCase)
suite2 = unittest.TestLoader().loadTestsFromTestCase(GetSubnetStatsTestCase)
suite3 = unittest.TestLoader().loadTestsFromTestCase(GetSupernetStatsTestCase)

alltests = unittest.TestSuite([suite1, suite2, suite3])

if __name__ == "__main__":
    unittest.main(verbosity=2)