---
title: "Stage 1: Extracting submissions and analyzing subreddits"
layout: default
---

In this first stage, two different tasks were performed: The extraction of submissions of workstations sent to a list of subreddits (e.g. _/r/workstations_), and the identification of subreddits that are commonly used by programmers (e.g. _/r/python_).

## Extracting submissions

To extract submissions containing images of workstations, we focused our efforts in three specific subreddits: _/r/workstations_,_/r/workspaces_, _/r/battlestations_. The extraction was made using PRAW (Python Reddit API Wrapper). For each subreddit, we extracted the top, hot and new submissions, always ignoring duplicates. Each submission was saved in JSON format, and each file was named with the submission identifier on Reddit. The keys of each JSON file were:

- `submission_id`: The identifier of the submission on Reddit.
- `submission_title`: The title of the submission on Reddit.
- `submission_url`: The link to the submission on Reddit.
- `submission_img_url`: The link to the submission image (i.e. workstation) on Reddit.
- `submission_author_name`: The name of the author on Reddit.
- `submission_author_id`: The identifier of the author on Reddit.
- `submission_author_subreddits`: The subreddits that the author interacted with and that are publicly available on his profile.

One of our biggest concerns in this study was: How to identify a submission made by a developer? To solve this problem, we tried to use different strategies: First, we tried to identify submissions made by developers by analyzing the title and comments of every submission using a set of keywords (e.g. Software, Code, Java), but we found a lot of false positives using this strategy. Then, we decided to manually analyze the profile of the authors, but we noticed that it would take too much time. At the end, we decided to use the following strategy: For each submission, we extract and save all the subreddits found in the author's profile, in which he commented or posted something. Then, using a spreadsheet, we identified for all the subreddits found in the submissions, which subreddits are commonly used by developers. Then, using the `submission_authors_subreddits` again, we identified which images were sent by developers. In other words, if the profile of the author contained a developer-related subreddit, we considered the submission as made by a developer.
