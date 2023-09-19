# SemEval-2024 Task 8: Multigenerator, Multidomain, and Multilingual Black-Box Machine-Generated Text Detection

[![Code License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://raw.githubusercontent.com/mbzuai-nlp/SemEval2024-task8/subtask_A_and_B/LICENSE)

<p align="left" float="left">
  <img src="images/MBZUAI-logo.png" height="40" />
</p>


[Subtasks](#subtasks) | [Data Source](#data_source) | [Data Format](#data_format) | [Evaluation Metrics](#scorer_and_official_evaluation_metrics) | [Baselines](#baselines) | [Organizers](#organizers) | [Contacts](#contacts)

Large language models (LLMs) are becoming mainstream and easily accessible, ushering in an explosion of machine-generated content over various channels, such as news, social media, question-answering forums, educational, and even academic contexts. Recent LLMs, such as ChatGPT and GPT-4, generate remarkably fluent responses to a wide variety of user queries. The articulate nature of such generated texts makes LLMs attractive for replacing human labor in many scenarios. However, this has also resulted in concerns regarding their potential misuse, such as spreading misinformation and causing disruptions in the education system. Since humans perform only slightly better than chance when classifying machine-generated vs. human-written text, there is a need to develop automatic systems to identify machine-generated text with the goal of mitigating its potential misuse. 

We offer three subtasks over two paradigms of text generation: (1) **full text** when a considered text is entirely written by a human or generated by a machine; and (2) **mixed text** when a machine-generated text is refined by a human or a human-written text paraphrased by a machine.

## Subtasks

- **Subtask A. Binary Human-Written vs. Machine-Generated Text Classification:** Given a full text, determine whether it is human-written or machine-generated. There are two tracks for subtask A: monolingual (only English sources) and multilingual.

- **Subtask B. Multi-Way Machine-Generated Text Classification:** Given a full text, determine who generated it. It can be human-written or generated by a specific language model.

- **Subtask C. Human-Machine Mixed Text Detection:** Given a mixed text, where the first part is human-written and the second part is machine-generated, determine the boundary, where the change occurs.

## <a name="data_source"></a>Data Source
The data for the task is an extension of the M4 dataset. Here are current statistics about the dataset.

<p align="center" width="80%">
    <a><img src="images/data_statistics.png" alt="Title" style="width: 80%; min-width: 250px; display: block; margin: auto;"></a>
</p>

The M4 dataset is described in the following [arXiv paper](https://arxiv.org/abs/2305.14902):

```bibtex
@article{wang2023m4,
      title={{M4}: Multi-generator, Multi-domain, and Multi-lingual
                   Black-Box Machine-Generated Text Detection}, 
      author={Yuxia Wang and
              Jonibek Mansurov and
              Petar Ivanov and
              Jinyan Su and
              Artem Shelmanov and
              Akim Tsvigun and
              Chenxi Whitehouse and
              Osama Mohammed Afzal and
              Tarek Mahmoud and
              Alham Fikri Aji and
              Preslav Nakov},
      year={2023},
      journal={arXiv:2305.14902},
      primaryClass={cs.CL}
}
```

## <a name="data_format"></a>Data Format

The datasets are JSONL files.
The data is located in the following folders:
* **Subtask A:**
  * Monolingual track:
    * subtaskA/data/subtaskA_train_monolingual.jsonl
    * subtaskA/data/subtaskA_dev_monolingual.jsonl
  * Multilingual track:
    * subtaskA/data/subtaskA_train_multilingual.jsonl
    * subtaskA/data/subtaskA_dev_multilingual.jsonl
* **Subtask B:**
  * subtaskB/data/subtaskB_train.jsonl
  * subtaskB/data/subtaskB_dev.jsonl
* **Subtask C:**
  * subtaskC/data/subtaskC_train.jsonl
  * subtaskC/data/subtaskC_dev.jsonl


### Statistics
| Subtask                     |  #Train |   #Dev  |
|:----------------------------|--------:|--------:|
| Subtask A (monolingual)     | 119,757 |   5,000 |
| Subtask A (multilingual)    | 172,417 |   4,000 |
| Subtask B                   |  71,027 |   3,000 |
| Subtask C                   |   3,649 |     505 |

### Data Download Instructions

To download the dataset for this project, follow these steps:

1. Install the `gdown` package using pip:

```
pip install gdown
````

2. Use `gdown` to download the dataset folders by providing the respective file IDs for each subtask:

| Task          | Google Drive Folder Link                                                                                           | File ID                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Whole dataset | [Google Drive Folder](https://drive.google.com/drive/folders/14DulzxuH5TDhXtviRVXsH5e2JTY2POLi)            | 14DulzxuH5TDhXtviRVXsH5e2JTY2POLi            |
| Subtask A     | [Google Drive Folder](https://drive.google.com/drive/folders/1CAbb3DjrOPBNm0ozVBfhvrEh9P9rAppc)            | 1CAbb3DjrOPBNm0ozVBfhvrEh9P9rAppc            |
| Subtask B     | [Google Drive Folder](https://drive.google.com/drive/folders/11YeloR2eTXcTzdwI04Z-M2QVvIeQAU6-)            | 11YeloR2eTXcTzdwI04Z-M2QVvIeQAU6-            |
| Subtask C     | [Google Drive Folder](https://drive.google.com/drive/folders/16bRUuoeb_LxnCkcKM-ed6X6K5t_1C6mL)            | 16bRUuoeb_LxnCkcKM-ed6X6K5t_1C6mL            |

```
gdown --folder https://drive.google.com/drive/folders/<file_id>
```
Make sure to replace `<file_id>` with the respective file IDs provided above when running the `gdown` command for the desired dataset.

3. After downloading place the files in their respective subtask folder. 





### Input Data Format

#### Subtask A:
An object in the JSON format:
```
{
  id -> identifier of the example,
  label -> label (human text: 0, machine text: 1,),
  text -> text generated by a machine or written by a human,
  model -> model that generated the data,
  source -> source (Wikipedia, Wikihow, Peerread, Reddit, Arxiv)  on English or language (Arabic, Russian, Chinese, Indonesian, Urdu, Bulgarian, German)
}
```

#### Subtask B:
An object of the JSON has the following format:
```
{
  id -> identifier of the example,
  label -> label (human: 0, chatGPT: 1, cohere: 2, davinci: 3, bloomz: 4, dolly: 5),
  text -> text generated by machine or written by human,
  model -> model name that generated data,
  source -> source (Wikipedia, Wikihow, Peerread, Reddit, Arxiv) on English
}
```


#### Subtask C:
An object of the JSON has the following format:
```
{
  id -> identifier of the example,
  label -> label (index of the word split by whitespace where change happens),
  text -> text generated by machine or written by human,
}
``` 

### Prediction File Format and Format Checkers

A prediction file must be one single JSONL file for all texts. The entry for each text must include the fields "id" and "label".  

The format checkers verify that your prediction file complies with the expected format. They are located in the ```format_checker``` module in each subtask directory.

#### Subtask A:
```python
python3 subtaskA/format_checker/format_checker.py --pred_files_path=<path_to_your_results_files> 
```

#### Subtask B:
```python
python3 subtaskB/format_checker/format_checker.py --pred_files_path=<path_to_your_results_files> 
```

### Subtask C:
To launch it, please run the following command:
```python
python3 subtaskC/format_checker/format_checker.py --pred_files_path=<path_to_your_results_files> 
```

Note that format checkers can not verify whether the prediction file you submit contains predictions for all test instances because it does not have an access to the test file.

## <a name="scorer_and_official_evaluation_metrics"></a>Scorer and Official Evaluation Metrics

The scorers for the subtasks are located in the ```scorer``` modules in each subtask directory.
The scorer will report the official evaluation metric and other metrics for a given prediction file.

### Subtask A:
The **official evaluation metric** for the Subtask A is **accuracy**. However, the scorer also reports macro-F1 and micro-F1. 

The scorer is run by the following command:
```python
python3 subtaskA/scorer/scorer.py --gold_file_path=<path_to_gold_labels> --pred_file_path=<path_to_your_results_file> 
```

### Subtask B:
The **official evaluation metric** for the Subtask B is **accuracy**. However, the scorer also reports macro-F1 and micro-F1. 

The scorer is run by the following command:
```python
python3 subtaskB/scorer/scorer.py --gold_file_path=<path_to_gold_labels> --pred_file_path=<path_to_your_results_file> 
```

### Subtask C:
The **official evaluation metric** for Subtask C is the **Mean Absolute Error (MAE)**. This metric measures the absolute distance between the predicted word and the actual word where the switch between human and machine occurs.
To launch it, please run the following command:
```python
python3 subtaskC/scorer/scorer.py --gold_file_path=<path_to_gold_labels> --pred_file_path=<path_to_your_results_file> 
```

## <a name="baselines"></a>Baselines

### Task A

Running the Transformer baseline:
 ```
python3 subtaskA/baseline/transformer_baseline.py --train_file_path <path_to_train_file> --test_file_path <path_to_test_file> --prediction_file_path <path_to_save_predictions> --subtask A --model <path_to_model>
 ```

The average results for the monolingual setup across three runs for RoBERTa is 0.74;

The average results for the multilingual setup across three runs for XLM-R is 0.72;

### Task B

Running the Transformer baseline:
 ```
python3 subtaskB/baseline/transformer_baseline.py --train_file_path <path_to_train_file> --test_file_path <path_to_test_file> --prediction_file_path <path_to_save_predictions> --subtask B --model <path_to_model>
 ```
The average results across three runs for RoBERTa is 0.75;

### Task C

Running the Transformer baseline
 ```
bash subtaskC/baseline/run.sh
 ```
The average MAE score across three runs for longformer is: 3.53 ± 0.212

To modify the hyperparameters, please edit the corresponding python command within the run.sh file.


## Organizers

- Yuxia Wang, Mohamed bin Zayed University of Artificial Intelligence
- Alham Fikri Aji, Mohamed bin Zayed University of Artificial Intelligence
- Artem Shelmanov, Mohamed bin Zayed University of Artificial Intelligence
- Akim Tsvigun, Semrush
- Chenxi Whitehouse, Mohamed bin Zayed University of Artificial Intelligence
- Petar Ivanov, Sofia University
- Jonibek Mansurov, Mohamed bin Zayed University of Artificial Intelligence
- Jinyan Su, Mohamed bin Zayed University of Artificial Intelligence
- Tarek Mahmoud, Mohamed bin Zayed University of Artificial Intelligence
- Osama Mohammed Afzal, Mohamed bin Zayed University of Artificial Intelligence
- Toru Sasaki, Technical University Darmstadt
- Thomas Arnold, Technical University Darmstadt
- Iryna Gurevych, Mohamed bin Zayed University of Artificial Intelligence
- Nizar Habash, Mohamed bin Zayed University of Artificial Intelligence
- Preslav Nakov, Mohamed bin Zayed University of Artificial Intelligence

## Contacts

Google group: [https://groups.google.com/g/semeval2024-task8/](https://groups.google.com/g/semeval2024-task8/)  
Email: semeval2024-task8@googlegroups.com
