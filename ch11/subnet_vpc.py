import boto3 

KEY_PAIR = "<insert key pair name>"
IMAGE_ID = "<insert image id>" # You can use this one for a default linux: "ami-05f7491af5eef733a"

ec2_resource = boto3.resource('ec2')

vpc = ec2_resource.create_vpc(CidrBlock='10.10.0.0/16')
vpc.wait_until_available()


print(f"Created vpc {vpc.id}")

subnet = vpc.create_subnet(CidrBlock='10.10.1.0/24')

net_inf = []
net_inf.append({
    'SubnetId': subnet.id,
    'DeviceIndex': 0
})
i = ec2_resource.create_instances(ImageId=IMAGE_ID,
                                  KeyName=KEY_PAIR,
                                  NetworkInterfaces=net_inf,
                                  MaxCount=1,
                                  MinCount=1
    )
print(f"Instance with id {i[0].id} created")