from flask import Flask, request
import json
from SudokuSolver import Solver

obj = Solver.SudokuSolver()

app = Flask(__name__)


@app.route('/sudoku', methods=['POST', 'GET'])
def home_page():
    if request.method == 'GET':
        return '<h1>Do a Post request with your sudoku board in 2D Array.</h1><br><h2>Like this:- [[0,0,0],[7,8,0],[0,0,0]]</h2>'
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        grid = json.loads(data)
    return str(obj.solve(grid))


if __name__ == '__main__':
    app.run()

# Post Request Format:
# http://127.0.0.1:5000/sudoku with this array as parameter [[3, 0, 6, 5, 0, 8, 4, 0, 0],[5, 2, 0, 0, 0, 0, 0, 0, 0],[0, 8, 7, 0, 0, 0, 0, 3, 1],[0, 0, 3, 0, 1, 0, 0, 8, 0],[9, 0, 0, 8, 6, 3, 0, 0, 5],[0, 5, 0, 0, 9, 0, 6, 0, 0],[1, 3, 0, 0, 0, 0, 2, 5, 0],[0, 0, 0, 0, 0, 0, 0, 7, 4],[0, 0, 5, 2, 0, 6, 3, 0, 0]]
