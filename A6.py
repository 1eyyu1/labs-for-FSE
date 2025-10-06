sec = int(input("Введите количество секунд:"))

hours = (sec//3600) % 24
minutes = (sec%3600) // 60
seconds = sec % 60

print("{}:{:02}:{:02}".format(hours,minutes,seconds))