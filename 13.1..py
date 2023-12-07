from flask import Flask, request
import math

app = Flask(__name__)
@app.route('/summa')

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:number>')
def check_prime(number):
    is_prime_number = is_prime(number)
    response = {
        "Number": number,
        "isPrime": is_prime_number
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
