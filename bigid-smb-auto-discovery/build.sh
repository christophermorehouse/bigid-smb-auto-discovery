#!/bin/bash

python3 setup.py build_exe

# Remove cf_Freeze license
rm build/smb-auto-discovery-script/frozen_application_license.txt

# Create application tarball for deployment
cd build
tar -zcvf smb-auto-discovery-script.tar.gz smb-auto-discovery-script