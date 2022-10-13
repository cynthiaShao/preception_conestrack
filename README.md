
## Submission Specification
- Your code should be written in either Matlab, Python, or C++.
- Please upload your code to a public github repository for us to review
- Please document your code. The more readable your code is the better you can show your coding skills.
- Please include a README that contains the following:
    - answer.png
    - Methodology 
    - What did you try and why do you think it did not work.
    - What libraries are used

## Answer Image
The false_answer image is attached below, and the program code also write a picture in the same directory as the cones_detect file.
![image](https://user-images.githubusercontent.com/107283860/195726851-fef66ea2-b8b6-4cd3-84b0-75e743c0182a.png)


## Methodology


## What I tried / What didn't work
I think the hardest part is how to correctly identify the red cone. During the recognition process, my code is constantly identifying other red objects in the picture, and other objects similar to cones other than the red cones that need to be identified. In addition, I failed to connect the cones into two lines. The method I used was wrong to connect the center points of all the cones. I couldn't find a way to connect the two lines of cones separately. 

## What Libraries I used
I used cv2 in python-opencv, numpy to solve some parts involved array, matplotlib to process/plot the graphic version of the png image as well as imutils to solve the part involves contour. 
