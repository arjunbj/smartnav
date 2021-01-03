FROM osrf/ros:noetic-desktop-full

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphic 
RUN apt-get update && apt-get -y install git
RUN apt-get -y install ros-noetic-catkin python3-catkin-tools 
RUN apt -y install python3-catkin-lint python3-pip
RUN pip3 install osrf-pycommon
WORKDIR /home
RUN mkdir catkin_ws
WORKDIR catkin_ws
RUN mkdir src
WORKDIR src
RUN git clone https://github.com/arjunbj/smartnav.git
WORKDIR /home/catkin_ws
#RUN bash /opt/ros/noetic/setup.bash
#RUN rosdep update
#RUN catkin build hector_slam
RUN catkin config \
      --extend /opt/ros/noetic \
      --cmake-args \
        -DCMAKE_BUILD_TYPE=Release && \
    catkin build hector_slam

 	
