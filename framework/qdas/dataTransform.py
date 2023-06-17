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


#Transform predicted RE labels into appropriate format using defined functions
qDasRePred = transformReXlsx(predResults)
qDasRePred.index.names = ['abstract', 'sentence no']


#Merge RE predictions with POS tagged sentences, NER and RE gold
qDasNerComplete = pd.merge(qDasNerComplete,qDasRePred, how='outer', 
                           left_index=True, right_index=True)
                           
                           
#Export QDAS .xlsx file to local drive
%cd /content/drive/MyDrive/pl-marker-evaluation-script/pl-marker
qDasNerComplete.to_excel('Qdas.xlsx')
