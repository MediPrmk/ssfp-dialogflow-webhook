from flask import Flask, request, jsonify

app = Flask(__name__)

def get_bplus_dosage(weight):
    try:
        weight = float(weight)
        if 4.0 <= weight <= 4.4:
            return "For 4.0–4.4 kg: 120g/day, 4 feeds/day, 4 packets/month"
        elif 4.5 <= weight <= 6.9:
            return "For 4.5–6.9 kg: 180g/day, 4 feeds/day, 5 packets/month"
        elif 7.0 <= weight <= 8.9:
            return "For 7.0–8.9 kg: 240g/day, 4 feeds/day, 7 packets/month"
        elif 9.0 <= weight <= 11.4:
            return "For 9.0–11.4 kg: 340g/day, 4 feeds/day, 9 packets/month"
        elif weight >= 11.5:
            return "For 11.5 kg and above: 360g/day, 4 feeds/day, 11 packets/month"
        else:
            return "Please enter a weight above 4.0 kg"
    except:
        return "Invalid weight. Please enter a number."

@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    weight = req.get("queryResult", {}).get("parameters", {}).get("number")
    response = get_bplus_dosage(weight)
    return jsonify({"fulfillmentText": response})

if __name__ == '__main__':
    app.run()
