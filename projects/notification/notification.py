from email import message
from turtle import title
from plyer import notification
import time

notify_text = "Hi, i am reminder. please smoke now!"

if __name__ == '__main__':
    while True:
        notification.notify(
            title = '*** SMOKE TIME ***',
            message = notify_text,
            app_icon = 'D:/laragon/www/python/projects/notification/notify.ico',
            timeout = 5
        )

        time.sleep(20)    