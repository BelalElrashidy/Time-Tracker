from datetime import datetime
import psutil
import win32process, win32gui
distractions = ["YouTube", "league of legends", "Valorant", "Rainbow", "Minecraft","Visual Studio Code"]
w = win32gui
window_name = w.GetWindowText(w.GetForegroundWindow())
window_name = str(window_name)
start_time = datetime.now().replace(microsecond=0)
while True:
    new_window_name = w.GetWindowText(w.GetForegroundWindow())
    if window_name!=new_window_name:
        stop_time = datetime.now().replace(microsecond=0)
        for i in distractions:
            if str(new_window_name).lower().find(i.lower()) != -1:
                file = open("Tracker.txt",'a',encoding="utf-8")
                file.write("You have been distracted from the work by " + i +".\n")
                file.close()
                window_name = i       
        print(f"{window_name} Time Spent: {stop_time-start_time}")
        window_name =new_window_name
        start_time = datetime.now().replace(microsecond=0)