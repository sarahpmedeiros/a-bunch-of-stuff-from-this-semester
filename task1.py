from mrjob.job import MRJob
import json

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        r = json.loads(line)
        print (r['review_id'])
        print ('stop')
        lineSplit = r['text'].split()
        for word in lineSplit:
            word = word.lower()
            word = word.replace(',','')
            word = word.replace('.','')
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRWordFrequencyCount.run()

