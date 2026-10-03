import json,re
m=json.load(open('m.json')); c=json.load(open('canvas/project/canvas.json'))
for f,(h,w) in m.items():
    if f=='StyleGuide.dc.html': continue
    H=int(h*1.06/20+1)*20
    c['boards'][f]['h']=H
    s=open('canvas/project/'+f).read()
    s=re.sub(r'min-height: \d+px; background: #0A0C10; display: flex',f'min-height: {H}px; background: #0A0C10; display: flex',s,1)
    s=re.sub(r'"\$preview":\{"width":(\d+),"height":\d+\}',lambda mm:f'"$preview":{{"width":{mm.group(1)},"height":{H}}}',s)
    open('canvas/project/'+f,'w').write(s)
c['boards']['StyleGuide.dc.html']['h']=1900
for k,b in c['boards'].items():
    if b.get('page')=='site' and k!='StyleGuide.dc.html': b['y']=2400
c['notes']['t1']['y']=2100
n=c['notes']
n['n3']['text']="Orange dashed chips = TODO(founder). Build hides any row, sentence or FAQ still marked TODO. No real numbers, clients, logos or faces are invented on these boards."
n['n4']['text']="Words on every board come from content/ (SEO Content, T9/T9b/T9c, D21–D31). Status labels: AI vision = Prototype · pilot partners welcome; Cleaning robot = In development; Humanoid + Arm = Built to order; Raqib = Early build."
n['n6']['text']="P4 has no spec table yet: cleaning modes hidden until the founder answers (D29). Raqib boards R1–R3 are on their own canvas page."
c['notes']['t1']['text']="Cybertronix website · Midnight Lab · one board per page (docs/PAGES.md, P1–P13)"
c['createdOnFiles']={"v":1,"at":"2026-10-03T12:00:00Z"}
json.dump(c,open('canvas/project/canvas.json','w'),ensure_ascii=False,indent=1)
print(len(c['boards']), [p['id'] for p in c['pages']])
