'''this python function is to fetch list of ami's which are tagged with specific key value'''

import boto3
import os

def get_ami_details(region):
    filters = [
        {
            'Name':'tag:allowed_ami', #here Name can be replaced with any other tags
            'Values':['True']         #Here values can be replaced with any other values
        }
    ]
    response = boto3.client('ec2',
                        region_name=region,
                        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
                       )
    
    ami_details = response.describe_images(Filters = filters)
    ami_detailed_list =[]
    ami_ids = {}

    for image in ami_details['Images']:
        ami_ids.update({'ImageId':image['ImageId']})
        ami_detailed_list.append(ami_ids)
    
    print(ami_detailed_list)


'''Get the details from us-east-1 region'''
if __name__=='__main__':
    get_ami_details('us-east-1')

