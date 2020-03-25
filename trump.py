from flask import Flask
from flask import render_template
import random
import requests

app = Flask(__name__)


@app.route('/play')
def get_pokemon():
    pokemon_id = random.randrange(1, 20)
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id))

    stats = response.json()['stats']
    pokemon_stats = {}

    for stat in stats:
        stat_name = stat['stat']['name']
        stat_score = stat['base_stat']
        pokemon_stats[stat_name] = stat_score

    return render_template('pokemon.html', stats=pokemon_stats)
