import json
from httprunner import __version__
from pactverify.matchers import Matcher, Like, EachLike, Term, Enum, PactVerify, PactVerifyError
from pacts import Pact


def pactverify(response, pact_name):
    if not hasattr(Pact, pact_name):
        raise PactVerifyError('{}契约未找到'.format(pact_name))

    # print(11111,dir(response))
    rsp_json = response.resp_obj.json()

    expect_format = getattr(Pact, pact_name)
    mPactVerify = PactVerify(expect_format)
    mPactVerify.verify(rsp_json)
    response.verify_result = mPactVerify.verify_result
    response.verify_info = mPactVerify.verify_info
