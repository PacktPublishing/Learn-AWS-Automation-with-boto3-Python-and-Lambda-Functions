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
            my_req_instance_object=ec2_con_re.Instance(instance_id)
            #print(dir(my_req_instance_object))
            print("Starting ec2 instance.....")
            my_req_instance_object.start()
	elif opt==2:
            instance_id=input('Enter your EC2 Instance Id: ')
            my_req_instance_object=ec2_con_re.Instance(instance_id)
            print("Stopping ec2 instance.....")
            my_req_instance_object.stop()
	elif opt==3:
            instance_id=input('Enter your EC2 Instance Id: ')
            my_req_instance_object=ec2_con_re.Instance(instance_id)
            print("Terminating ec2 instance.....")
            my_req_instance_object.terminate()
	elif opt==4:
            print("Thank you for using this script")
            sys.exit()
	else:
	    print("Your option is invalid. Please try once again")
