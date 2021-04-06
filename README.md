# Detecting sunspots from a picture of the sun

This is a fun project I started on a weekend. The idea is simple: Get an image and mark the sunspos with a green square.

For this task I noticed online that *cv2* was the best option to work with picture files.

In the begining we load the file using the integreted function of *cv2*. After that we visualize it.
Then the fun part starts. using the function in line 20  we threshold the image so that only the sunspots remain.

After the threshholding we have to convert the data into something we can work with. *cv2* has a fucntion for this that converts the data into NumPy array.
You can see that because we only need the sunspots we have to use the circle equation (line 36) to make sure that we do not detect the sun itself.
The next integreted function (line 43) gets us the surface of each sunspot and then we use a *for* loop to mark each sunspot with a green rectangle (line 33).

From the pictures below you can see that from picture 1 that is the input we get the output with he detection.

This code is not perfect and has some problems but its a nice first implementation for a weekend project for a newbie python programer.
