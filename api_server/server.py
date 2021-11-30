from bottle import route, run, response, request
import json

@route('/')
def main():
  response.content_type = "application/json"
  return json.dumps({"msg":"Hola Mundo del API!!!"})

# http://localhost:5000/sum?num1=?&num2=?
@route('/suma')
def sum():
  num1 = int(request.query["num1"])
  num2 = int(request.query["num2"])
  result = {"num1": num1, "num2":num2, "resultado": (num1 + num2)}
  response.content_type = "application/json"
  return json.dumps(result)

@route('/login', method="POST")
def login():
  user = request.POST.get('user','').strip()
  pswd = request.POST.get('pswd', '').strip()
  response.content_type = "application/json"
  return json.dumps({"user": user, "loginok": True})




run(host="localhost", port=5000, debug=True)
