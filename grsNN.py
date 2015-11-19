# Name: grsNN
# Author: Diana Marusic 
# Country of origin: Republic of Moldova
# Date: 15 nov 2015
# Project: (c)GRS
# Description: grsNN is a library created for (c)GRS system. It can create a pseudo neural
# network, train it and recognize trained gestures.
#
# Tests: none
#
# ---------Functions:---------------
# deleteAllGests() - deletes all gestures from the database/storage file
# trainGest(gesture_name) - function for "learning" a new gesture
# recogGest() - function that Recognizes the most probable gesture from the trained ones


import os
from grslib import init_GRS, get_data, init_server, stop_server_conn, stop_serial_conn


def N0(x0, y0, z0, wx0, wy0, wz0):
	return x0*wx0 + y0*wy0 + z0*wz0;

def N1(x1, y1, z1, wx1, wy1, wz1):
	return x1*wx1 + y1*wy1 + z1*wz1;

def N2(x2, y2, z2, wx2, wy2, wz2):
	return x2*wx2 + y2*wy2 + z2*wz2;

def N3(x3, y3, z3, wx3, wy3, wz3):
	return x3*wx3 + y3*wy3 + z3*wz3;

def N4(x4, y4, z4, wx4, wy4, wz4):
	return x4*wx4 + y4*wy4 + z4*wz4;

def N5(x5, y5, z5, wx5, wy5, wz5):
	return x5*wx5 + y5*wy5 + z5*wz5;

def xs(x0, x1, x2, x3, x4, x5, w0, w1, w2, w3, w4, w5):
	return x0*w0 + x1*w1 + x2*w2 + x3*w3 + x4*w4 + x5*w5;

def ys(y0, y1, y2, y3, y4, y5, w0, w1, w2, w3, w4, w5):
	return y0*w0 + y1*w1 + y2*w2 + y3*w3 + y4*w4 + y5*w5;

def zs(z0, z1, z2, z3, z4, z5, w0, w1, w2, w3, w4, w5):
	return z0*w0 + z1*w1 + z2*w2 + z3*w3 + z4*w4 + z5*w5;

def deleteAllGests():
	os.remove("trained.txt");

