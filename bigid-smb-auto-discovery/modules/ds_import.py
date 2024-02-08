import re, json, requests
import modules.config as config

headers = {
 'Content-Type': 'application/json',
  'Authorization': config.bigid_auth_token
}

def create_import(ds_dict):
    # Create a ds connection for every share name found on SMB server. Use the prefixed share name as the DS connection name.
    for ds_name, import_status in ds_dict.items():
        if import_status == 'true':
            # Remove prefix from share name to use as Shared Resource name within DS connection
            regex_string = config.ds_prefix + r' - (.*)'
            ds_name_no_prefix = re.search(regex_string, ds_name).group(1).strip()

            # Create the DS connection dictionary
            ds_connection = {
                "ds_connection": {
                    "name": ds_name,
                    "sharedResource": ds_name_no_prefix,
                    "is_encrypt_data": "false",
                    "enabled": "yes",
                    "tags": [],
                    "smbServer": config.smb_server_hostname,
                    "domain": config.domain_name,
                    "multiple_shares_enabled": "false",
                    "is_system_shares": "false",
                    "type": "smb",
                    "is_credential": "false",
                    "username": config.username,
                    "password": config.password,
                    "include_file_types": "true",
                    "scanner_group": "default",
                    "custom_fields": [],
                    "owners_v2": [],
                    "security_tier": "1",
                    "metadataAclScanEnabled": "false",
                    "dsAclScanEnabled": "false",
                    "is_ocr_enabled": "false",
                    "classification_is_enabled": "true",
                    "ner_classification_is_enabled": "true",
                    "Is_sample_folders": config.ds_sample_folders,
                    "folder_percent_to_sample": config.ds_sample_folder_percent_size,
                    "Is_sample_files": config.ds_sample_file_content,
                    "differential": "false",
                    "scanWindowName": [],
                    "notAddToScope": "true",
                }
            }

            # Convert the DS connection dictionary to JSON for import
            ds_connections_json = json.dumps(ds_connection, indent=4)

            # Import DS connection to BigID
            response = requests.request("POST", config.bigid_url + '/api/v1/ds_connections', headers=headers, data=ds_connections_json)
            print(response.text + '\" has been created')
        else:
            print(ds_name + ' has been skipped because it already exists')