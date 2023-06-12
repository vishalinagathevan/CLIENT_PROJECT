# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json

global sessionToken, SessionToken

SessionToken='{"sessionToken": "eyJraWQiOiJtb2NrLW9hdXRoMi1zZXJ2ZXIta2V5IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwY2Y0MzQzMi1lZWRkLTQyOWUtYmY5MS1iM2E1NzQ2ZTgyNTgiLCJzY3AiOiJVc2VyLlJlYWQiLCJ2ZXIiOiIyLjAiLCJhaW8iOiJkZjcxMWIyNy0xOWZiLTQzYTQtOGY4OS0yOWUyNTA4YTYzMWIiLCJhenBhY3IiOiIxIiwiaXNzIjoiaHR0cHM6XC9cL2Zha2VkaW5ncy5kZXYtZ2NwLm5haXMuaW9cL2Zha2UiLCJvaWQiOiI4OGIxY2E1NS04YmQ0LTQ2NDEtYjFiZC1mMDA0YWNmNjQ1ZmQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJub3Rmb3VuZCIsImF1ZCI6Im5vdGZvdW5kIiwibmJmIjoxNjA5ODM3NjI0LCJhenAiOiJjbGllbnQgaWQgcMOlIGRlbiBzb20gc3DDuHIiLCJuYW1lIjoibm90Zm91bmQiLCJleHAiOjE2MTM0Mzc2MjQsImlhdCI6MTYwOTgzNzYyNCwianRpIjoiMzYxNzNhMGQtZjUwMi00MmE5LTliY2QtOGZkY2I4MTVkN2NkIn0.dTVyG7aXiNaTiwiYZnZEcvx2kAHu8xyM6EjGx4-Xl6Lh-u3G9jXLwfJvOCMDyYJTpP8AMdnndjsI-yiQEroU2qds2QCHbRTR7ZDXCmjbslk-u-yLF-6f6y1xen749hSultAtCoY5UGfWT9et5368UqFgs2x3mbqZQQ3DnetAeBX9RIUkjugObaJo30kdWj4oduopIYiD0H7kyeCKGxZDbc0LElNQP8kt6RjeMe13HdHYNeXZWuQNSCImMr1R-AdQ2XR_uBDXGDCC7mnyW3ONLQL9BUS4D80qHXNtCWlWD09XsI9k8FOBT_kD3BeIoXA8jD4K-9W4fmaU2_K_8K6eqQ"}'
accessToken = '{"accessToken": "V5IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwY2Y0MzQzMi1lZWRkLTQyOWUtYmY5MS1iM2E1NzQ2ZTgyNTgiLCJzY3AiOiJVc2VyLlJlYWQiLCJ2ZXIiOiIyLjAiLCJhaW8iOiJkZjcxMWIyNy0xOWZiLTQzYTQtOGY4OS0yOWUyNTA4YTYzMWIiLCJhenBhY3IiOiIxIiwiaXNzIjoiaHR0cHM6XC9cL2Zha2VkaW5ncy5kZXYtZ2NwLm5haXMuaW9cL2Zha2UiLCJvaWQiOiI4OGIxY2E1NS04YmQ0LTQ2NDEtYjFiZC1mMDA0YWNmNjQ1ZmQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJub3Rmb3VuZCIsImF1ZCI6Im5vdGZvdW5kIiwibmJmIjoxNjA5ODM3NjI0LCJhenAiOiJjbGllbnQgaWQgcMOlIGRlbiBzb20gc3DDuHIiLCJuYW1lIjoibm90Zm91bmQiLCJleHAiOjE2MTM0Mzc2MjQsImlhdCI6MTYwOTgzNzYyNCwianRpIjoiMzYxNzNhMGQtZjUwMi00MmE5LTliY2QtOGZkY2I4MTVkN2NkIn0.dTVyG7aXiNaTiwiYZnZEcvx2kAHu8xyM6EjGx4-Xl6Lh-u3G9jXLwfJvOCMDyYJTpP8AMdnndjsI-yiQEroU2qds2QCHbRTR7ZDXCmjbslk-u-yLF-6f6y1xen749hSultAtCoY5UGfWT9et5"}'
jobId = "1234"

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# creating an auth obj
class Auth(Resource):
  
    def post(self):
        data = request.get_json()
        sessionToken = jsonify({"sessionToken": "eyJraWQiOiJtb2NrLW9hdXRoMi1zZXJ2ZXIta2V5IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwY2Y0MzQzMi1lZWRkLTQyOWUtYmY5MS1iM2E1NzQ2ZTgyNTgiLCJzY3AiOiJVc2VyLlJlYWQiLCJ2ZXIiOiIyLjAiLCJhaW8iOiJkZjcxMWIyNy0xOWZiLTQzYTQtOGY4OS0yOWUyNTA4YTYzMWIiLCJhenBhY3IiOiIxIiwiaXNzIjoiaHR0cHM6XC9cL2Zha2VkaW5ncy5kZXYtZ2NwLm5haXMuaW9cL2Zha2UiLCJvaWQiOiI4OGIxY2E1NS04YmQ0LTQ2NDEtYjFiZC1mMDA0YWNmNjQ1ZmQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJub3Rmb3VuZCIsImF1ZCI6Im5vdGZvdW5kIiwibmJmIjoxNjA5ODM3NjI0LCJhenAiOiJjbGllbnQgaWQgcMOlIGRlbiBzb20gc3DDuHIiLCJuYW1lIjoibm90Zm91bmQiLCJleHAiOjE2MTM0Mzc2MjQsImlhdCI6MTYwOTgzNzYyNCwianRpIjoiMzYxNzNhMGQtZjUwMi00MmE5LTliY2QtOGZkY2I4MTVkN2NkIn0.dTVyG7aXiNaTiwiYZnZEcvx2kAHu8xyM6EjGx4-Xl6Lh-u3G9jXLwfJvOCMDyYJTpP8AMdnndjsI-yiQEroU2qds2QCHbRTR7ZDXCmjbslk-u-yLF-6f6y1xen749hSultAtCoY5UGfWT9et5368UqFgs2x3mbqZQQ3DnetAeBX9RIUkjugObaJo30kdWj4oduopIYiD0H7kyeCKGxZDbc0LElNQP8kt6RjeMe13HdHYNeXZWuQNSCImMr1R-AdQ2XR_uBDXGDCC7mnyW3ONLQL9BUS4D80qHXNtCWlWD09XsI9k8FOBT_kD3BeIoXA8jD4K-9W4fmaU2_K_8K6eqQ"})
        return sessionToken  


