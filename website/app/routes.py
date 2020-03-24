from app import app
import parseCovid

@app.route('/')
@app.route('/title')

def hello():
    return parseCovid.parse()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
