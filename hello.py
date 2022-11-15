from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    #return "<h1>Hello, World!</h1>"
    return render_template('home.html')

@app.route("/hola/<name>")ef hello(name):
    #return f"<h1>Hola {name}<h1>"
    return render_template('hola.html', name=name)

@app.route('/rick/<page>')
def rick_and_morty(page=1):
   

    url = f'https://rickandmortyapi.com/api/character/?page={page}'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

        #print(response.json())
    respuesta_json = response.json()
    info = respuesta_json['info']
    personajes = respuesta_json['results']

    next = int(page) + 1
    prev = int(page) - 1

    return render_template('rick.html', personajes=personajes, prev=prev, next=next )

@app.route('/search', methods=['GET', 'POST'])
def search():
    search = request.form['search']
    if len (search) > 0:
        url = f'https://rickandmortyapi.com/api/character/?name={search}'
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        respuesta_json = response.json()
        info = respuesta_json['info']
        personajes = respuesta_json['results']
        if info['page'] > 1:
            next = 2
            prev = 1

        return render_template('rick.html', personajes=personajes, prev=prev, next=next)
    else:
        
  


if __name__=='__main__':
    app.run(debug=True)