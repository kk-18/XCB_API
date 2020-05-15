import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/index/shop/{sid}/services'
api_name = '007-获取门店服务信息'
xcb_request = XCBRequest('app')


@allure.feature('门店首页')
@allure.story(api_name)
@allure.title('门店下服务信息')

def test_case_1():
    """
    用例描述：门店服务信息
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    data={
        'sid':69
    }

    resp = xcb_request.get(api.format(**data),headers=headers)

    assert resp.code == 0