#Create a new DataFrame dropping nested end token entities for later analysis
endGoldNer = goldNer.drop_duplicates(subset=['end_ident'], keep=False)
endPredNer = predNer.drop_duplicates(subset=['end_ident'], keep=False)


#Merge NER gold labels and predictions for end tokens using defined function
mergeDf(endGoldNer, endPredNer, 'end_ident', 'Entity')
cmNerGoldEnd = goldList
cmNerPredEnd = predList


#Display a Confusion Matrix of NER end token only raw values
cmdEnd = ConfusionMatrixDisplay.from_predictions(cmNerGoldEnd, cmNerPredEnd)
fig, ax = plt.subplots(figsize=(15,15))
cmdEnd.plot(ax=ax)


#Display a Confusion Matrix of NER end token only normalised values
cmdEndNorm = ConfusionMatrixDisplay.from_predictions(cmNerGoldEnd, 
                                                     cmNerPredEnd, 
                                                     normalize='true')
fig, ax = plt.subplots(figsize=(15,15))
cmdEndNorm.plot(ax=ax)
