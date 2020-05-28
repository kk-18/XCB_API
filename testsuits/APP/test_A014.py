import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/scan'
api_name = '014-扫码开箱'
xcb_request = XCBRequest('app')


@allure.feature('订单')
@allure.story(api_name)
@allure.title('扫码开箱--多个订单')

def test_case_1():
    """
    用例描述：托管养车订单--未支付---待存钥匙状态
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    data={
        'sid': 69,
        'sn':'test123',
        'type':1
    }

    resp = xcb_request.get(api,data=data,headers=headers)

    assert 'list' in resp.data
