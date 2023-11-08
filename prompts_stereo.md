Now i will describe the scene in the images, this is a robotic experiment setup, the platform is the white surface. One camera is hanged above the surface and looking down at the surface. The other camera is located left to the scene. Please combine the two images to understand the scene.

Now we define the orientation description in this view to describe the moving direction of the robot's end in based on the first camera's image to locate the "front, back, left, right, up and down".


up: to the upper boundary of the first image
down: to the lower boundary of the firstimage
left: to the left boundary of the first image.
right: to the right boundary of the first image
dive: move the end effector towards the surface, please do it when the suction cup is directly above the object to be picked in the task. After "dive" you should turn on the suction cup to pick up the object.
rise: move the end effector away from the surface. Please do it after you turn on the suction cup and grasp the object.

Now i will describe the task: this is a robotic pick and place task, the blue suction gripper is the robot end-effector. Note that movements and alignments mentioned in the task corresponds to the direction of movement of the end-effector. The task includes several steps of moving the blue suction cup to the position directly above the object, diving and activating on the suction cup, rising to lift the object, then moving to the target position, deactivating the suction cup.

During the moving, you should always check the relative postion of the objects from the updated image and update a proper moveing direction from "up","down","left","right". Usually you need to change the direction at least once to align the object with the suction cup.
 
------
I'm going to provide you with a prompt template for a task, for example, the template reads: pick the strawberry into the red plate.
 
I need you to guide the movement of the robot's end in a step-by-step fashion, based on the given image pair.
 
Your given output should follow the following manner: 
{movement: "right", suction_on: False, success: False}, 
i.e., the output should be a json dictionary where the key of the movement should be one of the orientations described above, and the suction_on indicates whether or not the suction cup needs to be activated in order to command the Robot to grab the object, when it is True then activate the suction cups, when it is False then deactivate the suction cups. Do not activate it until it actually reach the object you want to grasp or the task will be failed. The meaning of success is whether the task has been completed or not, if it has been completed then the value is set to True, so that I will not continue to update you with new image pair, indicating that the task is completed. 

After you give the output, the robot will excecute your command and I will give you a new image pair describing the scene after your command. and you should understand what your command affect and based on the updated image pair to predict what is the next command to finish the given task.
 
Attention: You just need to provide the output of the predicted next action in the current state, after which I will update the picture pair and then predict the next movement based on the new picture pair.
 
When the task starts, the output should follow the dictionary format described above.

These are the task descriptions. This task is very important to me so please be careful about your answer and think twice before you give it. 

Question: Based on the current state in the image, what should be the next action to pick up the plum?

Answer: