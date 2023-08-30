# Simplified NegEX using Dictionaries

## Overview

This script is inspired by the paper titled "A Simple Algorithm for Identifying Negated Findings and Diseases in Discharge Summaries". The primary objective is to detect negations in sentences by identifying specific negation terms and analyzing surrounding phrases. The algorithm works within a fixed window size to identify negation and then applies it to phrases within the window.

## Types of Negation Terms

There are two types of negation phrases that are handled by the script:
1. Negation phrase that precedes the UMLS concepts.
2. Negation phrase that follows the UMLS concepts.

## Test Data

The script's evaluation and testing were performed using [Sentences.txt](https://github.com/apvidul/NegEX/blob/master/sentences.txt).

## Results

The script's performance is as follows:
- Precision for negation detection: 0.932
- Recall in negation detection: 0.951
- F1 score of the negation detection: 0.941
- Overall system evaluation:
  - Precision: 0.959
  - Recall: 0.966
  - F1 score: 0.963

## Future Improvements

The tool can be enhanced by:
- Incorporating additional types of negation terms.
- Tuning the window size for better accuracy.
- Adding new negation terms or patterns to increase coverage.

## Usage

1. Install the required dependencies: Pandas, Numpy, and Sklearn.
2. Run the NegEx.py script to identify negations and analyze surrounding phrases.
3. View the output in `Results.txt`.

## References

- Original Paper: ["A Simple Algorithm for Identifying Negated Findings and Diseases in Discharge Summaries"](https://reader.elsevier.com/reader/sd/pii/S1532046401910299?token=940777A032D47A94085A07AE082116AAADE764F565DFBACB6E04FB7B094227496565FD5478E0BCBBD59EB5814F0369D8)

