from flask import Flask
import logging

app = Flask(__name__)
app.config.update(DEBUG=True)
app.debug_log_format = "%(levelname)s in %(module)s [%(lineno)d]: %(message)s"

@app.route("/log")
def logger():
    app.logger.debug("DEBUG 메시지를 출력했어요.")
    return "flask 인스턴스에서 출력되는 기본 로그 메시지 형태 변경"

app.run()