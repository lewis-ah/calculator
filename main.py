from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    name = "budi"
    umur = "13"
    return render_template("home.html", name=name, umur=umur)

@app.route("/hitung")
def hitung():
    angka1 = request.args.get("a1")
    angka2 = request.args.get("a2")
    operator = request.args.get("op")

    if not (angka1 and angka2 and operator):
        return "Parameter 'a1', 'a2', dan 'op' harus ada.", 400

    try:
        angka1 = int(angka1)
        angka2 = int(angka2)
    except ValueError:
        return "Parameter 'a1' dan 'a2' harus angka.", 400

    if operator == "sum":
        hasil = angka1 + angka2
    elif operator == "sub":
        hasil = angka1 - angka2
    elif operator == "mul":
        hasil = angka1 * angka2
    elif operator == "div":
        if angka2 == 0:
            return "Tidak dapat membagi dengan nol.", 400
        hasil = angka1 / angka2
    else:
        return "Operator salah. Gunakan 'sum', 'sub', 'mul', atau 'div'.", 400

    return render_template("hitung.html", a1=angka1, a2=angka2, op=operator, hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)