def trainGest(gesture_name):
	SAMPLES = 10
	path = "Gestures/"
	gesture = gesture_name;

	
   	print "--- training gesture " + gesture_name + " ---"

   	# Init output file
	output = open(path + gesture + "/" + "out.txt", "w+")
	output.write("---N0---N1---N2---N3---N4---N5---xs---ys---zs---")
	output.write("\n")

	# Init trained_gestures file
	trained = open("trained.txt", "r+")
	if not trained.read(1):
		  trained.close()
		  trained = open("trained.txt", "w+")
		  trained.write("- Name ----N0---N1---N2---N3---N4---N5---xs---ys---zs---")
		   
	trained.close()
	trained = open("trained.txt", "a+")
	trained.write("\n")
	
	# Init  dependent variables
	sum_N0 = 0;
	sum_N1 = 0;
	sum_N2 = 0;
	sum_N3 = 0;
	sum_N4 = 0;
	sum_N5 = 0;
	sum_xs = 0;
	sum_ys = 0;
	sum_zs = 0;
	min_N0 = 70000;
	min_N1 = 70000;
	min_N2 = 70000;
	min_N3 = 70000;
	min_N4 = 70000;
	min_N5 = 70000;
	min_xs = 70000;
	min_ys = 70000;
	min_zs = 70000;
	max_N0 = -80000;
	max_N1 = -80000;
	max_N2 = -80000;
	max_N3 = -80000;
	max_N4 = -80000;
	max_N5 = -80000;
	max_xs = -80000;
	max_ys = -80000;
	max_zs = -80000;

	k = 0
	for i in range(0, SAMPLES):
			print "Sensor "
			sensorData = get_data()


			print "SAMPLE" + str(i)

			print sensorData[0]
			print sensorData[1]
			dataS0 = sensorData[0].split()
			dataS1 = sensorData[1].split()
			dataS2 = sensorData[2].split()
			dataS3 = sensorData[3].split()
			dataS4 = sensorData[4].split()
			dataS5 = sensorData[5].split()
			print dataS1[0]

			x0 = float(dataS0[0])
			y0 = float(dataS0[1])
			z0 = float(dataS0[2])
			x1 = float(dataS1[0])
			y1 = float(dataS1[1])
			z1 = float(dataS1[2])
			x2 = float(dataS2[0])
			y2 = float(dataS2[1])
			z2 = float(dataS2[2])
			x3 = float(dataS3[0])
			y3 = float(dataS3[1])
			z3 = float(dataS3[2])
			x4 = float(dataS4[0])
			y4 = float(dataS4[1])
			z4 = float(dataS4[2])
			x5 = float(dataS5[0])
			y5 = float(dataS5[1])
			z5 = float(dataS5[2])

			# Calculate and print results
			N0_out = N0(x0, y0, z0, 1, 1, 1)
			N1_out = N1(x1, y1, z1, 1, 1, 1)
			N2_out = N2(x2, y2, z2, 1, 1, 1)
			N3_out = N3(x3, y3, z3, 1, 1, 1)
			N4_out = N4(x4, y4, z4, 1, 1, 1)
			N5_out = N5(x5, y5, z5, 1, 1, 1)
			xs_out = xs(x0, x1, x2, x3, x4, x5, 1, 1, 1, 1, 1, 1)
			ys_out = ys(y0, y1, y2, y3, y4, y5, 1, 1, 1, 1, 1, 1)
			zs_out = zs(z0, z1, z2, z3, z4, z5, 1, 1, 1, 1, 1, 1)
			
			print "N0:"
			print N0_out
			print "N1:"
			print N1_out
			print "N2:"
			print N2_out
			print "N3:"
			print N3_out
			print "N4:"
			print N4_out
			print "N5:"
			print N5_out
			print "xs:"
			print xs_out
			print "ys:"
			print ys_out
			print "zs:"
			print zs_out

			sum_N0 += N0_out
			sum_N1 += N1_out
			sum_N2 += N2_out
			sum_N3 += N3_out
			sum_N4 += N4_out
			sum_N5 += N5_out
			sum_xs += xs_out
			sum_ys += ys_out
			sum_zs += zs_out

			if min_N0 > N0_out:
				min_N0 = N0_out
			if min_N1 > N1_out:
				min_N1 = N1_out
			if min_N2 > N2_out:
				min_N2 = N2_out
			if min_N3 > N3_out:
				min_N3 = N3_out
			if min_N4 > N4_out:
				min_N4 = N4_out
			if min_N5 > N5_out:
				min_N5 = N5_out
			if min_xs > xs_out:
				min_xs = xs_out
			if min_ys > ys_out:
				min_ys = ys_out
			if min_zs > zs_out:
				min_zs = zs_out

			print "max_n1 = " + str(max_N1)
			print "n1_out= " + str(N1_out)
			if max_N0 < N0_out:
				max_N0 = N0_out
			if max_N1 < N1_out:
				max_N1 = N1_out
				print "max_n1 = " + str(max_N1)
			if max_N2 < N2_out:
				max_N2 = N2_out
			if max_N3 < N3_out:
				max_N3 = N3_out
			if max_N4 < N4_out:
				max_N4 = N4_out
			if max_N5 < N5_out:
				max_N5 = N5_out
			if max_xs < xs_out:
				max_xs = xs_out
			if max_ys < ys_out:
				max_ys = ys_out
			if max_zs < zs_out:
				max_zs = zs_out

			output.write("   ")
			output.write("{}  ".format((N0_out)))
			output.write(" " + str(N1_out) + " ")
			output.write(" " + str(N2_out) + " ")
			output.write(" " + str(N3_out) + " ")
			output.write(" " + str(N4_out) + " ")
			output.write(" " + str(N5_out) + " ")
			output.write(" " + str(xs_out) + " ")
			output.write(" " + str(ys_out) + " ")
			output.write(" " + str(zs_out) + " ")
			output.write("\n")

			# print k
			k += 1
			print "-----------------------"

	print "Done collecting data"

	k = k-1
	med_N0 = float("{0:.2f}".format(sum_N0 / float(k)))
	med_N1 = float("{0:.2f}".format(sum_N1 / float(k)))
	med_N2 = float("{0:.2f}".format(sum_N2 / float(k)))
	med_N3 = float("{0:.2f}".format(sum_N3 / float(k)))
	med_N4 = float("{0:.2f}".format(sum_N4 / float(k)))
	med_N5 = float("{0:.2f}".format(sum_N5 / float(k)))
	med_xs = float("{0:.2f}".format(sum_xs / float(k)))
	med_ys = float("{0:.2f}".format(sum_ys / float(k)))
	med_zs = float("{0:.2f}".format(sum_zs / float(k)))

	delta_N0 = max_N0 - min_N0
	delta_N1 = max_N1 - min_N1
	delta_N2 = max_N2 - min_N2
	delta_N3 = max_N3 - min_N3
	delta_N4 = max_N4 - min_N4
	delta_N5 = max_N5 - min_N5
	delta_xs = max_xs - min_xs
	delta_ys = max_ys - min_ys
	delta_zs = max_zs - min_zs

	output.write("------------ average values ---------------\n")
	output.write(" " + str(med_N0))
	output.write(" " + str(med_N1))
	output.write(" " + str(med_N2))
	output.write(" " + str(med_N3))
	output.write(" " + str(med_N4))
	output.write(" " + str(med_N5))
	output.write(" " + str(med_xs))
	output.write(" " + str(med_ys))
	output.write(" " + str(med_zs))
	output.write("\n")

	output.write("----------- delta ----------------\n")
	output.write("   " + str(delta_N0))
	output.write("   " + str(delta_N1) + " ")
	output.write("   " + str(delta_N2) + " ")
	output.write("  " + str(delta_N3) + " ")
	output.write("  " + str(delta_N4) + " ")
	output.write("  " + str(delta_N5) + " ")
	output.write("  " + str(delta_xs) + " ")
	output.write("  " + str(delta_ys) + " ")
	output.write("  " + str(delta_zs) + " ")
	output.write("\n")

	# # write minimal values
	# trained.write(gesture)
	# trained.write(" ")
	# trained.write(" " + str(min_N0))
	# trained.write(" " + str(min_N1))
	# trained.write(" " + str(min_N2))
	# trained.write(" " + str(min_N3))
	# trained.write(" " + str(min_N4))
	# trained.write(" " + str(min_N5))
	# trained.write(" " + str(min_xs))
	# trained.write(" " + str(min_ys))
	# trained.write(" " + str(min_zs) + "\n")

	print "trained:" + str(med_N0) + "	"  + str(int(round(med_N1)))
	# write average values
	trained.write(gesture)
	trained.write(" ")
	trained.write(" " + str(int(round(med_N1))))
	trained.write(" " + str(int(round(med_N1))))
	trained.write(" " + str(int(round(med_N2))))
	trained.write(" " + str(int(round(med_N3))))
	trained.write(" " + str(int(round(med_N4))))
	trained.write(" " + str(int(round(med_N5))))
	trained.write(" " + str(int(round(med_xs))))
	trained.write(" " + str(int(round(med_ys))))
	trained.write(" " + str(int(round(med_zs))))
	trained.write("\n\r")

	# # write maximum values	
	# trained.write(gesture)
	# trained.write(" ")
	# trained.write(" " + str(max_N0))
	# trained.write(" " + str(max_N1))
	# trained.write(" " + str(max_N2))
	# trained.write(" " + str(max_N3))
	# trained.write(" " + str(max_N4))
	# trained.write(" " + str(max_N5))
	# trained.write(" " + str(max_xs))
	# trained.write(" " + str(max_ys))
	# trained.write(" " + str(max_zs) + "\n")

	output.close()
	trained.close()


