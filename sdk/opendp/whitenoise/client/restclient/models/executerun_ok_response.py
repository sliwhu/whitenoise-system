# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExecuterunOKResponse(Model):
    """ExecuterunOKResponse.

    :param result: Json string result,  TODO release document
    :type result: str
    """

    _attribute_map = {
        'result': {'key': 'result', 'type': 'str'},
    }

    def __init__(self, result=None):
        super(ExecuterunOKResponse, self).__init__()
        self.result = result