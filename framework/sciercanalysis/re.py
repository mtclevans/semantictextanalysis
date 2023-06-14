#Create totals for RE test set
testRe = transformData(testData, 'relations', 'Relation')
testRe = nameColumns(testRe, 'Relation')
reTestTotals = pd.DataFrame(testRe.value_counts(subset='Relation_type'),
                             columns = ['Test'])


#Create totals for RE dev set
devRe = transformData(devData, 'relations', 'Relation')
devRe = nameColumns(devRe, 'Relation')
reDevTotals = pd.DataFrame(devRe.value_counts(subset='Relation_type'),
                            columns = ['Dev'])


#Create totals for RE train set
trainRe = transformData(trainData, 'relations', 'Relation')
trainRe = nameColumns(trainRe, 'Relation')
reTrainTotals = pd.DataFrame(trainRe.value_counts(subset='Relation_type'),
                              columns = ['Train'])


#Merge into all NER totals into one table for train, dev and test
reTotals = pd.merge(pd.merge(reTestTotals, reDevTotals, on='Relation_type'),
                     reTrainTotals, on='Relation_type')


#Create columns to display % split of NER labels for train, dev and test
reTotals['Dev %'] = (100 * (reTotals.groupby('Relation_type')['Dev']\
                      .transform('sum')) / reTotals['Dev'].sum())
reTotals['Train %'] = (100 * (reTotals.groupby('Relation_type')['Train']\
                              .transform('sum')) / reTotals['Train'].sum())
reTotals['Test %'] = (100 * (reTotals.groupby('Relation_type')['Test']\
                             .transform('sum')) / reTotals['Test'].sum())


#Rearrange dataframe columns to presentable format
reTotals = reTotals[['Train', 'Train %', 'Dev', 'Dev %', 'Test', 'Test %']]


#Create a totals column for train, dev and test
reTotals.loc['Total']= reTotals.sum()


#Display NER dataset statistics
reTotals
