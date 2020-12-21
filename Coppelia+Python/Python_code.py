import numpy as np
import sim
import sys
import time
import ikpy

#-----Try to connect---------------
sim.simxFinish(-1)
your_IP='192.168.0.11'
clientID = sim.simxStart(your_IP,19999,True,True,10000,5)
if clientID != -1:
 print("Connected to remote API server")
else:
 print("Not connected to remote API server")
 sys.exit ("could not connect")

#-----Start the Paused Simulation
err_code = sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot)
#-----Initialize Joint Handles---------
err_code,j1 = sim.simxGetObjectHandle(clientID,"SS2",sim.simx_opmode_blocking)
err_code,j2 = sim.simxGetObjectHandle(clientID,"SS1",sim.simx_opmode_blocking)
err_code,j3 = sim.simxGetObjectHandle(clientID,"SS3",sim.simx_opmode_blocking)
err_code,j4 = sim.simxGetObjectHandle(clientID,"SS4",sim.simx_opmode_blocking)
err_code,j5 = sim.simxGetObjectHandle(clientID,"F2",sim.simx_opmode_blocking)
err_code,j6 = sim.simxGetObjectHandle(clientID,"F1",sim.simx_opmode_blocking)
err_code,j7 = sim.simxGetObjectHandle(clientID,"F3",sim.simx_opmode_blocking)
err_code,j8 = sim.simxGetObjectHandle(clientID,"F4",sim.simx_opmode_blocking)

err_code,j9  = sim.simxGetObjectHandle(clientID,"W2",sim.simx_opmode_blocking)
err_code,j10 = sim.simxGetObjectHandle(clientID,"W1",sim.simx_opmode_blocking)
err_code,j11 = sim.simxGetObjectHandle(clientID,"W3",sim.simx_opmode_blocking)
err_code,j12 = sim.simxGetObjectHandle(clientID,"W4",sim.simx_opmode_blocking)

err_code,j13 = sim.simxGetObjectHandle(clientID,"W5",sim.simx_opmode_blocking)
t = time.time() #record the initial time

def roll(velocity):
    
    err_code = sim.simxSetJointTargetVelocity (clientID, j9,velocity,sim.simx_opmode_streaming) # set the postion of J3
   
    err_code = sim.simxSetJointTargetVelocity (clientID, j11,velocity,sim.simx_opmode_streaming) # set the postion of J3
 
    err_code = sim.simxSetJointTargetVelocity (clientID, j12,velocity,sim.simx_opmode_streaming) # set the postion of J3

    err_code = sim.simxSetJointTargetVelocity (clientID, j10,velocity,sim.simx_opmode_streaming) # set the postion of J3
  
def down_up(pos_val):
   
    err_code = sim.simxSetJointTargetPosition (clientID, j6,pos_val,sim.simx_opmode_streaming) # set the postion of J3
    
    err_code = sim.simxSetJointTargetPosition (clientID, j5,pos_val,sim.simx_opmode_streaming) # set the postion of J3
    
    err_code = sim.simxSetJointTargetPosition (clientID, j7,pos_val,sim.simx_opmode_streaming) # set the postion of J3
    
    err_code = sim.simxSetJointTargetPosition (clientID, j8,pos_val,sim.simx_opmode_streaming) # set the postion of J3
      

def turn(upper_pos):
  
    err_code = sim.simxSetJointTargetPosition (clientID, j1,upper_pos,sim.simx_opmode_streaming) # set the postion of J1

    err_code = sim.simxSetJointTargetPosition (clientID, j2,upper_pos,sim.simx_opmode_streaming) # set the postion of J2
  
    #err_code = sim.simxSetJointTargetPosition (clientID, j11,upper_pos,sim.simx_opmode_streaming) # set the postion of J3
  
    #err_code = sim.simxSetJointTargetPosition (clientID, j12,upper_pos,sim.simx_opmode_streaming) # set the postion of J3

n=0

while(time.time()-t)<20: #run for 20 seconds

    a = np.transpose(np.asmatrix(np.linspace(1, 450, 500)))

    b = np.transpose(np.asmatrix(np.linspace(1, -300, 500)))

    c = np.transpose(np.asmatrix(np.linspace(1, -200, 500)))


    rolling = np.radians(360) # in degrees 0
    print(rolling)
    roll(rolling)
    time.sleep(1)

    turning = np.radians(15) # in degrees 0
    print(turning)
    turn(turning)
    time.sleep(3)
    if n<1:
        up_down = np.radians(27) # in degrees 0
        print(up_down)
        down_up(up_down)
        time.sleep(1)

        down_up(-up_down)
        time.sleep(1)

        down_up(up_down)
        time.sleep(1)
        n+=1

    turn(-turning)
    time.sleep(3)

sim.simxStopSimulation(clientID,sim.simx_opmode_oneshot)
print("Done")

