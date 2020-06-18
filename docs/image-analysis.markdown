---
title: "Using LabelImg to Annotate Workstations"
layout: default
---
<style>
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 60%;
    }
</style>

## Introduction
Our mission for this task is to identify classes of objects in pictures of workstations.
To perform the task, we are going to use LabelImg, an annotation tool that is commonly used in object detection techniques. The task
is divided in groups of researchers, where each group will analyze a predefined set of workstations:

<b>Group 0:</b>
- Dane Acena
- Makayla Moster 

<b>Group 1:</b>
- Felipe Fronchetti
- Luiz Susin

<b>Group 2:</b>
- Boden Kahn
- Douglas Krug

If your name is listed in one of the groups above, please follow the tutorial below to perform the task.

## Preparing the environment
### - Step 1: Installing LabelImg
First, you will have to install the annotation tool. The tutorial explaining how to install it is available at:

<a href="https://github.com/tzutalin/labelImg/blob/master/README.rst#installation">README.rst#installation<a>

Find the correct instruction for your operating system and install LabelImg on your computer.

### - Step 2: Setting up LabelImg

 After installing the annotation tool, you have to prepare it for our analysis. First, replace the `data/predefined_classes.txt` file that is inside the LabelImg folder you downloaded with the following file:

<a href="download_files/predefined_classes.txt" download>predefined_classes.txt</a>

This file contains all the categories of objects we are going to identify in the images. Please, do not use the `predefined_classes.txt` file that originally comes with LabelImg, it does not contain the correct set of classes. 

After replacing the original `predefined_classes.txt` file with ours, download the zip file below that corresponds to your group:

- <a href="https://drive.google.com/file/d/1XDFOSfOD2ygFRv2iEd9iG1-V48dFdpQr/view?usp=sharing">Group 0.zip</a> (Dane and Makayla)
- <a href="https://drive.google.com/file/d/1ELJbMgJIDk2KXv6QVhxEGV6qyA5Exzts/view?usp=sharing">Group 1.zip</a> (Felipe and Luiz)
- <a href="https://drive.google.com/file/d/1LB71MJ_CcPssY7bWkPUjizOp317wz0u3/view?usp=sharing">Group 2.zip</a> (Boden and Douglas)

Each file contains two folders, `Group λ (IMG)`, that contains the set of images that your group will analyze, and `Group λ (XML)`, a folder that each group will use to save their annotations. Do not download a zip file that was not made for your group.

Extract the zip file in a safe and known location of your computer (e.g. the Documents folder), and proceed to the next step.

### - Step 3: Quick tutorial on LabelImg

Execute LabelImg on your computer (`python3 labelImg.py`). Click on the `Open Dir` button available on the left sidebar, and select the `Group λ (IMG)` folder that you extracted during Step 2:

<img src="gifs/open-dir.gif" class="center">

This action will load all images of the `Group λ (IMG)` folder into LabelImg. You can now browse the images using the `File List` section at the bottom right of the tool:

<img src="gifs/file-list.gif" class="center">

To save all notes in the correct folder, click the `Change  Save Dir` button on the left sidebar and select the `Group λ (XML)` folder that you 
extracted during Step 2:

<img src="gifs/change-savedir.gif" class="center">

To identify a new object in an image is quite simple: Click on the `Create RectBox` button available on the left sidebar, and using the mouse pointer create a rectangle over the image where the object that you want to identify is located. A list of categories will be displayed. Select the most appropriate category for the object you want to identify:

<img src="gifs/create-rectbox.gif" class="center">

If the object you want to identify is not related to one of the categories available in the list, ignore it by clicking the exit button and proceeding to the next object. Also make sure that the rectangles you have created are positioned correctly. You can use the mouse cursor to adjust the size of an incorrectly positioned rectangle:

<img src="gifs/resize-rectbox.gif" class="center">

After identifying all the possible objects in an image, click on the `Save` button on the left sidebar to export your annotations to a XML file.
Make sure that a XML file is being created at the `Group λ (XML)` folder.

## Performing the analysis

If you and your group have everything installed, it's time to start the analysis. The analysis is done individually, therefore, all members of a group must have the software installed on their computers. You <b>MUST NOT</b> do the analysis in groups.

 As you can see in the `File List` section, every image file starts with an index `1, 2, 3, 4... N`. You must follow this index to perform the analysis, starting by analyzing the image with index equal to `1` and ending by analyzing the image with index greater than or equal to `143` (The last index varies from group to group).

But wait! You may also notice that some filenames end with the word `checkpoint`. A `checkpoint` is a moment when you and your group will stop the analysis to discuss what you have done. You will find a new `checkpoint` whenever you advance 10% of the
set of images you are analyzing. You must use every checkpoint to discuss the disagreements (e.g. To discuss why you identified an object that the other student did not identify), and to calculate the agreement for the last 10% of images that you and the other student analyzed. Please, also make sure that one member of your group is saving the final notes after each discussion, so we can use it after the analysis. In other words, when you find a disagreement, make sure that someone is saving the notes you decided to use after the discussion.

To calculate the agreement for the last 10% of images that you and your group analyzed, count the number of identified labels that match between you and the other student, and divide it by the number of labels identified. Here is an example:

<center>
<table>
  <tr>
    <th>Images</th>
    <th>Labels Identified by Student A</th>
    <th>Labels Identified by Student B</th>
  </tr>
  <tr>
    <td>1_97i6mn.jpg</td>
    <td>Keyboard, Mouse </td>
    <td>Keyboard</td>
  </tr>
  <tr>
    <td>2_b2ixh4.jpg</td>
    <td>Router, Monitor, Mouse</td>
    <td>Router</td>
  </tr>
  <tr>
    <td>3_god2vo.jpg</td>
    <td>Laptop</td>
    <td>Mouse</td>
  </tr>
</table><br>
Labels that match between Student A and B: 2<br>
Number of labels identified: 7<br>
Agreement: 2 / 7 = 0.28 = 28%
</center>

If the agreement found at a checkpoint is greater than or equal to 60%, you and the other student can stop discussing disagreements.
Just divide the remaining images into two parts, so that each student analyzes a part. <b>Discussions or checkpoints
are no longer needed if the agreement is greater than or equal to 60%</b>. However, if the agreement is less than 60%, you and the other student must analyze the next 10% of your set of images until the next checkpoint. Repeat the process until an agreement of 60% or more is reached.

When your group has finished analyzing all the images, send the final notes in a zip file to `fronchettl@vcu.edu`.

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
11. After analyzing all the images, regroup the final XML files of your group into a zip file and send it to `fronchettl@vcu.edu`.

Feel free to send me a message if you feel that you need assistance with this tutorial: `fronchettl@vcu.edu`.