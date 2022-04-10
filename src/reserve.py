# import
import sso
import smtplib
from email.mime.text import MIMEText
import traceback
import postdata
import ProcessData

class Reserve(object):
    def __init__(self, user_id, passwd, area_name, place, time, mail_user = None, mail_pass = None):
        self.user_id = user_id
        self.passwd = passwd
        self.area_name = area_name
        self.area_map = {'篮球': '"icon":"#icon-lanqiu",', '武术散打': '"icon":"#icon-wushu",',\
                         '舞蹈': '"icon":"#icon-wudao",', '乒乓': '"icon":"#icon-pingpangqiuyundongmianxing",',\
                         '健美操': '"icon":"#icon-jianmeicao",', '台球': '"icon":"#icon-taiqiu",'
                        }
        self.area = self.area_map.get(self.area_name)
        self.place = place
        self.time = time
        self.mail_user = mail_user
        self.mail_pass = mail_pass

    def send_email(self, success = False):
        if self.mail_pass == None or self.mail_user == None:
            return
        else:
            # get smtp server
            sender = self.mail_user
            receiver = self.mail_user
            mail_temp_data = self.mail_user.split('@')
            mail_host_pre = 'smtp.'
            mail_host = mail_host_pre + mail_temp_data[1]

            print("Sending email...")

            if success:
                context = '预约成功，' + self.area_name + ' ' + self.place + ' ' + self.time
            else:
                context = '没约到'

            message = MIMEText(context, 'plain', 'utf-8')
            message['Subject'] = '体育馆预定'
            message['From'] = sender
            message['To'] = receiver

            try:
                smtpObj = smtplib.SMTP_SSL(mail_host,465)
                smtpObj.login(self.mail_user,self.mail_pass)
                smtpObj.sendmail(sender,receiver,message.as_string())
                smtpObj.quit()
                print('Sending Success.')
            except smtplib.SMTPException as e:
                print('Sending Failed',e)

    def reserve(self):
        # define const url
        areas_url = 'https://tycg.dlut.edu.cn/diantuo/fieldSale/listApiFieldSaleNew1.do'
        place_url = 'https://tycg.dlut.edu.cn/diantuo/fieldSale/listFieldSale.do'

        s = sso.login(self.user_id, self.passwd)
        fieldSaleId = s.post(areas_url, postdata.constructParaField(), headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                                  'Content-Type': 'application/json'}).text
        fieldSaleId = ProcessData.get_fieldSaleId(fieldSaleId, self.area)
