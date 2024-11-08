from flask import Flask, jsonify, request

app = Flask(__name__)

heart_records = [
    {
        "heart_id" : "",
        "date" : "",
        "heart_rate" : ""
    }
]

# Create a REST API using FLASK insert a new heart record to a JSON file. The heart rate information is composed of heart_id, date and heart_rate.  (3 points)

@app.route('/heart_records', methods = ['POST'])
def new_record():
    record = request.get_json()
    heart_records.append(record)
    
    return ("Successful"), 200
    #Vhan Randolp S. Pena

# 2. Create a REST API using FLASK to read a heart information from a JSON file. The heart rate information is composed of heart_id, date and heart_rate. (3 points)
@app.route('/heart_records', methods = ["GET"])
def getRecords():
    return jsonify(heart_records)

# 3. Create a REST API using FLASK to read a heart information of a specific heart_id from a JSON file. The heart rate information is composed of heart_id, date and heart_rate. (3 points)
@app.route('/heart_records/<int:id>', methods = ["GET"])
def getSpecificRecord(id):
    return jsonify(heart_records[id])

# 4. Create a REST API using FLASK to update a heart record of a specific heart_id. The heart rate information is composed of heart_id, date and heart_rate.  (3 points)
@app.route('/heart_records/<int:id>', methods = ["PUT"])
def updateRecord(id):
    heart_record = request.get_json()
    heart_records[id] = heart_record

    return jsonify(heart_records[id]), 200

# 5. Create a REST API using FLASK to delete a heart record of a specific heart_id. The heart rate information is composed of heart_id, date and heart_rate.  (3 points).
@app.route('/heart_records/<int:id>', methods = ["DELETE"])
def deleteRecord(id):
    heart_records.pop(id)

    return jsonify(heart_records), 200

if __name__ == '__main__':
    app.run()




