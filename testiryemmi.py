from flask import Flask, jsonify

app = Flask('__main__')


@app.route('/')
def index():
    return 'Hello world'


@app.route('/api/json')
def json():
    return jsonify({'a':1234, 'b':654})


if __name__ == '__main__':
    app.run()




