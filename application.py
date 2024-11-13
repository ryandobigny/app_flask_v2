from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/rapport', methods=['POST'])
def verification():
    nb = False
    letter_min = False
    letter_maj = False

    mdp = request.form['nomUser']
    if not mdp:
        return redirect(url_for('index'))
    nb = mdp[-1] in '0123456789' #is digit
    for chr in mdp:
        if chr.islower():
            letter_min = True
        if  chr.isupper():
            letter_maj = True
    result = nb and letter_min and letter_maj
    return render_template('rapport_erreurs.html', nb=nb, letter_maj=letter_maj, letter_min=letter_min, result=result, mdp=mdp)



if __name__ == '__main__':
    app.run(debug=True)
