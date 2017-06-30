import json
f = open('x.txt', 'r')
js=f.read()
obj=json.loads(js)
sessions=[]
for o in obj:
	dictionary={}

	dictionary['id']=o['id']
	dictionary['title']=o['title']
	dictionary['speakers']=o['speakers']
	dictionary['subtitle']=o['subtitle']
	dictionary['short_abstract']=""
	dictionary['session_type']={}
	start=o['details'].split("\u")[0]
	dictionary['start_time']=start.split("day")[1]
	end=o['details'].split("\u2013")[0]
	dictionary['end_time']=end.split("in")[0]
	dictionary['track']=o['track']
	dictionary['comments']= ""
	dictionary['language']="English"
	dictionary['slides']=""
	dictionary['audio']=""
	dictionary['video']=""
	dictionary["level"]=""
	dictionary["signup_url"]=""
	dictionary['state']="accepted"
	dictionary['microlocation']={}
	dictionary['microlocation']['id']=""
	dictionary['microlocation']['name']=o['details'].split("in")[1]
	sessions.append(dictionary)
sessions_json=json.dumps(sessions)
print sessions_json