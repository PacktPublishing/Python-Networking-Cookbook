infra_parts = ["10.2.10.", "10.30.2."]
user_parts = ["10.50.2.", "10.60."]

def check_ip(ip_addr):
    for net_part in infra_parts:
        if ip_addr.startswith(net_part):
            print(f"{ip_addr} is of type 'infra'")
    
    for net_part in user_parts:
        if ip_addr.startswith(net_part):
            print(f"{ip_addr} is of type 'user'")

check_ip("10.2.10.1")
check_ip("10.50.2.3")