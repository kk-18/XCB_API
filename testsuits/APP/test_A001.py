import allure

from utils.xcb_req import XCBRequest



api = '/api/v1.0/comment'
api_name = '001-获取门店评论列表'
xcb_request = XCBRequest('app')

@allure.feature('门店--首页')
@allure.story(api_name)
@allure.title('评论分类展示--全部')

def test_case_general_1(get_app_token):
    """
    用例描述：全部评论
    """
    headers={}
    headers["token"] = get_app_token

    data ={
        "sid": 69,
        "comment_type ":0,
        "page_number":1
    }

    resp = xcb_request.get(api, data=data,headers=headers)
    assert 'total' in resp.data

@allure.feature('门店--首页')
@allure.story(api_name)
@allure.title('评论分类展示--好评')
def test_case_general_2(get_app_token):
    """
    用例描述：好评
    """
    headers={}
    headers["token"] = get_app_token

    data ={
        "sid": 69,
        "comment_type":1,
        "page_number":1
    }

    resp = xcb_request.get(api, data=data,headers=headers)
    a=1
    for i in resp.data['list']:
        if i['star']<3:
            a=0
    assert a==1

@allure.feature('门店--首页')
@allure.story(api_name)
@allure.title('评论分类展示--差评')
def test_case_general_3(get_app_token):
    """
    用例描述：差评
    """
    headers={}
    headers["token"] =get_app_token

    data ={
        "sid": 69,
        "comment_type":2,
        "page_number":1
    }

    resp = xcb_request.get(api, data=data,headers=headers)
    a=1
    for i in resp.data['list']:
        if i['star']>=3:
            a=0
    assert a==1

@allure.feature('门店--首页')
@allure.story(api_name)
@allure.title('评论分类展示--有图')
def test_case_general_4(get_app_token):
    """
    用例描述：有图
    """
    headers={}
    headers["token"] =get_app_token

    data ={
        "sid": 69,
        "comment_type":3,
        "page_number":1
    }

    resp = xcb_request.get(api, data=data,headers=headers)
    a=1
    for i in resp.data['list']:
        if i['images'] == '':
            a=0
    assert a==1
'''
@allure.feature('门店--首页')
@allure.story('门店评论')
@allure.title('门店评分计分规则')
def test_case_general_5():
    """
    用例描述： 累计评分综合/点评次数
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP

    data ={
        "sid": 69,
        "comment_type":0,
        "page_number":1
    }

    resp = xcb_request.get(api, data=data,headers=headers)
    a=1
    for i in resp.data['list']:
        if i['images'] == '':
            a=0
    assert a==1
'''
@allure.feature('门店--首页')
@allure.story(api_name)
@allure.title('门店评论展示顺序规则')
def test_case_general_6(get_app_token):
    """
    用例描述： 用户点评时间倒序
    """
    headers={}
    headers["token"] = get_app_token

    data ={
        "sid": 69,
        "comment_type":0,
        "page_number":1
    }

    resp = xcb_request.get(api, data=data,headers=headers)
    a=resp.data['list'][0]['created_ts']
    b=0
    for i in resp.data['list']:
        if i['created_ts'] <=a:
            a=i['created_ts']
        else:
            b=1
            break
    assert b==0