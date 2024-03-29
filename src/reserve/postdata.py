# import
import datetime


def getWeekday():
    today = datetime.date.today()
    week_day_map = {0: '星期一',
                    1: '星期二',
                    2: '星期三',
                    3: '星期四',
                    4: '星期五',
                    5: '星期六',
                    6: '星期日'
                    }
    return week_day_map.get(datetime.date.weekday(today))


def constructParaField():
    al = {
        '"deliveryTerminal"': '"门户端"',
        '"fieldSaleStatus"': '1',
        '"operator_role"': '"admin"',
        '"orgId"': '"c4f67f3177d111e986f98cec4bb1848c"',
        '"today"': '"' + str(datetime.date.today()) + '"',
        '"week"': '"' + getWeekday() + '"'
    }
    return '{' + ','.join([i + ':' + j for i, j in al.items()]) + '}'


def constructParaPlaceField(id):
    al = {
        '"fieldSaleId"': '"' + id + '"',
        '"operator_role"': '"admin"',
        '"orgId"': '"c4f67f3177d111e986f98cec4bb1848c"',
        '"today"': '"' + str(datetime.date.today()) + '"',
        '"week"': '"' + getWeekday() + '"'
    }
    return '{' + ','.join([i + ':' + j for i, j in al.items()]) + '}'


def orderChildListTemp(id, price, time, place_no, place, fieldName, x, y):
    al = {
        '"fieldSaleId"': '"' + id + '"',
        '"length"': '60',
        '"money"': '"' + str(int(price)) + '"',
        '"num"': '1',
        '"price"': str(price),
        '"status"': '0',
        '"step"': '30',
        '"time"': '"' + time + '"',
        '"place_no"': place_no,
        '"place"': place,
        '"date"': '"' + str(datetime.date.today()) + '"',
        '"fieldName"': fieldName,
        '"x"': x,  # 场地排列
        '"y"': y  # 时间排列
    }
    return '[{' + ','.join([i + ':' + j for i, j in al.items()]) + '}]'


def constructParaReserve(id, price, time, place_no, place, fieldName, x, y, sign):
    al = {
        '"fieldName"': fieldName,
        '"goodsParentType"': '"field定"',
        '"insurance"': '0',
        '"offMainSumPrice"': '"' + str(int(price)) + '"',
        '"operator_role"': '"admin"',
        '"orderBackPrice"': '0',
        '"orderChildListTemp"': orderChildListTemp(id, price, time, place_no, place, fieldName, x, y),
        '"orderMainId"': '""',
        '"orderMainSumHaspay"': '"' + str(int(price)) + '"',
        '"orderMainSumPrice"': '"' + str(int(price)) + '"',
        '"orderMains"': '[]',
        '"orderReturnSourceObj"': '{}',
        '"orderServiceChildList"': '[]',
        '"orgId"': '"c4f67f3177d111e986f98cec4bb1848c"',
        '"payCode"': '""',
        '"payType"': '"SMARTCARDPOS-ONLINE"',
        '"platform"': '"PCWEB"',
        '"printStatus"': '1',
        '"sign"': '"' + sign + '"',
        '"today"': '"' + str(datetime.date.today()) + '"',
        '"flreeCountFlag"': 'false'
    }
    return '{' + ','.join([i + ':' + j for i, j in al.items()]) + '}'


def constructParaSign():
    al = {
        '"operator_role"': '"admin"',
        '"orgId"': '"c4f67f3177d111e986f98cec4bb1848c"'
    }
    return '{' + ','.join([i + ':' + j for i, j in al.items()]) + '}'


def constructParaPay(payid):
    al = {
        '"orderMainId"': payid,
        '"orgId"': '"c4f67f3177d111e986f98cec4bb1848c"'
    }
    return '{' + ','.join([i + ':' + j for i, j in al.items()]) + '}'
