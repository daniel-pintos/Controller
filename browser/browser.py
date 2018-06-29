from flask import Flask, jsonify, current_app, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"


@app.route('/')
def index():
    if 'username' in session:
        return render_template("index.html"), 200
    return redirect(url_for('login'))


# O escape() precisa ser usado apenas se você não estiver usando um template.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html'), 200


@app.route("/show_config/")
def list():
    querystring_args = request.args.to_dict()
    post_args = request.form.to_dict()
    return jsonify(
        debug=current_app.config.get('DEBUG'),
        args=querystring_args,
        vars=post_args
    )


@app.route('/logout')
def logout():
    session.pop('username', None)  # Apaga os dados de login lá da session
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
