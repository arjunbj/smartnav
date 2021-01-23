#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import picar
from picar import back_wheels, front_wheels


picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"

fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)
cam = camera.Camera(debug=False, db=db_file)

cam.ready()
bw.ready()
fw.ready()

SPEED = 60
bw_status = 0
fw_status = 0
cam_status = 0


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    global SPEED, bw_status, fw_status, cam_status
    
    if data.data == 'q':
        # Neutral key
        # Depending on the status value it should do things
        if not cam_status:
            cam.ready()
            cam_status = 0
        
        if not bw_status:
            bw.stop()
            bw_status = 0
        else:
            bw.ready()
            bw_status = 0

        if not fw_status:
            fw_status = 0
            fw.turn_straight()


    elif data.data == 'w':
        bw.speed = SPEED
        bw.forward()
        bw.status = 1
        
    elif data.data == 's':
        bw.speed = SPEED
        bw.backward()
        bw_status = -1

    elif data.data == 'a':
        fw.turn_left()
        fw_status = -1
    elif data.data == 'd':
        fw.turn_right()
        fw_status = 1
    
    elif data.data == 'u':
        cam.turn_up(20)
        cam_status = 1

    elif data.data == 'j':
        cam.turn_down(20)
        cam_status = 2

    elif data.data =='h':
        cam.turn_left(40)
        cam_status = 3
    elif data.data == 'k':
        cam.turn_right(40)
        cam_status = 4
            
    elif data.data == 'r':
        # reset key
        bw_status = 0
        fw_status = 0
        cam_status = 0
        fw.turn_straight()
        bw.stop()
        bw.ready()
        fw.ready()
        cam.ready()


def listener():

    rospy.init_node('keyboard_subscriber_and_control', anonymous=True)

    rospy.Subscriber('keyboard_topic', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
