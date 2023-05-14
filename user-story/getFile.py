import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to SFTP server
ssh_client.connect(hostname='shell.puv.fi', username='e2000575', password='HOANlun1998', port=22)

# open SFTP session
sftp = ssh_client.open_sftp()

sftp.chdir('/u/d/e2000575')

remote_path = './incoming/CompanyFile.csv'
local_path = 'E:/User-Story/user-story/CompanyFile_A.csv'
sftp.get(remote_path, local_path)

sftp.close()
ssh_client.close()