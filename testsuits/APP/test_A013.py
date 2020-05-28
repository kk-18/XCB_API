import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/order/{order_id}'
api_name = '013-取消订单'
xcb_request = XCBRequest('app')


@allure.feature('订单')
@allure.story(api_name)
@allure.title('取消托管养车订单')

def test_case_1(ordernew_type0):
    """
    用例描述：托管养车订单--未支付---待存钥匙状态
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    data={
          'order_id': ordernew_type0
    }

    resp = xcb_request.put(api.format(**data),headers=headers)

    assert resp.code == 0
@allure.feature('订单')
@allure.story(api_name)
@allure.title('取消预约养车订单')

def test_case_1(ordernew_type1):
    """
    用例描述：预约养车订单--未支付---未过期
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    data={
          'order_id': ordernew_type1
    }

    resp = xcb_request.put(api.format(**data),headers=headers)

    assert resp.code == 0