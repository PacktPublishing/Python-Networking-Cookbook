import pprint
from netmiko import ConnectHandler

connection_info = {
    'device_type': 'cisco_ios',
    'host': '<insert host>',
    'port': 22, # Change if your port is different
    'username': '<insert username>',
    'password': '<insert password>'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show interfaces", use_genie=True)
    
    for name, details in out.items():
        print(f"{name}")
        print(f"- Status: {details.get('enabled', None)}")
        print(f"- Physical address: {details.get('phys_address', None)}")
        print(f"- Duplex mode: {details.get('duplex_mode', None)}")
        
        for counter, count in details.get('counters', {}).items():
            if isinstance(count, int):
                if count > 0:
                    print(f"- {counter}: {count}")
            elif isinstance(count, dict):
                for sub_counter, sub_count in count.items():
                    if sub_count > 0:
                        print(f"- {counter}::{sub_counter}: {sub_count}")