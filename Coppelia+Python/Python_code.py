import numpy as np
import sim
import sys
import time
import ikpy

#-----Try to connect---------------
sim.simxFinish(-1)
your_IP='192.168.0.7'
clientID = sim.simxStart(your_IP,19999,True,True,10000,5)
if clientID != -1:
 print("Connected to remote API server")
else:
 print("Not connected to remote API server")
 sys.exit ("could not connect")

#-----Start the Paused Simulation
err_code = sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot)
#-----Initialize Joint Handles---------
err_code,L2 = sim.simxGetObjectHandle(clientID,"Revolute_upper_blue",sim.simx_opmode_blocking)
err_code,L1 = sim.simxGetObjectHandle(clientID,"Revolute_upper_gold",sim.simx_opmode_blocking)
err_code,L3 = sim.simxGetObjectHandle(clientID,"Revolute_upper_green",sim.simx_opmode_blocking)
err_code,L4 = sim.simxGetObjectHandle(clientID,"Revolute_upper_white",sim.simx_opmode_blocking)
err_code,F2 = sim.simxGetObjectHandle(clientID,"Revolute_lower_blue",sim.simx_opmode_blocking)
err_code,F1 = sim.simxGetObjectHandle(clientID,"Revolute_lower_gold",sim.simx_opmode_blocking)
err_code,F3 = sim.simxGetObjectHandle(clientID,"Revolute_lower_green",sim.simx_opmode_blocking)
err_code,F4 = sim.simxGetObjectHandle(clientID,"Revolute_lower_purple",sim.simx_opmode_blocking)

err_code,W2  = sim.simxGetObjectHandle(clientID,"blue_wheel",sim.simx_opmode_blocking)
err_code,W1 = sim.simxGetObjectHandle(clientID,"gold_wheel",sim.simx_opmode_blocking)
err_code,W3 = sim.simxGetObjectHandle(clientID,"green_wheel",sim.simx_opmode_blocking)
err_code,W4 = sim.simxGetObjectHandle(clientID,"purple_wheel",sim.simx_opmode_blocking)
t = time.time() #record the initial time

def roll(velocity):
    
    err_code = sim.simxSetJointTargetVelocity (clientID, W2,velocity,sim.simx_opmode_streaming) # set the postion of J3
   
    err_code = sim.simxSetJointTargetVelocity (clientID, W3,velocity,sim.simx_opmode_streaming) # set the postion of J3
 
    err_code = sim.simxSetJointTargetVelocity (clientID, W4,velocity,sim.simx_opmode_streaming) # set the postion of J3

    err_code = sim.simxSetJointTargetVelocity (clientID, W1,velocity,sim.simx_opmode_streaming) # set the postion of J3
  
def down_up(pos_val):
   
    err_code = sim.simxSetJointTargetPosition (clientID, F1,pos_val,sim.simx_opmode_streaming) # set the postion of J3
    
    err_code = sim.simxSetJointTargetPosition (clientID, F2,pos_val,sim.simx_opmode_streaming) # set the postion of J3
    
    err_code = sim.simxSetJointTargetPosition (clientID, F3,pos_val,sim.simx_opmode_streaming) # set the postion of J3
    
    err_code = sim.simxSetJointTargetPosition (clientID, F4,pos_val,sim.simx_opmode_streaming) # set the postion of J3
      

def turn(upper_pos):
  
    err_code = sim.simxSetJointTargetPosition (clientID, L1,upper_pos,sim.simx_opmode_streaming) # set the postion of J1

    err_code = sim.simxSetJointTargetPosition (clientID, L2,(upper_pos),sim.simx_opmode_streaming) # set the postion of J2
  
    # err_code = sim.simxSetJointTargetPosition (clientID, j3,upper_pos,sim.simx_opmode_streaming) # set the postion of J3
  
    # err_code = sim.simxSetJointTargetPosition (clientID, j4,upper_pos,sim.simx_opmode_streaming) # set the postion of J3



while (time.time()-t)<20: #run for 20 seconds

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

    up_down = np.radians(27) # in degrees 0
    print(up_down)
    down_up(up_down)
    time.sleep(1)

    down_up(-up_down)
    time.sleep(1)

    turn(-turning)
    time.sleep(3)

sim.simxStopSimulation(clientID,sim.simx_opmode_oneshot)
print("Done")

