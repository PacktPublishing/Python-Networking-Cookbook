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

filter = """
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
            </interface>
        </interfaces>
    </filter>
"""
conf = device.get_config(source='running', filter=filter).data_xml
pprint.pprint(conf)