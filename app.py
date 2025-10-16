from flask import FLask

app= FLask(__name__)
counter=0

@app.route('/')
def.hello():
    global counter
    counter +=1
    return f'Hello Docker!Visited{counter}.'

@app.route('/goodbye')
def goodbye():
    return 'GoodBye from Docker!'

if __name__== '__main__':
    app.run(host='0.0.0.0',port=5000)
