import boto3
import sys
aws_mag_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

while True:
	print("This script performs the following actions on ec2 instance")
	print("""
		1. start
		2. stop
		3. terminate
		4. Exit""")
	opt=int(input("Enter your option: "))
	if opt==1:
            instance_id=input('Enter your EC2 Instance Id: ')
            #print(dir(my_req_instance_object))
            print("Starting ec2 instance.....")
            ec2_con_cli.start_instances(InstanceIds=[instance_id])
	elif opt==2:
            instance_id=input('Enter your EC2 Instance Id: ')
            print("Stopping ec2 instance.....")
            ec2_con_cli.stop_instances(InstanceIds=[instance_id])
	elif opt==3:
            instance_id=input('Enter your EC2 Instance Id: ')
            print("Terminating ec2 instance.....")
            ec2_con_cli.terminate_instances(InstanceIds=[instance_id])
	elif opt==4:
            print("Thank you for using this script")
            sys.exit()
	else:
	    print("Your option is invalid. Please try once again")