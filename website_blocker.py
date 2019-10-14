from datetime import datetime as dt
import time

# local file where hosts are stored
hosts = '/etc/hosts'
#hosts_temp = 'hosts'
redirect = '127.0.0.1'
# list of websites we want to block
block_list = ['www.reddit.com', 'www.twitter.com', 'https://twitter.com/' ]

while True:
    # check if current time is between 8 and 18h
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print('Working hours')
        # open and read the content of the hosts file
        with open(hosts,'r+') as file:
            content = file.read()
            # loop through the file, if sites are already in list pass, if not, add them
            for website in block_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + '  ' + website + '\n')
    else:
        with open(hosts, 'r+') as file:
            # content is now a list
            content = file.readlines()
            # place cursor on the start of the file
            file.seek(0)
            for line in content:
                # if blocked site not in line, write that line
                if not any(website in line for website in block_list):
                    file.write(line)
            # removes everything below our new written text
            file.truncate()

    time.sleep(120)
