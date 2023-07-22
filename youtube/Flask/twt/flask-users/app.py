import sqlite3

from flask import Flask, request, jsonify, render_template

# import os
import os
# print("Current Working Directory:", os.getcwd())
db_path = os.path.join(os.getcwd(), "customers.db")
print(db_path)


# connect to db
# conn = sqlite3.connect('customer.db')
conn = sqlite3.connect(db_path)

# create a cursor
# c = conn.cursor()

# create a table
# c.execute("""CREATE TABLE customers(
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             email TEXT NOT NULL
#             )
#             """)

# insert into db
# c.execute("""INSERT INTO customers VALUES('mihai', 'popescu', 'mihai@mihi.com')""")

# insert many customers
# many_customers = [
#     ('gicu', 'unu', 'g@dsa.com'),
#     ('gogu', 'doi', 'doi@email.com'),
#     ('fane', 'trei', 'trei@email.com'),
# ]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# query & fetch
# c.execute('SELECT rowid, * FROM customers')
# c.fetchone()
# c.fetchmany(3)
# # print(c.fetchall())
# items = c.fetchall()
# print(items)
# for item in items:
#     print(item)

# c.execute("SELECT * FROM customers WHERE email = 'trei@email.com'")
# items = c.fetchall()
# print(items)


# commit our command
# conn.commit()

# close connection
# conn.close()

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
# basedir = os.path.abspath(os.path.dirname(__file__))
# Initialize the db
# db = SQLAlchemy(app)


users = []


@app.route('/')
def home():
    # return 'Home'
    # con = sqlite3.connect("customer
    # s.db")
    # con.row_factory = sqlite3.Row
    #
    # cur = con.cursor()
    # cur.execute("SELECT rowid, * FROM customers")
    #
    # rows = cur.fetchall()
    # con.close()
    #
    # print(rows)
    # # title = 'blog'
    # return render_template('index.html', rows=rows)

    try:
        # con = sqlite3.connect(db_path)
        con = sqlite3.connect("customer.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM customers")

        rows = cur.fetchall()
        con.close()

        return render_template('index.html', rows=rows)
    except Exception as e:
        # Print the error for debugging purposes (optional)
        print("An error occurred:", str(e))
        # Return an error message or redirect to an error page if necessary
        return "An error occurred. Please try again later."


@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "some@email.com"
    }
    """querry params
    http://127.0.0.1:5000/get-user/1?extra="hellow"
    """
    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200
    # http://127.0.0.1:5000/get-user/1


@app.route('/create-user', methods=["POST"])
def create_user():
    data = request.get_json()
    print(data)
    users.append(data)
    print(users)
    return jsonify(data), 201


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
