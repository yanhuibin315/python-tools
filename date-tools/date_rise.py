"""
日期递增
例如：
2021-01-01  --->  2021-01-02
"""

def date_rise_by_day(date):
    """
    日期按天递增操作
    :param date:
    :return:
    """
    MONTH_31 = ["01", "03", "05", "07", "08", "10", "12"]
    MONTH_30 = ["04", "06", "09", "11"]
    year = date.split("-")[0]
    month = date.split("-")[1]
    day = date.split("-")[2]
    if month in MONTH_31:
        if day == "31":
            if month == "12":
                return str(int(year)+1)+"-01-01"
            month = "0"+str(int(month)+1) if (int(month)+1) < 10 else str(int(month)+1)
            return year+"-"+month+"-01"
        day = "0"+str(int(day)+1) if (int(day)+1) < 10 else str(int(day)+1)
        return year+"-"+month+"-"+str(day)
    if month in MONTH_30:
        if day == "30":
            month = "0" + str(int(month) + 1) if (int(month) + 1) < 10 else str(int(month) + 1)
            return year + "-" + month + "-01"
        day = "0" + str(int(day) + 1) if (int(day) + 1) < 10 else str(int(day) + 1)
        return year + "-" + month + "-" + str(day)
    if day=="28":
        month = "0" + str(int(month) + 1) if (int(month) + 1) < 10 else str(int(month) + 1)
        return year+"-"+month+"-01"
    day = "0" + str(int(day) + 1) if (int(day) + 1) < 10 else str(int(day) + 1)
    return year + "-" + month + "-" + str(day)

def date_rise_by_month(date):
    """
    日期按月递增
    """
    # TO DO
    pass

def date_rise_by_year(date):
    """
    日期按年递增
    """
    # TO DO
    pass