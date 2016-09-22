from twisted.web.static import File
from klein import Klein
import time

app = Klein()


@app.route('/hello')
def hello(request):
    time.sleep(2)
    return File('./templates/hello.html')

if __name__ == '__main__':
    app.run('localhost', 9090)
