import boto3

def send_message():
	sqs_client = boto3.client('sqs', region_name='us-east-1')
	queue_url = 'https://sqs.us-east-1.amazonaws.com/117793179715/myQueue'
	response = sqs_client.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageBody=(
            'Qual é o doce mais doce que o doce de batata doce?'
        )
    )
	print(response)

if __name__ == '__main__':
	response = send_message()