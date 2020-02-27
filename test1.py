import json

class manager:

  def __init__(self, name, project):
    self.name = name
    self.project = project 
 

class watcher:
  def __init__(self, name, project):
    self.name = name
    self.project = project




managers={}
watchers={}
listMana=[]
listWat=[]
def takePriority(pri):
   return(pri['priority'])

with open('source_file_2.json') as f1:
  data=f1.read()
  obj = json.loads(data)
  obj.sort(key=takePriority)

  for j in range(0,len(obj)):
     for i in obj[j]['managers']:
       listMana.append(manager(i,obj[j]['name']))
       
         
  for j in range(0,len(obj)):
     for i in obj[j]['watchers']:
       listWat.append(manager(i,obj[j]['name']))


  for i in listMana:
      managers[str(i.name)]=[]

  for i in listWat:
      watchers[str(i.name)]=[]

  for i in listMana:
      managers[str(i.name)].append(str(i.project)) 

  for i in listWat:
      watchers[str(i.name)].append(str(i.project))


  with open('managers.json', 'w') as json_file:
    json.dump(managers, json_file)

  with open('watchers.json', 'w') as json_file:
    json.dump(watchers, json_file)
  



   
   
  
  
  
