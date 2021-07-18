import pathlib
import mne

study_name = 'age-prediction-benchmark'

bids_root = pathlib.Path(
    "/storage/store2/data/CHBMP_EEG_and_MRI/ds_bids_chbmp/")

deriv_root = pathlib.Path("/storage/store2/derivatives/CHBMP_EEG_and_MRI/")

demo_root = pathlib.Path('/storage/store2/data/CHBMP_Cognitive_Scales')

task = 'protmap'

datatype = 'eeg'
ch_types = ['eeg']

eeg_template_montage = mne.channels.make_standard_montage(
    'standard_1005'
).rename_channels(
    {'FFT7h': 'FFC7h', 'FFT8h': 'FFC8h'})

l_freq = 0.1
h_freq = 49

eog_channels = ['EOI', 'EOD']

find_breaks = False

spatial_filter = None

reject = 'autoreject_global'

on_error = 'abort'
on_rename_missing_events = 'warn'

N_JOBS = 10

epochs_tmin = 0
epochs_tmax = 10
baseline = None

rename_events = {
    "ojos abiertos": "eyes/open",
    "ojos cerrados": "eyes/closed",
    "hiperventilacion 1": "hyperventilation/1",
    "hiperventilacion 2": "hyperventilation/2",
    "hiperventilacion 3": "hyperventilation/3",
    "photic stimulation": "vis"
}

conditions = ["eyes/open", "eyes/closed"]

event_repeated = 'drop'
l_trans_bandwidth = 'auto'

h_trans_bandwidth = 'auto'


random_state = 42

shortest_event = 1

log_level = 'info'

mne_log_level = 'error'

# on_error = 'continue'
on_error = 'continue'
