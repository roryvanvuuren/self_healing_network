from flask import Flask, render_template, jsonify
from scripts.check_ping import check_ping
from scripts.check_dns import check_dns

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('nethome.html')

@app.route('/get_ping_results', methods=['GET'])
def get_ping_results():
    ping_results = check_ping()
    return jsonify({'ping_results': ping_results})  # Return results in a dictionary format

@app.route('/check_dns')
def check_dns_route():
    dns_results = check_dns()
    return {'dns_results': dns_results}

if __name__ == '__main__':
    app.run(debug=True)
