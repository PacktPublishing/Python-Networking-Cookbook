import boto3 

DST_CIDR = "0.0.0.0/0"

ec2_resource = boto3.resource('ec2')

vpc = ec2_resource.create_vpc(CidrBlock='10.10.0.0/16')
vpc.wait_until_available()


print(f"Created vpc {vpc.id}")

subnet = vpc.create_subnet(CidrBlock='10.10.1.0/24')
print(f"Created subnet {subnet.id}")

gateway = ec2_resource.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=gateway.id)
print(f"Created gateway {gateway.id} and associated with {vpc.id}")

route_table = ec2_resource.create_route_table(VpcId=vpc.id)
route_table.associate_with_subnet(SubnetId=subnet.id)
print(f"Created route table {route_table.id}")

r = route_table.create_route(DestinationCidrBlock=DST_CIDR, GatewayId=gateway.id)
print(f"Created route {r} for {DST_CIDR} block")