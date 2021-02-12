from pymongo import MongoClient


client = MongoClient("mongodb+srv://pyhackons:pyhackons@cluster0.ajjz3.mongodb.net/crowdengine?retryWrites=true&w=majority")
db = client['CrowdEngine']
doc = db['movies']
client.close()


movieslist = list(doc.find({'Movies': { '$exists': 'true' } },{'Movies':1,'_id':0})) #list(doc.find({'movie': { '$exists': 'true' } },{'movie':1,'_id':0}))

movieslist = a = [i['Movies'] for i in movieslist]
size = len(movieslist)


def page(pg , index):
    
    if pg == 'next':
        if size-1 > index:
            return movieslist[index+1]
        elif size-1 == index:
            return movieslist[0]
    elif pg == 'pre':
        if index == 0 :
            return movieslist[size-1]
        else:
            return movieslist[index-1]

def write(**kwargs):
    client = MongoClient("mongodb+srv://pyhackons:pyhackons@cluster0.ajjz3.mongodb.net/crowdengine?retryWrites=true&w=majority")
    db = client['CrowdEngine']
    doc = db['movies']     
    doc.update({'Movies':kwargs['movie']},{ '$set':{'actor':kwargs['actor'],'duration':kwargs['duration'],'role':kwargs['role'],'dresscolor':kwargs['dresscolor'],'target':kwargs['target']} })