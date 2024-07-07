from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            material TEXT NOT NULL,
            unidad TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            total REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    codigo = request.form['codigo']
    material = request.form['material']
    unidad = request.form['unidad']
    cantidad = int(request.form['cantidad'])
    precio = float(request.form['precio'])
    total = cantidad * precio

    conn = get_db_connection()
    conn.execute('''
        INSERT INTO items (codigo, material, unidad, cantidad, precio, total)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (codigo, material, unidad, cantidad, precio, total))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        codigo = request.form['codigo']
        material = request.form['material']
        unidad = request.form['unidad']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        total = cantidad * precio

        conn.execute('''
            UPDATE items
            SET codigo = ?, material = ?, unidad = ?, cantidad = ?, precio = ?, total = ?
            WHERE id = ?
        ''', (codigo, material, unidad, cantidad, precio, total, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete_item(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)