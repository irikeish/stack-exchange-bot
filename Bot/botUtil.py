from chatbot import Chat,reflections,multiFunctionCall
import json,requests

pairs = ([

    ("(Do you know about|what is|tell me about)(.*)",
    ("{% call whoIs: %2 %}",)),

    ("(get |Show |give |display )(recently posted |new |newest |latest |recent posted |recently ask |recent )(\d*)(.*)( questions which are not answered| questions which are unanswered| questions| ques)(.*)", 
    ("{% call getQues: %3 %4 %5 %}",)),

    ("(get |Show |give |display )(\d+)( recently posted| recent posted| new| newest| latest| recently ask| recent)(.*)( questions which are not answered| questions which are unanswered| questions| ques)(.*)", 
    ("{% call getQues: %2 %4 %5 %}",)),

    

])


BASE_URL="http://api.stackexchange.com/2.2"



def getNextPage(url,tag,next):
    url=url.format(tag,next)
    try:
        res=requests.request("GET", url)
        return res
    except: return False



def getQues(query,sessionID="general"):


    print query


    num_ques=5
    tag=""
    isAnswer=True
    data=query.split()
    print data


    if data[0].isdigit():
        num_ques=int(data[0])
        tag=data[1]
        if 'not' in data or  'unanswered' in data:
            isAnswer=False
    else:
        tag=data[0]


    next=1
    print tag
    url=BASE_URL+"/questions?page={1}&order=desc&sort=activity&tagged={0}&site=stackoverflow"
    response=""
    count=0


    while count<num_ques:
        res=getNextPage(url,tag,next)
        next=next+1
        if res==False:
            break
        data=json.loads(res.text)
        for item in data["items"]:
            if count<num_ques:
                if isAnswer:
                    response=response + "<br>" + "<a href="+item["link"]+">"+item["title"]+"</a>"
                   
                elif isAnswer==item["is_answered"]:
                   response=response + "<br>" + "<a href="+item["link"]+">"+item["title"]+"</a>"
                count=count+1
            else: break;
    return response




def whoIs(query,sessionID="general"):
    print query
    url=BASE_URL+"/tags/{0}/wikis?site=stackoverflow".format(query)


    try:
        res=requests.request("GET", url)
        data=json.loads(res.text)
        reply = data["items"][0]["excerpt"]
        return reply
    except:
        return "I don't know about "+query
        
    
# call = multiFunctionCall({"whoIs":whoIs,"getQues":getQues})
# firstQuestion="Hi, I am your stackExchange bot. What can I do for you?"
# Chat(pairs, reflections,call=call).converse(firstQuestion)

