import json

with open('config.json') as f:
    config = json.load(f)

pins = config['pins']
params = config['parameters']