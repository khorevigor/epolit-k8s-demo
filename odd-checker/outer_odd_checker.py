from flask import Flask, request, jsonify
import os

app = Flask(__name__)
inner_odd_checker_path = f'{os.environ["INNER_ODD_CHECKER_URL"]}:{os.environ["INNER_ODD_CHECKER_PORT"]}/{os.environ["INNER_ODD_CHECKER_ENDPOINT"]}'


@app.route("/outer_odd_checker", methods=["GET"])
def is_odd():
    if request.is_json:
        data = request.json
        return jsonify({"message": f'Got data from request: {data}'})
    else:
        return jsonify({"message": "no data is present"})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8899, debug=True)
