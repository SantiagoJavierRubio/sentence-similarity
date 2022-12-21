import os
from flask import Flask, request, jsonify, abort
from sentence_transformers import util
import pickle

app = Flask(__name__)

# model = SentenceTransformer('bert-base-nli-mean-tokens')
# pickle.dump(model, open('model.sav', 'wb'))

model = pickle.load(open('model.sav', 'rb'))

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