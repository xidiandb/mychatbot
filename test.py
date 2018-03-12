# import requests
# import json
# ss=requests.get('http://192.168.1.130:5000/chatbot/api?question=你好')
#
# d=json.loads(ss.text)
#
# print(d['anwser'])
# from bot import Bot
#
# bot=Bot('db',db='data/mybot1.db')
#
# #bot.train(file='data/data.xls')
#
# while True:
#     word = input('>')
#     print(bot.get_response(word))
# def sort_list(list1):
#     for i in range(len(list1)):
#         x=list1[i]
#         j=i
#         while j>0 and list1[j-1]>x:
#             list1[j]=list1[j-1]
#             j-=1
#         list1[j]=x
#
import re
from flask import Flask, render_template, request, jsonify
from config import DevConfig
from flask.ext.sqlalchemy import SQLAlchemy
from bot import Bot

app = Flask(__name__)

app.config.from_object(DevConfig)

db = SQLAlchemy(app)

bot=Bot('db',db='data/test.db')
class Conversation(db.Model):
    rowid=db.Column(db.Integer,primary_key=True)
    ask = db.Column(db.String(255))
    answer = db.Column(db.String(255))

    def __init__(self,ask):
        self.ask=ask

    def __repr__(self):
        return "<User '{}'>".format(self.ask)


@app.route('/')
def home():
    conv = Conversation.query.order_by(Conversation.rowid).all()
    return render_template(
        'index.html',
        conv=conv
    )
@app.route('/license')
def test():
    return render_template(
        'license.html'
    )
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404

@app.route('/chatbot/api', methods=['GET'])
def get_task():
    word = request.args['question']
    ret = bot.get_response(word)
    return jsonify({'anwser': ret})
        # 增
    #ask=Conversation(ask='你好')
    #db.session.add(ask)
    #db.session.commit()
    # 查
    #conv=Conversation.query.order_by(Conversation.ask).limit(5).all()
    # 分页
    # page=Conversation.query.paginate(1,10)
    # s=''
    # for i in page.items:
    #     s+=i.ask
    # return s
    # 条件查询 Model.query.filter_by(ask='xxx').all()这个是确切知道查找的值
    # filter(Model.id > 1).all()则不是严格的等于
    # 改
    # Conversation.query.filter_by(rowid=1).update({
    #     'ask':'CA QQ 远程 咨询 号码 是 多少 ？'
    # })
    # 删除
    # conv=Model.query.fileter_by(row_id=1).first()
    # db.session.delete(user)
    # db.session.commit()
    # page=Conversation.query.all()
    # s=''
    # for i in page:
    #     s+=str(i.rowid)+'---->'+i.ask+'<br>'+str(i.answer)+'<br/>'
    #
    # return s
if __name__=="__main__":
    app.run()