import allure

from utils.xcb_req import XCBRequest




api = '/api/v1.0/order/info/{order_id}'
api_name = '010-订单详情'
xcb_request = XCBRequest('app')


@allure.feature('订单')
@allure.story(api_name)
@allure.title('订单详情--待支付--待存钥匙--托管养车')

def test_case_1(ordernew_type0,get_app_token):
    """
    用例描述：
    """
    headers={}
    headers["token"] = get_app_token
    data={
        'order_id':ordernew_type0
    }

    resp = xcb_request.get(api.format(**data),headers=headers)
    print(resp.data)
    assert resp.code == 0

@allure.feature('订单')
@allure.story(api_name)
@allure.title('订单详情--待支付--待接单--托管养车')

def test_case_1(ordernew_type0,get_app_token):
    """
    用例描述：
    """
    headers={}
    headers["token"] = get_app_token
    data={
        'order_id':ordernew_type0
    }

    resp = xcb_request.get(api.format(**data),headers=headers)
    print(resp.data)
    assert resp.code == 0