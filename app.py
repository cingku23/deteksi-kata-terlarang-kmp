from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ================= KMP =================
def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return True
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False
# =======================================

with open("data_kata.txt", encoding="utf-8") as f:
    kata_terlarang = [k.strip().lower() for k in f]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cek", methods=["POST"])
def cek():
    text = request.json["text"].lower()
    ditemukan = []

    for kata in kata_terlarang:
        if kmp_search(text, kata):
            ditemukan.append(kata)

    return jsonify({
        "blocked": len(ditemukan) > 0,
        "kata": ditemukan
    })

if __name__ == "__main__":
    app.run(debug=True)
