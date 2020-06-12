import pytest
import time

from utils.xcb_req import XCBRequest
from const import check_level
from utils.sqlclient import SQLclient
from utils.esclient import ESclient

#获取小程序token
@pytest.fixture(scope='session')
def get_app_token():
    xcb_request = XCBRequest('app')
    headers = {
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTA0ODQwNTAsImp0aSI6IjI3Iiwic3ViIjoie1wiYWxpX3VpZFwiOlwiXCIsXCJvcGVuaWRcIjpcIm85WG1nNGdRVm9mMmZ0ZzFFZWdacDdNU256RFlcIixcInBob25lXCI6XCIxODQwODI1MTE5M1wifSJ9.FfluM7SrEA-seQ1GPqNIvPSTUd1q1nIf6mvBKrPbEdE',
    }
    api = '/api/v1.0/token'
    resp = xcb_request.put(api, headers=headers)

    return resp.data["token"]

#获取智能柜token
@pytest.fixture(scope='session')
def get_cabinet_token():
    xcb_request = XCBRequest('cabinet')
    body={
        'sid':69,
        'sa_no':'test123'
    }
    api = '/api/v1/token'
    resp = xcb_request.get(api, data=body)

    return resp.data["token"]

#获取托管养车新订单
@pytest.fixture()
def ordernew_type0():
    """
    指定用户&&托管养车&&待支付&&待存钥匙
    """
    sql='''
    select id from db_xcb.t_order where uid=27 and  service_type=0 and status=0 and pay_status =0
    '''
    order_id=SQLclient().sql_client(sql)
    if order_id == None:
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
    else:
            return order_id[0]


#获取预约养车新订单
@pytest.fixture()
def ordercomment_type1():
    """
    指定用户&&托管订单&&待评论
    """
    sql = '''
        select id from db_xcb.t_order where uid=27 and  service_type=1 and status=50 and comment =0
        '''
    order_id = SQLclient().sql_client(sql)
    return order_id[0]

#获取可评论订单
@pytest.fixture()
def ordercomment_type1():
    """
    指定用户&&托管订单&&待评论
    """
    sql = '''
        select id from db_xcb.t_order where uid=27 and  service_type=1 and status=50 and comment =0
        '''
    order_id = SQLclient().sql_client(sql)
    return order_id[0]


#托管订单用户取钥匙前先支付
@pytest.fixture()
def orderuser_f_type1():
    """
     修改mysql和ES
    """
    sql1 = '''
        select id from db_xcb.t_order where uid=27 and  service_type=1 and status=40 and pay_status =0
        '''
    order_id = SQLclient().sql_client(sql1)
    sql2="update db_xcb.t_order id set pay_status=0  where id=%s"
    sql_result = SQLclient().sql_client(sql2,order_id[0])
    index='xcb-order.test.order'
    body={
          "script": {
            "source": "ctx._source['pay_status']=1"
          },
          "query": {
            "bool": {
              "must": [
                {
                  "match": {
                    "id": {
                      "query": order_id[0]
                    }
                  }
                }
              ]
            }
          }
        }
    es_result=ESclient().update(index=index,body=body)
    return order_id[0]