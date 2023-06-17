#Set precision to no decimal places for average sentences per abstract
pd.set_option('precision', 2)

#Count the number of sentences in the train set
countSentences(trainData)
trainSents = sentences
trainCount = float(count)


#Count the number of sentences in the dev set
countSentences(devData)
devSents = sentences
devCount = float(count)


#Count the number of sentences in the test set
countSentences(testData)
testSents = sentences
testCount = float(count)


#Average the number of sentences per abstract in the train set
meanSentences(trainSents)
trainAvg = float(avgSents)


#Average the number of sentences per abstract in the dev set
meanSentences(devSents)
devAvg = float(avgSents)


#Average the number of sentences per abstract in the test set
meanSentences(testSents)
testAvg = float(avgSents)


#Create a totals column for train, dev and test total and average sentences
stats = pd.DataFrame({'Sentences': [trainCount, devCount, testCount],
                      'Avg. Sentences': [trainAvg, devAvg, testAvg]}, 
                     index=['Train', 'Dev', 'Test'])


#Display Sentence dataset statistics
stats
