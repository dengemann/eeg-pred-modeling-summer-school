import os
import pathlib
import json
import mne
import config_chbp_eeg as cfg
import pandas as pd

import mne_bids

subjects = pd.read_csv(cfg.bids_root / "participants.tsv", sep = '\t')

demo_df = pd.read_csv(cfg.demo_root / "Demographic_data.csv", skiprows=1)
demo_df['subject'] = demo_df.pop('Code')
demo_df.set_index('subject', inplace=True)

json_list = list()
for sub in subjects.participant_id:
    fname = (
      cfg.bids_root / sub / 'eeg' / f'{sub}_task-protmap_eeg.json')
  
    if fname.exists():
        with open(fname, 'r') as fid:
            dd = json.load(fid)
        dd['subject'] = sub
        json_list.append(dd)

df = pd.DataFrame(json_list)
df['subject'] = df['subject'].str.replace('sub-', '')
df.set_index('subject', inplace=True)

df[demo_df.columns[:4]] = demo_df.loc[df.index, demo_df.columns[:4]]

df['montage'] = 'small'

df.loc[df.EEGChannelCount > 62, 'montage'] = 'big'
df['gender_code'] = df['Gender'].map({"F": 1, "M": 2})
df.groupby('montage')['Age', 'gender_code', 'Weight lb'].mean()
