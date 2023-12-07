from flask import Flask, jsonify

app = Flask(__name__)

lentokentat = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Municipality": "London"},
    # Lisää muita lentokenttiä tarpeen mukaan
}


@app.route('/kentta/<string:icao>')
def hae_lentokentta(icao):
    lentokentta_tiedot = lentokentat.get(icao.upper())

    if lentokentta_tiedot:
        vastaus = {
            "ICAO": icao.upper(),
            "Name": lentokentta_tiedot["Name"],
            "Municipality": lentokentta_tiedot["Municipality"]
        }
    else:
        vastaus = {"error": "Lentokenttätietoja ei löytynyt."}

    return jsonify(vastaus)


if __name__ == '__main__':
    app.run(debug=True)
