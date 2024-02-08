# SMB Auto Discovery

## Author
Christopher Morehouse

## Description

The SMB Auto Discovery script retrieves a list of shares from an SMB server and automatically creates a data source connection in BigID for every share found. 
If a data source with the same share name already exists in BigID, the script will skip the creation of that data source.
The status of the data source creation is printed to the console as well as to a ds_import_status.log file that gets generated in the script's root directory.

## Script Configuration

Before running the script, you will need to generate a refresh token. Refresh tokens are obtained from the BigID UI under Administration -> Access Management.
You will need to create the refresh token under a user who has the proper roles configured for making API calls.
Refer to the BigID documentation for specifics on users and roles.

Once you have the refresh token, edit the env_config.yaml with the proper environment settings:

```yaml
SMB Server:
- host: "Hostname or IP of SMB Server"
- domain_name: "Domain name if required"
- username: "SMB server username"
- password: "SMB server password"

BigID Server:
- bigid_url: "URL of BigID server. example - https://bigidhost.com"
- bigid_auth_token: "Refresh token generated under BigID UI: Administration -> Access Management -> User"
- ds_prefix: "Prefix to be added to Data Source name"
- ds_sample_folders: "set to true by default" 
- ds_sample_folder_percent_size: "set to 5 by default"
- ds_sample_file_content: "set to true by default"
- ds_scanner_group: "set to 'default' by default"
```

Save the changes to the yaml config file and execute the script.

## Running the script

To execute the script using a python interpreter, you will first need to import the dependencies in the requirements.txt.
You can do this by running the following command: 

```sh
pip install -r requirements.txt
```

Once dependencies are installed, run the script with the following command: 

```sh
python main.py
```

## Build an executable binary for deployment

The preferred method for deployment is to build a self-contained package that includes all the dependencies as well as a run-time environment.
Using this method, users will not have to install python or any dependency libraries. They just edit the env_config.yaml and execute the binary.

cx_Freeze is used to build the binary and will need to be installed first in order to create the deployment package. For more information on cx_Freeze:

Project page: https://pypi.org/project/cx-Freeze/

Project documentation: https://cx-freeze.readthedocs.io/en/latest/

You can install cx_Freeze in a Python environment by running the following command:

```sh
pip install --upgrade cx_Freeze
```

Once cx_Freeze is installed you can continue with building the self-contained package by executing the build.sh script with the following command: 

```sh
sh build.sh
```

A "build" folder will get created that contains the directory with the executable and dependancy library. A tarball of the executable directory also gets created.
You can send this tarball to users or wherever the script will be deployed to.

The command to execute the binary: 

```sh
./smb-auto-discovery
```
