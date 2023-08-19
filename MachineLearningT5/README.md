# MachineLearningT5
Machine Learning Project Group 11 - Part 1-4

This is a Sentiment Analysis Project. Train and test data (Labelled and unlabelled) are attached in files provided.

Complete Part 1 and 2 to obtain estimated emission and transmission parameters. 

Part 1:
Ensure that the file paths are aligned with the downloaded folder name. 

Select run all, run all cells. 

To run EvalScript, do the following:
python evalResult.py ../ES/dev.out ../ES/dev.p1.out
python evalResult.py ../RU/dev.out ../RU/dev.p1.out


Part 2:
## Estimate Transition Parameters :
Use the formula -> transition probability = count ( prev_state -> current_state ) / count ( prev_state )

Returns a dictionary transition_probability which is of the form:

{('O', 'START'): 0.9289176090468497, ('O', 'O'): 0.885720190121926} 

where the transition probability of state START to state O is 0.9289 and transition probability of state O to state O is 0.8857

## Viterbi Algorithm :
Complete Part 3 to integrate obtained emission and transmission parameters into algorithm.

Complete Part 4 to suggest alternative model for Sentiment Analysis. In this case, we looked into the process of smoothing.

