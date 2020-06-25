---
title: "Repository Overview"
layout: default
---
To simplify the understanding of our work, we divided it in stages:

![GIF - File List](imgs/png/method-overview.png)

### Stage 1

In the first stage, we extract submissions of workstations from three different subreddits. We save the metadata of these submissions in a folder in JSON format. We then analyze the profiles of authors who submitted the workstations, in order to identify which subreddits they usually interact with. This step was the first one created to identify which authors are developers. The complete list of subreddits found in the authors' profile is then exported to a spreadsheet called _authors-subreddits.csv_. Our idea was to manually analyze the subreddits found in the authors' profile using this spreadsheet, identify which subreddits were related to content for developers, and use these subreddits to identify which authors are developers. For this reason, we create a _word\_list.txt_ file containing keywords commonly associated to developers. These keywords are then used in Stage 2 to identify which subreddits are associated to content for developers in the _authors-subreddits.csv_ spreadsheet.

Read more: [Stage 1: Extracting submissions and analyzing subreddits](stage_one.html)

### Stage 2

In the second stage, we first analyze the spreadsheet _authors-subreddits.csv_ using the set of keywords. If a keyword is present in the name or description of the subreddit, we consider the subreddit as related to developers (e.g. _/r/python_ is a developer-related subreddit). Using the list of subreddits related to content for developers we identify in our list of submissions which submissions were made by developers (i.e. if an author contains in his profile a subreddit associated to developers, then the author is a developer). Next, we create a spreadsheet called _developers-submissions.csv_ containing all submissions of workstations that were probably sent by developers. At this point, we already know which authors are probably developers and consequently, which submissions were probably made by developers.

### Stage 3

The first thing we do in stage three is to manually analyze the _developers-submissions.csv_ spreadsheet looking for false positives. We remove invalid submissions (e.g. submissions that do not contain a workstation). We then use the final version of _developers-submissions.csv_ to generate two new spreadsheets: _developers-submissions-labels.csv_ and _developers-submissions-analysis.csv_. The first one (_developers-submissions-labels.csv_) contains one hundred submissions and is used to generate a list of categories of commonly found in workstations. This list of objects was saved in a spreadsheet file called _labels.csv_. The second spreadsheet (_developers-submissions-analysis.csv_) contains all submissions made by developers divided in groups for manual analysis. The ideia in this part of our study is to identify in the images of the workstations which objects could be found, in order to generate some cool insights (e.g. average of monitors, brand of earphones, etc). The images are downloaded from Reddit and saved in a folder, and the manual analysis is performed. All the objects observed for each image are annotated and saved in XML format.
