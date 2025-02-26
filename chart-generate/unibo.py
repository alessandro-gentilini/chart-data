import json
import svgwrite
import math

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

def color(field):
    return field['color']

def compress(x):
    return x
    return 500*math.pow(x,1/4)



eoni = []
ere = []
periodi = []

for L1 in data['hasTopConcept']:
    eoni.append({'name':name(L1), 'rank':rank(L1),'begin':begin(L1), 'end':end(L1), 'color':color(L1)})
    for L2 in L1['narrower']:
        ere.append({'name':name(L2), 'rank':rank(L2),'begin':begin(L2), 'end':end(L2), 'color':color(L2)})
        if 'narrower' in L2:
            for L3 in L2['narrower']:
                periodi.append({'name':name(L3), 'rank':rank(L3),'begin':begin(L3), 'end':end(L3), 'color':color(L3)})

dwg = svgwrite.Drawing('/home/ag/prj/chart-data/chart-generate/unibo.svg', profile='tiny')

rect_width = 1000

for item in eoni:
    top = compress(item['end'])
    bottom = compress(item['begin'])
    color = item['color']
    name = item['name']
    
    rect = dwg.add(dwg.rect(insert=(0, top), size=(rect_width, bottom-top), fill=color))
    text = dwg.add(dwg.text(name, insert=(rect_width/2, (top+bottom)/2), fill='white', text_anchor='middle'))

for item in ere:
    top = compress(item['end'])
    bottom = compress(item['begin'])
    color = item['color']
    name = item['name']
    
    rect = dwg.add(dwg.rect(insert=(1000, top), size=(rect_width, bottom-top), fill=color))
    text = dwg.add(dwg.text(name, insert=(1000+rect_width/2, (top+bottom)/2), fill='white', text_anchor='middle'))

    
for item in periodi:
    top = compress(item['end'])
    bottom = compress(item['begin'])
    color = item['color']
    name = item['name']
    
    rect = dwg.add(dwg.rect(insert=(2000, top), size=(rect_width, bottom-top), fill=color))
    text = dwg.add(dwg.text(name, insert=(2000+rect_width/2, (top+bottom)/2), fill='white', text_anchor='middle'))

dwg.save()





    # eone
    # era
    # periodo
    # qualche epoca