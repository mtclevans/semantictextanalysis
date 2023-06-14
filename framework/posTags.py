#Transform SCIERC test sentences into appropriate format using defined functions
qDas = transformData(testData, 'sentences', 'sentences')


#Assign POS tags to all sentences in the SCIERC test set and transform into
#appropriate format
posTags(qDas)
qDasFinal = posTagDf
qDasFinal = pd.DataFrame(qDasFinal.stack(), columns = ['Sentence'])
qDasFinal.index.names = ['abstract', 'sentence no']
