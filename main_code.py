from flask import Flask, render_template, request
from app import buscar_jogador
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():

    return render_template('index.html', value='')

@app.route("/busca", methods=['POST', 'GET'])

def busca():
    NAME_PLAYER = request.args.get('name')
    TEAM_PLAYER = request.args.get('team')

    name, age, club, position, market_value = buscar_jogador(NAME_PLAYER, TEAM_PLAYER)
    string_sender = name + ','

    if string_sender != ',':
        string_return = 'Informações não encontradas'
    else:
        string_return = name + ', jogador do: ' + club + ' possui: ' + age + ' anos' + ', joga de: ' + position + ' e seu valor de mercado é: ' + market_value

    return render_template('index.html', value=string_return)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)

