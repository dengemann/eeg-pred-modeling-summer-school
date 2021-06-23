import pathlib

study_name = 'age-prediction-benchmark'

bids_root = pathlib.Path(
    "/storage/store2/data/CHBMP_EEG_and_MRI/ds_bids_chbmp/")

deriv_root = pathlib.Path("/storage/store2/derivatives/CHBMP_EEG_and_MRI/")

ch_types = ['eeg']

conditions = ['rest']
