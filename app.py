from flask import Flask, jsonify
from flask_cors import CORS  # 跨域支持
import json

app = Flask(__name__)
CORS(app)  # 启用 CORS

@app.route('/api/movies', methods=['GET'])
def get_movies():
    with open("movies.json", "r", encoding="utf-8") as f:
        movies = json.load(f)
    return jsonify(movies)

if __name__ == "__main__":
    app.run(debug=True)