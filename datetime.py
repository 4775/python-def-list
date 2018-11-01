from datetime import datetime
from datetime import timedelta

#現在の時刻を取得
ima = datetime.now()
print(ima)

now = datetime.now()
print(now.year, '年', sep='')
print(now.month, '月', sep='')
print(now.day, '日', sep='')
print(now.hour, '時', sep='')
print(now.minute, '分', sep='')
print(now.second, '秒', sep='')

#日付を作成
one_day = datetime(, 1, 31)
print(one_day)

one_datetime = datetime(2016, 5, 5, 14, 15, 30)
print(one_datetime)

#日付を文字列に変換Ω
one_day = datetime(2016, 8, 11)

str_one_day = one_day.strftime('%Y/%m/%d')
print(str_one_day)

str_time = one_day.strftime('%H:%M:%S')
print(str_time)

#文字列を日付に変換
str_date = '2016年12月31日'
one_date = datetime.strptime(str_date, '%Y年%m月%d日')
print(one_date)

one_day = datetime.strptime(str_day, '%Y/%m/%d %H:%M:%S')
print(one_day)

#〇〇前後の日付を取得
olympic_day = datetime(2020, 7, 24)
before_2days = olympic_day - timedelta(days=2)
# 表示
print(before_2days.strftime('%Y-%m-%d'))
