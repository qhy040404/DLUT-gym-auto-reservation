def get_fieldSaleId(data, area):
    data = data.split(area)
    data = data[1]
    data = data.split('"inBg"')
    data = data[0]
    data = data.strip(',')
    data = data.split(':')
    data = data[1]
    data = data.strip('"')
    return data
