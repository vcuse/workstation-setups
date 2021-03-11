---
title: "Extracting metadata from subreddits and profiles"
layout: default
toc: true
---

In this first stage, two different tasks were performed: The extraction of submissions of workstations sent to a list of subreddits (e.g. _/r/workstations_), and the extraction of subreddits with which the authors of the submissions interacted in their profiles.

### Extraction of submissions

To extract submissions containing images of workstations, we focused our efforts in three specific subreddits: _/r/workstations_,_/r/workspaces_, _/r/battlestations_. The extraction was made using PRAW (Python Reddit API Wrapper). For each subreddit, we extracted the top, hot and new submissions, always ignoring duplicates. Each submission was saved in JSON format, and each file was named with the submission identifier on Reddit. The keys/values of each JSON file were:

- `submission_id`: The identifier of the submission on Reddit.
- `submission_title`: The title of the submission on Reddit.
- `submission_url`: The link to the submission on Reddit.
- `submission_img_url`: The link to the submission image (i.e. workstation) on Reddit.
- `submission_author_name`: The name of the author on Reddit.
- `submission_author_id`: The identifier of the author on Reddit.
- `submission_author_subreddits`: The subreddits that the author interacted with and that are publicly available on his profile.

One of our biggest concerns in this study was: If we are only interested in developers, how to identify a submission made by a developer? To solve this problem, we tried to use different strategies: First, we tried to identify submissions made by developers by analyzing the title and comments of every submission using a set of keywords (e.g. software, code, java), but we found a lot of false positives using this strategy. Then, we decided to manually analyze the profile of the authors, but we noticed that it would take too much time. At the end, we decided to use the following strategy: For each submission, we extracted and saved all the subreddits found in the author's profile, in which he/she commented or posted something. Then, using a spreadsheet, we manually identified for all the subreddits found in their profiles, which subreddits are commonly used by developers. Using this same spreadsheet, we then identified which images were sent by developers. In summary, if the profile of an author contained a developer-related subreddit, we considered the submission of the workstation as made by a developer.

### Creation of authors-subreddits.csv

As mentioned earlier, we generated a spreadsheet file called _authors-subreddits.csv_, containing the subreddits with which the authors of the submissions publicly interacted in their profiles. This spreadsheet file contains the following columns:

- `subreddit`: The full name of the subreddit on Reddit.
- `description`: The public description of the subreddit on Reddit.
- `id`: The identifier of the subreddit on Reddit.
- `is_valid`: A boolean column used in our analysis to identify if the subreddit is related to developers or not.

### Creation of word_list.txt

To identify which subreddits in the _authors-subreddits.csv_ spreadsheet were related to content for developers, we used a set of keywords. These keywords were divided in two categories:

- Programming languages: We considered names of programming languages as keywords in our analysis. To represent our list of languages, we used the fifty most popular languages according to the [Tiobe Index](https://www.tiobe.com/tiobe-index/) website. Date of extraction: May 27th, 2020.
- Tech terms: Inspired by the [TechTerms](https://techterms.com/category/technical) website, we also added to our word list a set of terms commonly used by developers such as _code_, _development_ and _programming_.

The _word\_list.txt_ file was used in Stage 2 to analyze the _authors-subreddits.csv_ spreadsheet.

### Links

- Script files: [main.py](https://github.com/vcuse/workstations/blob/master/code/main.py),
                [stage_one.py](https://github.com/vcuse/workstations/blob/master/code/stage_one.py),
                [reddit_parser.py](https://github.com/vcuse/workstations/blob/master/code/reddit_parser.py).
- Data: [JSON files](https://github.com/vcuse/workstations/tree/master/data/submissions),
        [authors_subreddits.csv](https://github.com/vcuse/workstations/blob/master/data/authors-subreddits.csv),
        [word_list.txt](https://github.com/vcuse/workstations/blob/master/data/word_list.txt).
