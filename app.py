from flask import Flask, render_template, request, session, redirect, url_for
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate random secret key

@app.route('/')
def index():
    """Halaman utama untuk memilih mode game"""
    return render_template('index.html')

@app.route('/game/<mode>')
def game(mode):
    """Halaman game dengan mode yang dipilih"""
    if mode == 'easy':
        session['max_number'] = 10
        session['max_attempts'] = 5
    elif mode == 'medium':
        session['max_number'] = 50
        session['max_attempts'] = 7
    elif mode == 'hard':
        session['max_number'] = 100
        session['max_attempts'] = 10
    else:
        return redirect(url_for('index'))
    
    # Generate angka rahasia
    session['secret_number'] = random.randint(1, session['max_number'])
    session['attempts'] = 0
    session['guesses'] = []
    
    return render_template('game.html', mode=mode)

@app.route('/guess', methods=['POST'])
def guess():
    """Proses tebakan dari user"""
    try:
        user_guess = int(request.form['guess'])
    except (ValueError, KeyError):
        return render_template('game.html', 
                             error="Masukkan angka yang valid!",
                             guesses=session.get('guesses', []))
    
    session['attempts'] += 1
    secret = session['secret_number']
    max_attempts = session['max_attempts']
    
    # Simpan history tebakan
    if 'guesses' not in session:
        session['guesses'] = []
    
    if user_guess < secret:
        hint = "Terlalu kecil! 📉"
        session['guesses'].append({'number': user_guess, 'hint': hint})
    elif user_guess > secret:
        hint = "Terlalu besar! 📈"
        session['guesses'].append({'number': user_guess, 'hint': hint})
    else:
        # Menang!
        return render_template('result.html', 
                             won=True, 
                             attempts=session['attempts'],
                             secret=secret)
    
    # Cek apakah sudah habis kesempatan
    if session['attempts'] >= max_attempts:
        return render_template('result.html', 
                             won=False, 
                             attempts=session['attempts'],
                             secret=secret)
    
    session.modified = True
    return render_template('game.html', 
                         guesses=session['guesses'],
                         attempts=session['attempts'],
                         max_attempts=max_attempts)

@app.route('/reset')
def reset():
    """Reset game dan kembali ke halaman utama"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
