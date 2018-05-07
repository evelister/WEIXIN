import time
from wxpy import *

bot = Bot(cache_path='wxpy.pkl')

def get(i):
    with open('晚安.txt', 'r', encoding='utf-8') as f:
        line = f.readlines()[i]
    return line

def send(i):
    myfriend = bot.friends().search('微信好友昵称')[0]
    myfriend.send(get(i))
    i += 1

def main():
    for i in range(3650):
        send(i)
        time.sleep(5)

if __name__ == '__main__':
    main()
