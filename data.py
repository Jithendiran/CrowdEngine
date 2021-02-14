from pymongo import MongoClient


client = MongoClient("mongodb+srv://pyhackons:pyhackons@cluster0.ajjz3.mongodb.net/crowdengine?retryWrites=true&w=majority")
db = client['CrowdEngine']
doc = db['actress']
client.close()


movieslist = list(doc.find({'Actress Name': { '$exists': 'true' } },{'Actress Name':1,'_id':0})) #list(doc.find({'movie': { '$exists': 'true' } },{'movie':1,'_id':0}))

movieslist = a = [i['Actress Name'] for i in movieslist]
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
    doc = db['actress']     
   
   
    doc.insert_one({'Actress Name':kwargs['actor'],'Movie Count':kwargs['movie'],'Screen Duration':kwargs['duration'],'Instagram Followers':kwargs['insta'],'Dress match meter':kwargs['dress'],'Consistency':kwargs['consistency'],'Critic Score':kwargs['criticscore']})
