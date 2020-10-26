#!/usr/bin/python3

import os

# Part 1
def get_class_stats(ip_addr):
    """takes ip_addr (string)
    returns:
    - CLASS
    - # NETWORKS FOR CLASS
    - # HOSTS FOR CLASS
    - # FIRST IP FOR CLASS
    - # LAST IP FOR CLASS
    """

    # create binary representation of ip_addr
    binary_rep = to_binary_string(ip_addr)

    # get the first 4 bit of the address
    # prefix_nibble = binary_rep[0][:4]

    # join the list of bytes into a single
    # string of bits
    binary_rep = "".join(binary_rep)

    # find the index of the first 0 in the address
    index = binary_rep.find("0")

    # set our prefix bits to be all bits up to and
    # including our first 0. This let's us determine
    # what class of network the IP is from.
    prefix_bits = binary_rep[:index + 1]

    # calculate IP address' network class
    ip_addr_class = chr(index + 65)

    if (ip_addr_class == "D") or (ip_addr_class == "E"):
        class_num_networks = "N/A"
        num_addressable_hosts = "N/A"
    else:
        # let our (index + 1) be set as an ID
        # in order to represent classes.
        # 1 --> A
        # 2 --> B
        # 3 --> C
        # This makes it easier to perform the following
        # calcualtions.
        network_class_id = index + 1

        # Calculate the # Network for a class.
        #
        # get the # network bits for class.
        num_network_bits = ((network_class_id) * 8) - (network_class_id)

        # get the number of networks for class.
        class_num_networks = 2 ** (num_network_bits)

        # Calculate the # Hosts for class.

        # subtract the number of network bits from 4 (4 represents the
        # number of bytes in an IPv4 address) i.e get the number of host
        # bits for a class by multiplying the number of free bytes possible
        # (1-3) by 8 (the number of bits per byte) and as
        # such, the number of unique hosts possible.
        num_addressable_hosts = 2 ** ((4 - (network_class_id)) * 8)

    # Calculate the range of addresses for class.
    #
    # Calculate first address (START OF RANGE).
    # Simply append 0's to the end of the prefix nibble.
    # I.e setting all bits after the prefix to 0.
    #first_ip_binary = [str(prefix_nibble) + "0000"] + ["00000000"]*3
    first_ip_binary = [str(prefix_bits) + ("0" * (8 - len(prefix_bits)))] + ["00000000"]*3

    # convert first address in range to decimal dot notation.
    first_ip_decimal = to_decimal_dot(first_ip_binary)

    # Calculate last address (END OF RANGE).
    # Simply append 1's to the end of the class prefix bits, creating
    # the 32 bit binary representation of the address.
    last_ip_binary = [str(prefix_bits) + ("1" * (8 - len(prefix_bits)))] + ["11111111"]*3

    # convert first address in range to decimal dot notation.
    last_ip_decimal = to_decimal_dot(last_ip_binary)

    # Print all details.
    print(f"Class: {ip_addr_class}")
    print(f"Network: {class_num_networks}")
    print(f"Host: {num_addressable_hosts}")
    print(f"First Address: {first_ip_decimal}")
    print(f"Last Address: {last_ip_decimal}")

    return [ip_addr_class, class_num_networks, num_addressable_hosts, first_ip_decimal, last_ip_decimal]


