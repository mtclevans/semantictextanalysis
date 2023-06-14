import pandas as pd


#Define a function to add attributes in an input file to a list for validation
def setSelections(inputData):
  global selections
  selections = []
  for k in inputData:
    selections.append(k)
    
    
    #Define a dictionary of lists for entity and relation type columns
#This dictionary must be further extended in the event of a new data attributes
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
  #Validation to ensure attribute selected is present in input file
  if selection in selections:
    labels = pd.DataFrame(dataInput[selection].to_list(),
                          index = dataInput.index)
  else:
    raise ValueError ('Please choose a data subset from the input file: ' 
                      + str(selections))
  #Define a global docKey attribute to merge data with its abstract index
  global docKey
  docKey = pd.DataFrame(dataInput['doc_key']).astype(str)
  #Merge attribute selection with its docKey
  labels = labels.merge(docKey, how='left',
                                left_index=True, right_index=True,
                                indicator=True, validate='1:1')
  #Validation to ensure that all data has a docKey, then set docKey as index
  if 'left_only' in labels['_merge']:
    raise Exception ('Misaligned document keys. Check the input data.')
  else:
    labels.set_index('doc_key', inplace=True)
    labels.drop('_merge', axis=1, inplace=True)
    #Depending on analysis type, split lists and assign relevant columns
    #Validation to raise error if analysis types is not in types dictionary
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




!python -m pip install nltk==3.5
import nltk
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