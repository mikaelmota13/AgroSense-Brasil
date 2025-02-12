from flask import Flask, session, render_template, request, redirect, url_for, flash
import sqlite3 as sql
import hashlib

app=Flask(__name__)

@app.route("/")
@app.route("/login_user", methods=["POST", "GET"])
def login_user():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        
        senha_sha512 = hashlib.sha512(senha.encode()).hexdigest()
        
        con = sql.connect("form_db.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE NOME=? AND SENHA=?", (nome, senha_sha512))
        data = cur.fetchone()
        
        if data:
            session["user_id"] = data["ID"]
            return redirect(url_for("dashboard_user"))
        else:
            flash("Email ou senha incorretos", "danger")
    
    return render_template("login_user.html")

@app.route("/index")
def index():
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users")
    data=cur.fetchall()
    return render_template ("index.html", datas=data)

@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    if request.method=="POST":
        nome=request.form["nome"]
        email=request.form["email"]
        senha=request.form["senha"]
        
        senha_sha512 = hashlib.sha512(senha.encode()).hexdigest()

        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("insert into users(NOME,EMAIL,SENHA) values (?,?,?)", (nome, email, senha_sha512))
        con.commit()
        flash("Dados cadastrados", "success")
        return redirect(url_for("login_user"))

    return render_template("add_user.html")

@app.route("/edit_user/<string:id>", methods=["POST","GET"])
def edit_user(id):
    if request.method=="POST":
        nome=request.form["nome"]
        email=request.form["email"]
        senha=request.form["senha"]
        
        senha_sha512 = hashlib.sha512(senha.encode()).hexdigest()

        
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("update users set NOME=?,EMAIL=?,SENHA=? where ID=?", (nome, email, senha_sha512, id))
        con.commit()
        flash("Dados atualizados", "success")
        return redirect(url_for("index"))
    con=sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where ID =?", (id,))
    data=cur.fetchone()
    return render_template("edit_user.html", datas=data)

@app.route("/delete_user/<string:id>", methods=["GET"])
def delete_user(id):
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("delete from users where ID=?", (id,))
    con.commit()
    flash("Dados deletados", "warning")
    return redirect(url_for("index"))

@app.route("/dashboard_user")
def dashboard_user():
    if "user_id" not in session:
        flash("Faça login primeiro", "warning")
        return redirect(url_for("login_user"))

    user_id = session["user_id"] 

    con = sql.connect("form_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM sectors WHERE PROPRIETARIO = ?", (user_id,))
    setores = cur.fetchall()

    variaveis_por_setor = {}
    for setor in setores:
        cur.execute("SELECT * FROM variaveis WHERE SETOR = ?", (setor["ID"],))
        variaveis_por_setor[setor["ID"]] = cur.fetchall()

    con.close()

    return render_template("dashboard_user.html", setores=setores, variaveis_por_setor=variaveis_por_setor, user_id=user_id)


@app.route("/add_setor/<int:id>", methods=["POST", "GET"])  
def add_setor(id):
    if request.method == "POST":
        nome = request.form["nome_setor"]
        capacidade_reservatorio = request.form["capacidade_reservatorio"]
        poco_profundidade = request.form["profundidade_poco"]

        con = sql.connect("form_db.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO sectors (NOME, PROPRIETARIO, CAPACIDADE_RESERVATORIO, POCO_PROFUNDIDADE) VALUES (?, ?, ?, ?)",
            (nome, id, capacidade_reservatorio, poco_profundidade)
        )
        con.commit()
        flash("Setor cadastrado com sucesso", "success")
        return redirect(url_for("dashboard_user"))

    return render_template("dashboard_user.html")


@app.route("/variaveis/<int:id>", methods=["GET"])
def variaveis(id):
    con = sql.connect("form_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM variaveis WHERE SETOR = ?", (id,))
    variaveis = cur.fetchall()

    return render_template("variaveis.html", variaveis=variaveis)

@app.route('/remove_setor/<int:id>', methods=['GET'])
def remove_setor(id):
    con = sql.connect('form_db.db')
    cur = con.cursor()
    cur.execute('DELETE FROM sectors WHERE ID = ?', (id,))
    con.commit()
    con.close()
    return redirect(url_for('dashboard_user'))  


if __name__=='__main__':
    app.secret_key="admin123"
    app.run(debug=True)

        




    