#Transform gold NER labels into appropriate format using defined functions
qDasNer = transformData(entPredTest, 'ner', 'qdas')
qDasNer = pd.DataFrame(qDasNer.stack(), columns = ['Entities_Gold'])
qDasNer.index.names = ['abstract', 'sentence no']


#Transform predicted NER labels into appropriate format using defined functions
transformData(entPredTest, 'predicted_ner', 'qdas')
qDasNerPred = labels
qDasNerPred = pd.DataFrame(qDasNerPred.stack(), columns = ['Entities_Pred'])
qDasNerPred.index.names = ['abstract', 'sentence no']


#Merge NER Gold Labels and Predictions with POS tagged sentences
qDasNerComplete = pd.merge(qDasFinal,qDasNer, how='outer', 
                           left_index=True, right_index=True)
qDasNerComplete = pd.merge(qDasNerComplete,qDasNerPred, how='outer', 
                           left_index=True, right_index=True)


#Transform gold RE labels into appropriate format using defined functions
qDasRe = transformData(entPredTest, 'relations', 'qdas')
qDasRe = pd.DataFrame(qDasRe.stack(), columns = ['Relations_Gold'])
qDasRe.index.names = ['abstract', 'sentence no']


#Merge RE Gold Labels and Predictions with POS tagged sentences
qDasNerComplete = pd.merge(qDasNerComplete,qDasRe, how='outer', 
                           left_index=True, right_index=True)


##Define a function to transform data RE predictions into .xlsx format
#A new function is required due to only partial data transformation compared to
#RE prediction transformation for Confusion Matrix analysis
#This function can be employed for any .xlsx export required using run_re.py

def transformRePred2 (dataInput):
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
                         columns = ['Sentence', 'Relations_Pred'])
    rePreds.drop('Sentence', axis=1, inplace=True)
    return rePreds


#Transform predicted RE labels into appropriate format using defined functions
qDasRePred = transformRePred2(predResults)
qDasRePred.index.names = ['abstract', 'sentence no']


#Merge RE predictions with POS tagged sentences, NER and RE gold
qDasNerComplete = pd.merge(qDasNerComplete,qDasRePred, how='outer', 
                           left_index=True, right_index=True)
                           
                           
#Export QDAS .xlsx file to local drive
%cd /content/drive/MyDrive/pl-marker-evaluation-script/pl-marker
qDasNerComplete.to_excel('Qdas.xlsx')
