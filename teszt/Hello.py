import sqlite3
import streamlit as st 


def sql_letrehoz():
    conn = sqlite3.connect("vevok.db")
    c = conn.cursor()
    sql = '''
      SELECT name
      FROM sqlite_master
      WHERE type = 'table' AND name = 'vevok'
      '''
    c.execute(sql)
    if not c.fetchone():
        sql = '''
        CREATE TABLE vevok (nev text, cim text , telefon text)
        '''
        c.execute(sql)
    conn.commit()
    conn.close()

def sql_megtekint():
    conn = sqlite3.connect("vevok.db")
    c = conn.cursor()
    sql = '''
    SELECT * FROM vevok
    '''
    c.execute(sql)
    vevok = c.fetchall()
    conn.commit()
    conn.close()
    return vevok

def sql_hozzaad(nev,cim,telefon):
    conn = sqlite3.connect("vevok.db")
    c = conn.cursor()
    sql = '''
    INSERT INTO vevok VALUES(?,?,?)
    '''
    c.execute(sql,(nev,cim,telefon))
    conn.commit()
    conn.close()

sql_letrehoz()

st.title("Vevők")
malac = st.number_input('malac')
nev = st.text_input("Név")
cim = st.text_input("Cím")
telefon = st.text_input("Telefon szám")

if st.button("hozzáad"):
    sql_hozzaad(nev,cim,telefon)

if st.button("töröl"):
    ...
if st.button("aktualizál"):
    ...
if st.button("keres"):
    ...
if st.button("megjelenít"):
    
    table = sql_megtekint()
    st.header("Vevők") 
    st.write(table)

