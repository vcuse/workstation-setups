---
title: "Stage 2: Identifying submissions made by developers"
layout: default
---

In the second stage, two main tasks were performed: the analysis of the spreadsheet _authors-subreddits.csv_ and the creation of the spreadsheet _developers-submissions.csv_.

## Analysis of authors-subreddits.csv

Using the keywords defined in the _word\_list.txt_ file, the list of subreddits found in the profile of the authors (_authors-subreddits.csv_) were manually analyzed. If a keyword was found in the description or title of a subreddit, we changed the value of the `is_valid` column to TRUE, defining the subreddit as one related to software development. To facilitate our queries, we used the "Find in document" system of Google Docs (CTRL + F), searching for each keyword separately.

## Creation of developers-submissions.csv

Using the list of subreddits associated to software development that we identified above, we identified using the `submission_author_subreddits` field of each JSON file which submissions were made by developers in our dataset. In other words, if the list of subreddits with which an author interacted on her/his profile (`submission_author_subreddits`) included a subreddit related to software development, we considered the author as a developer. The list of submissions submitted by developers was saved in a spreadsheet file called _developers-submissions.csv_ with the following columns:

- `submission_id`: The identifier of the submission on Reddit.
- `submission_url`: The link to the submission on Reddit.
- `image_url`: The link to the submission image (i.e. workstation) on Reddit.
- `author_name`: The name of the author on Reddit.
- `author_id`: The identifier of the author on Reddit.
- `subreddits_found`: The subreddits associated to software development found in the author's profile.

It is valid to mention that, to avoid duplicates in this spreadsheet file, we ignored two or more submissions made by a same author. With the spreadsheet created, two researchers also manually
analyzed the submissions in order to identify the invalid ones.

We considered as invalid submissions:

- Submissions of old images (e.g. [tg7dwx1twjt11.jpg](https://i.redd.it/tg7dwx1twjt11.jpg), [emqdek3dgx051.jpg](https://i.redd.it/emqdek3dgx051.jpg), [BoaamNM.jpg](https://i.imgur.com/BoaamNM.jpg))
- Submissions of images that did not contain a workstation for software development (e.g. [weeku8hmdun31.png](https://i.redd.it/weeku8hmdun31.png), [bzKW7BY.jpg](https://i.imgur.com/bzKW7BY.jpg),[7z6diya32xr41.jpg](https://i.redd.it/7z6diya32xr41.jpg), [91bz1vs9w3j41.jpg](https://i.redd.it/91bz1vs9w3j41.jpg))
- Submissions of edited images, animations, cartoons or similar (e.g. [I0rmt4y](https://imgur.com/a/I0rmt4y))
- Submissions of images at work (e.g. [hxupdsad01q21.jpg](https://i.redd.it/hxupdsad01q21.jpg), [sfm8ri4l20041.jpg](https://i.redd.it/sfm8ri4l20041.jpg), [COlGU8D.jpg](https://i.imgur.com/COlGU8D.jpg))$
- Submissions of images where the workstation was not very clear or was difficult to analyze (e.g. [](https://i.redd.it/v8taf68e3c841.jpg), [6npct2uc52h41.jpg](https://i.redd.it/6npct2uc52h41.jpg), [HKCyt7b.jpg](https://i.imgur.com/HKCyt7b.jpg), [98oes67ueq051.jpg](https://i.redd.it/98oes67ueq051.jpg)).
- Submissions of images containing humans and/or private information.

$ Our paper is focused only on workstations at home, for this reason we disconsidered images at work.

Some users also submitted galleries instead of a single image (e.g. [5Cm4z](https://imgur.com/a/5Cm4z)). From these galleries, we selected the image that clearly captures the entire workstation (e.g. the gallery [5Cm4z](https://imgur.com/a/5Cm4z) was converted to [uaxM4xz.jpg](https://i.imgur.com/uaxM4xz.jpg)).
