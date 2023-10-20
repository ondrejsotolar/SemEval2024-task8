# README for the SemEval2024-task8
# =================================

# To run the scripts you will need the libraries in requirements.txt. 
# Install them into a venv (using python 3.8+):
$ python -m venv path/to/myenv

# Activate the venv:
$ source path/to/myenv/bin/activate

# The data are downloaded to appollo.fi.muni:/nlp/projekty/msg_anon/SemEval2024-Task8/
# You can create a symlink in the project dir:
$ ln -s /nlp/projekty/msg_anon/SemEval2024-Task8 SemEval2024-Task8/data

# Train the baseline for task A:
$ cd SemEval2024-Task8; CUDA_VISIBLE_DEVICES=1 python subtaskA/baseline/transformer_baseline_ballanced.py -tr data/SubtaskA/subtaskA_train_monolingual.jsonl -t data/SubtaskA/subtaskA_dev_monolingual.jsonl -sb A -m distilbert-base-uncased -p data/distilbert_1ep

# Evaluate the solution for task A:
$ python subtaskA/scorer/scorer.py -g data/SubtaskA/subtaskA_dev_monolingual.jsonl -p data/distilbert_1ep 
