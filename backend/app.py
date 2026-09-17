import os
import re

from flask import Flask, jsonify, request

app = Flask(__name__)
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/process")
def process_submission():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    message = str(data.get("message", "")).strip()

    if not name or not email or not message:
        return jsonify(error="Name, email, and response are required."), 400
    if not EMAIL_PATTERN.fullmatch(email):
        return jsonify(error="Please provide a valid email address."), 400

    return jsonify(
        message=f"Thanks, {name}. Your response was processed successfully.",
        submission={"name": name, "email": email, "message": message},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))