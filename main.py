from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import db_actions
from db import create_db


app = Flask(__name__)
api = Api(app)


class Race(Resource):
    def get(self, id=0):
        if not id:
            races = db_actions.get_races()
            return row_to_json(races)

        race = db_actions.get_race(id)
        if race:
            return row_to_json([race])

        return "Відсутна гонка"

def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument("gp")
    parser.add_argument("laps")
    params = parser.parse_args()
    id = db_actions.add_race(**params)
    answer = jsonify(f"Гонку успішно додано під id {id}")
    answer.status_code = 200
    return answer




    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("gp")
        parser.add_argument("laps")
        params = parser.parse_args()
        answer = db_actions.update_race(id, **params)
        answer = jsonify(answer)
        answer.status_code = 200
        return answer

    def delete(self, id):
        answer = jsonify(db_actions.delete_race(id))
        answer.status_code = 200
        return answer


def row_to_json(races: list):
    races_json = []

    for race in races:
        races_json.append({
            "id": race.id,
            "gp": race.gp,
            "laps": race.laps
        })

    races_json = jsonify(races_json)
    races_json.status_code = 200

    return races_json


api.add_resource(Race, "/api/races/", "/api/races/<int:id>/")


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=3000)