from stage_one import StageOneMethod
from stage_two import StageTwoMethod
from stage_three import StageThreeMethod

# stage_one_method = StageOneMethod()
# subreddits = ['workspaces', 'workstations', 'battlestations']
# stage_one_method.create_submissions_dataset(subreddits, '../data/submissions/')
# stage_one_method.create_subreddits_spreadsheet('../data/submissions/', '../data/users-subreddits.csv')

# stage_two_method = StageTwoMethod()
# submissions = stage_two_method.find_developers_submissions('../data/submissions/','../data/users-subreddits.csv')
# stage_two_method.create_developers_spreadsheet(submissions, '../data/developers-submissions.csv')

stage_three_method = StageThreeMethod()
# stage_three_method.prepare_developers_spreadsheet_for_labeling('../data/developers-submissions.csv', '../data/developers-submissions-labels.csv', 100)
stage_three_method.prepare_developers_spreadsheet_for_analysis('../data/developers-submissions.csv', '../data/developers-submissions-analysis.csv', '../data/img/', 3)
