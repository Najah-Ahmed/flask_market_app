from flask import Flask,render_template

app=Flask(__name__)



@app.route('/')
def hello():
  return 'hello app'


@app.route('/home')
def hello_temp():
  return render_template('index.html.j2')




if __name__=='__main__':
  app.run(debug=True)