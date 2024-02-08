import ipaddress, socket, yaml, os
import modules.create_access_token as access_token

# Set parent directory
path = os.path.abspath(__file__)
dir_path = os.path.dirname(os.path.dirname(path))

# Get configuration from yaml file
try:
    # Run this if executing from cx_Freeze binary
    with open(dir_path + '/../env_config.yaml', "r") as f:
        config_yaml = yaml.safe_load(f)
except:
    #Run this if executing from python interpreter
    with open(dir_path + '/env_config.yaml', "r") as f:
        config_yaml = yaml.safe_load(f)

print('env_config.yaml found in: ' + dir_path + '/')

# Set global variables with values from yaml file
smb_server = config_yaml['SMB Server'][0]['host']
domain_name = config_yaml['SMB Server'][1]['domain_name']
username = config_yaml['SMB Server'][2]['username']
password = config_yaml['SMB Server'][3]['password']
bigid_url = config_yaml['BigID Server'][0]['bigid_url']

refresh_token = config_yaml['BigID Server'][1]['bigid_auth_token']
bigid_auth_token = access_token.get_access_token()

ds_prefix = config_yaml['BigID Server'][2]['ds_prefix']
ds_sample_folders = config_yaml['BigID Server'][3]['ds_sample_folders']
ds_sample_folder_percent_size = config_yaml['BigID Server'][4]['ds_sample_folder_percent_size']
ds_sample_file_content = config_yaml['BigID Server'][5]['ds_sample_file_content']
ds_scanner_group = config_yaml['BigID Server'][6]['ds_scanner_group']

# Check if smb server is an ip address or a hostname
try:
    ipaddress.ip_address(smb_server)
    smb_server_hostname = socket.gethostbyaddr(smb_server)[0]
except ValueError:
    smb_server_hostname = smb_server