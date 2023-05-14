import schedule
import time
import sftpServer


def task():
    print(sftpServer.task())


def remove():
    sftpServer.clear_log_file()


# Execute the function task in sftpServer.py at 8:30 AM every day
schedule.every().days.at("08:30:00").do(task)

# Execute the function clear_log_file in sftpServer.py at the end of the day.
schedule.every().days.at("23:59:59").do(remove)

while True:
    schedule.run_pending()
    time.sleep(1)

