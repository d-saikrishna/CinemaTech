import os
import pandas as pd

root = os.getcwd()

scripts_path = root + '/scripts/'

with open(scripts_path + 'ahalya.txt') as f:
    lines = f.readlines()

actions = []
for line in lines:
    if len(line) < 4:
        continue
    actions.append(line)

shot_division_df = pd.DataFrame()

shot_division_df['action'] = actions
shot_division_df['shot'] = None
shot_division_df['lens'] = None
shot_division_df['CGI?'] = None

shot_division_df.to_csv('shot_division/shot_division_ahalya.csv',
                        index=False)

