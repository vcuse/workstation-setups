import praw
import prawcore
import logging

class RedditParser:
    def __init__(self, client_id, client_secret, user_agent, exceptions_filename):
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  user_agent=user_agent)
        self.logger = logging.getLogger('RedditParser')
        file_handler = logging.FileHandler(exceptions_filename)
        self.logger.addHandler(file_handler)

    def parse_user_comments(self, username, limit=None):
        comments = []

        try:
            redditor = self.reddit.redditor(username)

            print('Extracting `top` comments for `u/{}`'.format(username))
            for comment in redditor.comments.top(limit=limit):
                print('Comment ID: {}, Username: {}'.format(comment.id, username))
                comment.mode = 'top'
                if comment not in comments:
                        comments.append(comment)


            print('Extracting `hot` comments for `u/{}`'.format(username))
            for comment in redditor.comments.hot(limit=limit):
                print('Comment ID: {}, Username: {}'.format(comment.id, username))
                comment.mode = 'hot'
                if comment not in comments:
                    comments.append(comment)


            print('Extracting `new` submissions for `u/{}`'.format(username))
            for comment in redditor.comments.new(limit=limit):
                print('Comment ID: {}, Username: {}'.format(comment.id, username))
                comment.mode = 'new'
                if comment not in comments:
                    comments.append(comment)

        except prawcore.exceptions.Forbidden as e: 
            self.logger.error(e)

        return comments

    def parse_user_submissions(self, username, limit=None):
        submissions = []

        try:
            redditor = self.reddit.redditor(username)

            print('Extracting `top` submissions for `u/{}`'.format(username))
            for submission in redditor.submissions.top(limit=limit):
                print('Submission ID: {}, Username: {}'.format(submission.id, username))
                submission.mode = 'top'
                if submission not in submissions:
                    submissions.append(submission)

            print('Extracting `hot` submissions for `u/{}`'.format(username))
            for submission in redditor.submissions.hot(limit=limit):
                print('Submission ID: {}, Username: {}'.format(submission.id, username))
                submission.mode = 'hot'
                if submission not in submissions:
                    submissions.append(submission)

            print('Extracting `new` submissions for `u/{}`'.format(username))
            for submission in redditor.submissions.new(limit=limit):
                print('Submission ID: {}, Username: {}'.format(submission.id, username))
                submission.mode = 'new'
                if submission not in submissions:
                    submissions.append(submission)

        except prawcore.exceptions.Forbidden as e: 
            self.logger.error(e)

        return submissions

    def parse_subreddit_information(self, subreddit):
        subreddit_info = None

        try:
            subreddit_info = self.reddit.subreddit(subreddit)
        except prawcore.exceptions.Forbidden as e:
            self.logger.exception(e)

        return subreddit_info

    def parse_subreddit_submissions(self, subreddit, limit=None):
        submissions = []

        subreddit = self.reddit.subreddit(subreddit)

        print('Extracting `top` submissions for `r/{}`'.format(subreddit))
        for submission in subreddit.top(limit=limit):
            print('Submission ID: {}, Subreddit: {}'.format(submission.id, subreddit))
            submission.mode = 'top'
            if submission not in submissions:
                submissions.append(submission)

        print('Extracting `hot` submissions for `r/{}`'.format(subreddit))
        for submission in subreddit.hot(limit=limit):
            print('Submission ID: {}, Subreddit: {}'.format(submission.id, subreddit))
            submission.mode = 'hot'
            if submission not in submissions:
                submissions.append(submission)

        print('Extracting `new` submissions for `r/{}`'.format(subreddit))
        for submission in subreddit.new(limit=limit):
            print('Submission ID: {}, Subreddit: {}'.format(submission.id, subreddit))
            submission.mode = 'new'
            if submission not in submissions:
                submissions.append(submission)

        return submissions