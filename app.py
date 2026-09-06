from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    question = request.form.get("question", "").strip()

    if not question:
        return render_template("index.html", answer="Please enter a question.")

    answer = get_response(question)

    return render_template(
        "index.html",
        question=question,
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)