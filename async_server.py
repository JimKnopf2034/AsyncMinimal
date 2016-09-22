from klein import Klein
import time

app = Klein()


@app.route('/hello')
def hello(request):
    time.sleep(2)
    return "Hello World!"

if __name__ == '__main__':
    app.run('localhost', 9090)
