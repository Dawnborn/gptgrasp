Now i will describe the scene in the given image, this is a robotic experiment setup, the platform is the white surface. The camera is hanged above the surface and looking down at the surface.

Now we define the orientation description in this view to describe the 6 moving directions of the robot's end in terms of "up, down, left, right, dive and rise".

up: to the upper boundary of the image
down: to the lower boundary of the image.
left: to the left boundary of the image.
right: to the right boundary of the image.
dive: move the end effector towards the surface, please do it when the suction cup is directly above the object to be picked in the task then turn on the suction cup.
rise: move the end effector away from the surface. Please do it immediately after you turn on the suction cup and grasp the object.

Now i will describe the task: this is a robotic pick and place task, the white part with the blue suction gripper is the robot end-effector. The task includes several steps of moving the end-effector to the position directly above the object, diving and activating on the suction cup, rising to lift the object, then moving to the target position, deactivating the suction cup to drop the object.

After given the new image, you should always check the relative postion of the objects from the updated image and update a proper moveing direction from "up","down","left","right". Usually you need to change the direction at least once to align the object with the suction cup.
 
------
I'm going to provide you with a prompt template for a task, for example, the task template reads: pick the strawberry into the red plate.
 
I need you to guide the movement of the robot's end to finish the step in a step-by-step fashion. Which means, you should first give the next step movement based on the current state in the image to finish the task. Then the robot will perform your command and I will give you a new image of the scene after your command. You should understand the new scene, check the relative position of the end-effector and the object, then give the next step command to finish the task based on the new image. We will do it over and over again until the task is done or failed.
 
Your output command should like the following manner: 
`{movement: "right", suction_on: False, success: False}`, 
i.e., the output should be a json dictionary where the keyword `movement` should be one of the 6 directions described above. The `suction_on` indicates whether or not the suction cup needs to be activated in order to command the Robot to grab the object, when it is True then activate the suction cups, when it is False then deactivate the suction cups. Do not activate it until it actually reach the object you want to grasp or the task will be failed. The meaning of the keyword `success` is whether the task has been completed or not, if it has been completed then the value is set to True, so that I will not continue to update you with the picture, indicating that the task is completed. 
When I give you the new image, you will find and tell me about the new positions of the end-effector and the object and their relative postions on the new image, then return the above json dictionary in your answer.

Attention: You just need to provide the output of the predicted next action in the current state, after which I will update the picture and then predict the next movement based on the new picture.
 
Note that movement corresponds to the direction of movement of the end of the robot.
 
When the task starts, the output should follow the dictionary format described above.

These are the task descriptions. This task is very important to me so please try your best. And you should be careful about your answer and think twice before you give it. If you understand the instructions please tell me you are ready, and I will give you the task.