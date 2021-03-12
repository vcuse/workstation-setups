---
title: "Overview"
layout: default
toc: true
---

To simplify the understanding of our work, we divided it in stages:

![GIF - File List]({{ '/img/png/method-overview.png' | prepend: site.baseurl }})

### Stage 1

In the first stage, our primary task was to extract metadata from submissions of three subreddits (_r/workstations_,_r/workspaces_ and _r/battlestations_). We choose these subreddits because they usually contain images of workstations. The submissions were extracted using the PRAW library and were saved in a folder in JSON format. During the extraction of these submissions, we also extracted the subreddits with which the authors of these submissions interacted in their profiles. We considered interactions as submissions or comments sent to a subreddit.

The list of subreddits with which the authors of the submissions interacted was saved in a spreadsheet callled _authors-subreddits.csv_. In this first stage, we also created a _word\_list.txt_ file containing keywords commonly associated to software development. These keywords were used in Stage 2 to identify which subreddits were associated to developers in the _authors-subreddits.csv_ spreadsheet.

Read more: [Stage 1: Extracting metadata from subreddits and users' profiles](stage_one.html)

### Stage 2

The second stage was used to identify which submissions sent to one of the three subreddits (_r/workstations_,_r/workspaces_ and _r/battlestations_) were submitted by developers. First, we manually analyzed the spreadsheet _authors-subreddits.csv_ using the set of keywords from _word\_list.txt_. If a keyword was used in the name or description of a subreddit, we considered the subreddit as related to developers (e.g. _/r/python_ is a developer-related subreddit because it contains the keyword _python_). Using the list of subreddits related to software development we identified in our list of submissions which submissions were made by developers (i.e. if an author contains in his/her profile an interaction with a subreddit associated to software development, then the author is a developer). Next, we created a spreadsheet called _developers-submissions.csv_ containing all submissions of workstations that were probably sent by developers. At this point, we already knew which authors were probably developers and consequently, which submissions were probably submitted by developers.

Read more: [Stage 2: Identifying submissions made by developers](stage_two.html)

### Stage 3

In stage three, the first thing we did was to manually analyze the _developers-submissions.csv_ spreadsheet, removing false positives. We considered as false positives submissions that, for example, did not contain a workstation. We then used the final version of _developers-submissions.csv_ to generate two new spreadsheets: _developers-submissions-labels.csv_ and _developers-submissions-analysis.csv_. The first one (_developers-submissions-labels.csv_) contained one hundred submissions and was used to generate a list of categories of objects commonly found in workstations. This list of objects was saved in a spreadsheet file called _labels.csv_. The second spreadsheet (_developers-submissions-analysis.csv_) contained all submissions and was divided in four in groups for qualitative analysis. The ideia in this part of our study was to identify in the images of workstations which objects could be found, in order to generate some interesting insights (e.g. average of monitors, brands of laptops, etc). The workstations images were downloaded from Reddit and saved in a folder, and the manual analysis was performed. All the objects observed for each image were annotated and saved by the groups in XML format.

Read more: [Using LabelImg to Annotate Workstations](image-analysis.html)