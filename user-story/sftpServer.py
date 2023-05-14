import paramiko
import logging
import helper


def task():
    # set up SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connect to SFTP server
    ssh_client.connect(hostname='shell.puv.fi', username='e2000575', password='HOANlun1998', port=22)

    # open SFTP session
    sftp = ssh_client.open_sftp()

    # Change current directory
    sftp.chdir('/u/d/e2000575')

    # sftp.mkdir("incoming")
    # sftp.mkdir("processed")

    # Check current working directory
    path = sftp.getcwd()
    print("Current working directory" + path)

    # List all directories and files
    directory_incoming = sftp.listdir('./incoming')
    directory_processed = sftp.listdir('./processed')

    # Check the directory contains the csv file
    check_file_in = directory_incoming.__contains__('CompanyFile.csv')
    check_file_pro = directory_processed.__contains__('CompanyFile.csv')

    print("All files in folder processed: ", directory_processed)

    # Create a log file named result.log to check
    logging.basicConfig(filename="result.log", level=logging.INFO)

    if check_file_pro:
        get_timer = helper.get_time()
        logging.info("File ", directory_processed, "existed")
        logging.info(f"The data has been successfully transferred into database! Time: {get_timer}")

    else:
        get_timer = helper.get_time()
        logging.error("Error!")
        logging.info(f"This folder does not contain the file! Time: {get_timer}")
        logging.info(f"All files in folder incoming: {directory_incoming}.")
        print(f"Check file existed: {check_file_in} in folder incoming.")

    # close SFTP session and SSH client
    sftp.close()
    ssh_client.close()


# Clear the content of log file in the end of the day
def clear_log_file():
    log_file_path = './result.log'

    # Open log file and clear the content
    with open(log_file_path, "w") as log_file:
        log_file.write("")

# task()
# remove_log_file()
