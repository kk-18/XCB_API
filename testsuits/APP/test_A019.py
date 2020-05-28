import allure

from utils.xcb_req import XCBRequest
from const import check_level



api = '/api/v1.0/vehicle/license'
api_name = '019-行驶证加车'
xcb_request = XCBRequest('app')


@allure.feature('我的')
@allure.story(api_name)
@allure.title('行驶证加车--必录项')

def test_case_1():
    """
    用例描述：仅必录项---返回车系车款信息
    """
    headers={}
    headers["token"] = check_level.TOKEN_APP
    data={
            "is_temp": 0,
            "owner": "啦啦啦",
            "plate_no": "川A12345",
        }

    resp = xcb_request.post(api,data=data,headers=headers)

    assert 'vehicle_styles' in resp.data
