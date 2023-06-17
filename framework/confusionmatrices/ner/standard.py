#Read entity prediction file also containing gold labels into Pandas Dataframe
try:
  #Change directory path depending on model import and IDE employed
  %cd /content/drive/MyDrive/pl-marker-evaluation-script/pl-marker/sciner-scibert
  entPredTest = pd.read_json('ent_pred_test.json', lines=bool)
except FileNotFoundError:
  print('File not found. Check file path and run_acener.py has been evaluated')


#Add attributes present in entity prediction file to a list of attributes
setSelections(entPredTest)


#Transform gold NER labels into appropriate format using defined functions
goldNer = transformData(entPredTest, 'ner', 'Entity')
goldNer = nameColumns(goldNer, 'Entity')
goldNer.reset_index(inplace=True)


#Create unique identifiers for merging gold NER labels with NER predictions
goldNer['start_ident'] = (goldNer['abstract'].astype(str) 
                               + goldNer['Entity_start'].astype(str))
goldNer['end_ident'] = (goldNer['abstract'].astype(str) 
                             + goldNer['Entity_end'].astype(str))
goldNer['total_ident'] = (goldNer['abstract'].astype(str) 
                               + goldNer['Entity_start'].astype(str)
                               + goldNer['Entity_end'].astype(str))


#Restructure gold NER required data columns into expected order
goldNer = goldNer[['abstract', 'start_ident', 'end_ident', 'total_ident',
                             'Entity_type']]
                             
                       
#Transform predicted NER labels into appropriate format using defined functions
predNer = transformData(entPredTest, 'predicted_ner', 'Entity')
predNer = nameColumns(predNer, 'Entity')
predNer.reset_index(inplace=True)


#Create unique identifiers for merging predicted NER labels with NER gold labels
predNer['start_ident'] = (predNer['abstract'].astype(str)
                               + predNer['Entity_start'].astype(str))
predNer['end_ident'] = (predNer['abstract'].astype(str) 
                             + predNer['Entity_end'].astype(str))
predNer['total_ident'] = (predNer['abstract'].astype(str)
                               + predNer['Entity_start'].astype(str) 
                               + predNer['Entity_end'].astype(str))


#Restructure NER prediction required data columns into expected order
predNer = predNer[['start_ident', 'end_ident',
                            'total_ident', 'Entity_type']]
                            
                            
#Evaluation Metric
#Entity prediction: An entity is correctly predicted when both the entity
#boundaries and entity type match the gold label provided by the input data


#Define a list of possible unique identifiers
#This list must be further extended in the event of a new unique identifiers
idents = ['total_ident', 'start_ident', 'end_ident', 'strictReIdent']


#Define a function to merge gold and prediction dataframes on unique identifier
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
  
  
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

#Merge NER gold labels and predictions 'using defined function
mergeDf(goldNer, predNer, 'total_ident', 'Entity')
cmNerGold = goldList
cmNerPred = predList


#Display a Confusion Matrix of NER raw values
cmdNer = ConfusionMatrixDisplay.from_predictions(cmNerGold, cmNerPred)
fig, ax = plt.subplots(figsize=(15,15))
cmdNer.plot(ax=ax)


#Display a Confusion Matrix of NER normalised values for Recall evaluation
cmdNerNorm = ConfusionMatrixDisplay.from_predictions(cmNerGold, cmNerPred,
                                                     normalize='true')
fig, ax = plt.subplots(figsize=(15,15))
cmdNerNorm.plot(ax=ax)
