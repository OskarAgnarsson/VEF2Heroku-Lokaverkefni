from sys import argv
import bottle
from bottle import *
import pymysql

@route('/')
def index():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_vef2lok')
    cur = conn.cursor()

    cur.execute("SELECT Frett_ID,Titill,SUBSTR(Texti,1,30) FROM 1610013090_vef2lok.frettir ORDER BY Frett_ID DESC")
    result = cur.fetchall()
    return template('index',result=result)

@route('/frett<tel>')
def frett(tel):
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_vef2lok')
    cur = conn.cursor()

    cur.execute("SELECT Frett_ID,Titill,Texti FROM 1610013090_vef2lok.frettir WHERE Frett_ID=%s",(tel))
    result = cur.fetchall()
    return template('frett',result=result,id=tel)

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
        return "Rangt lykilorð eða notandanafn <a href='/'>Heim</a>"

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

@route('/nyfrett', method='POST')
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
    redirect('/')


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

@route('/breyta',method='POST')
def breyta():
    f = request.forms.get('f')
    r = request.forms.get('r')
    ti = request.forms.get('ti')
    te = request.forms.get('te')
    br = request.forms.get('breyta')

    if br == 'Breyta':
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_vef2lok')
        cur = conn.cursor()
        cur.execute("UPDATE 1610013090_vef2lok.frettir SET Rit_ID=%s WHERE Frett_ID=%s",(r,f))
        conn.commit()
        cur.execute("UPDATE 1610013090_vef2lok.frettir SET Titill=%s WHERE Frett_ID=%s",(ti,f))
        conn.commit()
        cur.execute("UPDATE 1610013090_vef2lok.frettir SET Texti=%s WHERE Frett_ID=%s",(te,f))
        conn.commit()
        cur.close()
        conn.close()
    else:
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_vef2lok')
        cur = conn.cursor()
        cur.execute("DELETE FROM 1610013090_vef2lok.frettir WHERE Frett_ID=%s",(f))
        conn.commit()
        cur.close()
        conn.close()
    redirect('/')

    
##########################################
@error(404)
def villa(error):
    return "<h2>Error 404: Not Found</h2>"

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

run(host='localhost', port=8080, reloader=True)

#bottle.run(host="0.0.0.0", port=argv[1])
