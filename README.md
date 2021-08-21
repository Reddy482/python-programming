## Steps to get the list of ami's from aws account
1. Download [python](https://www.python.org/downloads/) runtime from python offical page.
2. By default pip will be installed along with python if not download pip (pip is package installer)
3. install Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources ̉      from your Python scripts.

### Steps to build image and run container
   
1. docker image build --build-arg aws_access_key_id=$AWS_ACCESS_KEY_ID --build-arg aws_secret_access_key=$AWS_SECRET_ACCESS_KEY --tag <imageName> .
2. Before building the image "AWS_ACCESS_KEY_ID" and "AWS_SECRET_ACCESS_KEY" should be exported as environmental variables in docker host.
3. docker container run --name <containerName> -itd <imageName>
4. Output is displayed as "[{'ImageId': 'ami-005db969'}, {'ImageId': 'ami-005db969'}]"
