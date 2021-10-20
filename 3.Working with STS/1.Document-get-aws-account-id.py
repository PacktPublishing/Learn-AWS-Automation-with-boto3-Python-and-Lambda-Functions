import boto3

aws_mag_con_root=boto3.session.Session(profile_name="root")
sts_con_cli=aws_mag_con_root.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity()
print(response.get('Account'))

aws_mag_con_ec2_dev=boto3.session.Session(profile_name="ec2_developer")
sts_con_cli=aws_mag_con_ec2_dev.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity()
print(response['Account'])