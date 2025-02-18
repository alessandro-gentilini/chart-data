import json

# Open the JSON file
with open('./out/chart.json') as file:
    # Load the JSON data
    data = json.load(file)

# Print the contents of the JSON file
#print(data)

def get_rank(field):
    return field['rank'].split('/')[-1]

def get_name(field,language='it'):
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

# Print all the topconcept fields
for L1 in data['hasTopConcept']:
    print(get_name(L1),'\t',get_rank(L1),'\t',begin(L1),'->',end(L1))
    for L2 in L1['narrower']:
        print('\t',get_name(L2),'\t',get_rank(L2),'\t',begin(L2),'->',end(L2))
        if 'narrower' in L2:
            for L3 in L2['narrower']:
                print('\t\t',get_name(L3),'\t',get_rank(L3),'\t',begin(L3),'->',end(L3))

    # eone
    # era
    # periodo
    # qualche epoca