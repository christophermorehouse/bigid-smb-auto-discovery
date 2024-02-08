import requests
import modules.config as config

headers = {
  'Authorization': config.bigid_auth_token
}

# Get all ds connections from BigID
response = requests.get(config.bigid_url + '/api/v1/ds_connections', headers=headers).json()['ds_connections']

def get_ds_connections():
    # Create ds names list
    ds_names_list = []

    # Loop through json response, grab the ds name, and append to list
    for connection in response:
        if 'name' in connection:
            ds_names_list.append(connection['name'])

    return ds_names_list