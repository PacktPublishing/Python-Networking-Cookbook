from ncclient import manager
import pprint

conn_info = {
    "host": "<insert host>",
    "port": 830, # change port
    "username": "<insert username>",
    "password": "<insert password>",
    "hostkey_verify": False
}

device = manager.connect(**conn_info)

conf = device.get_config(source='running').data_xml

pprint.pprint(conf)