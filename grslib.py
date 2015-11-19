# function list:
# def init_hardware(com_port,baud_rate):
# def init_server():
# def init_GRS():
# def get_raw_data():
# def get_data():
# def send_raw_data_to_server():
# def send_data_to_server():
# def get_data_for_calib():
# def save_raw_data()
# # def test_calib():
# def stop_server_conn():
# def stop_serial_conn():


import time
import sys
import serial
import websocket
# from websocket import create_connection
# from grsNN import trainGest, recogGest

ser = None
ws = None


def init_hardware(com_port,baud_rate):
    global ser;
    if baud_rate <= 0:
        baud_rate = 19200

    try:
        ser = serial.Serial('COM'+com_port,baud_rate,timeout=0.1)
    except:
        try:
           serial.Serial()
           serial.port = '/dev/ttyUSB'+com_port
           serial.baudrate = baud_rate
           serial.timeout = 0.1
           ser.open()
           print "/dev/ttyUSB"+com_port
        except:
            print "Cannot open COM Port"
            sys.exit(1)

    print "------------------------------------------"
    print "Init"
    usart = ser.readline()
    if not usart:
        print "Communication failed (USART)."
        sys.exit(1)
    print "USART init done."

    for i in range(0, 4):
        initData = ser.readline()
        if not initData:
            print "Sensor initialization failed."
            sys.exit(1)
        else:
            print initData
    print "Initialization done."
    print "------------------------------------------"


def init_server(server):
    global ws;
    try:
            ws = websocket.create_connection(server)
    except:
        try:
            server = "ws://localhost:5000/echo"
        except:
            print "Cannot connect to WebSocket Server"
            sys.exit(2)
    test_server_conn()



def init_GRS(com_port, server):
    init_hardware(com_port, 19200)
    init_server(server)


def save_raw_data(ser, samples):
    f1 = open("s0_raw.txt", "w")
    f2 = open("s1_raw.txt", "w")
    f3 = open("s2_raw.txt", "w")
    f4 = open("s3_raw.txt", "w")
    f5 = open("s4_raw.txt", "w")
    f6 = open("s5_raw.txt", "w")

    for i in range(0, samples):
        sensorData = get_raw_data()
        f1.write(sensorData[0] + "\n")
        f2.write(sensorData[1] + "\n")
        f3.write(sensorData[2] + "\n")
        f4.write(sensorData[3] + "\n")
        f5.write(sensorData[4] + "\n")
        f6.write(sensorData[5] + "\n")

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
 

def get_raw_data():
        global ser
        filter_N = 5
        frequency = 600 * filter_N
        period = 1.0/frequency
        total = 0
        fail = 0
        rate = 0
        SAMPLES = 2000;
        
        
        ser.write("G")
        print "~~~~~~~~~~~~~Command:Get raw data~~~~~~~~~~~~~~~~~~~"
        
        tick = time.time()
        sums = [0.0] * 18
        curr_fails = 0

        data = ser.readline().replace("\n","").replace("\r","")
        # print data,data[0],data[len(data)-1]
        if not data or data[0] != 's' or data[len(data)-1] != 'f':
                fail+=1
                curr_fails += 1
                print "Check sensors or just late data"
                print data
                # !!!!!!!!!!!!
                # continue
        data = data[1:-1]
        print data
        print "Fail rate: %s\n" % rate
        data.replace(" ", "\t");
        sensorData = data.split(';')
        print sensorData
        print "Frequ: %s" % (1.0/ (time.time()-tick+0.0000001))
        tick = time.time()

        return sensorData


def get_data():
        print " call"
        global ser
        filter_N = 5
        frequency = 600 * filter_N
        period = 1.0/frequency
        total = 0
        fail = 0
        rate = 0

        tick = time.time()
        sums = [0.0] * 18
        curr_fails = 0

        ser.write("S")
        data = ser.readline().replace("\n","").replace("\r","")
        
        print data
        # print data,data[0],data[len(data)-1]
        if not data or data[0] != 's' or data[len(data)-1] != 'f':
                fail+=1
                curr_fails += 1
                print "Check sensors or just late data"
                # !!!!!!!!!!!!
                # continue
        data = data[1:-1]

    
        print "Fail rate: %s\n" % rate

        print "Frequ: %s" % (1.0/ (time.time()-tick+0.0000001))
        tick = time.time()
        data = data.split(";")
        print data
        return data


def send_raw_data_to_server():
    global ws
    data = get_raw_data()
    ws.send(data)


def send_data_to_server():
    global ws
    data = get_data()
    ws.send(data)

def get_data_for_calib():
    save_raw_data()

def calibrate():
        global ser
        filter_N =      5
        frequency = 600 * filter_N
        period = 1.0/frequency
        total = 0
        fail = 0
        rate = 0
        calibr = ""
        
        f_calibrate = open("calibration.txt", "r").readlines()

        ser.write("C")
        print "Debug calibrate"
        data = ser.readline();
        if not data: 
                print "Check sensors or just late data"
        print data
                
        print "Calibrated data from file:"
        for line in f_calibrate:
                calibr = line
                print "calibration=", calibr
                calibr = calibr.replace("\n", "")
                calibr = calibr.replace(" ", "")
                ser.write(calibr+"\n\r")
                data = ser.readline()
                print data
                print "----------------------"
        print "All data for calibration sent"
        print "\n\r"


def test_server_conn():
    global ws
    try:
        ws.send("Hello server!")
        print "Data sent"
        ws.receive()
    except:
        print "Server connection error"

    
def stop_server_conn():
    global ws
    try:
        ws.close()
    except:
        "Closing server connection error"


def stop_serial_conn():
    global ser
    ser.close()


# def test_calib():