from flask import Blueprint, jsonify, request, Response
import time

r = Blueprint("api", __name__)

# /// Routes ///


#//////////////////////////////////////////////////////////////////
#test methods 

@r.route("/")
def index():
    return jsonify({"Lexiden": "Root"})

#http post to regurgitate what you type to this endpoint
@r.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({"you_sent": data})

# Health check
@r.route("/health")
def health():
    return jsonify({"status": "operational"})

#SSE streams were an alien concept for me personally so I created this small
#timer stream to get the hang of it
@r.route('/utcstream')
def stream():
    def event_stream():
        #entrance points
        t1 = time.time()
        while True:
            yield f"{int(time.time()-t1)} seconds elapsed since access.\n\n"
            time.sleep(1)
    return Response(event_stream(), mimetype="text/event-stream")

@r.route('/chatstreamtest',methods = ["GET","POST"])
def chatstream():
    if request.method == 'GET':
        # handle GET request
        return "Fetching chat stream..."
    elif request.method == 'POST':
        # handle POST request
        return "Sending chat message..."

#end of test methods
#/////////////////////////////////////////////////////////////////////


#entry point for AI chatbot interaction.
#GET = retrieve msg | POST = send msg
@r.route('/chatstream',methods = ["GET","POST"])
def chatstream():
    if request.method == 'GET':
        # handle GET request
        return "Fetching chat stream..."
    elif request.method == 'POST':
        # handle POST request
        return "Sending chat message..."