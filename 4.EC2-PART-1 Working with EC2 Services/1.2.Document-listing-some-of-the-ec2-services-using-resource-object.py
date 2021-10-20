import boto3
from pprint import pprint
aws_mag_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
'''
for each_instance in ec2_con_re.instances.all():
	#print(dir(each_instance))
	print("The Image Id is: {}\nThe Instance Id Is: {}\nThe Instance Launch Time is: {}".format(each_instance.image_id,each_instance.instance_id,each_instance.launch_time.strftime("%Y-%m-%d")))
	print("-------------------")
'''
for each_volume in ec2_con_re.volumes.all():
	#print(dir(each_volume))
	print("The volume id is: {}\nThe AvailabilityZone is: {}\nThe VolumeType is: {}".format(each_volume.volume_id,each_volume.availability_zone,each_volume.volume_type))
	print("-----------------------------")
	 
