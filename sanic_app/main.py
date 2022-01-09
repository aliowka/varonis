
from sanic_jwt.decorators import protected
from app import app

@protected
@app.route("/normalize", methods=["POST",])
async def normalize(request):
    
    data = request.json.get("data")
    one_line_normalizer = lambda data: {d['name']: list(filter(lambda k: 'Val' in k, d))[0] for d in data}
    return one_line_normalizer(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
