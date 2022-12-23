from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return redirect('http://localhost:2000')

# @app.route("/http://localhost:3000")
# def endpoint():
#     print("Yay")
@app.route('/my-link/')
def my_link():
  return render_template("/templates/welcome.html")

if __name__ == '__main__':
  app.run(host = 'localhost', port = 2000, debug=True)