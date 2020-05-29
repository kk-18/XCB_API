import allure

from utils.xcb_req import XCBRequest



api = '/api/v1.0/comment'
api_name = '002-新增评论'
xcb_request = XCBRequest('app')

@allure.feature('门店--首页')
@allure.story(api_name)
@allure.title('评论新增---仅点星')

def test_case_general_1(get_app_token,ordercomment_type1):
    """
    用例描述：托管订单
    """
    headers={}
    headers["token"] = get_app_token

    body ={
          "content": "",
          "file_path": [
          ],
          "order_id": ordercomment_type1,
          "sid": 0,
          "star": 1
        }

    resp = xcb_request.post(api, data=body,headers=headers)
    assert resp.code== 0
