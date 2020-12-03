import boto3

cm = boto3.client('amscm', region_name='us-east-1')
print(cm)

