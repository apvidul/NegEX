# Simplified NegEX using Dictionaries

1)This script was written based on the paper "A Simple Algorithm for Identifying Negated Findings and Diseasesin Discharge Summaries" to identify negations in a sentence.<br>
https://reader.elsevier.com/reader/sd/pii/S1532046401910299?token=940777A032D47A94085A07AE082116AAADE764F565DFBACB6E04FB7B094227496565FD5478E0BCBBD59EB5814F0369D8

2)Identifies a neagation term in a sentence and look for phrases within a fixed window size. The negation is then applied to all/some the phrases surrounding the negation term <br>

3)There are different type of negation terms. We basically deal with 2 types
-negation phrase that preceds the UMLS terms and the negation phrase the follows UMLS terms<br>

4)The test data to eavluate this tool is obtained from https://github.com/apvidul/negex/blob/master/negex.python/Annotations-1-120.txt <br>

# Results<br>
-Precision in identifying negations in the sentences = 0.961<br>
-Recall in indentifying negations in the entire test data = 0.729<br>
-Evaluation of the entire system:  (precision,recall,fscore) =(0.9440791925594441, 0.8468962282461021, 0.8847802452721746) <br>

5)The tool can be improved by adding additonaly types of negations terms, tuning the window size, adding new negation terms/patterns<br>

6)The output can be viewedt Results.txt
