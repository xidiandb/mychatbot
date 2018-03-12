from gensim.models import word2vec
from compare import MyComparsion
from db import SqliteDao as sqlitedao
from trainer import MyTrainer
import random

class Bot(object):

    def __init__(self,name,**kwargs):
        self.name=name
        model_dir = kwargs.get('model','data/dict.model')
        self.model=word2vec.Word2Vec.load(model_dir)
        self.db = kwargs.get('db','data/mybot1.db')
        self.comparsion=MyComparsion(self.model)

    def get_response(self,input_item):
        response=self.generate_response(input_item)
        return response

    def generate_response(self,input_statement):
        dao=sqlitedao(self.db)
        ask=dao.get_all()
        cos_max=-10
        close_sen=''
        close_row_id=random.randint(0,len(ask))
        for k,v in ask.items():
            num=self.comparsion.compare(k,input_statement)
            if num>=cos_max:
                cos_max=num
                close_sen=k
                close_row_id=v
        #print(cos_max)
        # if cos_max < 0.977:
        #     return ('对不起，小bot还在学习中')
        return dao.get_from_id(close_row_id)

    def generate_random_response(self):

        pass

    def train(self,file):
        trainer=MyTrainer()
        trainer.train(file,self.db)