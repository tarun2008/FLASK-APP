from flask import Flask,request,jsonify
app = Flask(__name__)
data =[{
    'id': 1,
     'name' : 'Raju',
    'contact':'9987644456',   
    'done':False
},{
    'id': 2,
    'name' : 'Navya',
    'contact':'9503600920',    
    'done':False
}]
@app.route('/adddata',methods = ["POST"])
def adddata ():
    if not request.json:
        return jsonify({
            'status':'Error',
            'message':'Please provide the data'
        })
    contact ={
        'id':data[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',''),
        'done':False
    }   
    data.append(contact) 
    return jsonify({
        'status':'Success',
        'message':'Task added succesfully'
    })
if __name__ == '__main__':
    app.run()