import serial

ser = serial.Serial('COM4', 9600)
s = [0]
while True:
	message = str(ser.readline())
	print(message)
	#initiale = str(message[2:][:-8], 16)
	finale = int(message[5:][:-5], 16)
	print(finale)
	#print(initiale, finale)
	