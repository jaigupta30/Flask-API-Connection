from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='templates')

# Route to display the table
@app.route('/')
def display_table():
    # Connect to the database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Execute a query to fetch data from the table
    cursor.execute("SELECT Title, Runtime, Year, Genre, Overview FROM movies")

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Render the template and pass the data to it
    return render_template('table.html', rows=rows)

if __name__ == '__main__':
    app.run()
