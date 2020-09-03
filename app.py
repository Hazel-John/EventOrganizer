#!env3/bin/python3
from flask import Flask,jsonify,abort,make_response,request

app = Flask(__name__)

eventList = [
        {
            'id':1,
            'Title':'ML Class',
            'Date and Time':'04/09/2020 9:00am',
            'url':'https://meet.google.com/prr-sfaq-mcg',
            'done':False
            },
        {
            'id':2,
            'Title':'ACA Class',
            'Date and Time':'04/09/2020 10:00am',
            'url':'https://meet.google.com/rxs-whyu-kox',
            'done':False
            },
          {
            'id':3,
            'Title':'Webinar-First Aid & Pre-Hospital Care',
            'Date and Time':'04/09/2020 7:00pm',
            'url':'https://meet.google.com/lookup/firxui1yuy',
            'done':False
            },
          {
            'id':4,
            'Title':'Ardelis Tech - Standup Meet',
            'Date and Time':'04/09/2020 9:30pm',
            'url':'https://meet.google.com/pud-wtyq-qpf',
            'done':False
            },
          {
            'id':5,
            'Title':'ML Lab Class',
            'Date and Time':'04/09/2020 2:00pm',
            'url':'https://meet.google.com/pud-wtyq-qpf',
            'done':False
              }
        ]

@app.route('/events/api/eventList', methods=['GET'])
def get_tasks():
    return jsonify({'eventList':eventList})

@app.route('/events/api/eventList/<int:event_id>', methods=['GET'])
def get_task(event_id):
    event = [event for event in eventList if event['id'] == event_id]
    if len(event) == 0:
        abort(404)
    return jsonify({'event':event[0]})

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error':'Not Found'}),404)

@app.route('/events/api/eventList' , methods=['POST'])
def create_event():
    if not request.json or not 'Title' or not 'Date and Time' or not 'url' in request.json:
        abort(400)
    event = {
            'id' : eventList[-1]['id']+1,
            'Title' : request.json['Title'],
            'Date and Time' : request.json['Date and Time'],
            'url' : request.json['url'],
            'done' : False
            }
    eventList.append(event)
    return jsonify({'event':event}), 201

@app.route('/events/api/eventList/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
     event = [event for event in eventList if event['id'] == event_id]
     if len(event) == 0:
         abort(404)
     eventList.remove(event[0])
     return jsonify ({'result':True})

@app.route('/events/api/eventList/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = [event for event in eventList if event['id'] == event_id]
    if len(event) == 0:
        abort(404)
    if not request.json:
        abort(400)
    event[0]['Title'] = request.json.get('Title', event[0]['Title'])
    event[0]['Date and Time'] = request.json.get('Date and Time', event[0]['Date and Time'])
    event[0]['url'] = request.json.get('url', event[0]['url'])
    event[0]['done'] = request.json.get('done', event[0]['done'])
    return jsonify({'event': event[0]})
if __name__ == '__main__':
    app.run(debug=True)
