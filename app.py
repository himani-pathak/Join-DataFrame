from flask import Flask, jsonify, request
import pandas as pd
from joiner import Joiner
import json
app = Flask(__name__)
def validate_json(json_data):
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError as e:
        return False, "Invalid JSON format"

    if not isinstance(data, dict):
        return False, "Invalid JSON. Expected a JSON object."
    # validations Checks
    if 'joinType' not in data:
        return False, "Missing 'joinType' key in the JSON."
    elif data['joinType'] not in ['leftJoin', 'innerJoin', 'fullOuterJoin', 'rightJoin']:
        return False, "Invalid value for 'joinType'. Possible values are: leftJoin, innerJoin, fullOuterJoin, rightJoin."
    elif 'joiningKeys' not in data:
        return False, "Missing 'joiningKeys' key in the JSON."
    elif not isinstance('joiningKeys', list) or len('joiningKeys') == 0:
        return False
    elif len('df1') != len('result'):
        return False,"Join Operation is not Properly Done"
    elif len(set('df1.columns').intersection('df2.columns')) == 0:
        return False,"No common key found to join the tables."

    return True, "Valid JSON"

@app.route('/joinDataframes', methods=['POST'])
def join_dataframes():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Convert the JSON data to dataframes
        df1 = pd.DataFrame(data['df1'])
        df2 = pd.DataFrame(data['df2'])
        join_type = data['joinType']
        
        joining_keys = data['joiningKeys']
        # Create an instance of the Joiner class
        joiner = Joiner(df1, df2,join_type,joining_keys)
        # Perform the left join operation using the join_dataframes method
        result = joiner.join_dataframes()
        
        
        # Convert the resulting dataframe to JSON
        result_json = result.to_json(orient='records')
        return result_json

    except Exception as e:
        return ({'error': str(e)})
    


if __name__ == '__main__':
    app.run(debug = True)






