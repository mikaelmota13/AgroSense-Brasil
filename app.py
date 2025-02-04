from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
@app.route("/login_user", methods=["POST", "GET"])
def login_user():
    if request.method=="POST":
        nome=request.form["nome"]
        senha=request.form["senha"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("select * from users where NOME=? and SENHA=?", (nome, senha))
        data=cur.fetchone()
        print(data)
        if data:
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
      #
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("insert into users(NOME,EMAIL,SENHA) values (?,?,?)", (nome, email, senha))
        con.commit()
        flash("Dados cadastrados", "success")
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:id>", methods=["POST","GET"])
def edit_user(id):
    if request.method=="POST":
        nome=request.form["nome"]
        email=request.form["email"]
        senha=request.form["senha"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("update users set NOME=?,EMAIL=?,SENHA=? where ID=?", (nome, email, senha, id))
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
    return render_template("dashboard_user.html")

@app.route("/add_setor", methods=["POST", "GET"])
def add_setor():
    return render_template("add_setor.html")

if __name__=='__main__':
    app.secret_key="admin123"
    app.run(debug=True)

        




    