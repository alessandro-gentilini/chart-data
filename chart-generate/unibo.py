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

def broader(field):
    result = None
    try:
        result = field["broader"][0]
    except:
        result = None
    return result

def color(field):
    return field['color']



def compress(x):
    return math.log10(x)

def timespan(x):
    return compress(begin(x)-end(x))



eoni = []
ere = []
periodi = []

for L1 in data['hasTopConcept']:
    eoni.append({'name':name(L1), 'rank':rank(L1),'begin':begin(L1), 'end':end(L1), 'color':color(L1), 'timespan':timespan(L1), 'broader':broader(L1)})
    for L2 in L1['narrower']:
        ere.append({'name':name(L2), 'rank':rank(L2),'begin':begin(L2), 'end':end(L2), 'color':color(L2), 'timespan':timespan(L2), 'broader':broader(L2)})
        if 'narrower' in L2:
            for L3 in L2['narrower']:
                periodi.append({'name':name(L3), 'rank':rank(L3),'begin':begin(L3), 'end':end(L3), 'color':color(L3), 'timespan':timespan(L3), 'broader':broader(L3)})

dwg = svgwrite.Drawing('/home/ag/prj/chart-data/chart-generate/unibo.svg', profile='tiny')




eoni.sort(key=lambda x: x['end'])
ere.sort(key=lambda x: x['end'])
periodi.sort(key=lambda x: x['end'])

dwg2 = svgwrite.Drawing('/home/ag/prj/chart-data/chart-generate/unibo2.svg', profile='tiny')
rect_width = 1000

level = 0
top = 0
for item in eoni:
    color = item['color']
    name = item['name']
    H = 100*item['timespan']
    
    rect = dwg2.add(dwg.rect(insert=(level*rect_width, top), size=(rect_width, H), fill=color))
    text = dwg2.add(dwg.text(name, insert=(level*rect_width+rect_width/2, top+H/2), fill='black', text_anchor='middle', font_size=36))
    top = top+H

level = level+1
top = 0
for item in ere:
    color = item['color']
    name = item['name']
    H = 100*item['timespan']
    
    rect = dwg2.add(dwg.rect(insert=(level*rect_width, top), size=(rect_width, H), fill=color))
    text = dwg2.add(dwg.text(name, insert=(level*rect_width+rect_width/2, top+H/2), fill='black', text_anchor='middle', font_size=36))
    top = top+H

level = level+1
top = 0
for item in periodi:
    color = item['color']
    name = item['name']
    H = 100*item['timespan']
    
    rect = dwg2.add(dwg.rect(insert=(level*rect_width, top), size=(rect_width, H), fill=color))
    text = dwg2.add(dwg.text(name, insert=(level*rect_width+rect_width/2, top+H/2), fill='black', text_anchor='middle', font_size=36))
    top = top+H

dwg2.save()    







level = 0

for item in eoni:
    top = item['end']
    bottom = item['begin']
    color = item['color']
    name = item['name']
    
    rect = dwg.add(dwg.rect(insert=(level*rect_width, top), size=(rect_width, bottom-top), fill=color))
    text = dwg.add(dwg.text(name, insert=(level*rect_width+rect_width/2, (top+bottom)/2), fill='black', text_anchor='middle'))

level = level+1

for item in ere:
    top = item['end']
    bottom = item['begin']
    color = item['color']
    name = item['name']
    
    rect = dwg.add(dwg.rect(insert=(level*rect_width, top), size=(rect_width, bottom-top), fill=color))
    text = dwg.add(dwg.text(name, insert=(level*rect_width+rect_width/2, (top+bottom)/2), fill='black', text_anchor='middle'))

level = level+1

for item in periodi:
    top = item['end']
    bottom = item['begin']
    color = item['color']
    name = item['name']
    
    rect = dwg.add(dwg.rect(insert=(level*rect_width, top), size=(rect_width, bottom-top), fill=color))
    text = dwg.add(dwg.text(name, insert=(level*rect_width+rect_width/2, (top+bottom)/2), fill='black', text_anchor='middle'))

dwg.save()

print("")

for item in eoni:
    print(item)

print("")

for item in ere:
    print(item)

print("")

for item in periodi:
    print(item)    








    # eone
    # era
    # periodo
    # qualche epoca