# creating an access obj
class AccessToken(Resource):        
        def post(self): 
            global sessionToken             
            if SessionToken == '{"sessionToken": "eyJraWQiOiJtb2NrLW9hdXRoMi1zZXJ2ZXIta2V5IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwY2Y0MzQzMi1lZWRkLTQyOWUtYmY5MS1iM2E1NzQ2ZTgyNTgiLCJzY3AiOiJVc2VyLlJlYWQiLCJ2ZXIiOiIyLjAiLCJhaW8iOiJkZjcxMWIyNy0xOWZiLTQzYTQtOGY4OS0yOWUyNTA4YTYzMWIiLCJhenBhY3IiOiIxIiwiaXNzIjoiaHR0cHM6XC9cL2Zha2VkaW5ncy5kZXYtZ2NwLm5haXMuaW9cL2Zha2UiLCJvaWQiOiI4OGIxY2E1NS04YmQ0LTQ2NDEtYjFiZC1mMDA0YWNmNjQ1ZmQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJub3Rmb3VuZCIsImF1ZCI6Im5vdGZvdW5kIiwibmJmIjoxNjA5ODM3NjI0LCJhenAiOiJjbGllbnQgaWQgcMOlIGRlbiBzb20gc3DDuHIiLCJuYW1lIjoibm90Zm91bmQiLCJleHAiOjE2MTM0Mzc2MjQsImlhdCI6MTYwOTgzNzYyNCwianRpIjoiMzYxNzNhMGQtZjUwMi00MmE5LTliY2QtOGZkY2I4MTVkN2NkIn0.dTVyG7aXiNaTiwiYZnZEcvx2kAHu8xyM6EjGx4-Xl6Lh-u3G9jXLwfJvOCMDyYJTpP8AMdnndjsI-yiQEroU2qds2QCHbRTR7ZDXCmjbslk-u-yLF-6f6y1xen749hSultAtCoY5UGfWT9et5368UqFgs2x3mbqZQQ3DnetAeBX9RIUkjugObaJo30kdWj4oduopIYiD0H7kyeCKGxZDbc0LElNQP8kt6RjeMe13HdHYNeXZWuQNSCImMr1R-AdQ2XR_uBDXGDCC7mnyW3ONLQL9BUS4D80qHXNtCWlWD09XsI9k8FOBT_kD3BeIoXA8jD4K-9W4fmaU2_K_8K6eqQ"}':
                data = request.get_json()
                accessToken = jsonify({ 'success': 'True',"accessToken": "V5IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwY2Y0MzQzMi1lZWRkLTQyOWUtYmY5MS1iM2E1NzQ2ZTgyNTgiLCJzY3AiOiJVc2VyLlJlYWQiLCJ2ZXIiOiIyLjAiLCJhaW8iOiJkZjcxMWIyNy0xOWZiLTQzYTQtOGY4OS0yOWUyNTA4YTYzMWIiLCJhenBhY3IiOiIxIiwiaXNzIjoiaHR0cHM6XC9cL2Zha2VkaW5ncy5kZXYtZ2NwLm5haXMuaW9cL2Zha2UiLCJvaWQiOiI4OGIxY2E1NS04YmQ0LTQ2NDEtYjFiZC1mMDA0YWNmNjQ1ZmQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJub3Rmb3VuZCIsImF1ZCI6Im5vdGZvdW5kIiwibmJmIjoxNjA5ODM3NjI0LCJhenAiOiJjbGllbnQgaWQgcMOlIGRlbiBzb20gc3DDuHIiLCJuYW1lIjoibm90Zm91bmQiLCJleHAiOjE2MTM0Mzc2MjQsImlhdCI6MTYwOTgzNzYyNCwianRpIjoiMzYxNzNhMGQtZjUwMi00MmE5LTliY2QtOGZkY2I4MTVkN2NkIn0.dTVyG7aXiNaTiwiYZnZEcvx2kAHu8xyM6EjGx4-Xl6Lh-u3G9jXLwfJvOCMDyYJTpP8AMdnndjsI-yiQEroU2qds2QCHbRTR7ZDXCmjbslk-u-yLF-6f6y1xen749hSultAtCoY5UGfWT9et5"})
                return accessToken
            else:
                return None
            
