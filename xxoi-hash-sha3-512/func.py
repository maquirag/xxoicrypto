#
# xxoi-hash-sha3-512
#
# Serverless Function running under FN PROJECT
# https://fnproject.io/

import io
from hashlib import sha3_512
from fdk import response

def handler(ctx, data: io.BytesIO = None):
    message = data.getvalue()
    hashed = sha3_512(message).hexdigest()
    return response.Response(ctx, response_data=hashed)
    