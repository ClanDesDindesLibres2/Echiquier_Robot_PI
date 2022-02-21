import threading
from Comm.EthernetComm import *
from Comm.MessageIO import *
from Comm.SerialComm import *
from Comm.driveManager import *


from Cinematic.PositionSolver import *
from Cinematic.JoinSystem import *
from Cinematic.LinearJoin import *
from Cinematic.RevoluteJoin import *
from Cinematic.robotAPI import *
from test.TestCinematic.testRobotAPI import *



class app:
    def __init__(self):
        self.commPort = None
        self.messageIO = MessageIO()
        self.messageIO.addDevice(SerialComm("COM3", 57000))
        self.driveManager = DriveManager([0, 0, 0, 0], self.messageIO)
        
        self.JS = JoinSystem([LinearJoin(VectorSpaceAxis.X, np.array([0, 0, 0]), [0, 0.40], hardwareStepDistance= 0.0000098046875)])
        self.JS.addJoin(RevoluteJoin(VectorSpaceAxis.Y, np.array([0, 0.1283, 0]), [-math.pi/4, 2 * math.pi-0.4], hardwareStepDistance= math.pi*2/4096))
        self.JS.addJoin(RevoluteJoin(VectorSpaceAxis.Y, np.array([0, 0.245, 0]), [-math.pi/4, 2 * math.pi-0.4], hardwareStepDistance= math.pi*2/4096))
        self.JS.addJoin(RevoluteJoin(VectorSpaceAxis.X, np.array([0, 0.32824, 0]), [-math.pi/2-0.4, 2 * math.pi-0.4], hardwareStepDistance= math.pi*2/4096))


        self.robot = robotAPI(self.JS,[0., 0., 0.,0. ], self.driveManager)

    def newConnection(self, conn):
        self.commPort = EthernetComm(conn)
        self.messageIO.addDevice(self.commPort)
        while True:
            msg = self.messageIO.readMessage(1)
            if msg != None:
                print("type:", msg.getType())
                print("paload size: ", msg.getPayloadSize())
                print("payload :", msg.getPayload())
                self.robot.executeCommand(msg)


if __name__ == '__main__':
    #TEST1 qui compile sans erreurs : 
    #Joins = JoinSystem()
    #Messenger = MessageIO()
    #Messenger.addDevice(SerialComm("COM3", 57000))
    #Joins.addJoin(RevoluteJoin(VectorSpaceAxis.Y, np.array([0, 0.1283, 0]), [-math.pi/4, 2 * math.pi-0.4], hardwareStepDistance= math.pi*2/4096))  
    #driveManager = DriveManager([0],Messenger)
    #driveManager.setJoinPosition([1])
    
    #TEST 2 
    Messenger = MessageIO()
    Messenger.addDevice(SerialComm("COM3", 57000))
    driveManager = DriveManager([0], Messenger)
    Joins = JoinSystem()
    Joins.addJoin(RevoluteJoin(VectorSpaceAxis.Y, np.array([0, 0, 0]), [-math.pi/4, 2 * math.pi-0.4], hardwareStepDistance= math.pi*2/4096))
    robot =  robotAPI(Joins,[0.], driveManager)
    msg = ControlMessage(ControlMessage.SET_JOIN_POSITION, [2500])
    print('message : ' , msg)
    robot.executeCommand(msg)


    
    
