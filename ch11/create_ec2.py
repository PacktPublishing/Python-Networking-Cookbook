import boto3

ec2 = boto3.resource('ec2')

KEY_PAIR = "<insert key name>"
IMAGE_ID = "<insert ami>" # You can use this one for a default linux: ami-05f7491af5eef733a"

i = ec2.create_instances(ImageId=IMAGE_ID,
                         KeyName=KEY_PAIR,
                         MaxCount=1,
                         MinCount=1)

print(i)