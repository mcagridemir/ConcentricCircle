#! /usr/bin/env python
#To make this file executable run this command on terminal
#chmod u+x ~/path/to/.py extension file

import rospy
from geometry_msgs.msg import Twist
import math

rospy.init_node('walker', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

speed = 10
angle = 90

PI= math.pi

def getRadius():
    global radius
    inputRadius = input("Enter radius: ")
    radius = float(inputRadius)/7.0

def rotateToForward():
    vel_msg = Twist()

    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    #vel_msg.angular.z = 0

    vel_msg.angular.z = abs(angular_speed)

    t0 = rospy.Time.now().to_sec()

    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

def goToForward(rad, x):
    vel_msg = Twist()
    vel_msg.linear.x = x
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    currDistance = 0

    t0 = rospy.Time.now().to_sec()
    
    while(currDistance<rad):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        currDistance = rad*(t1-t0)


    velocity_publisher.publish(vel_msg)

def rotateToClockwise(sSpeed, z):
    vel_msg = Twist()
    vel_msg.angular.z = -z
    current_distance = 0

    t0 = rospy.Time.now().to_sec()
    
    while(current_distance < sSpeed):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = sSpeed*(t1-t0)

def createCircle(pCircle, dist, x, z):
    vel_msg = Twist()
    vel_msg.linear.x = x
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -z

    t0 = rospy.Time.now().to_sec()
    currPCircle = 0

    while(currPCircle<pCircle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        currPCircle = dist*(t1-t0)

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0

    velocity_publisher.publish(vel_msg)

if _name_ == '_main_':
    
        try:
            getRadius()

            rotateToForward()
            goToForward(radius,0.5*radius)
            rotateToClockwise(speed,angle*PI/180)
            createCircle(2*PI*radius,radius,0.5*radius,1.0)
        
            rotateToForward()
            goToForward(2*radius,1.0*radius)
            rotateToClockwise(speed,angle*PI/180)
            createCircle(2*2*PI*radius,2*radius,1.5*radius,1.0)
            
            rotateToForward()
            goToForward(2*radius,1.0*radius)
            rotateToClockwise(speed,angle*PI/180)
            createCircle(2*2*2*PI*radius,2*2*radius,2.5*radius,1.0)
            
            rotateToForward()
            goToForward(2*radius,1.0*radius)
            rotateToClockwise(speed,angle*PI/180)
            createCircle(2*2*2*2*PI*radius,2*2*2*radius,3.5*radius,1.0)
        except rospy.ROSInterruptException: pass
