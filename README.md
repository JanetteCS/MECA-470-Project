# MECA-470-Project - Quadruped
Group Luis Arevalo, Janette Calvillo Solis and Nick Lauer <br>
Sessions: 30 <br>
Hours: 100 <br>

## 1. Introduction <br>
The Quadruped project involved using Coppelia to recreate and adding wheels to the current mini MIT cheetah. The project also required the MIT code to be converted to ROS, and Visual Code was used to interface ROS and Coppelia.<br>


## 2. Design <br>
##2.1 Coppelia Model <br>
The cheetah (Figure 1) was recreated using solidworks which allowed for proper assembly and prpvided the option ofexporting the model as URDF files that are compatible with Coppelia <br>
![](coppelia_cheetah.PNG)<br>
Figure 1. Imageof cheetah in coppelia<br>


# 3 Implementation<br>
## 3.1 Visual Studio<br>
Vissual Study (VS) was used to ssh into the virtual machine containing ROS for this project. The after connecting VS to the virtual machine, the file named simpleTest.py was used to test and verify VS was connecting properly to Coppelia once VS was connected to the virtual machine. <br>

After verifying the API interface was working, the coppelia model named, Cheetah_shaky_stabilized_rev_2.ttt was opened in Coppelia and a python file named Python_code.py stored insode the virtual machined was opned through VS. The simulation was then started in Coppelia before running the python file in VS. The python file was able to control the Coppelia model of the cheetah as shown in the video file named, video_VS - ssh-to-VM-API-Coppelia.mp4


## 3.2 Python in ROS <br>

![](coppelia_cheetah.PNG)<br>


