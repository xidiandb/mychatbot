import os
from tqdm import tqdm
from db import SqliteDao
import xlrd
import jieba
class MyTrainer():
    def train(self,file,db_dir):
        if os.path.exists(db_dir):
            os.remove(db_dir)
        dao=SqliteDao(db_dir)
        dao.build_table()
        try:
            excel = xlrd.open_workbook(file)
        except Exception:
            raise FileNotFoundError
        #获取第一个sheet
        sheet = excel.sheets()[0]
        #打印第i行数据
        rows= sheet.nrows
        for i in tqdm(range(0,rows)):
            a=sheet.row_values(i)[0]
            a=str(a)
            try:
                a=jieba.cut(a)
                a=' '.join(a)
            except Exception:
                pass
            b=sheet.row_values(i)[1]
            b=str(b)
            #print(a,b)
            count=0
            try:
                dao.insert(a,b)
                count+=1
                if count>=500:
                    count=0
                    dao.commit()
            except Exception :
                #print('insert error')
                pass
                #raise IOError
        dao.commit()