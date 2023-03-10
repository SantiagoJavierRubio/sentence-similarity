import os
from flask import Flask, request, jsonify, abort
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)

model = SentenceTransformer('sentence-transformers/paraphrase-albert-small-v2')

@app.route("/")
def index():
    return "Welcome to the sentence similarity API. Post to /check-similarity"
@app.route('/check-similarity', methods=["POST"])
def main():
    inputs = request.get_json(True)
    if "authorization_token" not in inputs or inputs['authorization_token'] != os.environ.get("AUTH_TOKEN"): 
        abort(401)
    embeddingOriginal = model.encode(inputs['original'])
    embeddingCompare = model.encode(inputs['answer'])
    cosine_score = util.cos_sim(embeddingOriginal, embeddingCompare)
    response = dict(score=cosine_score.item())
    return jsonify(response)

def create_app():
    return app