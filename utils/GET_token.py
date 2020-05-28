import json
from utils.xcb_req import XCBRequest

xcb_request = XCBRequest('app')
def Get_token():
    headers = {
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTA0ODQwNTAsImp0aSI6IjI3Iiwic3ViIjoie1wiYWxpX3VpZFwiOlwiXCIsXCJvcGVuaWRcIjpcIm85WG1nNGdRVm9mMmZ0ZzFFZWdacDdNU256RFlcIixcInBob25lXCI6XCIxODQwODI1MTE5M1wifSJ9.FfluM7SrEA-seQ1GPqNIvPSTUd1q1nIf6mvBKrPbEdE',
    }
    api = '/api/v1.0/token'
    resp = xcb_request.put(api, headers=headers)

    return resp.data["token"]
