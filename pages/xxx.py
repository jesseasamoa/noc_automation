import call_api
import os
import sys
import hmac
import hashlib
import json
import configparser

from urllib.request import urlopen, Request

print(call_api.api_call({'key/info', 'pretty'}, request=json))