import boto3

ec2 = boto3.client('ec2')

vpc_data = ec2.describe_vpcs()

print("VPCs")
for v in vpc_data['Vpcs']:
    print(f"VPC Id: {v['VpcId']}")
    instance_data = ec2.describe_instances(Filters=[
        {
            "Name": "vpc-id",
            "Values": [
                v['VpcId']
            ]
        }
    ])
    
    if len(instance_data['Reservations']) > 0:
        for res_num in range(0, len(instance_data['Reservations'])):
            for i in instance_data['Reservations'][res_num].get('Instances', []):
                print(f"- {i['InstanceType']} launched at {i['LaunchTime']}")
