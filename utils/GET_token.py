import json
from utils.xcb_req import XCBRequest

xcb_request = XCBRequest('app')
def Get_token():
    headers = {
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODg4NDg1ODEsImp0aSI6IjIyIiwic3ViIjoie1wiYWxpX3VpZFwiOlwiMjA4ODExMjcxMTUxMTQ4NFwiLFwib3BlbmlkXCI6XCJcIixcInBob25lXCI6XCIxODA4MTk0MDgxOVwifSJ9.1dr2U_tKrVePNSP8T8Krrd6Gia0m1AVqrnlTknCUykA',
    }
    api = '/api/v1.0/token'
    resp = xcb_request.put(api, headers=headers)

    return resp.data["token"]
