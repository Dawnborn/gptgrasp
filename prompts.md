# Long version prompt

on the white board and diana.

```
Now i will describe the scene, this is a robotic experiment setup, the platform is the black desk. The camera is hanged above the surface and looking down at the surface.
 
Now i will describe the task: this is a robotic pick and place task, the white part with the blue suction gripper is the robot end-effector.
 
Now we define the orientation description in this view to describe the motion of the robot's end in terms of the camera's field of view to locate the "front, back, left, right, up and down".


front: to the upper boundary of the image
back: to the lower boundary of the image
left: to the left boundary of the image.
right: to the right boundary of the image
up: in the opposite direction to gravity
down: direction of gravity
 
------
I'm going to provide you with a prompt template for a task, for example, the template reads: pick the strawberry into the red plate.
 
I need you to guide the movement of the robot's end.
 
Your given output should follow the following manner: 
{movement: "right", suction_on: False, success: False}, 
i.e., the output should be a dictionary where the key of the movement should be one of the orientations described above, and the suction_on indicates whether or not the suction cup needs to be activated in order to command the Robot to grab the object, when it is True then activate the suction cups, when it is False then deactivate the suction cups, where the meaning of success is whether the task has been completed or not, if it has been completed then the value is set to True, so that I will not continue to update you with the picture, indicating that the task is completed. 
When we update the image, you will only update me with the above dictionary and not have to reply with anything else.
 
You just need to provide the output of the predicted next action in the current state, after which I will update the picture and then predict the next movement based on the new picture.
 
Note that movement corresponds to the direction of movement of the end of the robot.
 
When the task starts, the output should follow the dictionary format described above, and nothing more!

These are the task descriptions. This task is very important to me so please be careful about your answer and think twice before you give it. 

Next, I will provide you with the task templates, are you ready? 
```