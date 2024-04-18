import boto3

# Cria uma sessão com as credenciais
session = boto3.Session(
    aws_access_key_id='YOUR_ID',
    aws_secret_access_key='YOUR_ACESS_KEY',
)

# Conecta ao S3
s3 = session.resource('s3')

# Imprime buckets e seus arquivos
for bucket in s3.buckets.all():
    print("Bucket name:", bucket.name)
    for key in bucket.objects.all():
        print(f'\t', key.key)
