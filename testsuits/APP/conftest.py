import pytest
import time

from utils.xcb_req import XCBRequest
from const import check_level

@pytest.fixture()
def ordernew_type0():
    """
    托管养车&&待支付&&待存钥匙
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

@pytest.fixture()
def ordernew_type1():
    """
    预约订单待支付
    """
    api = '/api/v1.0/order'
    xcb_request = XCBRequest('app')
    # 获取当前日的第二天9点和12点时间戳，作为预约订单时间
    cur_time = int(time.time())  # 当前时间
    start_stamp = (cur_time - (cur_time % (24 * 3600))) + (25 * 3600)
    end_stamp = (cur_time - (cur_time % (24 * 3600))) + (28 * 3600)
    headers = {}
    headers["token"] = check_level.TOKEN_APP

    body = {
        "amount": 1,
        "c_name": "深云智能",
        "cid": 63,
        "name": "测试-1",
        # "parking_type": 0,
        "reservation_end": end_stamp,
        "reservation_start": start_stamp,
        "phone": "18408251193",
        "plate_no": "川A1123B",
        "services": [
            {
                "num": 1,
                "price_id": 140
            }
        ],
        "shop": "深云智能·银泰城店",
        "sid": 69,
        "type": 1
    }

    resp = xcb_request.post(api, data=body, headers=headers)
    return resp.data['order_id']