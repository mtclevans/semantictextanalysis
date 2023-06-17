#Create a DataFrame with duplicated nested start tokens - gold entities
nestedStartGold = goldNer[goldNer.duplicated(['start_ident'], keep=False)]
print('Total Nested Start Tokens Gold Entities: ')
print(len(nestedStartGold.index))


#Create a DataFrame with duplicated nested start tokens - predicted entities
nestedStartPred = predNer[predNer.duplicated(['start_ident'], keep=False)]


#Create a DataFrame with duplicated nested end tokens - gold entities
nestedEndGold = goldNer[goldNer.duplicated(['end_ident'], keep=False)]
print('Total Nested End Tokens Gold Entities: ')
print(len(nestedEndGold.index))


#Create a DataFrame with duplicated nested end tokens - predicted entities
nestedEndPred = predNer[predNer.duplicated(['end_ident'], keep=False)]


#Start token as nested pair
#Merge NER gold labels and predictions for nested start tokens using function
#A prediction is correct if both inner and outer nested entities are predicted
mergeDf(nestedStartGold, nestedStartPred, 'total_ident', 'Entity')
cmNerGoldNestedNewStart = goldList
cmNerPredNestedNewStart = predList

#Display a Confusion Matrix of NER nested start tokens raw values
#The sample is too small to generate normalised recall evaluation
cmdNestedStartNew = ConfusionMatrixDisplay\
.from_predictions(cmNerGoldNestedNewStart, cmNerPredNestedNewStart)
fig, ax = plt.subplots(figsize=(15,15))
cmdNestedStartNew.plot(ax=ax)


#End token as nested pair
#Merge NER gold labels and predictions for nested end tokens using function
#A prediction is correct if both inner and outer nested entities are predicted
mergeDf(nestedEndGold, nestedEndPred, 'total_ident', 'Entity')
cmNerGoldNested = goldList
cmNerPredNested = predList

#Display a Confusion Matrix of NER nested end tokens raw values
cmdNestedEnd = ConfusionMatrixDisplay.from_predictions(cmNerGoldNested, 
                                                       cmNerPredNested)
fig, ax = plt.subplots(figsize=(15,15))
cmdNestedEnd.plot(ax=ax)

#Display a Confusion Matrix of NER nested end token normalised values
cmdNestedEndNorm = ConfusionMatrixDisplay.from_predictions(cmNerGoldNested,
                                                           cmNerPredNested,
                                                           normalize='true')
fig, ax = plt.subplots(figsize=(15,15))
cmdNestedEndNorm.plot(ax=ax)


#Start token one of a pair
#Merge NER gold labels and predictions for nested start tokens using function
#A prediction is correct if one of inner or outer nested entities are predicted
mergeDf(nestedStartGold, predNer, 'total_ident', 'Entity')
cmNerGoldNestedNewStart = goldList
cmNerPredNestedNewStart = predList


#Display a Confusion Matrix of NER nested start tokens raw values
#The sample is too small to generate normalised recall evaluation
cmdNestedStartNew = ConfusionMatrixDisplay\
.from_predictions(cmNerGoldNestedNewStart, cmNerPredNestedNewStart)
fig, ax = plt.subplots(figsize=(15,15))
cmdNestedStartNew.plot(ax=ax)


#End token one of a pair
#Merge NER gold labels and predictions for nested end tokens using function
#A prediction is correct if one of inner or outer nested entities are predicted
mergeDf(nestedEndGold, predNer, 'total_ident', 'Entity')
cmNerGoldNestedNew = goldList
cmNerPredNestedNew = predList


#Display a Confusion Matrix of NER nested end tokens raw values
cmdNestedEndNew = ConfusionMatrixDisplay.from_predictions(cmNerGoldNestedNew, 
                                                          cmNerPredNestedNew)
fig, ax = plt.subplots(figsize=(15,15))
cmdNestedEndNew.plot(ax=ax)


#Display a Confusion Matrix of NER nested end token normalised values
cmdNestedEndNewNorm = ConfusionMatrixDisplay.from_predictions(cmNerGoldNestedNew, 
                                                              cmNerPredNestedNew, 
                                                              normalize='true')
fig, ax = plt.subplots(figsize=(15,15))
cmdNestedEndNewNorm.plot(ax=ax)
