import json

json_filename = 'data/cad.json'

with open(json_filename, 'r') as f:
    contents = json.load(f)
    searching_for = [asteroid for asteroid in contents['data'] if asteroid[0] == '2002 PB' and  '2000-Jan-01' in asteroid[3] ]
    print(searching_for)

""" March 9th, 2021

Ran 73 tests in 3.363s

FAILED (failures=50) """