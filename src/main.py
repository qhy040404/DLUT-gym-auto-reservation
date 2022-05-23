# import
import reserve

# userdata
user_id = ''  # 学号
passwd = ''  # 密码
area_name = ''  # 运动场馆名
place = ''  # 几号场
time = ''  # 时间段
mail_user = ''  # 不需要请删除单引号，并输入None
mail_pass = ''  # 输入邮箱授权码，不需要请删除单引号，并输入None

# userdata_example
# 以下为userdata段示例
'''
user_id = '20211234567'
passwd = '123456'
area_name = '乒乓'
place = '1号场'
time = '13:00-13:30'
mail_user = None
mail_pass = None
'''

# 可以选择的场馆请在reserve.py中查看

# main
user = reserve.Reserve(user_id, passwd, area_name, place, time, mail_user, mail_pass)
result = user.reserve()

if result is True:
    print('Success.')
else:
    print('Error.')
