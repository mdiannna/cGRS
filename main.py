from grslib import init_GRS, get_raw_data, get_data, init_server, stop_server_conn, stop_serial_conn
from grsNN import recogGest, trainGest
import sys
import win32api, win32con

def click(x,y):
    # win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

if __name__ == "__main__":
	command = sys.argv[2]
	com_port = sys.argv[1]
	try:
		server = sys.argv[3]
	except:
		server = "ws://localhost:5000/echo"

	init_GRS(com_port, server)
	init_server(server)

	# print "get data:"
	# print get_data()

	#trainGest("Vitea")
#	print "gesture:"
	print "gesture: " + recogGest()

	#if recogGest() == "click":
	#	print "click"
	# 	click(10, 10)

	stop_server_conn()
	stop_serial_conn()


