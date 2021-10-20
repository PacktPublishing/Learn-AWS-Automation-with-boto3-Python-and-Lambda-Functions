import boto3 
import time
aws_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")
'''
my_inst_ob=ec2_con_re.Instance("i-002d4110f1199166f")
print("Starting given instance....")
my_inst_ob.start()
my_inst_ob.wait_until_running()  #Resource waiter waits for 200sec(40 checks after every 5 sec)
print("Now your instance is up and running")
'''
'''
print("Starting ec2 instace...")
ec2_con_cli.start_instances(InstanceIds=['i-002d4110f1199166f'])
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-002d4110f1199166f']) #40 checks after every 15 sec
print("Now your ec2 instace is up and running")
'''
my_inst_ob=ec2_con_re.Instance("i-002d4110f1199166f")
print("Starting given instance....")
my_inst_ob.start()
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-002d4110f1199166f'])
print("Now your ec2 instace is up and running")











'''
while True:
	my_inst_ob=ec2_con_re.Instance("i-002d4110f1199166f")
	print("The current status of ec2 is: ",my_inst_ob.state['Name'])
	if my_inst_ob.state['Name']=="running":
		break
	print("Wating to get running status....")
	time.sleep(5)
'''
