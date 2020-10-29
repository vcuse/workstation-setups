import os
import csv
import urllib.request
from numpy import array_split, floor

class StageThreeMethod:
    def prepare_developers_spreadsheet_for_labeling(self, developers_path, labels_path, n_rows):
        if not os.path.isfile(developers_path):
            raise FileNotFoundError

        with open(developers_path, 'r') as developers_spreadsheet:
            reader = csv.DictReader(developers_spreadsheet)
            rows = [row for row in reader]

            if len(rows) >= n_rows:    
                with open(labels_path, 'w') as labeling_file:
                    writer = csv.DictWriter(labeling_file, reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows[:n_rows])
            else:
                print('Number of rows is smaller than n_rows.')

    def prepare_developers_spreadsheet_for_analysis(self, developers_path, analysis_path, img_folder_path, n_groups):
        if not os.path.isfile(developers_path):
            raise FileNotFoundError

        with open(developers_path, 'r') as developers_spreadsheet:
            reader = csv.DictReader(developers_spreadsheet)
            rows = [row for row in reader]
            rows_per_group = array_split(rows, n_groups) 

            with open(analysis_path, 'w') as analysis_file:
                fieldnames = reader.fieldnames + ['group','checkpoint']
                writer = csv.DictWriter(analysis_file, fieldnames)
                writer.writeheader()

                for group_number, group_rows in enumerate(rows_per_group):
                    group_name = 'Group {}'.format(group_number)
                    group_img_folder_path = os.path.join(img_folder_path, group_name)
                    checkpoint = 0.10

                    if not os.path.isdir(group_img_folder_path):
                        os.makedirs(group_img_folder_path)

                    for row_number, row in enumerate(group_rows):
                        row['group'] = group_name
                        extension = '.jpg'

                        if row['image_url'].endswith('.jpg'):
                            extension = '.jpg'
                        elif row['image_url'].endswith('.png'):
                            extension = '.png'
                        else:
                            print(row['image_url'])
                            raise Exception
                        
                        if row_number ==  floor(checkpoint * len(group_rows)):
                            filename = str(row_number + 1) + '_' + row['submission_id'] + '_checkpoint' + extension
                            row['checkpoint'] = 'Checkpoint! Time to discuss!'
                            checkpoint = checkpoint + 0.10
                        else:
                            filename = str(row_number + 1) + '_' + row['submission_id'] + extension
                            row['checkpoint'] = 'Analyze the images individually ...'

                        img_filepath = os.path.join(group_img_folder_path, filename)
                        urllib.request.urlretrieve(row['image_url'], img_filepath)
                        writer.writerow(row)
