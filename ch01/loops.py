network_part = "192.168.2."
host_parts = [20, 40, 60]

for host_part in host_parts:
    ip = network_part + str(host_part)
    print("The router IP is: " + ip)