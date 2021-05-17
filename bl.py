
import bluetooth
import time
bd_addr = "00:20:08:00:33:FB"
port = 1
time.sleep(1)
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
time.sleep(10)
sock.send("F")
time.sleep(1)
sock.close()