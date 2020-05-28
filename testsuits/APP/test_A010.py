import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/order/info/{order_id}'
api_name = '010-订单详情'
xcb_request = XCBRequest('app')


@allure.feature('门店首页')
@allure.story(api_name)
@allure.title('门店下服务信息')

def test_case_1():
    """
    用例描述：店铺列表
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP

    resp = xcb_request.get(api,headers=headers)

    assert resp.code == 0

