import boto3
import csv
aws_mag_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
cnt=1
csv_ob=open("inventory_info.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Privat_Ip'])
for each in ec2_con_re.instances.all():
	print(cnt,each,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address)
	csv_w.writerow([cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address])

	cnt+=1
csv_ob.close()