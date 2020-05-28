import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/order/pay'
api_name = '004-支付订单'
xcb_request = XCBRequest('app')

'''
@allure.feature('订单')
@allure.story(api_name)
@allure.title('支付订单')

def test_case_1(ordernew_type0):
    """
    用例描述：支付宝支付
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    body ={
            "order_id": ordernew_type0,
            "pay_mode": 1
        }

    resp = xcb_request.post(api, data=body,headers=headers)

    assert resp.code == 0
'''