from flask import Flask , jsonify, request

api_Obj = Flask(__name__)

contact_list = [
    {
        'id' : 1,
        'Contact': "2335674321", 
        'Name' : "Alex", 
        
    },
      {
        'id' : 2,
        'Contact': "2398459321", 
        'Name' : "Alexa", 
    }
]

@api_Obj.route("/")
def helloWorld():
    return "helloo"


@api_Obj.route("/add-data" , methods = ["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please add the contact"
        })

    contact = {
        'id' : contact_list[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
    }

    contact_list.appends(contact)

    return jsonify({
        "status" : "success",
        "message" : "Contact added!!!"
    })



@api_Obj.route("/get-data")
def getTask():
    return jsonify({
        "data" : contact_list,
    })




if __name__ == '__main':
    api_Obj.run()

    
