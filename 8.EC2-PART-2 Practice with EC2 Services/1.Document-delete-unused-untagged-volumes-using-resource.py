import boto3

aws_mag_con=boto3.session.Session(profile_name="ec2_developer")
'''
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name='us-east-1')
f_ebs_unused={"Name":"status","Values":["available"]}
for each_volume in ec2_con_re.volumes.filter(Filters=[f_ebs_unused]):
	if not each_volume.tags:
		print(each_volume.id, each_volume.state,each_volume.tags)
		print("Deleting unused and untagged volumes.....")
		each_volume.delete()

print("Delted all unused unatageed volumes.")
'''
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name='us-east-1')
for each_item in ec2_con_cli.describe_volumes()['Volumes']:
	if not "Tags" in each_item  and each_item['State']=='available':
		print('Deleting ',each_item['VolumeId'])
		ec2_con_cli.delete_volume(VolumeId=each_item['VolumeId'])
print("Delete all unused and untagged volumes.")