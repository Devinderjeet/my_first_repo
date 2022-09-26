import boto3
import requests

def handler(event):
    lambda_client = boto3.client('lambda')
    resp = lambda_client.list_functions()
    for fn in resp['Functions']:
        n = fn['FunctionName']
        if n.startswith(event):
            print(n)

# handler('d')

def req():
    x = requests.get('https://www.google.com/search?q=gmail&rlz=1C1CHBF_enIN969IN969&oq=gmail&aqs=chrome.0.69i59l2j0i131i433i512l2j0i433i512j0i131i433i512j69i65j69i61.1799j0j7&sourceid=chrome&ie=UTF-8')
    print(x.status_code)
    print(x.text)

req()