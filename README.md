# Polish-Morphology-LSTM
Trains a fairseq LSTM to predict polish word-endings

Uses labeled data from the pol.tsv file to train an LSTM.
 - The tsv file is split into three columns:
 1) nominative casing
 2) genitive casing
 3) gender of the word
 
 
 First, split the data into train, test, and dev files. Do this by using the inputReader.py script.
 
Next, run the output_script.py script to split the data into source (nom forms) and target (gen source) files.

The pre-process, train, and generate commands are included.

the WER_calulator script will calculate how accurate the LSTM is in generation.