def recogGest():
	# global gesture_recog
	gesture_recog ="None"
	trained = open("trained.txt")
	gestures = trained.readlines()
	print "gestures: "
	print gestures[1]
	gestures.remove(gestures[0])

	sensorData = get_data()

	dataS0 = sensorData[0].split()
	dataS1 = sensorData[1].split()
	dataS2 = sensorData[2].split()
	dataS3 = sensorData[3].split()
	dataS4 = sensorData[4].split()
	dataS5 = sensorData[5].split()

	x0 = float(dataS0[0])
	y0 = float(dataS0[1])
	z0 = float(dataS0[2])
	x1 = float(dataS1[0])
	y1 = float(dataS1[1])
	z1 = float(dataS1[2])
	x2 = float(dataS2[0])
	y2 = float(dataS2[1])
	z2 = float(dataS2[2])
	x3 = float(dataS3[0])
	y3 = float(dataS3[1])
	z3 = float(dataS3[2])
	x4 = float(dataS4[0])
	y4 = float(dataS4[1])
	z4 = float(dataS4[2])
	x5 = float(dataS5[0])
	y5 = float(dataS5[1])
	z5 = float(dataS5[2])



	# calculate neuron values
	N0_out = N0(x0, y0, z0, 1, 1, 1)
	N1_out = N1(x1, y1, z1, 1, 1, 1)
	N2_out = N2(x2, y2, z2, 1, 1, 1)
	N3_out = N3(x3, y3, z3, 1, 1, 1)
	N4_out = N4(x4, y4, z4, 1, 1, 1)
	N5_out = N5(x5, y5, z5, 1, 1, 1)
	xs_out = xs(x0, x1, x2, x3, x4, x5, 1, 1, 1, 1, 1, 1)
	ys_out = ys(y0, y1, y2, y3, y4, y5, 1, 1, 1, 1, 1, 1)
	zs_out = zs(z0, z1, z2, z3, z4, z5, 1, 1, 1, 1, 1, 1)

	min_k = 70000  
	
	for gesture in gestures:
		print gesture
		values = gesture.replace("\n", "").replace("\r", "").split()
		print "values:"
		print values

		if values != []:
			# print "values:"
			# print values
			N0_current = values[1]
			N1_current = values[2]
			N2_current = values[3]
			N3_current = values[4]
			N4_current = values[5]
			N5_current = values[6]
			xs_current = values[7]
			ys_current = values[8]
			zs_current = values[9]
		
			if N0_out == 0:
				N0_out += 1
			if N1_out == 0:
				N1_out += 1
			if N2_out == 0:
				N2_out += 1
			if N3_out == 0:
				N3_out += 1
			if N4_out == 0:
				N4_out += 1
			if N5_out == 0:
				N5_out += 1
			if xs_out == 0:
				xs_out += 1
			if ys_out == 0:
				ys_out += 1
			if zs_out == 0:
				zs_out += 1

			# similarity coefficient
			k_N0 = abs(float(N0_current) - float(N0_out))
			k_N1 = abs(float(N1_current) - float(N1_out))
			k_N2 = abs(float(N2_current) - float(N2_out))
			k_N3 = abs(float(N3_current) - float(N3_out))
			k_N4 = abs(float(N4_current) - float(N4_out))
			k_N5 = abs(float(N5_current) - float(N5_out))
			k_xs = abs(float(xs_current) - float(xs_out))
			k_ys = abs(float(ys_current) - float(ys_out))
			k_zs = abs(float(zs_current) - float(zs_out))
			k_sum = k_N0 + k_N1 + k_N2 + k_N3 + k_N4 + k_N5 + k_xs + k_ys + k_zs
			# print k_N0, k_N1, k_N2, k_N3, k_N4, k_N5, k_xs, k_ys, k_zs, k_sum
			diff_k = k_sum / 9
			# print values[0], diff_k

			if diff_k < min_k:
				min_k = diff_k
				gesture_recog = values[0]
	return gesture_recog
		
