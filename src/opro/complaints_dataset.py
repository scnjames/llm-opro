import json
from typing import List
from schema import ProblemExample

from src.opro.config import FINAL_ANSWER_SEP


def get_dataset(filename) -> List[ProblemExample]:
    target_path = rf"data/{filename}"
    with open(target_path, "r") as file:
        raw_data = json.loads(file.read())

    dataset = [
        ProblemExample(
            question=x["question"], answer=x["answer"].replace("####", FINAL_ANSWER_SEP)
        )
        for x in raw_data
    ]

    return dataset
