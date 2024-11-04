from flask import Flask, request
import threading
import os
import time

app = Flask(__name__)

def perform_action(action):
    time.sleep(0.2)
    if action == 'sleep':
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif action == 'shutdown':
        os.system("shutdown /s /f /t 0")
    elif action == 'restart':
        os.system("shutdown /r /f /t 0")
    elif action == 'lock':
        os.system("rundll32.exe user32.dll,LockWorkStation")

@app.route('/control', methods=['GET'])
def control():
    action = request.args.get('action')
    if action == 'sleep':
        threading.Thread(target=perform_action, args=('sleep',)).start()
        print("PC is going to sleep")
        return "PC is going to sleep", 200
    elif action == 'shutdown':
        threading.Thread(target=perform_action, args=('shutdown',)).start()
        print("PC is shutting down")
        return "PC is shutting down", 200
    elif action == 'restart':
        threading.Thread(target=perform_action, args=('restart',)).start()
        print("PC is restarting")
        return "PC is restarting", 200
    elif action == 'lock':
        threading.Thread(target=perform_action, args=('lock',)).start()
        print("PC is locking")
        return "PC is locking", 200
    else:
        print("Invalid action")
        return "Invalid action", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
