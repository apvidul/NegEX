"""
Tool : simplified NegEX in python
Objective: Identifying negations in sentences.
Author: Vidul Ayakulangara Panickan
Date: 09/24/2019
Description: Idea behing the tool is from the paper "A Simple Algorithm for
Identifying Negated Findings and Diseases in Discharge Summaries 2001,
by WW Chapman
"""


import re
import csv
import pandas as pd
import numpy as np
from sklearn.metrics import precision_recall_fscore_support

def create_map(lst): #Creating a dictionary of negation phrases for faster lookup
    dictionary = {}
    for item in lst:
        words = item.split(" ")
        if words[0] in dictionary:
            dictionary[words[0]].append(item)
        else:
            dictionary[words[0]] = list()
            dictionary[words[0]].append(item)
    return dictionary



#Laoding the different kind of negation phrases

negations = pd.read_csv('negex_triggers.txt', sep ='\t\t', names=["Negation Phrase","Type"])

#Extracting prenegation and postnegation phrases from the annotation file
pren_phrases = list(negations[negations["Type"]=="[PREN]"]["Negation Phrase"])
post_phrases= list(negations[negations["Type"]=="[POST]"]["Negation Phrase"])


#Generating seperate dictonaries for identifying prenegation and postnegation phrases
pren_dictionary = create_map(pren_phrases)
post_dictionary = create_map(post_phrases)


#Loading the data from which information is to be extracted
sentences = pd.read_csv('sentences.txt', sep ='\t')
#print sentences.columns


#Creating new columns to add our findings later on
sentences["Extracted Findings"] = "No Result"
sentences["Extracted_Result"] = "Affirmed" #Just a default value

#You can have a peek at the dataframes by uncommenting the below
# print negations.head(5)
# print sentences.head(5)


#Again for faster lookup while searching for the string "[Phrase]"
# using dictionaries makes string comparrison a bit faster (Avoids bottleneck)
dic={}
dic["[PHRASE]"] = 1


#window size determins how many tokens you want to look ahead or lookback
#The orginial paper metnions a window size of 5
window_size = 5

#Iterationg through the dataframe/table row by row
for index, row in sentences.iterrows():

    """
    Things to Note
    1)The Concept corresponds to the medical PHRASE in the report. The PHRASE identifies
    the medical condition/ inference about a patient. This is usually converted to
    the corresponding UMLS term. Since I don't have access to the terms, I will be
    using the [PHRASE] tag to identify these terms/ statements.
    2)We will be iterating through each row of the table extracting one sentence at a time
    """

    #Uncomment below to see how the raw data looks like
    #print(row['Concept'], row['Sentence'])


    phrase = row['Concept'].lower()
    sentence = row['Sentence'].lower()

    sentence_words = sentence.split(" ")

    #Identifying phrases in the sentence

    sentence =sentence.replace(phrase,"[PHRASE]" +" "+phrase+ " "+ "[PHRASE] ")


    #Identifying the pre negations in the sentence

    for word in sentence_words:
        if word in pren_dictionary:
            pren_phrases = pren_dictionary[word]
            for phrase in pren_phrases:
                sentence =sentence.replace(phrase,"[PREN]" +" "+phrase+ " "+ "[PREN] ")


    sentence_words = sentence.split(" ")

    #Extracting the next tokens in the window size to look for PHRASES/UMLS terms
    #in actual application


    for pos in range(len(sentence_words)):
        if sentence_words[pos]=="[PREN]":

            if pos + window_size < len(sentence_words):
                words = sentence_words[pos : pos+ window_size]
            else:

                words = sentence_words[pos:]



            for word in words:
                if word in dic:

                    #For simplicity, we would be looking for all PHRASES after
                    #the PREN negation tag.
                    sub_string =" ".join(sentence_words[pos:])

                    pattern = r"\[PHRASE\](.*?)\[PHRASE\]"
                    string = re.findall(pattern, sub_string, flags=0)

                    if len(string):
                        sentences.at[index,'Extracted Findings'] = "[pre NEGATED]" + string[0]
                        sentences.at[index,'Extracted_Result'] = "Negated"
                        

    #Identifying the POST negations in the sentence


    for word in sentence_words:
        if word in post_dictionary:
            post_phrases = post_dictionary[word]
            for phrase in post_phrases:
                sentence =sentence.replace(phrase,"[POST]" +" "+phrase+ " "+ "[POST] ")

    #Uncomment below to see how the processed text looks like after Identifying
    #the POST negations
    #print sentence

    sentence_words = sentence.split(" ")



    for pos in range(len(sentence_words)):
        if sentence_words[pos]=="[POST]":

            if pos - window_size<0:
                words = sentence_words[:pos]
            else:
                words = sentence_words[pos- window_size:pos]



            #For simplicity, we would be looking for all PHRASES before
            #the POST negation tag.

            for word in words:
                if word in dic:
                    sub_string =" ".join(sentence_words[:pos])
                    print sub_string


                    pattern = r"\[PHRASE\](.*?)\[PHRASE\]"
                    string = re.findall(pattern, sub_string, flags=0)
                    if len(string):
                        sentences.at[index,'Extracted Findings'] = "[pos NEGATED]" + string[0]
                        sentences.at[index,'Extracted_Result'] = "Negated"

                        
#Comparing the acutal results and extracted results
print sentences



#Results
predicted =  sentences[sentences.Extracted_Result == "Negated"]
predicted_negations = predicted.shape[0]
predicted_negation_actually_true = predicted[predicted.Negation== "Negated"]
predicted_negation_actually_true_count = predicted_negation_actually_true.shape[0]


actual = sentences[sentences.Negation == "Negated"]
total_negations = actual.shape[0]


print predicted_negations, total_negations
print "Recall in detecting negations:", predicted_negations/float(total_negations)
print "Precision in detecting negations", float(predicted_negation_actually_true_count)/predicted_negations

y_true = np.array(sentences["Negation"])
y_pred = np.array(sentences["Extracted_Result"])
print y_true
print y_pred

print "Evaluation of the entire system (precision,recall,fscore)"
print precision_recall_fscore_support(y_true, y_pred, average='macro')
