"""
比较两个日期字符串大小
例： 2021-01-01 < 2021-01-02
"""

def compare_date(date1, date2):
    """
    if date2>date1 return True
    """
    year1, month1, day1 = date1.split("-")
    year2, month2, day2 = date2.split("-")
    if year2 > year1:
        return True
    elif year1 > year2:
        return False
    if month2 > month1:
        return True
    elif month1 > month2:
        return False
    if day2 > day1:
        return True
    elif day1 > day2:
        return False
    return True