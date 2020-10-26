import tkinter as tk
import ip_calculator as ipc

window = tk.Tk()
first_frame = tk.Frame(window)
third_frame = tk.Frame(window)
second_frame = tk.Frame(window)
########################################
first_frame.pack(side="top", fill="both", expand=True)
third_frame.pack(side="bottom", fill="both", expand=True)
second_frame.pack(side="bottom", fill="both", expand=True)
########################################

class_stats_title = tk.Label(first_frame, text="Part 1: IP Address Calculator.")
class_stats_title.pack()
class_stats_info = tk.Label(first_frame, text="Enter IP address below\n\n(e.g 192.168.0.1).\n\nPress ENTER to get the network class of the address and other statistics.")
class_stats_info.pack()

def callback_class_info():
    ip_addr = (e1.get())
    output = ipc.get_class_stats(ip_addr)
    output1.delete("1.0", "end")
    output1.insert(tk.END, print_class_info(output))

def print_class_info(output):
    network_class = (f"Class: {output[0]}")
    network_size = (f"Network: {output[1]}")
    num_hosts = (f"Host: {output[2]}")
    first_addr = (f"First Address: {output[3]}")
    last_addr = (f"Last Address: {output[4]}")

    screen_output = (f"{network_class}\n{network_size}\n{num_hosts}\n{first_addr}\n{last_addr}")

    return screen_output

# first entry box
e1 = tk.Entry(first_frame)
e1.pack()
e1.focus_set()

# button 1
b1 = tk.Button(first_frame, text="ENTER", width=20, command=callback_class_info)
b1.pack()


label_1 = tk.Label(first_frame, text="Output:")
label_1.pack()

output1 = tk.Text(first_frame, height=8, width=60)
output1.pack()
output1.insert(tk.END, "Output will print here.")

#######################################
#
# subnetting section of gui
#
subnet_stats_title = tk.Label(second_frame, text="Part 2 / 3: Subnet Calculator.")
subnet_stats_title.pack()
subnet_stats_info = tk.Label(second_frame, text="Please enter an ip address and subnet mask below.\n\n(e.g Format --> '192.168.0.0, 255.255.255.0') Please include comma!\n\nPress ENTER to get subnet data.")
subnet_stats_info.pack()

def callback_subnet_info():
    user_input = (e2.get())
    ip_addr, subnet_mask = user_input.split(",")
    output = ipc.get_subnet_stats(ip_addr, subnet_mask)
    output2.delete("1.0", "end")
    output2.insert(tk.END, print_subnet_info(output))

def print_subnet_info(output):
    address = (f"Address: {output[0]}")
    num_subnets = (f"Subnets: {output[1]}")
    hosts = (f"Addressable hosts per subnet: {output[2]}\n")
    valid_subnets = (f"Valid Subnets: {output[3]}\n")
    broadcast_addrs = (f"Broadcast Addresses: {output[4]}\n")
    first_addrs = (f"First Addresses: {output[5]}\n")
    last_addrs = (f"Last Addresses: {output[6]}")

    output = f"{address}\n{num_subnets}\n{hosts}\n{valid_subnets}\n{broadcast_addrs}\n{first_addrs}\n{last_addrs}"
    return output

e2 = tk.Entry(second_frame)
e2.pack()

b2 = tk.Button(second_frame, text="ENTER", width=20, command=callback_subnet_info)
b2.pack()

# outbox box for subnetting info
label_2 = tk.Label(first_frame, text="Output:")
label_2.pack()

output2 = tk.Text(second_frame, height=10, width=80)
output2.pack()
output2.insert(tk.END, "Output will print here.")

######################################
#
# supernetting section of gui
#
supernet_stats_title = tk.Label(third_frame, text="Part 4) Supernet Calculator.")
supernet_stats_title.pack()
subnet_stats_info = tk.Label(third_frame, text="Please enter a list of addresses.\nPress ENTER to get the supernet details.")
subnet_stats_info.pack()

def callback_supernet_info():
    user_input = (e3.get())
    output = ipc.get_supernet_stats(user_input.split(", "))
    output3.delete("1.0", "end")
    output3.insert(tk.END, print_supernet_info(output))

def print_supernet_info(output):
    ip_addr = (f"Address: {output[0]}")
    supernet_mask = (f"Network Mask: {output[1]}")
    return f"{ip_addr}\n{supernet_mask}"

# entry 3
e3 = tk.Entry(third_frame)
e3.pack()

# third button
b3 = tk.Button(third_frame, text="ENTER", width=20, command=callback_supernet_info)
b3.pack()

# output box for supernetting
label_3 = tk.Label(first_frame, text="Output:")
label_3.pack()

output3 = tk.Text(third_frame, height=10, width=80)
output3.pack()
output3.insert(tk.END, "Output will print here.")

tk.mainloop()