from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import pandas as pd
#append path of this file to sys.path
import os
import uvicorn
import uuid


items = {}

app = FastAPI()
#get parent file path of this file
parent_path = os.path.dirname(os.path.abspath(__file__))
print(parent_path)
templates = Jinja2Templates(directory=parent_path + "/templates")


@app.on_event("startup")
async def startup_event():
    # #create empty messages and labeled_messages
    items['messages'] = []
    items['labeled_messages'] = []
    items['training_id'] = str(uuid.uuid4())
    items['tags_list'] = []
    items['labels'] = []
    items['classes'] = []





@app.get("/")
def default(request: Request):
    msg_length = len(items['messages'])
    #check if length is even or odd
    if len(items['classes']) == 0:
        classes = [True]*msg_length
    else:
        classes = items['classes']

    if len(items['labels']) == 0:
        labels = ['']*msg_length
    else:
        labels = items['labels']

    if len(items['tags_list']) == 0:
        tags_list = [[]*msg_length]
    else:
        tags_list = items['tags_list']

    return templates.TemplateResponse("template.html", {'inputs': items['messages'], 'training_id' : items['training_id'], 'request': request, 'tags_list': tags_list, 'labels': labels, 'classes': classes})



@app.post("/store_messages")
async def store_messages(request: Request):
    params = await request.json()
    items['messages'].extend(params['message'])
    if 'tags_list' in params:
        items['tags_list'].extend(params['tags_list'])
    if 'labels' in params:
        items['labels'].extend(params['labels'])
    if 'classes' in params:
        items['classes'].extend(params['classes'])
    
    print(items['messages'])
    return {'length': len(items['messages'])}


"""
$.ajax({
    type: "POST",
    url: "/store_messages",
    data: {
      labelValues: labelValues,
      messageValues: messageValues,
      classificationValues: classificationValues
    },
    """
@app.post("/send_labels")
async def retrieve_messages(request: Request):
    params = await request.json()
    labelValues = params['labelValues']
    messageValues = params['messageValues']
    classificationValues = params['classificationValues']
    
    #create dataframe
    df = pd.DataFrame({'label': labelValues, 'message': messageValues, 'classification': classificationValues})
    #store in labeled_messages
    items['labeled_messages'].extend(df.to_dict('records'))
    #remove from messages
    items['messages'] = []
    items['tags_list'] = []
    items['labels'] = []
    items['classes'] = []
    
    
    return {'length': len(items['labeled_messages'])}
    

@app.get("/labeled_messages")
def get_labeled_messages():
    return items['labeled_messages']

@app.get("/check_if_done")
def check_if_done():
    if len(items['messages']) == 0:
        return {'done': True}
    else:
        return {'done': False}



    

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=False, workers=1)