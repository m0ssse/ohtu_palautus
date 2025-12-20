from flask import Flask, render_template, request, session, redirect, url_for
from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new-game', methods=['POST'])
def new_game():
    game_type = request.form.get('game_type')
    session['game_type'] = game_type
    session['tuomari'] = {
        'ekan_pisteet': 0,
        'tokan_pisteet': 0,
        'tasapelit': 0
    }
    
    if game_type == 'b':
        session['tekoaly_siirto'] = 0
    elif game_type == 'c':
        session['tekoaly_muisti'] = [None] * 10
        session['tekoaly_vapaa_indeksi'] = 0
    
    return redirect(url_for('play'))

@app.route('/play')
def play():
    if 'game_type' not in session:
        return redirect(url_for('index'))
    
    game_type = session['game_type']
    tuomari_data = session['tuomari']
    
    game_names = {
        'a': 'Pelaaja vs Pelaaja',
        'b': 'Pelaaja vs Tekoäly',
        'c': 'Pelaaja vs Parannettu Tekoäly'
    }
    
    return render_template('play.html', 
                         game_type=game_type,
                         game_name=game_names.get(game_type, ''),
                         tuomari=tuomari_data)

@app.route('/make-move', methods=['POST'])
def make_move():
    if 'game_type' not in session:
        return redirect(url_for('index'))
    
    ekan_siirto = request.form.get('move')
    game_type = session['game_type']
    
    if not _onko_ok_siirto(ekan_siirto):
        return redirect(url_for('game_over'))
    
    # Determine second player's move
    if game_type == 'a':
        tokan_siirto = request.form.get('player2_move')
        if not _onko_ok_siirto(tokan_siirto):
            return redirect(url_for('game_over'))
        computer_move = None
    elif game_type == 'b':
        tekoaly = Tekoaly()
        tekoaly._siirto = session.get('tekoaly_siirto', 0)
        tokan_siirto = tekoaly.anna_siirto()
        session['tekoaly_siirto'] = tekoaly._siirto
        computer_move = tokan_siirto
    elif game_type == 'c':
        muisti = session.get('tekoaly_muisti', [None] * 10)
        vapaa_indeksi = session.get('tekoaly_vapaa_indeksi', 0)
        tekoaly = TekoalyParannettu(10)
        tekoaly._muisti = muisti
        tekoaly._vapaa_muisti_indeksi = vapaa_indeksi
        tokan_siirto = tekoaly.anna_siirto()
        tekoaly.aseta_siirto(ekan_siirto)
        session['tekoaly_muisti'] = tekoaly._muisti
        session['tekoaly_vapaa_indeksi'] = tekoaly._vapaa_muisti_indeksi
        computer_move = tokan_siirto
    
    # Update score
    tuomari_data = session['tuomari']
    tuomari = Tuomari()
    tuomari.ekan_pisteet = tuomari_data['ekan_pisteet']
    tuomari.tokan_pisteet = tuomari_data['tokan_pisteet']
    tuomari.tasapelit = tuomari_data['tasapelit']
    
    tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
    
    session['tuomari'] = {
        'ekan_pisteet': tuomari.ekan_pisteet,
        'tokan_pisteet': tuomari.tokan_pisteet,
        'tasapelit': tuomari.tasapelit
    }
    
    # Check if game has ended (someone reached 5 wins)
    if tuomari.peli_paattynyt():
        session['game_ended'] = True
    
    move_names = {'k': 'Kivi', 'p': 'Paperi', 's': 'Sakset'}
    
    return render_template('result.html',
                         player1_move=move_names.get(ekan_siirto, ekan_siirto),
                         player2_move=move_names.get(tokan_siirto, tokan_siirto),
                         computer_move=computer_move,
                         game_type=game_type,
                         tuomari=session['tuomari'],
                         game_ended=session.get('game_ended', False))

@app.route('/game-over')
def game_over():
    tuomari_data = session.get('tuomari', {
        'ekan_pisteet': 0,
        'tokan_pisteet': 0,
        'tasapelit': 0
    })
    session.clear()
    return render_template('game_over.html', tuomari=tuomari_data)

def _onko_ok_siirto(siirto):
    return siirto == "k" or siirto == "p" or siirto == "s"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
