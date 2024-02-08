import socket
from smb.SMBConnection import SMBConnection
import modules.config as config

# Get hostname of machine running this script
client_name = socket.gethostname()

# Get list of SMB Shares
def get_smb_shares(server, username, password):
    conn = SMBConnection(username, password, client_name, server, domain = config.domain_name, use_ntlm_v2 = True)
    
    # Connect to the SMB server
    conn.connect(server, 139)
    
    # Retrieve the list of available shares
    shares = conn.listShares()

    # Disconnect from the SMB server
    conn.close()
    
    # Create share names lists
    shares_list = []

    for share in shares:
        # Exclude hidden shares
        if not share.isSpecial:
            # Add non-hidden share names to list and add prefix to name
            shares_list.append(config.ds_prefix + ' - ' + share.name)
            
    return shares_list