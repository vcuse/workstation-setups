import os
import json
import csv
import numpy as np

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
