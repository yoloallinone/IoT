import serial 
def read_rfid():
    ser=serial.Serial("/dev/ttyUSB0")
    ser.baudrate=9600
    data=ser.read(12)
    ser.close()
    return data

while True:
    id=read_rfid()
    print(id)
    if id=='1E005C1E5B07':
        print("Access Granted")
    else:
        print("Access Denied")
    
