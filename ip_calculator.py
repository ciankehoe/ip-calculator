#!/usr/bin/python3


# Test against : http://jodies.de/ipcalc
# https://erikberg.com/notes/networks.html

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
    binary_rep = to_binary_string(ip_addr)

    # calculate IP address' network class
    prefix_nibble = binary_rep[0][:4]
    ip_addr_class = chr(sum(int(bit) for bit in prefix_nibble) + 65)

    if (ip_addr_class == "D") or (ip_addr_class == "E"):
        class_num_networks = "N/A"
        num_addressable_hosts = "N/A"
    else:
        # calculate  # NETWORKS FOR CLASS
        # get's the # network bits for class
        num_network_bits = ord(ip_addr_class) - 64
        # calculate subnet mask size for given class
        subnet_mask_size = num_network_bits * 8
        class_num_networks = 2 ** (subnet_mask_size - num_network_bits)

        # HOSTS FOR CLASS
        num_addressable_hosts = 2 ** subnet_mask_size

    # GET CLASS RANGE
    # FIRST IP (START OF RANGE)
    #first_ip_binary = (str(prefix_nibble) + "0000" + (".00000000" * 3)).split(".")
    first_ip_binary = [str(prefix_nibble) + "0000"] + ["00000000"]*3
    # convert to list
    #first_ip_binary = [first_ip_binary[i:i+8] for i in range(0, 32, 8)]
    # convert first IP address to decimal dot notation
    first_ip_decimal = to_decimal_dot(first_ip_binary)

    # LAST IP (END OF RANGE)
    last_ip_binary = [str(prefix_nibble) + "1111"] + ["11111111"]*3
    last_ip_decimal = to_decimal_dot(last_ip_binary)

    print(f"Class: {ip_addr_class}")
    print(f"Network: {class_num_networks}")
    print(f"Host: {num_addressable_hosts}")
    print(f"First Address: {first_ip_decimal}")
    print(f"Last Address: {last_ip_decimal}")




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
    # get CIDR notation
    subnet_mask_binary = "".join(to_binary_string(subnet_mask))
    subnet_cidr = sum([int(bit) for bit in subnet_mask_binary]) # possibly make function for these?

    # Calculate # subnets on network
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

    i = 0
    while i <= mask_value:
        subnet_base_ip[index] = str(i)
        valid_subnets.append(".".join(subnet_base_ip))
        i += block_size

    # calculate broadcast addresses
    broadcast_addresses = []
    broadcast_addr_value = block_size - 1
    subnet_base_ip = ip_addr.split(".") # reset subnet_base_ip

    while (broadcast_addr_value) <= 255:
        subnet_base_ip[index] = str(broadcast_addr_value)
        remaining_bytes = index
        while remaining_bytes < len(subnet_base_ip) - 1:
            subnet_base_ip[index + 1] = str(255)
            remaining_bytes += 1
        broadcast_addresses.append(".".join(subnet_base_ip))
        broadcast_addr_value += block_size

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
    print(f"Last Addresses: {last_addresses}\n")


# Part 4
def get_supernet_stats(list_addresses):
    pass


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
 #split into array of four ["136","206","19","9"]
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

    # PART 1
    #get_class_stats("136.206.19.9")
    #print("#######################")
    #get_class_stats("224.192.16.5")
    #print("#######################")

    # PART 2
    get_subnet_stats("192.168.10.0","255.255.255.192")
    print("#################")
    print("CLASS B")
    get_subnet_stats("172.16.0.0", "255.255.255.252")

if __name__ == "__main__":
    main()