# creating an Scan obj
class ScanRepo(Resource):        
        def post(self):             
            if accessToken == '{"accessToken": "V5IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwY2Y0MzQzMi1lZWRkLTQyOWUtYmY5MS1iM2E1NzQ2ZTgyNTgiLCJzY3AiOiJVc2VyLlJlYWQiLCJ2ZXIiOiIyLjAiLCJhaW8iOiJkZjcxMWIyNy0xOWZiLTQzYTQtOGY4OS0yOWUyNTA4YTYzMWIiLCJhenBhY3IiOiIxIiwiaXNzIjoiaHR0cHM6XC9cL2Zha2VkaW5ncy5kZXYtZ2NwLm5haXMuaW9cL2Zha2UiLCJvaWQiOiI4OGIxY2E1NS04YmQ0LTQ2NDEtYjFiZC1mMDA0YWNmNjQ1ZmQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJub3Rmb3VuZCIsImF1ZCI6Im5vdGZvdW5kIiwibmJmIjoxNjA5ODM3NjI0LCJhenAiOiJjbGllbnQgaWQgcMOlIGRlbiBzb20gc3DDuHIiLCJuYW1lIjoibm90Zm91bmQiLCJleHAiOjE2MTM0Mzc2MjQsImlhdCI6MTYwOTgzNzYyNCwianRpIjoiMzYxNzNhMGQtZjUwMi00MmE5LTliY2QtOGZkY2I4MTVkN2NkIn0.dTVyG7aXiNaTiwiYZnZEcvx2kAHu8xyM6EjGx4-Xl6Lh-u3G9jXLwfJvOCMDyYJTpP8AMdnndjsI-yiQEroU2qds2QCHbRTR7ZDXCmjbslk-u-yLF-6f6y1xen749hSultAtCoY5UGfWT9et5"}':
                data = request.get_json()
                scanrepo = jsonify({"jobID": "1234","success": 'True'})
                return scanrepo
            else:
                 data = request.get_json()
                 scanrepo = jsonify({"jobID": "","success": 'False'})
                 return scanrepo 
 
 # creating an Scan status obj
class ScanStatus(Resource):        
        def post(self):             
            if jobId == "1234":
                data = request.get_json()
                scanstatus = jsonify({"status": "Submitted"})
                return scanstatus
            else:
                data = request.get_json()
                scanstatus = jsonify({"status": "Finished"})
                return scanstatus  
            
 # creating an Scan status obj
class ScanReport(Resource):        
        def post(self): 
            data = request.get_json()
            scanReport = jsonify([{"jobID":"1234", "summary.count":123}])
            return scanReport  
            
            
# adding the defined resources along with their corresponding urls
api.add_resource(Auth, '/api/v1/authn')
api.add_resource(AccessToken, '/api/v1/access')
api.add_resource(ScanRepo, '/api/v1/scans/repo')
api.add_resource(ScanStatus, '/api/v1/scans/status')
api.add_resource(ScanReport, '/api/v1/scans/report')

# driver function
if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port = 80, debug = False)