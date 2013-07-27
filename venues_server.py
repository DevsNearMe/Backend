#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request


# REST boilerplate set up with prototype venue type but needs to be changed based on
# data available. APIs first, database later. Hook REST api to android google maps api
# Use google places data side by side as well to 
# onClickMarker display which sources by weight accounted for the prediction e.g meetup
# was weighed more for a location, or twitter was weighed in more for a location
# the other thing to do is to hook a InfoWindowAdapter to it, grab photos from somewhere
# adding predictions for gender, age distribution estimates etc.

# Pull in some test data to implement. Explain that in reality celery background venues 
# will populate a database

app = Flask(__name__)

# Change to venues, which have autoincremented id, lat, lon, (/devsnearme/api/v0.1/venues?latitude=43.23432&longitude=-73.234234&radius)
# min_turnout, expected_turnout, max_turnout

results = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

venues = [
  {
     "geometry" : {
        "location" : {
           "lat" : 37.79593620000001,
           "lng" : -122.40000320
        }
     },
     "id" : 1,
     "name" : "Alley NYC",
     "types" : [ "iOS", "design" ],
 	 "min_attendance" : 17,
     "expected_attendance" : 41,
     "max_attendance" : 67,
     "factors" : {
    	"foursquare" : 0.45,
        "twitter" : 0.23,
        "meetup" : 0.15,
        "eventbrite" : 0.17
    }
  },
  {
     "geometry" : {
        "location" : {
           "lat" : 37.79593620000001,
           "lng" : -122.40000320
        }
     },
     "id" : 2,
     "name" : "Huge",
     "types" : [ "iOS", "Ruby" ],
 	 "min_attendance" : 32,
     "expected_attendance" : 41,
     "max_attendance" : 67,
     "factors" : {
      	"foursquare" : 0.45,
        "twitter" : 0.23,
        "meetup" : 0.15,
        "eventbrite" : 0.17
    }
  },
  {
     "geometry" : {
        "location" : {
           "lat" : 37.79593620000001,
           "lng" : -122.40000320
        }
     },
     "id" : 3,
     "name" : "Knewton",
     "types" : [ "Big data", "Python" ],
 	 "min_attendance" : 32,
     "expected_attendance" : 41,
     "max_attendance" : 67,
     "factors" : {
      	"foursquare" : 0.45,
        "twitter" : 0.23,
        "meetup" : 0.15,
        "eventbrite" : 0.17
    }
  }
]

#TODO Implement lat,lon, radius based fetch
# Allow query via names
@app.route('/devsnearme/api/v0.1/venues', methods = ['GET'])
def get_venues():
	if request.method == 'GET':
		type = request.args.get('type', '')
		name = request.args.get('name', '')	
		if (type == ''):
			return jsonify( { 'venues': venues } )
		else :
			venues_result = []
			for ven in venues:
				if type.lower() in (v.lower() for v in ven['types']):
					venues_result.append(ven)
			return jsonify( { 'venues': venues_result } )


@app.route('/devsnearme/api/v0.1/venues/<int:venue_id>', methods = ['GET'])
def get_venue(venue_id):
    venue = filter(lambda v: v['id'] == venue_id, venues)
    if len(venue) == 0:
        abort(404)
    return jsonify( { 'venue': venue[0] } )

@app.route('/devsnearme/api/v0.1/venues/<int:venue_id>', methods = ['GET'])
def get_venue(venue_id):
    venue = filter(lambda v: v['id'] == venue_id, venues)
    if len(venue) == 0:
        abort(404)
    return jsonify( { 'venue': venue[0] } )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

'''
@app.route('/devsnearme/api/v0.1/venues', methods = ['POST'])
def create_venue():
    if not request.json or not 'title' in request.json:
        abort(400)
    venue = {
        'id': venues[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    venues.append(venue)
    return jsonify( { 'venue': venue } ), 201
'''

@app.route('/devsnearme/api/v0.1/venues/<int:venue_id>', methods = ['DELETE'])
def delete_venue(venue_id):
    venue = filter(lambda t: t['id'] == venue_id, venues)
    if len(venue) == 0:
        abort(404)
    venues.remove(venue[0])
    return jsonify( { 'result': True } )
'''
@app.route('/devsnearme/api/v0.1/venues/<int:venue_id>', methods = ['PUT'])
def update_venue(venue_id):
    venue = filter(lambda t: t['id'] == venue_id, venues)
    if len(venue) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    venue[0]['title'] = request.json.get('title', venue[0]['title'])
    venue[0]['description'] = request.json.get('description', venue[0]['description'])
    venue[0]['done'] = request.json.get('done', venue[0]['done'])
    return jsonify( { 'venue': venue[0] } )
'''
if __name__ == '__main__':
    app.run(debug = True)