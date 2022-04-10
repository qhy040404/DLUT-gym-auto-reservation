# import
import reserve
import platform
import os
import sys

with open("config.conf","r") as config:
    configData = config.readlines()
    if len(configData) == 1:
        print('没有数据，正在启动配置生成器')
        if platform.system() == 'Windows':
            os.system('timeout 1 >nul && start ConfigGenerator.exe')
            sys.exit()
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            os.system('sleep 1 && ./ConfigGenerator')
            sys.exit()
        else:
            print('System Unknown.')
            sys.exit()
    configData.pop(0)

# user_id, passwd, area_name, place, time, mail_user = None, mail_pass = None
while len(userData) != 0:
    mail_user = None
    mail_pass = None

    userData = configData.pop(0).strip('\n').split()
    user_id = userData[0]
    passwd = userData[1]
    area_name = userData[2]
    place = userData[3]
    time = userData[4]
    if len(userData) == 5:
        pass
    elif len(userData) == 7:
        mail_user = userData[5]
        mail_pass = userData[6]
    else:
        print('Invalid Config.')
        sys.exit()

    user = reserve.Reserve(user_id, passwd, area_name, place, time, mail_user, mail_pass)
    result = user.reserve()
    if result is True:
        print('Success.')
    else:
        print('Error.')