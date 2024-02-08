import requests
import modules.config as config

def get_access_token():

    headers = {
        'Content-Type': 'application/json',
        'Authorization': config.refresh_token
        }
    
    system_token = requests.request("GET", config.bigid_url + '/api/v1/refresh-access-token', headers=headers).json()['systemToken']

    return system_token