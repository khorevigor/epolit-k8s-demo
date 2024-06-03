from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/inner_odd_checker", methods=["GET"])
def inner_odd_checker():
    if request.is_json:
        data = request.json
        print(f'Inner odd_checker received data from request: {data}')
        return jsonify({"message": f'Inner odd_checker received data from request: {data}'})
    else:
        print('Inner odd_checker got no data')
        return jsonify({"message": "Inner odd_checker got no data"})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7788, debug=True)
