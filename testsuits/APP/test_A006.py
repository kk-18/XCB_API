import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/index/shop/{sid}/cabinets'
api_name = '006-获取门店下智能柜信息'
xcb_request = XCBRequest('app')


@allure.feature('门店首页')
@allure.story(api_name)
@allure.title('门店智能柜列表信息')

def test_case_1():
    """
    用例描述：门店信息
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    data={
        'sid':69
    }

    resp = xcb_request.get(api.format(**data),headers=headers)

    assert resp.code == 0