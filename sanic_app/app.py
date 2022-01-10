import json
from sanic import Sanic, response
from sanic_jwt import Initialize, exceptions
from sanic_jwt.decorators import protected

from sanic_app.users import users


async def authenticate(request):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user_password = users.get(username, None)
    if user_password is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user_password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return dict(username=username, password=password)


app = Sanic(name="varonis_hw")
Initialize(app, authenticate=authenticate)

@protected
@app.route("/normalize", methods=["POST",])
async def normalize(request):
    
    data = json.loads(request.body)
    one_line_normalizer = lambda data: {d['name']: d[list(filter(lambda k: 'Val' in k, d))[0]] for d in data}
    return response.json(one_line_normalizer(data))
