---
title: "Identifying submissions of developers"
layout: default
toc: true
---

In the second stage, two main tasks were performed: the analysis of the spreadsheet _authors-subreddits.csv_ and the creation of the spreadsheet _developers-submissions.csv_.

### Analysis of authors-subreddits.csv

Using the keywords defined in the _word\_list.txt_ file, the list of subreddits found in the profile of the authors (_authors-subreddits.csv_) were manually analyzed. If a keyword was found in the description or title of a subreddit, we changed the value of the `is_valid` column to TRUE, defining the subreddit as one related to software developers. To facilitate our queries, we used the "Find in document" system of Google Docs (CTRL + F), searching for each keyword separately.

### Creation of developers-submissions.csv

Using the list of subreddits associated to software development that we identified above, we identified using the `submission_author_subreddits` field of each JSON file (which is also a list), which submissions were made by developers in our dataset. In other words, if the list of subreddits with which an author interacted on her/his profile (`submission_author_subreddits`) included a subreddit related to software development, we considered the author as a software developer. The list of submissions submitted by developers was saved in a spreadsheet file called _developers-submissions.csv_ with the following columns:

- `submission_id`: The identifier of the submission on Reddit.
- `submission_url`: The link to the submission on Reddit.
- `image_url`: The link to the submission image (i.e. workstation) on Reddit.
- `author_name`: The name of the author on Reddit.
- `author_id`: The identifier of the author on Reddit.
- `subreddits_found`: The subreddits associated to software development found in the author's profile.

It is valid to mention that, to avoid duplicates in this spreadsheet file, we ignored two or more submissions made by a same author.
