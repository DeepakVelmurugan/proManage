from flask import Flask,jsonify,request
from CRUD import CRUD
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    connectObj = CRUD.CRUD()
    if connectObj.connect()['message'] == 'Success':
        return '<b><i> Database connection successfull </i></b>'
    return jsonify({'error':'Unable to connect to database'}), 500

@app.route('/insert',methods=['POST'])
def insert_entry():
    reqData = request.get_json(force=True)
    #check story id
    if 'story_id' not in reqData.keys():
        return jsonify({'error':'Story is not provided'}), 500
    insertObj = CRUD.CRUD()
    if insertObj.insert_story(reqData)['message'] == 'Success':
        return '<b>Inserted successfully</b>'
    return jsonify({'error':'Insertion failed'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)