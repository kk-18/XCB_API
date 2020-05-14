import allure

from utils.xcb_req import XCBRequest
from const import check_level


api = '/api/v1.0/comment'
api_name = '002-新增评论'
xcb_request = XCBRequest('app')

@allure.feature('门店--首页')
@allure.story(api_name)
@allure.title('评论新增---仅点星')

def test_case_general_1():
    """
    用例描述：全部评论
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP

    body ={
          "content": "",
          "file_path": [
          ],
          "order_id": "string",
          "sid": 0,
          "star": 1
        }

    resp = xcb_request.post(api, data=body,headers=headers)
    assert resp.code== 0
