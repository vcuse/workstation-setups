import os
import json
import csv
import numpy as np

# Old images:
# https://i.redd.it/tg7dwx1twjt11.jpg
# https://i.redd.it/emqdek3dgx051.jpg
# https://i.imgur.com/BoaamNM.jpg

# Images that do not contain a developer workstation: 
# https://i.redd.it/weeku8hmdun31.png
# https://i.imgur.com/bzKW7BY.jpg
# https://i.redd.it/7z6diya32xr41.jpg
# https://i.redd.it/91bz1vs9w3j41.jpg

# Images edited/photoshoped:
# https://imgur.com/a/I0rmt4y

# Images at work:
# https://i.redd.it/hxupdsad01q21.jpg
# https://i.redd.it/sfm8ri4l20041.jpg
# https://i.imgur.com/COlGU8D.jpg

# Images where the workstation is not very clear: 
# https://i.redd.it/v8taf68e3c841.jpg
# https://i.redd.it/6npct2uc52h41.jpg
# https://i.imgur.com/HKCyt7b.jpg
# https://i.redd.it/98oes67ueq051.jpg

# From galleries like this:
# https://imgur.com/a/5Cm4z
# We selected a image that clearly captures the whole workstation, for example:
# https://i.imgur.com/uaxM4xz.jpg

# Images containing humans.

class StageTwoMethod:
    def find_developers_submissions(self, dataset_path, subreddits_path):
        subreddits_spreadsheet = open(subreddits_path, 'r')
        subreddits_spreadsheet_reader = csv.DictReader(subreddits_spreadsheet)
        developers_submissions = []
        authors = []

        subreddits_for_developers = []
        for subreddit in subreddits_spreadsheet_reader:
            if subreddit['is_valid'] == 'TRUE':
                subreddits_for_developers.append(subreddit['subreddit'])

        for submission_filename in os.listdir(dataset_path):
            submission_filepath = os.path.join(dataset_path, submission_filename)

            with open(submission_filepath, 'r') as submission_file:
                submission_data = json.load(submission_file)
                subreddits_found = []

                for subreddit in submission_data['submission_author_subreddits']:
                    if subreddit in subreddits_for_developers:
                        subreddits_found.append(subreddit)

                if subreddits_found and submission_data['submission_author_id'] not in authors:
                    img_url = submission_data['submission_img_url']
                    
                    # To avoid unknown/weird URLs, we just look at links that end in .jpg, .png or that are from imgur.com

                    if img_url.endswith('.png') or img_url.endswith('.jpg') or 'imgur.com' in img_url:
                        developer_data = {'submission_id': submission_data['submission_id'],
                                          'submission_url': 'https://reddit.com/{}'.format(submission_data['submission_url']),
                                          'image_url':  submission_data['submission_img_url'],
                                          'author_name': 'https://reddit.com/u/{}'.format(submission_data['submission_author_name']),
                                          'author_id': submission_data['submission_author_id'],
                                          'subreddits_found': ",".join(subreddits_found)}

                        authors.append(submission_data['submission_author_id']) # Removing duplicates
                        developers_submissions.append(developer_data)

        return developers_submissions

    def create_developers_spreadsheet(self, developers_submissions, spreadsheet_path):
        with open(spreadsheet_path, 'w') as developers_spreadsheet:
            fieldnames = ['submission_id', 'submission_url', 'image_url', 'author_name', 'author_id', 'subreddits_found']
            writer = csv.DictWriter(developers_spreadsheet, fieldnames)
            writer.writeheader()
            writer.writerows(developers_submissions)
