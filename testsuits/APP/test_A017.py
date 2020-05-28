import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/vehicle'
api_name = '017-获取车辆列表'
xcb_request = XCBRequest('app')


@allure.feature('我的')
@allure.story(api_name)
@allure.title('获取车辆列表')

def test_case_1():
    """
    用例描述：用户添加的车辆列表
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP

    resp = xcb_request.get(api,headers=headers)

    assert resp.code==0
