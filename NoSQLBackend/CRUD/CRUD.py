import boto3

class CRUD(object):
    def __init__(self):
        self.db_name = 'dynamodb'
        self.dynamo = None
        self.valid_keys = ['story_id','story_description','story_related_pics','story_comments']

    def connect(self):
        try: 
            self.dynamo = boto3.resource(self.db_name)
            result = {"message" : "Success"}
        except:
            result = {"message" : "Error"}
        return result
    '''
    reqData structure
    {
        'story_id' : 'string',
        'story_description' : 'string',
        'story_related_pics' : 'string urls',
        'story_comments' : {'user_name+comment_time' : 'entire_comment'}
    }
    '''
    def insert_story(self,reqData):
        self.connect()
        if len(set(list(reqData.keys())) & set(self.valid_keys)) == len(self.valid_keys):
            table = self.dynamo.Table('tbo_story_info')
            table.put_item(Item=reqData)
            return {"message" : "Success"}
        else:
            return {"message" : "Error"}




    
