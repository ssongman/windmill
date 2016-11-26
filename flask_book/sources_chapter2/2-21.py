@app.route('/board', defaults={'page': 'index'})
@app.route('/board/<page>') 