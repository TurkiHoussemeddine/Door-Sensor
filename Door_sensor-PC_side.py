import bluetooth
import os
import time

bd_addr = "98:D3:71:FD:B4:02"   # HC-06 @

port = 1    
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )    # set-up BT socket
sock.connect((bd_addr, port))   # connect to HC-06
print('Connected')  # print something to confirm



while True: 
    data = sock.recv(1024)  # collect received byte
    data = data.decode('ascii') # transform to ASCII form
    if(data == '0') or (data == '1'):       
        print(data)     # for debug
    if data == '0':    # if door detected (door is open)
        os.system('nircmd.exe mutesysvolume 1')    # use nircmd software through cmd line to mute pc
        os.system('nircmd.exe lockws')      # use nircmd software through cmd line to lock pc
        os.system('nircmd.exe monitor off')  # use nircmd software through cmd line to turn monitor off
        time.sleep(10)  # wait 10s 