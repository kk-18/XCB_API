import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/order/open_cabinet'
api_name = '012-选择订单开箱'
xcb_request = XCBRequest('app')


@allure.feature('订单')
@allure.story(api_name)
@allure.title('托管待支付订单存钥匙开箱')

def test_case_1(ordernew_type0):
    """
    用例描述：托管待支付订单存钥匙开箱
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    body={
          "order_id": ordernew_type0,
          "sid": 69,
          "sn": "test123",
          "type": 1
    }

    resp = xcb_request.post(api,headers=headers,data=body)

    assert resp.code == 0
