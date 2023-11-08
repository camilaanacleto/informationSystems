import json

def lambda_handler(event, context):
    body = event.get('body')

    if body is not None:
        data = json.loads(body)
        data['nome'] = 'Camiii'
    else:
        data = {'nome': 'Camii'}

    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
