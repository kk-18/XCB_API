import allure
import time

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/order'
api_name = '002-新增订单'
xcb_request = XCBRequest('app')

#获取当前日的第二天9点和12点时间戳，作为预约订单时间
cur_time = int(time.time())#当前时间
start_stamp = (cur_time - (cur_time % (24*3600))) +(25*3600)
end_stamp = (cur_time - (cur_time % (24*3600))) +(28*3600)

@allure.feature('订单')
@allure.story(api_name)
@allure.title('新增订单--托管养车必录项')


def test_case_general_1():
    """
    用例描述：基本必录项全录入
    """
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

    assert resp.code == 0


@allure.feature('订单')
@allure.story(api_name)
@allure.title('新增订单--预约到店必录项')

def test_case_general_2():
    """
    用例描述：基本必录项全录入
    """



    headers={}
    headers["token"] = check_level.TOKEN_APP

    body ={
          "amount": 1,
          "c_name": "深云智能",
          "cid": 63,
          "name": "测试-1",
         # "parking_type": 0,
          "reservation_end": end_stamp,
          "reservation_start": start_stamp ,
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
          "type": 1
        }

    resp = xcb_request.post(api, data=body,headers=headers)

    assert resp.code == 0


@allure.feature('订单')
@allure.story(api_name)
@allure.title('新增订单--总金额错误')

def test_case_general_3():
    """
    用例描述：总金额与服务项金额总和不等
    """



    headers={}
    headers["token"] = check_level.TOKEN_APP

    body = {
        "amount": 0,
        "c_name": "深云智能",
        "cid": 63,
        "name": "测试-1",
        # "parking_type": 0,
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
        "type": 0
    }

    resp = xcb_request.post(api, data=body,headers=headers)

    assert resp.code == 10033

@allure.feature('订单')
@allure.story(api_name)
@allure.title('新增订单--联系人电话为空')

def test_case_general_4():
    """
    用例描述：用户联系电话为空
    """



    headers={}
    headers["token"] = check_level.TOKEN_APP

    body = {
        "amount": 0,
        "c_name": "深云智能",
        "cid": 63,
        "name": "测试-1",
        # "parking_type": 0,
        "plate_no": "川A1123B",
        "services": [
            {
                "num": 1,
                "price_id": 140
            }
        ],
        "shop": "深云智能·银泰城店",
        "sid": 69,
        "type": 0
    }

    resp = xcb_request.post(api, data=body,headers=headers)

    assert resp.code == 10003


@allure.feature('订单')
@allure.story(api_name)
@allure.title('新增订单--车牌号为空')

def test_case_general_5():
    """
    用例描述：用户车牌号为空
    """



    headers={}
    headers["token"] = check_level.TOKEN_APP

    body = {
        "amount": 0,
        "c_name": "深云智能",
        "cid": 63,
        "name": "测试-1",
        # "parking_type": 0,
        "plate_no": "川A1123B",
        "services": [
            {
                "num": 1,
                "price_id": 140
            }
        ],
        "shop": "深云智能·银泰城店",
        "sid": 69,
        "type": 0
    }

    resp = xcb_request.post(api, data=body,headers=headers)

    assert resp.code == 10003