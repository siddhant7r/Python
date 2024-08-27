import json
python_data={
    'name':'Siddhant',
    'quali':"Btech"
}

json_data=json.dumps(python_data)

print(json_data)
print(type(json_data))


python_data=json.loads(json_data)
print(python_data)
print(type(python_data))