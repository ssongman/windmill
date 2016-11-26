from flask import Flask, request
from datetime import datetime

class dateKoreanType:
    def __init__(self, format):
        self.format = format
    
    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0], self.format)
    

@app.route("/board", methods=["GET", "POST"])
def board():
    print(request.values.getlist("dates", type=dateKoreanType("%Y-%m-%d")))
    return "날짜들은 콘솔을 확인해보세요"