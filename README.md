# Smartnav
Objective: Make an autonomous RC car to autonomously explore the environment and make a map of the environment

Dependencies:  
Install below dependencies before building this branch

export TURTLEBOT3_MODEL=burger  
sudo apt-get install ros-noetic-pcl-ros  
sudo apt-get install ros-noetic-pcl-conversions  
sudo apt-get install ros-noetic-navigation  
sudo apt-get install libsdl-dev  
sudo apt-get install libsdl-image1.2-dev  
sudo apt install ros-noetic-slam-gmapping  

How to launch:  

roslaunch turtlebot3_gazebo turtlebot3_world.launch  
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping  
roslaunch hector_exploration_node exploration_planner.launch  
rosrun hector_exploration_controller simple_exploration_controller  