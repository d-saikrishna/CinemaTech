import os
import pandas as pd
import spacy

def find_material_nouns(sentence):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the input sentence
    doc = nlp(sentence)
    
    # Define a list of material noun POS (Part of Speech) tags
    material_noun_pos_tags = ["NOUN"]
    
    # Find material nouns in the sentence
    material_nouns = [token.text for token in doc if token.pos_ in material_noun_pos_tags]
    
    return material_nouns

root = os.getcwd()

scripts_path = root + '/scripts/'

with open(scripts_path + 'ahalya.txt') as f:
    lines = f.readlines()

actions = []
nouns = []
for line in lines:
    if len(line) < 4:
        continue
    actions.append(line)
    nouns.append(find_material_nouns(line))

shot_division_df = pd.DataFrame()

shot_division_df['action'] = actions
shot_division_df['shot'] = None
shot_division_df['lens'] = None
shot_division_df['CGI?'] = None
shot_division_df['props'] = nouns

shot_division_df.to_csv('shot_division/shot_division_ahalya.csv',
                        index=False)

