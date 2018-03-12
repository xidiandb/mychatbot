from flask import Flask, jsonify
from flask import request
from bot import Bot
app = Flask(__name__)

bot=Bot('db')
@app.route('/chatbot/api', methods=['GET'])
def get_task():
    word=request.args['question']
    ret=bot.get_response(word)
    return jsonify({'anwser': ret})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')