import time
import data
import map
import datetime

data.ini()
start = datetime.datetime.now()
# print(start)
x = datetime.datetime.now() - datetime.timedelta(hours=1)
map.draw_map(data.get_data(x, start))


while True:
    time.sleep(60)
    current = datetime.datetime.now()
    a = data.get_data(start, current)
    map.draw_map(a)


