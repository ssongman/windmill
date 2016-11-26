from flask import Flask
import logging

app = Flask(__name__)
app.config.update(DEBUG=True)

@app.route("/log")
def logger():
    app.logger.debug("DEBUG 메시지를 출력합니다")
    return "콘솔을 확인하여 주시기 바랍니다."

app.run()