import json

with open('./out/chart.json') as file:
    data = json.load(file)

def rank(field):
    return field['rank'].split('/')[-1]

def name(field,language='it'):
    for f in field['altLabel']:
        if f['language']==language:
            return f['value']

def begin(field):
    result = None
    try:
        result = float(field["hasBeginning"]["inMYA"])
    except:
        result = float(field["hasBeginning"]["inMYA"]["value"])
    return result

def end(field):
    result = None
    try:
        result = float(field["hasEnd"]["inMYA"])
    except:
        result = float(field["hasEnd"]["inMYA"]["value"])
    return result    

eoni = []
ere = []
periodi = []

for L1 in data['hasTopConcept']:
    print(name(L1),'\t',rank(L1),'\t',begin(L1),'->',end(L1))
    eoni.append({'name':name(L1), 'rank':rank(L1),'begin':begin(L1), 'end':end(L1)})
    for L2 in L1['narrower']:
        print('\t',name(L2),'\t',rank(L2),'\t',begin(L2),'->',end(L2))
        if 'narrower' in L2:
            for L3 in L2['narrower']:
                print('\t\t',name(L3),'\t',rank(L3),'\t',begin(L3),'->',end(L3))

    # eone
    # era
    # periodo
    # qualche epoca