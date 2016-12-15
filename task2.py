from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        r = json.loads(line)
        reviewer = (r['review_id'])
        lineSplit = r['text'].split()
        for word in lineSplit:
            word = word.lower()
            word = word.replace(',','')
            word = word.replace('.','')
            yield word, reviewer

    def reducer(self, key, values):
        #if (len(list(values))<=1):
        yield key, list(values)

    def mapper2(self,key,values):
        #print (values)
        if (len(values)==1):
            yield values[0],1

    def reducer2(self,key,values):
        yield None, (sum(values),key)

    def reducer3(self,_,values):
        yield max(values)       
        
    def steps(self):
        return [
            MRStep(mapper = self.mapper,
                    reducer = self.reducer),
            MRStep(mapper = self.mapper2,
                    reducer = self.reducer2),
            MRStep(reducer = self.reducer3)]



if __name__ == '__main__':
    MRWordFrequencyCount.run()

