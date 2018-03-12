import re
import sqlite3

class Dao():
    pass

class SqliteDao(Dao):

    def __init__(self,db_dir):
        self.db_dir = db_dir
        try:
            self.conn = sqlite3.connect(self.db_dir)
            self.cur = self.conn.cursor()
        except Exception:
            raise ValueError

    def build_table(self):

        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS conversation
                (ask text, answer text);
                """)
        self.conn.commit()

    def get_all(self):
        ask=self.cur.execute('select rowid,ask from conversation')
        ask_list={}
        for row in ask:
            row_id=row[0]
            ask_list[row[1]]=row_id
        return ask_list
        
    def get_from_id(self,row_id):
        ans='对不起，小bot还在成长中'
        ret=self.cur.execute('''SELECT answer FROM conversation WHERE rowid = {} '''.format(row_id))
        for i in ret:
            ans=i[0]
        ans=ans.replace('[name]','你').replace('[cqname]','小bot')
        ans=re.sub('\[.+\]','',ans)
        return ans

    def insert(self,a,b):
            self.cur.execute("""
            INSERT INTO conversation (ask, answer) VALUES
            ('{}', '{}')
            """.format(a.replace("'", "''"), b.replace("'", "''")))

    def commit(self):
        self.conn.commit()