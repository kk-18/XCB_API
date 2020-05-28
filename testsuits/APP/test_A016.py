import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/user'
api_name = '015-获取用户昵称'
xcb_request = XCBRequest('app')


@allure.feature('我的')
@allure.story(api_name)
@allure.title('获取用户信息')

def test_case_1():
    """
    用例描述：用户信息
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP

    resp = xcb_request.get(api,headers=headers)

    assert resp.data['phone'] != ''
