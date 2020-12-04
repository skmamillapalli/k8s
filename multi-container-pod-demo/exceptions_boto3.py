import boto3, botocore
cfn_client=boto3.client('cloudformation')

try:
    cfn_client.describe_stacks(StackName='test-stack')
except botocore.exceptions.ClientError as e:
    if 'does not exist' in e.response.get('Error', {}).get('Message', ''):
        print('stack does not exist')
    print(e.response['Error']['Message'])

print('hello')

    