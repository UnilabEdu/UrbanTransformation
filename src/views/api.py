from flask_restx import Namespace, Resource
from src.models.member import Member
from src.models.activity import Activity

ns_members = Namespace("members", path="/api/members")
ns_activities = Namespace("activities", path="/api/activities")

@ns_members.route("/")
class MemberList(Resource):
    def get(self):
        members = Member.query.all()
        return [
            {
                "id": m.id,
                "name": m.name,
                "surname": m.surname,
                "contribution": m.contribution,
                "image": m.image,
                "email": m.email
            } for m in members
        ]

@ns_members.route("/<int:id>")
class MemberDetail(Resource):
    def get(self, id):
        m = Member.query.get_or_404(id)
        return {
            "id": m.id,
            "name": m.name,
            "surname": m.surname,
            "contribution": m.contribution,
            "image": m.image,
            "email": m.email
        }

@ns_activities.route("/")
class ActivityList(Resource):
    def get(self):
        activities = Activity.query.all()
        return [
            {
                "id": a.id,
                "title": a.title,
                "description": a.description,
                "DateTime": a.DateTime,
                "Time": a.Time
            } for a in activities
        ]

@ns_activities.route("/<int:id>")
class ActivityDetail(Resource):
    def get(self, id):
        a = Activity.query.get_or_404(id)
        return {
            "id": a.id,
            "title": a.title,
            "description": a.description,
            "DateTime": a.DateTime,
            "Time": a.Time
        }