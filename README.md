# OPRO Prompt Optimization
Implementing the prompt optimization from the paper "Large Language Models as Optimizers".

# Prerequisites
1. Python 3.9+
1. OpenAI API key

# Installation
Run `pip install -r requirements.txt` to install the required packages.

# Usage
Run `python opro.py` to run the prompt optimization.

# Overview of workflow
The aim of this repo is to use an LLM to optimize prompts when performing a given task. We have a dataset of questions 
and answers, where the answers include some basic working out.

In the context of this task, the training set is used to train the model in the sense that it is given to the LLM as an 
example of how to correctly work out the answer to the question. For this reason, the training examples are often 
referred to as 'demo examples'.

### Workflow

1. we take a seed instruction and create a set of prompts where each prompt contains:
      1. all the demo examples, where each question has the seed instruction appended to it
      1. a question from the test set at the end, to serve as the question for the LLM to answer
1. each of these prompts is then sent to the LLM to retrieve an answer to the question from the test set that was at the 
  end of the prompt
1. the results are the compared to the ground truth answer from the test set to give a 'score' to the seed instruction
1. this instruction and its score are saved
1. the LLM is then asked to generate 8 new ideas for instructions that can be added at the end of questions. This is done using a prompt containing:
      1. the previous instruction used and its score
      1. all the demo examples
      1. the instruction to come up with new ideas for instructions to add at the end of the questions
1. these 8 instructions then go through the same process as the seed instruction from steps 1-5. So instead of having 1 set 
of prompts at the end of step 1, we will have 8 sets of prompts where each set is the size of the test set.
1. once the new 8 instructions have had their scored worked out, they are saved with the seed instruction
1. these are ordered by score and the maximum score is stored
1. they are then added to the list of previous instructions used that are included in the prompt for the LLM to generate
   8 new instruction ideas
1. after this has repeated 5 times, the instruction that yielded the highest score on the test set is considered the 
   best instruction
  

# Citations
@misc{yang2023large,
      title={Large Language Models as Optimizers},
      author={Chengrun Yang and Xuezhi Wang and Yifeng Lu and Hanxiao Liu and Quoc V. Le and Denny Zhou and Xinyun Chen},
      year={2023},
      eprint={2309.03409},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
