import json
json_data='''{
    "name":"Siddhant",
    "age":28
}'''
print(type(json_data))
pyhton_data=json.loads(json_data)
print(pyhton_data)