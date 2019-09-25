# Simplified NegEX using Dictionaries

Requires: Pandas, Numpy and Sklearn


1)This script was written based on the paper "A Simple Algorithm for Identifying Negated Findings and Diseasesin Discharge Summaries" to identify negations in a sentence.<br>
https://reader.elsevier.com/reader/sd/pii/S1532046401910299?token=940777A032D47A94085A07AE082116AAADE764F565DFBACB6E04FB7B094227496565FD5478E0BCBBD59EB5814F0369D8

2)Identifies a neagation term in a sentence and looks for surrounging phrases within a fixed window size. The negation is then applied to all/some the phrases surrounding the negation term <br>

3)There are different type of negation terms. Here, we deal with 2 types 
-negation phrase that preceds the UMLS terms and the negation phrase the follows UMLS terms<br>

4)The test data to eavluate this tool is obtained from https://github.com/apvidul/negex/blob/master/negex.python/Annotations-1-120.txt <br>

# Results<br>
-Precision for negation detection = 0.932<br>
-Recall in negation detection = 0.951<br>
-Evaluation of the entire system:  (precision,recall,fscore) =(0.959, 0.966, 0.963) <br>

5)The tool can be improved by adding adding more types of negations terms, tuning the window size, adding new negation terms/patterns<br>

6)The output can be viewed at Results.txt
