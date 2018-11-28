from sys import argv
import bottle
from bottle import *
import pymysql

@route('/')
def index():
    return template('index')

@route('/innskra')
def innskra():
    return template('innskra')

@route('/nyskra')
def nyskra():
    return template('nyskra')

@route('/doinnskra', method='POST')
def inn():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_vef2lok')
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM 1610013090_vef2lok.ritstjori WHERE user=%s AND pass=%s",(u,p))
    result = cur.fetchone()

    if result[0] == 1:
        cur.close()
        conn.close()
        return template("ritstjori",u=u)
    else:
        cur.close()
        conn.close()
        return "Rangt lykilorð eða notandanafn"

@route('/donyskra', method='POST')
def ny():
    n = request.forms.get('nafn')
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_vef2lok')
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM 1610013090_vef2lok.ritstjori WHERE user=%s",(u))
    result = cur.fetchone()
    
    if result[0] == 0:
        cur.execute("INSERT INTO 1610013090_vef2lok.ritstjori(User, Nafn, Pass) VALUES (%s,%s,%s)",(u,n,p))
        conn.commit()
        cur.close()
        conn.close()
        return u, " hefur verið skráður <br> <a href='/'>Heim</a>"
    else:
        return u, " er frátekið notandanafn <br> <a href='/nyskra'>reyndu aftur</a>"

@route('/postfrett', method='POST')
def nyfrett():
    t = request.forms.get('titill')
    f = request.forms.get('frett')
    h = request.forms.get('hof')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_vef2lok')
    cur = conn.cursor()

    cur.execute("SELECT Rit_ID FROM 1610013090_vef2lok.ritstjori WHERE User=%s",(h))
    result = cur.fetchall()

    rit_id=result[0][0]

    cur.execute("INSERT INTO 1610013090_vef2lok.frettir(Rit_ID,Titill,Texti) VALUES (%s,%s,%s)",(rit_id,t,f))
    conn.commit()
    cur.close()
    conn.close()
    return template('ritstjori',u=h)


@route('/breytafrett', method='POST')
def breytafrett():
    h = request.forms.get('hof')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_vef2lok')
    cur = conn.cursor()


    cur.execute("SELECT Rit_ID FROM 1610013090_vef2lok.ritstjori WHERE User=%s",(h))
    result = cur.fetchall()


    rit_id=result[0][0]

    cur.execute("SELECT * FROM 1610013090_vef2lok.frettir WHERE Rit_ID=%s",(rit_id))
    result = cur.fetchall()

    return template('breyta',u=h,r=result)
    
##########################################
@error(404)
def villa(error):
    return "<h2>Error 404: Not Found</h2>"

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

run(host='localhost', port=8080, reloader=True)

#bottle.run(host="0.0.0.0", port=argv[1])
