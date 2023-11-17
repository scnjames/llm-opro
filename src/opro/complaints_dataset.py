import json
from typing import List
from schema import ProblemExample

from src.opro.config import FINAL_ANSWER_SEP


def get_dataset(filename) -> List[ProblemExample]:
    target_path = rf"data/{filename}.json"
    with open(target_path, "r"):
        raw_data = json.loads(target_path)

    dataset = [
        ProblemExample(
            question=x["question"], answer=x["answer"].replace("####", FINAL_ANSWER_SEP)
        )
        for x in raw_data
    ]

    return dataset
