from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/Time', methods=['POST'])
def receive_json_data():
    try:
        data = request.get_json()

        dateTime = data.get('message_datetime', None)

        if dateTime:
            datetime_obj = datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
            time = datetime_obj.time()
            result = {'Time_Stamp': str(time)}

            return jsonify(result)
        else:
            error_message = {'error': 'Error'}
            return jsonify(error_message)

    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message)

if __name__ == '__main__':
    app.run(port=3000)
