from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data (resets when server restarts)
voter_ids = {1,2,3,4,5,6,7,8}

votes = {
    "dem": 0,
    "rep": 0,
    "other": 0,
    "senate": 0,
    "house": 0,
    "governor": 0
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vote", methods=["POST"])
def vote():
    name = request.form["name"]
    age = int(request.form["age"])
    voter_id = int(request.form["voter_id"])

    if age < 18:
        return "You must be 18 or older to vote."

    if voter_id not in voter_ids:
        return "Invalid or already used voter ID."

    voter_ids.remove(voter_id)
    return render_template("vote.html", name=name)

@app.route("/submit_vote", methods=["POST"])
def submit_vote():
    party = request.form["party"]
    house = request.form["house"]

    # Party vote
    if party == "D":
        votes["dem"] += 1
    elif party == "R":
        votes["rep"] += 1
    elif party == "O":
        votes["other"] += 1

    # House vote
    if house == "S":
        votes["senate"] += 1
    elif house == "H":
        votes["house"] += 1
    elif house == "G":
        votes["governor"] += 1

    return redirect(url_for("results"))

@app.route("/results")
def results():
    return render_template("results.html", votes=votes, remaining=len(voter_ids))

if __name__ == "__main__":
    app.run(debug=True)