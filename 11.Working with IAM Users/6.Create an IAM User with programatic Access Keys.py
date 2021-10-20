#!/bin/python
import boto3
from random import choice
import sys



def get_iam_client_object():
    session=boto3.session.Session(profile_name="dev_root")                                                                
    iam_client=session.client(service_name="iam",region_name="us-east-1")
    return iam_client

def main():
   iam_client=get_iam_client_object()
   Iam_user_name="dowithpython@gmail.com"

   PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
   try:
      iam_client.create_user(UserName=Iam_user_name)
   except Exception as e:
      if e.response['Error']['Code']=="EntityAlreadyExists":
          print "Already Iam User with {} is exist".format(Iam_user_name)
          sys.exit(0)
      else:
         print "Please verify the following error and retry"
         print e
         sys.exit(0)
   response = iam_client.create_access_key(UserName=Iam_user_name)
   print "IAM User Name={}".format(Iam_user_name)
   print "AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAcc
essKey'])

   iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)
   return None

if __name__=="__main__":
    main()
