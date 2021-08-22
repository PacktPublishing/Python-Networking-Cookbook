from flask import Flask, request

app = Flask("webhook receiver")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['alertType'] == "Air Marshal - Rogue AP detected":
        print("Rogue AP detected!")
    
    return {'success': True}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)