# Part 2 --> takes Class C address
def get_subnet_stats(ip_addr, subnet_mask):
    """OUTPUTS:
    - IP_ADDR CIDR NOTATION
    - # SUBNETS ON NETWORK
    - # ADDRESSABLE HOSTS PER SUBNET
    - VALID SUBNETS
    - BROADCAST ADDRESS OF EACH SUBNET
    - VALID HOSTS ON EACH SUBNET
    """
    index = "".join(to_binary_string(ip_addr)).find("0")
    ip_addr_class = (chr(index + 65))

    # get CIDR notation
    subnet_mask_binary = "".join(to_binary_string(subnet_mask))
    subnet_cidr = sum([int(bit) for bit in subnet_mask_binary]) # possibly make function for these?

    # Calculate # subnets on network
    #num_subnets = 2 ** (subnet_cidr % 8)
    #num_subnets = 2 ** ((32 - subnet_cidr) % 8)

    class_b = False
    if (subnet_cidr >= 24) and ip_addr_class == "B":
        num_subnets = 2 ** (subnet_cidr - 16)
        class_b = True
    else:
        num_subnets = 2 ** (subnet_cidr % 8)

    # hosts
    unmasked_bits = 32 - subnet_cidr
    num_hosts_per_subnet = (2 ** unmasked_bits) - 2

    # calculate valid subnets (break down into function)
    for index, n in enumerate(subnet_mask.split(".")): # get subnet mask
        if int(n) < 255:
            mask_value = int(n)
            block_size = 256 - int(n)
            break

    valid_subnets = []
    subnet_base_ip = ip_addr.split(".")

    # generate valid subnets
    i = 0
    while i <= mask_value:
        subnet_base_ip[index] = str(i)
        valid_subnets.append(".".join(subnet_base_ip))
        i += block_size

    broadcast_addresses = []
    broadcast_addr_value = block_size - 1
    subnet_base_ip = ip_addr.split(".") # reset subnet_base_ip
    
    # calculate broadcast addresses
    while (broadcast_addr_value) <= 255:
        subnet_base_ip[index] = str(broadcast_addr_value)
        remaining_bytes = index
        while remaining_bytes < len(subnet_base_ip) - 1:
            subnet_base_ip[index + 1] = str(255)
            # if it's a class A address
            if index == 1:
                subnet_base_ip[index + 2] = str(255)
            remaining_bytes += 1
        broadcast_addresses.append(".".join(subnet_base_ip))
        broadcast_addr_value += block_size

    if class_b:
        # generate valid subnets
        new_valid_subnets = []
        for i in range(256):
            for subnet in valid_subnets:
                subnet = subnet.split(".")
                subnet[index-1] = str(i)
                new_valid_subnets.append(".".join(subnet))
        
        new_broadcast_addresses = []
        for k in range(256):
            for broadcast_addr in broadcast_addresses:
                broadcast_addr = broadcast_addr.split(".")
                broadcast_addr[index-1] = str(k)
                new_broadcast_addresses.append(".".join(broadcast_addr))


    # get first addresses
    first_addresses = []
    for entry in valid_subnets:
        entry = entry.split(".")
        entry[-1] = str(int(entry[-1]) + 1)
        first_addresses.append(".".join(entry))

    # get last addresses
    last_addresses = []
    for entry in broadcast_addresses:
        entry = entry.split(".")
        entry[-1] = str(int(entry[-1]) - 1)
        last_addresses.append(".".join(entry))

    # print all info
    print(f"Address: {ip_addr}/{subnet_cidr}")
    print(f"Subnets: {num_subnets}")
    print(f"Addressable hosts per subnet: {num_hosts_per_subnet}\n")
    print(f"Valid Subnets: {valid_subnets}\n")
    print(f"Broadcast Addresses: {broadcast_addresses}\n")
    print(f"First Addresses: {first_addresses}\n")
    print(f"Last Addresses: {last_addresses}")

    #print(new_valid_subnets)
    #print("##################")
    #print(len(new_broadcast_addresses))
    #print(new_broadcast_addresses)

    return [f"{ip_addr}/{subnet_cidr}", num_subnets, num_hosts_per_subnet, valid_subnets, broadcast_addresses, first_addresses, last_addresses]

# Part 4
def get_supernet_stats(list_addresses):
    list_addresses = ["".join(to_binary_string(entry)) for entry in list_addresses]

    longest_common_prefix = os.path.commonprefix(list_addresses)
    network_prefix_size = len(longest_common_prefix)

    # get full supernet address into binary string
    supernet_address = (longest_common_prefix) + ("0" * (32 - len(longest_common_prefix)))
    # get full supernet mask in binary
    supernet_mask = ("1" * len(longest_common_prefix)) + ("0" * (32 - len(longest_common_prefix)))

    # split binary string representations of supernet address and mask into list of binary bytes (maybe helper method)
    supernet_address = to_decimal_dot([(supernet_address[i:i+8]) for i in range(0, len(supernet_address), 8)])
    supernet_mask = to_decimal_dot([(supernet_mask[i:i+8]) for i in range(0, len(supernet_mask), 8)])

    print(f"Address: {supernet_address}/{network_prefix_size}")
    print(f"Network Mask: {supernet_mask}")


# Helper functions

def to_binary_string(ip_addr):
    """
    Converts an ip address represented as a string in decimal dot
    Assignment_1.md 10/11/2020
    5 / 6
    notation into a list of
    four binary strings
    each representing one byte of the address
    :param ip_addr: The ip address as a string in decimal dot notation
    e.g. "132.206.19.7"
    :return: An array of four binary strings each representing one byte
    of ip_addr e.g.
    ['10000100', '11001110', '00010011', '00000111']
    """
    # split into array of four ["136","206","19","9"]
    byte_split = ip_addr.split(".")
    # convert each number into a int, format it as binary, turn it back into a string
    # and return it as an array, isn't python great !
    return ['{0:08b}'.format(int(x)) for x in byte_split]


def to_decimal_dot(ip_addr_list):
    """
    Take in an array of four strings represting the bytes of an ip address
    and convert it back into decimal dot notation
    :param ip_addr_list: An array of four binary strings each
    representing one byte of ip_addr e.g. ['10000100', '11001110',
    '00010011', '00000111']
    :return: The ip address as a string in decimal dot notation e.g.
    '132.206.19.7'
    """
    # for each string in the list
    # use str(int(x,2)) to convert it into a decimal number
    # and then turn that number into a string e.g. '10000100' -> '132'
    # put all converted numbers into a list ["132","206","19","7"]
    # call ".".join on the list to merge them into a string separated by "."
    return ".".join([str(int(x,2)) for x in ip_addr_list])


def main():
    # this is the cunty one
    get_subnet_stats("136.10.0.0","255.255.255.224")

    #get_subnet_stats("192.168.10.0","255.255.255.192")

    #get_subnet_stats("136.206.16.0", "255.255.255.192")

    # PART 4
    #get_supernet_stats(["205.100.0.0","205.100.1.0","205.100.2.0","205.100.3.0"])
    #get_supernet_stats(["138.188.0.0","138.189.0.0","138.190.0.0","138.191.0.0"])


if __name__ == "__main__":
    main()
