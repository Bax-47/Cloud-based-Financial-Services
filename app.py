from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Customers')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    response = table.put_item(Item=data)
    return jsonify(response)

@app.route('/get_customers', methods=['GET'])
def get_customers():
    response = table.scan()
    return jsonify(response['Items'])

if __name__ == '__main__':
    app.run(debug=True)
