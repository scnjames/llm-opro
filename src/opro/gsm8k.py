import json
import os
from typing import List

from data_io import download_file
from data_io import get_cache_dir
from schema import ProblemExample

from src.opro.settings import FINAL_ANSWER_SEP

source_uri_format = "https://raw.githubusercontent.com/openai/grade-school-math/master/grade_school_math/data/{split}.jsonl"


def get_dataset(split: str = None) -> List[ProblemExample]:
    assert split in ["test", "train"]

    # target_path = os.path.join(get_cache_dir(), f'gsm8k_{split}.jsonl')
    # download_file(source_uri=source_uri_format.format(split=split), target_path=target_path)

    target_path = rf"C:/Users/sarah/OneDrive/Documents/code/{split}.jsonl"
    with open(target_path, "r") as fin:
        raw_data = [json.loads(x) for x in fin]

    dataset = [
        ProblemExample(
            question=x["question"], answer=x["answer"].replace("####", FINAL_ANSWER_SEP)
        )
        for x in raw_data
    ]

    return dataset
