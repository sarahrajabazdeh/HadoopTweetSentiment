# Data Science & Big Data Analytics Project

## Overview
The project is aimed to work with in the context of big data. It begins with an ingestion script responsible for reading data from the data source. Following ingestion, the data undergoes preprocessing using PySpark before being inserted into MongoDB for storage and further analysis.

Additionally, the project includes a Hadoop MapReduce job aimed at generating a dictionary of words from the dataset. This dictionary is then inserted in mongodb for further analysis.
The project leverages PySpark's machine learning libraries for advanced analytics tasks, including model building and evaluation.

In summary, the project includes data ingestion, preprocessing, storage, analysis and machine learning models within the context of big data analytics.

## MakeFile
This Makefile contains several commands to manage and execute tasks related to the project. Below is a brief description of each command along with its usage.

### Commands Available
- **initialization**: Initializes the project directories and copies the file in the Hadoop file system.

- **test-mapper**: Tests the mapper and reducer scripts with a sample input string that contains two records where each record contains a label and a text separated by a tab.
- **hadoop-mapper**: Runs the mapper and reducer scripts in the Hadoop file system.
- **top-10-words**: Runs the MongoDB query to get the top 10 words.
- **top-10-luw-gt-4-lte-7**: Runs the MongoDB query to get the top 10 words with length > 4 and <= 7.

### Usage
To use any of the commands, simply run `make <command>` in the terminal. For example, to initialize the project, you would run:\
`make initialization path=<path>`

For more details on each command, you can refer to the Makefile itself or use the `make help` command.

## Technologies
- Jupyter Notebook
- Python 
- PySpark
- Hadoop
- MongoDB 

## Dataset
We used the following dataset for this project:
[Kaggle - Sentiment140 Dataset with 1.6 million tweets](https://www.kaggle.com/datasets/kazanova/sentiment140/data)

## Flow Diagram
<a href="https://ibb.co/kqwW9vk"><img src="https://i.ibb.co/44X5Y39/Screenshot-from-2024-03-12-05-10-13.png" alt="Screenshot-from-2024-03-12-05-10-13" border="0"></a>
