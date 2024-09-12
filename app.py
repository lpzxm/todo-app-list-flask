from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para conectarse a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row  # Esto permite que los datos se devuelvan en un formato de diccionario
    return conn

# Ruta para mostrar las tareas
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Ruta para agregar una nueva tarea
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        task = request.form['task']
        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add.html')

# Ruta para eliminar una tarea
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
