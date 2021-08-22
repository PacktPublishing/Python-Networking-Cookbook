import boto3 

ec2_resource = boto3.resource('ec2')

vpc = ec2_resource.create_vpc(CidrBlock='10.10.0.1/16')
vpc.wait_until_available()

print(f"Created vpc {vpc.id}")