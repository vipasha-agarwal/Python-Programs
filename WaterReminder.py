import time
import os
# from win10toast import ToastNotifier
# toast = ToastNotifier()
# toast.show_toast(
#     "Notification",
#     "Hey Vipasha Drink water",
#     duration = 20,
#     icon_path = "icon.ico",
#     threaded = True,
# )


# Prepare the command as a string
cmd = "powershell -command \"$voice = New-Object -ComObject 'SAPI.SpVoice'; $voice.Speak('Hey Vipasha Drink Water'); New-BurntToastNotification -Text 'Notification Title', 'Hey Vipasha Drink Water'\""

# Execute the command
os.system(cmd)

