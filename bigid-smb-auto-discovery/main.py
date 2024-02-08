import os, time, datetime
import modules

# Set script path and directory
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

# Get all shares from SMB server
print('enumerating SMB server...')
smb_list = modules.get_smb_shares(modules.smb_server_hostname, modules.username, modules.password)

# Get all DS connections from BigID
print('getting list of data connection from BigID...')
ds_list = modules.get_ds_connections()

# Create dictionary of smb shares and specify if they exist or don't exist in BigID
ds_dict = {}

for status in smb_list:
    if status not in ds_list:
        ds_dict[status] = 'true'
    else:
        ds_dict[status] = 'false'

# Create DS connection JSON and import into BigID
print('creating data connections in BigID...')
modules.create_import(ds_dict)

created_count = 0
not_created_count = 0

# Write the status of DS connections to log file
with open(dir_path + '/ds_import_status.log', 'w') as f:
    for key, value in ds_dict.items():
        if value == 'true':
            f.write('Created: \"' + '%s' % key + '\"\n')
            created_count = created_count + 1
        else:
            f.write('Not created. Already Exists: \"' + '%s' % key + '\"\n')
            not_created_count = not_created_count + 1
    # Add timestamp to end of file
    ts = time.time()
    f.write('\nLogtime: \"' + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') + '\"')

print('\nNumber of new data connections created: ' + str(created_count))
print('Number data connections not created because they already exist in BigID: ' + str(not_created_count))
print('The list of data connections and their creation status has been logged in ds_import_status.log')