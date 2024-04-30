import pandas as pd
import os
from pathlib import Path


def generate_train_data():
    data = Path("./train")
    train_dataset = pd.DataFrame(columns=["phrase", "sentiment"])

    for folder in data.iterdir():
        if folder.name == ".DS_Store": continue
        
        for file in folder.glob("*.txt"):
            phrase = file.read_text()
            sentiment = folder.name
            train_dataset.loc[len(train_dataset)] = [phrase, sentiment]

    train_dataset.to_csv("train_dataset.csv", index=False)

    return 

def generate_test_data():
    data = Path("./test")
    test_dataset = pd.DataFrame(columns=["phrase", "sentiment"])

    for folder in data.iterdir():
        if folder.name == ".DS_Store": continue
        
        for file in folder.glob("*.txt"):
            phrase = file.read_text()
            sentiment = folder.name
            test_dataset.loc[len(test_dataset)] = [phrase, sentiment]

    test_dataset.to_csv("test_dataset.csv", index=False)

    return