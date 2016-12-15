from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        r = json.loads(line)
        user = r['review_id']
        bizID = r['business_id']
        yield user, bizID

    def reducer(self, key, values):
        yield key, list(values)

    def mapper2(self,key,values):
        yield (key,len(values)),values

    def mapper3(self,key,values):
        for x in values:
            yield x, key

    def reducer3(self,key,values):
        yield key, list(values)

    def mapper4(self,key,values):
        for x in values:
            for y in values:
                if (x!=y):
                    yield (x,y), key

    def reducer4(self,key,values):
        yield key, list(values)

    def mapper5(self,key,values):
        num = len(values)
        den = key[0][1] +key[1][1] - len(values)
        temp = num/den
        if temp >= 0.5:
            yield (key[0][0],key[1][0]), temp
            
    def steps(self):
        return [
            MRStep(mapper = self.mapper,
                    reducer = self.reducer),
            MRStep(mapper = self.mapper2),
            MRStep(mapper = self.mapper3,
                   reducer = self.reducer3),
            MRStep(mapper = self.mapper4,
                   reducer = self.reducer4),
            MRStep(mapper = self.mapper5)]



if __name__ == '__main__':
    MRWordFrequencyCount.run()

