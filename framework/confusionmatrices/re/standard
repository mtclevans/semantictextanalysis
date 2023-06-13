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


#Define a function to transform data relation predictions into DataFrame format

#A separate function is required due to a different file structure
#Both input SCIERC files and the entity prediction file contain
#dictionaries for each abstract, containing lists of attributes, which
#susequently contain lists of tokens, token ids and entity and relation types.
#However, the relation prediction output file contains one dictionary of key-value
#pairs, where each key pertains to an abstract number, and each value pertains
#a list of sentences, subsequently containing lists of token ids and relation
#types. Therefore, distinctly different data transformations requirements exist.

#This function can be employed for any PL-Marker evaluation using run_re.py

def transformRePred (dataInput):
  rePreds = pd.DataFrame(dataInput.stack(), columns=['relations'])
  rePreds.reset_index(inplace=True)
  rePreds.drop(['level_0', 'level_1'], axis=1)
  rePreds = pd.DataFrame(rePreds['relations'].to_list(), index = rePreds.index)
  rePreds = rePreds.merge(docKey, how='left',
                                left_index=True, right_index=True,
                                indicator=True, validate='1:1')
  #Validation to ensure that all data has a docKey, then and set docKey as index
  if 'left_only' in rePreds['_merge']:
    raise Exception ('Misaligned document keys. Check the input data.')
  else:
    rePreds.set_index('doc_key', inplace=True)
    rePreds.drop('_merge', axis=1, inplace=True)
    rePreds = pd.DataFrame(rePreds.stack(), columns=['Relations'])
    rePreds = pd.DataFrame(rePreds['Relations'].to_list(),
                         index = rePreds.index,
                         columns = ['Sentence', 'Relations'])
    rePreds.drop('Sentence', axis=1, inplace=True)
    rePreds = pd.DataFrame(rePreds['Relations'].to_list(),
                         index = rePreds.index)
    rePreds = pd.DataFrame(rePreds.stack(), columns = ['Relation'])
    rePreds = pd.DataFrame(rePreds['Relation'].to_list(), 
                           columns=['Entity_1',
                                    'Entity_2',
                                    'Relation_type'], index=rePreds.index)
    rePreds.index.names = ['abstract', 'sentence', 'relation']
    entity1 = pd.DataFrame(rePreds['Entity_1'].to_list(),
                           columns=['Start_token_entity_1',
                                    'End_token_entity_1'],
                           index=rePreds.index)
    entity2 = pd.DataFrame(rePreds['Entity_2'].to_list(),
                         columns=['Start_token_entity_2',
                                  'End_token_entity_2'],
                         index=rePreds.index)
    rePreds.reset_index(inplace=True)
    entity1.reset_index(inplace=True)
    entity1.drop(['abstract', 'sentence', 'relation'], axis=1, inplace=True)
    entity2.reset_index(inplace=True)
    entity2.drop(['abstract', 'sentence', 'relation'], axis=1, inplace=True)
    rePreds = rePreds.merge(entity1, how='left', left_index=True,
                                 right_index=True, validate='1:1')
    rePreds = rePreds.merge(entity2, how='left', left_index=True,
                                  right_index=True, indicator=True,
                                  validate='1:1')
  rePreds.drop(['Entity_1', 'Entity_2', '_merge'], axis=1, inplace=True)
  return rePreds
  
  
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
