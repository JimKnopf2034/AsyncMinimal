from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route('/hello')
def hello():
    time.sleep(3)
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(port=9090)
