#Transform gold RE labels into appropriate format using defined functions
goldRe = transformData(entPredTest, 'relations', 'Relation')
goldRe = nameColumns(goldRe, 'Relation')
goldRe.reset_index(inplace=True)


#Create unique identifiers for merging gold RE labels with RE predictions
goldRe['total_ident'] = (goldRe['abstract'].astype(str) 
                              + goldRe['Start_token_entity_1'].astype(str)
                              + goldRe['End_token_entity_1'].astype(str)
                              + goldRe['Start_token_entity_2'].astype(str)
                              + goldRe['End_token_entity_2'].astype(str))


#Restructure gold RE required data columns into expected order
goldReBoundaries = goldRe[['total_ident', 'Relation_type']]

  
  #Read Relation prediction file into Pandas Dataframe
try:
  %cd /content/drive/MyDrive/pl-marker-evaluation-script/pl-marker/scire-scibert
  predResults = pd.read_json('pred_results.json', lines=bool)
except FileNotFoundError:
  print('Files not found. Check file path and run_re.py has been evaluated.')


#Transform predicted RE labels into appropriate format using defined functions
predRe = transformRePred(predResults)


#Create unique identifiers for merging predicted RE labels with Gold RE labels
predRe['total_ident'] = (predRe['abstract'].astype(str) 
                              + predRe['Start_token_entity_1'].astype(str)
                              + predRe['End_token_entity_1'].astype(str)
                              + predRe['Start_token_entity_2'].astype(str)
                              + predRe['End_token_entity_2'].astype(str))


#Restructure predicted RE required data columns into expected order
predReBoundaries = predRe[['total_ident', 'Relation_type']]


#Evaluation Metric
#Relation prediction [Boundaries evaluation]: A relation is correctly predicted when both the boundaries of the subject and object entities and the relation type match the gold labels provided by the input data


#Merge RE gold labels and predictions using predefined function
mergeDf(goldReBoundaries, predReBoundaries, 'total_ident', 'Relation')
cmReGoldBoundaries = goldList
cmRePredBoundaries = predList


#Display a Confusion Matrix of RE raw values
cmdReBoundaries = ConfusionMatrixDisplay.from_predictions(cmReGoldBoundaries, 
                                                          cmRePredBoundaries)
fig, ax = plt.subplots(figsize=(15,15))
cmdReBoundaries.plot(ax=ax)


#Display a Confusion Matrix of RE normalised values for Recall evaluation
cmdReBoundariesNorm = ConfusionMatrixDisplay\
.from_predictions(cmReGoldBoundaries, cmRePredBoundaries, normalize='true')
fig, ax = plt.subplots(figsize=(15,15))
cmdReBoundariesNorm.plot(ax=ax)
