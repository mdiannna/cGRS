from grslib import init_GRS, get_raw_data, get_data, init_server, stop_server_conn, stop_serial_conn
from grsNN import recogGest, trainGest
import sys, time
import win32api, win32con

def click(x,y):
    # win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

SAMPLES = 10

if __name__ == "__main__":
	command = sys.argv[2]
	com_port = sys.argv[1]

	init_GRS(com_port, server)

	for i in range(0, SAMPLES):
		gest = recogGest()
		print "----- Recognized gesture:  " + gest
		if gest == "click":
			print "click"
			click(10, 10)
		time.sleep(2)

	stop_serial_conn()


