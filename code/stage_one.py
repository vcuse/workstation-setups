import os
import json
import csv
from reddit_parser import RedditParser

class StageOneMethod:
    def __init__(self):
        client_id = os.environ['REDDIT_ID']
        client_secret = os.environ['REDDIT_SECRET']
        user_agent = "desktop:reddit-parser-script:1.0 (by /u/{})".format(os.environ['REDDIT_USERNAME'])

        if not 'REDDIT_ID' in os.environ:
            raise('You did not set a REDDIT_ID variable in your environment variables.')
        if not 'REDDIT_USERNAME' in os.environ:
            raise('You did not set a REDDIT_USERNAME variable in your environment variables.')
        if not 'REDDIT_SECRET' in os.environ:
            raise('You did not set a REDDIT_SECRET variable in your environment variables.')

        self.parser = RedditParser(client_id, client_secret, user_agent, 'exceptions.log')

    def create_subreddits_spreadsheet(self, dataset_path, spreadsheet_path):
        subreddits = {}

        for filename in os.listdir(dataset_path):
            filepath = os.path.join(dataset_path, filename)

            with open(filepath, 'r') as json_file:
                json_data = json.load(json_file)

                for author_subreddit in json_data['submission_author_subreddits']:
                    if author_subreddit not in subreddits.keys():
                        subreddit_info = self.parser.parse_subreddit_information(author_subreddit)

                        if subreddit_info:
                            subreddit_row = {'subreddit': subreddit_info.display_name,
                                             'description': subreddit_info.public_description,
                                             'id': subreddit_info.id,
                                             'is_valid': False}

                            subreddits[author_subreddit] = subreddit_row

        with open(spreadsheet_path, 'w') as subreddits_spreadsheet:
            fieldnames = ['subreddit', 'description', 'id', 'is_valid']
            writer = csv.DictWriter(subreddits_spreadsheet, fieldnames)
            writer.writeheader()
            writer.writerows(subreddits.values())

    def create_submissions_dataset(self, subreddits, directory_path):
        submissions = []

        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)

        for subreddit in subreddits:
            submissions = submissions + self.parser.parse_subreddit_submissions(subreddit)

        for submission in submissions:
            submission_filepath = os.path.join(directory_path, submission.id + '.json')

            if not os.path.isfile(submission_filepath):
                author_subreddits = []

                if hasattr(submission.author, 'name'):
                    author_submissions = self.parser.parse_user_submissions(submission.author.name)
                    author_comments = self.parser.parse_user_comments(submission.author.name)

                    for author_submission in author_submissions:
                        if hasattr(author_submission.subreddit, 'display_name'):
                            if author_submission.subreddit.display_name not in author_subreddits:
                                author_subreddits.append(author_submission.subreddit.display_name)

                    for author_comment in author_comments:
                        if hasattr(author_comment.subreddit, 'display_name'):
                            if author_comment.subreddit.display_name not in author_subreddits:
                                author_subreddits.append(author_comment.subreddit.display_name)

                    submission_data = {
                        'submission_id': submission.id,
                        'submission_title': submission.title,
                        'submission_url': submission.permalink,
                        'submission_img_url': submission.url,
                        'submission_author_name': submission.author.name,
                        'submission_author_id': submission.author.id,
                        'submission_author_subreddits': author_subreddits,
                    }

                    with open(submission_filepath, 'w') as json_file:
                        json.dump(submission_data, json_file)


