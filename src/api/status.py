from flask_restx import Api, Resource, Namespace


ping_namespace = Namespace("status")


class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


ping_namespace.add_resource(Ping, "/status")
