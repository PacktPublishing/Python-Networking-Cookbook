from ncclient import manager
import pprint

conn_info = {
    "host": "10.10.20.48",
    "port": 830,
    "username": "developer",
    "password": "C1sco12345",
    "hostkey_verify": False
}

device = manager.connect(**conn_info)

vlan_conf = """
    <vlan xmlns="http://openconfig.net/yang/vlan">
        <vlan-id>10</vlan-id>
        <config>
            <name>New VLAN</name>
            <status>ACTIVE</status>
            <vlan-id>10</vlan-id>
        </config>
    </vlan>
"""

device.edit_config(target="running", config=vlan_conf)