from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html',num = 10)

if __name__ == '__main__':
    app.debug = True
    app.run()




from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    list = {'apple':'リンゴ','orange':'みかん','lemon':'レモン'}
    return render_template('index.html',list = list)

if __name__ == '__main__':
    app.debug = True
    app.run()