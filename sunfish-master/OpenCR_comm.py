# Communication between pi and OPEN_CR
import time
import serial

class communicationOPENCR:
    def __init__(self, port):
        self.port = port

    def sendDataOpenCR(self, pos1, pos2, piece):
        with serial.Serial(self.port, 57600, timeout=1) as OpenCR:
            time.sleep(0.1) #wait for serial to open
            if OpenCR.isOpen():
                print("{} connected!")
                try:
                    values = str(pos1) + " " + str(pos2) + " " +  str(piece)
                    print(values)
                    OpenCR.write(values.encode())
                    #time.sleep(0.1) #wait for OpenCR to answer
                    while OpenCR.inWaiting()==0: pass
                    if  OpenCR.inWaiting()>0: 
                        answer=OpenCR.readline()
                        OpenCR.flushInput() #remove data after reading
                        done = int(answer)
                        if done>=1:
                            done = done+1
                            #print(done)

                except KeyboardInterrupt:
                    print("KeyboardInterrupt has been caught.")

if __name__ == '__main__':
    openCR_comm = communicationOPENCR('/dev/ttyACM1')
    openCR_comm.sendDataOpenCR(12,14,0)