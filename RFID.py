import serial
def rfid_read():
    ser = serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 9600
    data = ser.read(12)
    ser.close()
    return data
try:
    while True:
        id = rfid_read()
        print(id)
        if (id =="1E005C1E5B07"):
            print("Access granted")
        else:
            print("Access denied")

except KeyboardInterrupt:
    print("stopped")
    
