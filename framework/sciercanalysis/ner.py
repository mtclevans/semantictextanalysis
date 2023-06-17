#Read in data from files SCIERC files
try:
  #Change directory path depending on model import and IDE employed
  %cd /content/drive/MyDrive/pl-marker-evaluation-script/pl-marker/scierc
  testData = pd.read_json('test.json', lines=bool)
  devData = pd.read_json('dev.json', lines=bool)
  trainData = pd.read_json('train.json', lines=bool)
except FileNotFoundError:
  print('File not found. Check file path and SCIERC files are present')


#Add attributes present in test file to a list of possible attribute selections
setSelections(testData)


#Create totals for NER test set
testNer = transformData(testData, 'ner', 'Entity')
testNer = nameColumns(testNer, 'Entity')
nerTestTotals = pd.DataFrame(testNer.value_counts(subset='Entity_type'),
                             columns = ['Test'])


#Create totals for NER dev set
devNer = transformData(devData, 'ner', 'Entity')
devNer = nameColumns(devNer, 'Entity')
nerDevTotals = pd.DataFrame(devNer.value_counts(subset='Entity_type'),
                            columns = ['Dev'])


#Create totals for NER train set
trainNer = transformData(trainData, 'ner', 'Entity')
trainNer = nameColumns(trainNer, 'Entity')
nerTrainTotals = pd.DataFrame(trainNer.value_counts(subset='Entity_type'),
                              columns = ['Train'])


#Merge into all NER totals into one table for train, dev and test
nerTotals = pd.merge(pd.merge(nerTestTotals, nerDevTotals, on='Entity_type'),
                     nerTrainTotals, on='Entity_type')


#Set precision to no decimal places complete entities and relations
pd.set_option('precision', 0)


#Create columns to display % split of NER labels for train, dev and test
nerTotals['Dev %'] = (100 * (nerTotals.groupby('Entity_type')['Dev']\
                             .transform('sum')) / nerTotals['Dev'].sum())
nerTotals['Train %'] = (100 *(nerTotals.groupby('Entity_type')['Train']\
                              .transform('sum')) / nerTotals['Train'].sum())
nerTotals['Test %'] = (100 *(nerTotals.groupby('Entity_type')['Test']\
                             .transform('sum')) / nerTotals['Test'].sum())


#Rearrange dataframe columns to presentable format
nerTotals = nerTotals[['Train', 'Train %', 'Dev', 'Dev %', 'Test', 'Test %']]


#Create a totals column for train, dev and test
nerTotals.loc['Total']= nerTotals.sum()


#Display NER dataset statistics
nerTotals
