# 定义校验契约类,定义每个接口的预期格式
from pactverify.matchers import Matcher, Like, EachLike, Term, Enum, PactVerify


class Pact:
    # /api/v1/auth接口契约
    api_v1_auth_get_pact = Matcher(
        {
            "msg": "success",
            "code": 0,
            "data": Like({
                # 类型不匹配错误
                "token": 11
            })
        }
    )
