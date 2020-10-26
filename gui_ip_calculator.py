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

# callback method for part 1 button. Get's called when user
# presses ENTER button.
def callback_class_info():
    ip_addr = (e1.get())
    output = ipc.get_class_stats(ip_addr)
    class_info_output.delete("1.0", "end")
    class_info_output.insert(tk.END, print_class_info(output))

# print details to output text box and is called by the callback method
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

class_info_output = tk.Text(first_frame, height=8, width=60)
class_info_output.pack()
class_info_output.insert(tk.END, "Output will print here.")

#######################################
#
# subnetting section of gui
#
subnet_stats_title = tk.Label(second_frame, text="Part 2 / 3: Subnet Calculator.")
subnet_stats_title.pack()
subnet_stats_info = tk.Label(second_frame, text="Please enter an ip address and subnet mask below.\n\n(e.g Format --> '192.168.0.0, 255.255.255.0') Please include comma!\n\nPress ENTER to get subnet data.")
subnet_stats_info.pack()

# callback method for part 2/3 button. Get's called when user
# presses ENTER button.
def callback_subnet_info():
    user_input = (subnet_entry_box.get())
    ip_addr, subnet_mask = user_input.split(",")
    output = ipc.get_subnet_stats(ip_addr, subnet_mask)
    subnet_stats_output.delete("1.0", "end")
    subnet_stats_output.insert(tk.END, print_subnet_info(output))

# print details to output text box and is called by the callback method
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

subnet_entry_box = tk.Entry(second_frame)
subnet_entry_box.pack()

subnet_button = tk.Button(second_frame, text="ENTER", width=20, command=callback_subnet_info)
subnet_button.pack()

# outbox box for subnetting info
label_2 = tk.Label(second_frame, text="Output:")
label_2.pack()

subnet_stats_output = tk.Text(second_frame, height=10, width=80)
subnet_stats_output.pack()
subnet_stats_output.insert(tk.END, "Output will print here.")

######################################
#
# supernetting section of gui
#
supernet_stats_title = tk.Label(third_frame, text="Part 4) Supernet Calculator.")
supernet_stats_title.pack()
subnet_stats_info = tk.Label(third_frame, text="Please enter a list of addresses.\nPress ENTER to get the supernet details.")
subnet_stats_info.pack()

# callback method for part 4 button. Get's called when user
# presses ENTER button.
def callback_supernet_info():
    user_input = (supernet_entry_box.get())
    output = ipc.get_supernet_stats(user_input.split(", "))
    supernet_stats_output.delete("1.0", "end")
    supernet_stats_output.insert(tk.END, print_supernet_info(output))

# print to screen and is called by the callback method
def print_supernet_info(output):
    ip_addr = (f"Address: {output[0]}")
    supernet_mask = (f"Network Mask: {output[1]}")
    return f"{ip_addr}\n{supernet_mask}"

# entry box 3
supernet_entry_box = tk.Entry(third_frame)
supernet_entry_box.pack()

# third button
supernet_button = tk.Button(third_frame, text="ENTER", width=20, command=callback_supernet_info)
supernet_button.pack()

# output box for supernetting
label_3 = tk.Label(third_frame, text="Output:")
label_3.pack()

supernet_stats_output = tk.Text(third_frame, height=10, width=80)
supernet_stats_output.pack()
supernet_stats_output.insert(tk.END, "Output will print here.")

tk.mainloop()