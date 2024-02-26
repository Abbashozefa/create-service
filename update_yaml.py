from flask import Flask, request
import yaml
import os

app = Flask(__name__)

@app.route('/update_replica', methods=['POST'])
def update_replica():
    # Assuming the microservice sends the replica number in the JSON body
    data = request.get_json()
    replica_number = data.get('replica_number')

    # Get the current working directory
    current_dir = os.getcwd()

    # Path to the values.yaml file
    values_yaml_path = os.path.join(current_dir, 'ss7lbchart', 'values.yaml')

    # Read the values.yaml file
    with open(values_yaml_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Update the replica number in the YAML data
    yaml_data['replicaCount'] = replica_number

    # Write the updated YAML data back to the file
    with open(values_yaml_path, 'w') as file:
        yaml.dump(yaml_data, file)

    return 'Replica number updated successfully'

if __name__ == '__main__':
    app.run(debug=True)
