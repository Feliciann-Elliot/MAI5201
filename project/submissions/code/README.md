# MAI5201 Course Project: BERT vs. n-Grams for Text Classification

## Overview

This project investigates the performance of contextual embeddings (BERT, SBERT) versus traditional n-gram FastText embeddings for text classification.  
It uses Kaggle datasets to evaluate classification accuracy, precision, recall, and F1-score.

---

## Project Structure

MAI5201_Course_Project/
│
├─ main.py # Main script to run experiments
├─ requirements.txt # Python dependencies
├─ fasttext_results.csv # Stores experiment results
├─ data/ # Folder for downloaded datasets
└─ README.md



---

## Setup Instructions

```bash


1. Install Dependencies
pip install -r requirements.txt

2. Run Script
python main.py

Running Single Experiments

Open main.py and locate the dataset list:

kaggle_datasets = [
    "amananandrai/ag-news-classification-dataset",
    "irustandi/yelp-review-polarity",
    "soumikrakshit/yahoo-answers-dataset",
    "kritanjalijain/amazon-reviews",
    "bhavikardeshna/amazon-customerreviews-polarity",
]

Important: Only enable one dataset at a time by commenting out the others. Then Run Script.

Below the main loop to run on these kaggle_datasets is code for single sentence testing you can uncomment it and comment the main loop to evaluate a single sentence and how it classifies 
(this can only be done once models have been trained). You will need to point the dataset_base and model_path to the name of the dataset/model you wish to evaluate.

```

