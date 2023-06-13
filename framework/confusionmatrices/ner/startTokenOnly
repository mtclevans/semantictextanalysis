#Create a new DataFrame dropping nested start token entities for later analysis
startGoldNer = goldNer.drop_duplicates(subset=['start_ident'], keep=False)
startPredNer = predNer.drop_duplicates(subset=['start_ident'], keep=False)


#Merge NER gold labels and predictions for start tokens using defined function
mergeDf(startGoldNer, startPredNer, 'start_ident', 'Entity')
cmNerGoldStart = goldList
cmNerPredStart = predList


#Display a Confusion Matrix of NER start token only raw values
cmdStart = ConfusionMatrixDisplay.from_predictions(cmNerGoldStart, 
                                                   cmNerPredStart)
fig, ax = plt.subplots(figsize=(15,15))
cmdStart.plot(ax=ax)


#Display a Confusion Matrix of NER start token only normalised values
cmdStartNorm = ConfusionMatrixDisplay.from_predictions(cmNerGoldStart, 
                                                       cmNerPredStart, 
                                                       normalize='true')
fig, ax = plt.subplots(figsize=(15,15))
cmdStartNorm.plot(ax=ax)
