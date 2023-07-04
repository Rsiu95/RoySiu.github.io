from flask import Flask, request, jsonify

# Create the flask Application
app = Flask(__name__)

# Create a root > end point (location on API) to obtain data from
'''
@app.route("/") # default root
def home():
    return "Home"
'''

# More complicated "Get" Route
@app.route("/get-user/<user_id>") # Path parameter > 
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    # Query parameter, when accessing a route we can parse a query paramater, an extra value that is included after the main path
    # i.e. "get-user/123?extra=hello world"

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    # Return data from a server, we query JSON (Javascript Object Notation)  > similar to a python dictionary
    return jsonify(user_data), 200 # >>> 200 standard HTTPS status code for success. More codes

@app.route("/create-user", methods=["POST"]) # possible to add extra methods, separate by comma
def create_user():
    data = request.get_json() # give all json data parsed in body of request
    
    return jsonify(data), 201

# HTTP Methods for other roots, common methods
# GET >> Request data from a specificed resource
# POST >> Create a resource/data
# PUT >> Update a resource/data
# DELETE >> Remove a resource/data

# Run the Flask Application
if __name__ == "__main__":
    app.run(debug=True)