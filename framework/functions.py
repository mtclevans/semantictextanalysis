import pandas as pd
!python -m pip install nltk==3.5
import nltk

#Data Transformation

#Define a function to add attributes in an input file to a list for validation
def setSelections(inputData):
  global selections
  selections = []
  for k in inputData:
    selections.append(k)
    
    
#Define a dictionary of lists for entity and relation type columns
#This dictionary must be extended for new attributes for alternative tasks or datasets
types = {
  'Entity': ['Entity_start', 'Entity_end', 'Entity_type'],
  'Relation': ['Start_token_entity_1', 'End_token_entity_1',
                    'Start_token_entity_2', 'End_token_entity_2',
                    'Relation_type']
}


#Define a function to transform data from JSON files into DataFrame format
#This function can be employed for any PL-Marker evaluation using run_acener.py
def transformData(dataInput, selection, type):
  global labels
  if selection in selections:
    labels = pd.DataFrame(dataInput[selection].to_list(),
                          index = dataInput.index)
  else:
    raise ValueError ('Please choose a data subset from the input file: ' 
                      + str(selections))
  global docKey
  docKey = pd.DataFrame(dataInput['doc_key']).astype(str)
  #Merge attribute selection with its docKey
  labels = labels.merge(docKey, how='left',
                                left_index=True, right_index=True,
                                indicator=True, validate='1:1')
  if 'left_only' in labels['_merge']:
    raise Exception ('Misaligned document keys. Check the input data.')
  else:
    labels.set_index('doc_key', inplace=True)
    labels.drop('_merge', axis=1, inplace=True)
    if type in types:
      labels = pd.DataFrame(labels.stack(), columns = [type])
      labels = pd.DataFrame(labels[type].to_list(),
                          index =labels.index)
      labels = pd.DataFrame(labels.stack(), columns =[type])
      labels = pd.DataFrame(labels[type].to_list(), index=labels.index)
      labels.index.names = ['abstract', 'sentence', type]
    elif type == 'sentences' or 'qdas':
      print('Limited data transformation required.')
    else:
      raise ValueError ('Please choose a correct type from: '+ str(types))
  return labels
  
  
  #Define a function to rename the column names, which can be later extended
def nameColumns(data, type):
  if type in types:
    data.columns = (types[type])  
  else:
    raise ValueError ('Please choose a correct type from: '+ str(types))
  return data


#Define a function to count the number of sentences in any given file
def countSentences(inputFile):
  global sentences
  global count
  sentences = pd.DataFrame(inputFile['sentences'].to_list(),
                           index = inputFile.index)
  sentences = pd.DataFrame(sentences.stack(), columns=['sentences'])
  count = sentences.count()
  return sentences, count


#Define a function to calculate the mean number of sentences for each abstract
def meanSentences(sentences):
  global avgSents
  avgSents = sentences.drop(['sentences'], axis=1).reset_index()
  avgSents.columns=['abstract', 'sentences']
  avgSents = pd.DataFrame(avgSents.value_counts(subset=['abstract']))
  avgSents = avgSents.sort_values(by='abstract', ascending=True)
  avgSents = avgSents.mean()
  return avgSents


#NER and Gold RE: Define a function to merge gold and prediction dataframes on unique identifier
#And create a list as input to SkLearn ConfusionMatrix
def mergeDf (gold, pred, ident, type):
  #Validation to ensure unique identifier is present in list of idents
  if ident in idents:
    print('Identifier accepted')
  else:
    raise ValueError ('Please choose a correct identifier from: '+ str(idents))
  #Validation to ensure analysis type is in directionary of types
  if type in types:
      print('Type accepted')
  else:
    raise ValueError ('Please choose a correct type from: '+ str(types.keys()))
  dfMerge = gold.merge(pred, how='left', left_on=ident, right_on=ident,
                        suffixes=('_GOLD', '_PRED'), indicator=True,
                        validate='1:1')
  if 'right_only' in dfMerge['_merge']:
    raise Exception ('Incorrect merge. Assess data merge for corrections.')
  else:
    global goldList
    global predList
    confusionGold = dfMerge[[type + '_type_GOLD']]
    confusionGold[type + '_type_GOLD'] = \
    confusionGold[type + '_type_GOLD'].astype(str)
    goldList = confusionGold[type + '_type_GOLD'].values.tolist()
    goldList
    confusionPred = dfMerge[[type + '_type_PRED']]
    confusionPred[type + '_type_PRED'] = \
    confusionPred[type + '_type_PRED'].astype(str)
    predList = confusionPred[type + '_type_PRED'].values.tolist()
    predList
  return goldList, predList


#Predictions RE: Define a function to transform data relation predictions into DataFrame format
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


#POS Tagging

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
#Note: As SCIERC test set is already tokenized, there is no requirement to call
#nltk.word_tokenize

#Define a function to create POS tags
def posTags(data):
  global posTagDf
  columns = list(data)
  column = 0
  for i in columns:
    result = pd.DataFrame(data[column].dropna())
    result[column] = pd.DataFrame(result[column].apply(nltk.pos_tag))
    if column == 0:
      posTagDf = pd.DataFrame(result)
    else:
      posTagDf = posTagDf.merge(result, how='left', left_on='doc_key',
                              right_on='doc_key')
    column = column + 1
  return posTagDf
