import requests 

import json
def sex_karwado(age,sex,evidence):
    url ="https://api.infermedica.com/v2/diagnosis"

    payload={'age':age,'sex':sex,'evidence':evidence}
    # payload={'age': 18, 'sex': 'male', 'evidence': [{'id': 's_21', 'choice_id': 'present', 'initial': True}, {'id': 's_102', 'choice_id': 'present', 'initial': True}], 'extras': {'enable_adaptive_ranking': True, 'disable_groups': True}}
    header={'App-Id':'33e7b86d','App-Key':'1c80f2d4577c86270a5c69f560068804','Content-Type':'application/json'}
    r=requests.post(url,data=json.dumps(payload),headers=header)
    

    data=r.json()
    print(data)

evidence= [{'id': 's_21', 'choice_id': 'present', 'initial': True}, {'id': 's_102', 'choice_id': 'present', 'initial': True}, {'id': 's_1193', 'choice_id': 'absent', 'initial': False}]

sex_karwado(18,"male",evidence)
