# import
import sso
import smtplib
from email.mime.text import MIMEText
import postdata
import ProcessData
import sys

class Reserve(object):
    def __init__(self, user_id, passwd, area_name, place, time, mail_user = None, mail_pass = None):
        self.user_id = user_id
        self.passwd = passwd
        self.area_name = area_name
        self.area_map = {'篮球': '"icon":"#icon-lanqiu",', '武术散打': '"icon":"#icon-wushu",',\
                         '舞蹈': '"icon":"#icon-wudao",', '乒乓': '"icon":"#icon-pingpangqiuyundongmianxing",',\
                         '健美操': '"icon":"#icon-jianmeicao",', '台球': '"icon":"#icon-taiqiu",'
                        }
        self.price_map = {'武术散打': 40.00,\
                         '舞蹈': 40.00, '乒乓': 2.00,\
                         '健美操': 40.00, '台球': 2.00
                        }
        self.area = self.area_map.get(self.area_name)
        self.price = self.price_map.get(self.area_name)
        self.place = place
        self.place_map = {'1号场': '0', '2号场': '1', '3号场': '2', '4号场': '3', '5号场': '4', '6号场': '5',\
                          '7号场': '6', '8号场': '7', '9号场': '8', '10号场': '9', '11号场': '10', '12号场': '11',\
                          '13号场': '12', '14号场': '13', '15号场': '14', '16号场': '15', '17号场': '16', '18号场': '17',\
                          '19号场': '18', '20号场': '19', '21号场': '20', '22号场': '21', '23号场': '22', '24号场': '23',\
                          '25号场': '24', '26号场': '25', '27号场': '26', '28号场': '27', '29号场': '28', '30号场': '29', 
                         } #篮球馆好像不一样，待补充
        self.x = self.place_map.get(self.place)
        self.place = '"' + self.place + '"'
        self.time = time
        self.time_map = {'13:00-13:30': 1, '13:30-14:00': 2, '14:00-14:30': 3, '14:30-15:00': 4,\
                         '15:00-15:30': 5, '15:30-16:00': 6, '16:00-16:30': 7, '16:30-17:00': 8,\
                         '17:00-17:30': 9, '17:30-18:00': 10, '18:00-18:30': 11, '18:30-19:00': 12,\
                         '19:00-19:30': 13, '19:30-20:00': 14, '20:00-20:30': 15, '20:30-21:00': 16,\
                         '21:00-21:30': 17
                        }
        self.y = str(self.time_map.get(self.time))
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.field_map = {'篮球': '"篮球馆(学生)"', '武术散打': '"武术散打馆(学生)"',\
                          '舞蹈': '"舞蹈馆(学生)"', '乒乓': '"乒乓球(学生)"',\
                          '健美操': '"健美操馆(学生)"', '台球': '"台球(学生)"'
                         }
        self.fieldName = self.field_map.get(self.area_name)

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
        sign_url = 'https://tycg.dlut.edu.cn/diantuo/createSign.do'
        addOrder_url = 'https://tycg.dlut.edu.cn/diantuo/addOrder.do?sign='
        pay_url = 'https://tycg.dlut.edu.cn/diantuo/pay/yuLanOnLinePay.do'

        s = sso.login(self.user_id, self.passwd)
        fieldSaleId = s.post(areas_url, postdata.constructParaField(), headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                                                'Content-Type': 'application/json'}).text
        fieldSaleId = ProcessData.get_fieldSaleId(fieldSaleId, self.area)
        place_detail_status = s.post(place_url, postdata.constructParaPlaceField(fieldSaleId), headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                                                                        'Content-Type': 'application/json'}).text

        place_detail_status = place_detail_status.split(',')
        place_detail_status = (':').join(place_detail_status).split(':')
        place_count = place_detail_status.count('"place_no"')
        place_no = None
        if place_count is 1:
            place_no = place_detail_status[place_detail_status.index('"place_no"') + 1]
            place_val = place_detail_status[place_detail_status.index('"place"') + 1]
            if place_val == self.place:
                pass
            else:
                print('Userdata is not equal to validate data. Exit.')
                sys.exit()
        else:
            for i in range(place_count):
                place_val = place_detail_status[place_detail_status.index('"place"') + 1]
                if place_val == self.place:
                    place_no = place_detail_status[place_detail_status.index('"place_no"') + 1]
                else:
                    place_detail_status.remove('"place_no"')
                    place_detail_status.remove('"place"')
        if place_no == None:
            print('Cannot find userdata in post.text. Exit.')
            sys.exit()

        sign = s.post(sign_url, postdata.constructParaSign(), headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                                                 'Content-Type': 'application/json'}).text.strip('}').split(':')
        sign = sign[1].strip('"')

        orderMainId = s.post(addOrder_url, postdata.constructParaReserve(fieldSaleId, self.price, self.time, place_no, self.place, self.fieldName, self.x, self.y, sign), headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                                                                                                                                                   'Content-Type': 'application/json'}).text.strip('{').split(',')
        orderMainId = orderMainId[0].split(':')
        orderMainId = orderMainId[1]

        payment = s.post(pay_url, postdata.constructParaPay(orderMainId), headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                                                   'Content-Type': 'application/json'}).text.strip('}').split(',')
        payment = payment[len(payment) - 1]

        if payment == '"message":"支付成功"':
            self.send_email(success = True)
            return True
        else:
            self.send_email(success = False)
            return False