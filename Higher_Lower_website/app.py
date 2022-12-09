from flask import Flask
from random import randint

app = Flask(__name__)

answer = randint(0,9)
print(answer)

#root route
@app.route('/')
def hello():
    return "<h2> Guess a number between 0 and 9 !</h2>" + '<img src="https://media2.giphy.com/media/Rs2QPsshsFI9zeT4Kn/giphy.gif?cid=ecf05e47pgrxhc9jpdv6fke9g405k3u8lxxgkhq34o53u8ak&rid=giphy.gif&ct=g" width="350" height="350" frameBorder="0" allowFullScreen/>'

#gues number through url 
@app.route('/<int:number>')
def guessing(number):
    if number < answer:
        return "<h1> Too low, try again !</h1>" + '<img src="https://media.giphy.com/media/nR4L10XlJcSeQ/giphy.gif" width="350" height="350" frameBorder="0" allowFullScreen/>'
    elif number > answer:
        return "<h1> Too high, try again !</h1>" + '<img src="https://media.giphy.com/media/efHwZH4DeN9ss/giphy.gif" width="350" height="350" frameBorder="0" allowFullScreen/>'
    else:
        return "<h1> Thats Right congrats !</h1>" + '<img src="https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif" width="350" height="350" frameBorder="0" allowFullScreen/>'

if __name__ == "__main__":
    app.run(debug=True)