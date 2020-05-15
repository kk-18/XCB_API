import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/order/list'
api_name = '011-获取订单列表'
xcb_request = XCBRequest('app')


@allure.feature('订单')
@allure.story(api_name)
@allure.title('订单列表--全部')

def test_case_1():
    """
    用例描述：订单列表--全部
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    data={
        'status':0
    }

    resp = xcb_request.get(api,headers=headers,data=data)

    assert resp.code == 0

@allure.feature('订单')
@allure.story(api_name)
@allure.title('订单列表--未完成')

def test_case_1():
    """
    用例描述：订单列表--未完成
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    data={
        'status':2
    }

    resp = xcb_request.get(api,headers=headers,data=data)

    assert resp.code == 0