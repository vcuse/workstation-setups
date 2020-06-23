---
title: "Using LabelImg to Annotate Workstations"
layout: default
---

## Introduction

Our mission for this task is to identify classes of objects in pictures of workstations.
To perform the task, we are going to use LabelImg, an annotation tool that is commonly used in object detection techniques. The task
is divided in groups of researchers, where each group will analyze a predefined set of workstations:

**Group 0:**

- Dane Acena
- Makayla Moster

**Group 1:**

- Felipe Fronchetti
- Luiz Susin

**Group 2:**

- Boden Kahn
- Douglas Krug

If your name is listed in one of the groups above, please follow the tutorial below to perform the task.

## Preparing the environment

### - Step 1: Installing LabelImg

First, you will have to install the annotation tool. The tutorial explaining how to install it is available at:

[README.rst#installation](https://github.com/tzutalin/labelImg/blob/master/README.rst#installation)

Find the correct instruction for your operating system and install LabelImg on your computer.

### - Step 2: Setting up LabelImg

 After installing the annotation tool, you have to prepare it for our analysis. First, replace the _predefined_classes.txt_ file that is inside the LabelImg data folder you downloaded with the following file:

[predefined_classes.txt](download_files/predefined_classes.txt)

This file contains all the categories of objects we are going to identify in the images. Please, do not use the _predefined_classes.txt_ file that originally comes with LabelImg, it does not contain the correct set of classes.

After replacing the original _predefined_classes.txt_ file with ours, download the zip file below that corresponds to your group:

- [Group 0.zip](https://drive.google.com/file/d/1XDFOSfOD2ygFRv2iEd9iG1-V48dFdpQr/view?usp=sharing) (Dane and Makayla)
- [Group 1.zip](https://drive.google.com/file/d/1ELJbMgJIDk2KXv6QVhxEGV6qyA5Exzts/view?usp=sharing) (Felipe and Luiz)
- [Group 2.zip](https://drive.google.com/file/d/1LB71MJ_CcPssY7bWkPUjizOp317wz0u3/view?usp=sharing) (Boden and Douglas)

Each file contains two folders, _Group λ (IMG)_, that contains the set of images that your group will analyze, _and Group λ (XML)_, a folder that each group will use to save their annotations. Do not download a zip file that was not made for your group.

Extract the zip file in a safe and known location of your computer (e.g. the Documents folder), and proceed to the next step.

### - Step 3: Quick tutorial on LabelImg

Execute LabelImg on your computer (`python3 labelImg.py`). Click on the _Open Dir_ button available on the left sidebar, and select the _Group λ (IMG)_ folder that you extracted during Step 2:

![GIF - Open Dir](gifs/open-dir.gif)

This action will load all images of the _Group λ (IMG)_ folder into LabelImg. You can now browse the images using the _File List_ section at the bottom right of the tool:

![GIF - File List](gifs/file-list.gif)

To save all notes in the correct folder, click the _Change  Save Dir_ button on the left sidebar and select the _Group λ (XML)_ folder that you 
extracted during Step 2:

![GIF - Save Dir](gifs/change-savedir.gif)

To identify a new object in an image is quite simple: Click on the _Create RectBox_ button available on the left sidebar, and using the mouse pointer create a rectangle over the image where the object that you want to identify is located. A list of categories will be displayed. Select the most appropriate category for the object you want to identify:

![GIF - Create RectBox](gifs/create-rectbox.gif)

If the object you want to identify is not related to one of the categories available in the list, ignore it by clicking the exit button and proceeding to the next object. Also make sure that the rectangles you have created are positioned correctly. You can use the mouse cursor to adjust the size of an incorrectly positioned rectangle:

![GIF - Resize RectBox](gifs/resize-rectbox.gif)

After identifying all the possible objects in an image, click on the _Save_ button on the left sidebar to export your annotations to a XML file.
Make sure that a XML file is being created at the _Group λ (XML)_ folder.

## Performing the analysis

If you and your group have everything installed, it's time to start the analysis. The analysis is done individually, therefore, all members of a group must have the software installed on their computers. **You must no do the analysis in groups**.

 As you can see in the _File List_ section, every image file starts with an index _1, 2, 3, 4... N_. You must follow this index to perform the analysis, starting by analyzing the image with index equal to _1_ and ending by analyzing the image with index greater than or equal to _143_ (The last index varies from group to group).

But wait! You may also notice that some filenames end with the word _checkpoint_. A _checkpoint_ is a moment when you and your group will stop the analysis to discuss what you have done. You will find a new _checkpoint_ whenever you advance 10% of the
set of images you are analyzing. You must use every checkpoint to discuss the disagreements (e.g. To discuss why you identified an object that the other student did not identify), and to calculate the agreement for the last 10% of images that you and the other student analyzed. Please, also make sure that one member of your group is saving the final notes after each discussion, so we can use it after the analysis. In other words, when you find a disagreement, make sure that someone is saving the notes you decided to use after the discussion.

To calculate the agreement for the last 10% of images that you and your group analyzed, count the number of identified labels that match between you and the other student, and divide it by the number of labels identified. Here is an example:

| Images       | Labels Identified by Student A | Labels Identified by Student B |
|--------------|--------------------------------|--------------------------------|
| 1_97i6mn.jpg | Keyboard, Mouse                | Keyboard                       |
| 2_b2ixh4.jpg | Router, Monitor, Mouse         | Router                         |
| 3_god2vo.jpg | Laptop                         | Mouse                          |

- Labels that match between Student A and B: 2
- Number of labels identified: 7
- Agreement: 2 / 7 = 0.28 = 28%

If the agreement found at a checkpoint is greater than or equal to 60%, you and the other student can stop discussing disagreements.
Just divide the remaining images into two parts, so that each student analyzes a part. **Discussions or checkpoints
are no longer needed if the agreement is greater than or equal to 60%**. However, if the agreement is less than 60%, you and the other student must analyze the next 10% of your set of images until the next checkpoint. Repeat the process until an agreement of 60% or more is reached.

When your group has finished analyzing all the images, send the final notes in a zip file to _fronchettl@vcu.edu_.

## Summary

If you are still confused about what you need to do, here is a brief summary:

1. Install LabelImg.
2. Set up LabelImg for analysis.
3. Learn how to use LabelImg by reading our quick tutorial.
4. Make sure that your group also finished the first three steps.
5. Start analyzing the images individually until you and your group reach a checkpoint.
6. Discuss the objects you have identified in the images with your group and calculate the agreement.
7. Make sure someone in the group is writing down for every image what you decided during the discussion to a XML file.
8. If the agreement is less than 60%, return to Step 5 but now labeling the next 10% of images. If the agreement is greater than or equal to 60%, proceed to Step 9.
9. Divide the images that have not been analyzed into two parts, so that each member of the group analyzes one part.
10. Analyze your part individually.
11. After analyzing all the images, regroup the final XML files of your group into a zip file and send it to _fronchettl@vcu.edu_.

Feel free to send me a message if you feel that you need assistance with this tutorial: _fronchettl@vcu.edu_.
