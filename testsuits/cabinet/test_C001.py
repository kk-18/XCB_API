import allure

from utils.xcb_req import XCBRequest

api = '/api/v1/cabinet/save_vcode'
api_name = '001-存钥匙'
xcb_request = XCBRequest('cabinet')
def test_case_general_1(get_cabinet_token,ordercomment_type1):
    """
    用例描述：托管订单
    """
    headers={
        'sid':69,
        'sa_no':'test123',
        'token':get_cabinet_token
    }

    body ={
        "vcode": "string"
        }

    resp = xcb_request.post(api, data=body,headers=headers)
    assert resp.code== 0