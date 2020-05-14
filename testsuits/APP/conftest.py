import pytest

from utils.xcb_req import XCBRequest
from const import check_level

@pytest.fixture()
def ordernew_type0():
    """
    托管养车待支付订单号
    """
    api = '/api/v1.0/order'
    xcb_request = XCBRequest('app')
    headers={}
    headers["token"] = check_level.TOKEN_APP

    body ={
          "amount": 1,
          "c_name": "深云智能",
          "cid": 63,
          "name": "测试-1",
         # "parking_type": 0,
          "phone": "18408251193",
          "plate_no": "川A1123B",
          "services": [
            {
              "num":1,
              "price_id": 140
            }
          ],
          "shop": "深云智能·银泰城店",
          "sid": 69,
          "type": 0
        }

    resp = xcb_request.post(api, data=body,headers=headers)

    return resp.data['order_id']