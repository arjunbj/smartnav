roscore &
ROSCORE_PID=$!
sleep 1


docker run -it --rm --privileged --net=host --env=NVIDIA_VISIBLE_DEVICES=all --env=NVIDIA_DRIVER_CAPABILITIES=all --env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 noetic_image 


wait $ROSCORE_PID
if [[ $? -gt 128 ]]
then
    kill $ROSCORE_PID 
fi
