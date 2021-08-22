from ncclient import manager

conn_info = {
    "host": "10.10.20.48",
    "port": 830,
    "username": "developer",
    "password": "C1sco12345",
    "hostkey_verify": False
}

device = manager.connect(**conn_info)

device.create_subscription()

while True:
    notification = device.take_notification()
    print(notification.notification_xml)