from json import dumps
from data_proxy import get_providers_by, is_availability_exist
from helpers import safe_cast
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/appointments', methods=['GET'])
def get_appointments():

    specialty = request.args.get('specialty')
    date = safe_cast(request.args.get('date'), int, 0)
    min_score = safe_cast(request.args.get('minScore'), float, 0)

    # parameters validation
    if date < 1000000000000:
        return Response("Bad date format", 400)
    if min_score < 0 or min_score > 10:
        return Response("minScore range 0-10 (inclusive)", 400)
    if not specialty:
        return Response("Specialty was not supplied", 400)

    prov_dict = get_providers_by(min_score=min_score, date=date, specialty=specialty )
    return dumps(prov_dict)


@app.route('/appointments', methods=['POST'])
def setup_appointment():
    data = request.json

    name = data['name']
    date = data['date']

    if not is_availability_exist(name, date):
        return Response("Success", 400)

    return Response("There are not available appointments", 200)


app.run()