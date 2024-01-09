import sqlite3
import streamlit as st

def create_database():
    
    conn = sqlite3.connect('asdasd.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='asdasd'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE customers
                     (name text, address text, phone text)''')
        conn.commit()
    conn.close()

def add_customer(name, address, phone):
    conn = sqlite3.connect('asdasd.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (name, address, phone))
    conn.commit()
    conn.close()

def delete_customer(name):
    conn = sqlite3.connect('asdasd.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE name=?", (name,))
    conn.commit()
    conn.close()

def update_customer(name, address, phone):
    conn = sqlite3.connect('asdasd.db')
    c = conn.cursor()
    c.execute("UPDATE customers SET address = ?, phone = ? WHERE name = ?", (address, phone, name))
    conn.commit()
    conn.close()

def view_customers():
    conn = sqlite3.connect('asdasd.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    customers = c.fetchall()
    conn.close()
    return customers

def search_customer(name, phone):
    conn = sqlite3.connect('asdasd.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE name=? OR phone=?", (name, phone))
    customers = c.fetchall()
    conn.close()
    return customers


def main():
    st.title("Vevők adatbázis")
    
    
    create_database()

    name = st.text_input("Név")
    address = st.text_input("Cím")
    phone = st.text_input("Telefonszám")
    st.sidebar.header("Válassz műveletet!")
    if st.sidebar.button("Hozzáad"):
        add_customer(name, address, phone)

    if st.sidebar.button("Töröl"):
        delete_customer(name)

    if st.sidebar.button("Aktualizál"):
        update_customer(name, address, phone)


    if st.sidebar.button("Keres"):
        customers = search_customer(name, phone)
        st.header("Customers File")
        st.table(customers)   

    if st.sidebar.button("Megtekint"):
        customers = view_customers()
        st.header("Customers File")
        st.table(customers)

if __name__ == '__main__':
    main()
