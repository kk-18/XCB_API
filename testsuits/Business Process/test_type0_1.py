import allure

from utils.xcb_req import XCBRequest
from utils.sqlclient import SQLclient
from utils.esclient import ESclient

@allure.feature("业务流程")
@allure.story("托管养车-成功案例")
@allure.title("测试用例名称：流程性的用例，添加测试步骤")
def test_add_goods_and_buy(get_app_token,get_cabinet_token):
    '''
    托管养车流程性用例:
    1、下单 2、存钥匙 3、门店接单 4、店员取钥匙 5、店员存钥匙 6、支付 7、取钥匙  8、评价
    '''
    with allure.step("step1：下单"):
        api_1 = '/api/v1.0/order'
        headers = {
            'token':get_app_token
        }

        body = {
            "amount": 1,
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

        resp_1 = XCBRequest('app').post(api_1, data=body, headers=headers)
        print("用户下单")

    with allure.step("step2：存钥匙"):

        api_2 = '/api/v1/cabinet/save_vcode'
        headers={
            'sid': '69',
            'sa_no': 'test123',
            'token': get_cabinet_token
        }

        body={
            "vcode": resp_1.data['vcode']
        }
        resp_2 = XCBRequest('cabinet').put(api_2, data=body, headers=headers)

        #调用接口关门
        api_2_2='/api/v1/cabinet/close'
        headers = {
            'sid': '69',
            'sa_no': 'test123',
            'token': get_cabinet_token
        }

        body = {
            "key_no": resp_2.data['key_no']
        }

        resp_2_2 = XCBRequest('cabinet').put(api_2_2, data=body, headers=headers)
        print("用户存钥匙")
    with allure.step("step3：门店接单"):
        api_3 = '/api/v1/order/receiving'

        body = {
              "brand_id": 0,
              "clerk": "string",
              "clerk_id": 0,
              "order_id":resp_1.data['order_id'],
              "phone": "18408251193",
              "vehicle_id": "string",
              "vehicle_source": 0
        }

        resp3 = XCBRequest('middle').put(api_3, data=body)
        print("门店接单")

    with allure.step("step4：店员取钥匙"):
        sql = '''
                       select message from db_xcb.t_order_item where order_id=%s and  status=20
                       ''' % resp_1.data['order_id']

        message = SQLclient().sql_client(sql)
        api_4='/api/v1/cabinet/fetch_vcode'
        headers = {
            'sid': '69',
            'sa_no': 'test123',
            'token': get_cabinet_token
        }

        f_key=(eval(message[0]))['f_key']
        body = {
            'vcode': f_key
        }

        resp_4 = XCBRequest('cabinet').put(api_4, data=body, headers=headers)
        # 调用接口关门
        headers = {
            'sid': '69',
            'sa_no': 'test123',
            'token': get_cabinet_token
        }

        body = {
            "key_no": resp_4.data['key_no']
        }
        resp_4_2 = XCBRequest('cabinet').put(api_2_2, data=body, headers=headers)
        print("店员取钥匙")
    with allure.step("step5：店员存钥匙"):
        headers = {
            'sid': '69',
            'sa_no': 'test123',
            'token': get_cabinet_token
        }
        s_key=(eval(message[0]))['s_key']
        body = {
            "vcode": s_key
        }

        resp_5 = XCBRequest('cabinet').put(api_2, data=body, headers=headers)
        # 调用接口关门
        headers = {
            'sid': '69',
            'sa_no': 'test123',
            'token': get_cabinet_token
        }

        body = {
            "key_no": resp_5.data['key_no']
        }

        resp_5_2 = XCBRequest('cabinet').put(api_2_2, data=body, headers=headers)

    with allure.step("step6：支付"):
        """
            修改mysql和ES
           """
        sql = "update db_xcb.t_order id set pay_status=1   where id=%s" % resp_1.data['order_id']
        sql_result = SQLclient().sql_client(sql)
        index = 'xcb-order.test.order'
        body = {
            "script": {
                "source": "ctx._source['pay_status']=1"
            },
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "id": {
                                    "query":resp_1.data['order_id']
                                }
                            }
                        }
                    ]
                }
            }
        }
        es_result = ESclient().update(index=index, body=body)
    with allure.step("step7：用户取回钥匙"):
        sql = "select message from db_xcb.t_order_item where order_id=%s and  status=40" % resp_1.data['order_id']

        message_7 = SQLclient().sql_client(sql)
        headers = {
            'sid': '69',
            'sa_no': 'test123',
            'token': get_cabinet_token
        }
        body = {
            "vcode": (eval(message_7[0]))['key']
        }

        resp_7 = XCBRequest('cabinet').put(api_4, data=body, headers=headers)
        # 调用接口关门
        headers = {
            'sid': '69',
            'sa_no': 'test123',
            'token': get_cabinet_token
        }
        body = {
            "key_no": (eval(message_7[0]))['key_no']
        }
        print(body)
        resp_7_2 = XCBRequest('cabinet').put(api_2_2, data=body, headers=headers)


    with allure.step("断言"):
        sql ="select status from db_xcb.t_order where id=%s " % resp_1.data['order_id']

        message_s = SQLclient().sql_client(sql)
        print(message_s[0])
        assert message_s[0]== 50
