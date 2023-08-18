# def sum_of_squares(nums, index):
#     if index < 0:
#         return 0
#     current_num = nums[index]
#     if current_num > 0:
#         return current_num ** 2 + sum_of_squares(nums, index - 1)
#     else:
#         return sum_of_squares(nums, index - 1)

# def read_input():
#     try:
#         return input()
#     except EOFError:
#         return None

# def read_input_int():
#     return int(read_input())

# def read_input_ints():
#     return list(map(int, read_input().split()))

# def process_test_case(results, num_test_cases):
#     if num_test_cases == 0:
#         return
#     _ = read_input_int()
#     numbers = read_input_ints()
#     result = sum_of_squares(numbers, len(numbers) - 1)
#     results.append(result)
#     process_test_case(results, num_test_cases - 1)

# def main():
#     num_test_cases = read_input_int()
#     results = []
#     process_test_case(results, num_test_cases)
    
#     for result in results:
#         print(result)

# if __name__ == "__main__":
#     main()

import requests
import hmac
import hashlib
import time
import sys
import struct
import json

from requests.auth import HTTPBasicAuth

root = "https://api.challenge.hennge.com/challenges/003"
content_type = "application/json"
userid = "rsiu95@gmail.com"
secret_suffix = "HENNGECHALLENGE003"
shared_secret = userid+secret_suffix

timestep = 30
T0 = 0

def HOTP(K, C, digits=10):
    """HTOP:
    K is the shared key
    C is the counter value
    digits control the response length
    """
    K_bytes = str.encode(K)
    C_bytes = struct.pack(">Q", C)
    hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
    return Truncate(hmac_sha512)[-digits:]

def Truncate(hmac_sha512):
    """truncate sha512 value"""
    offset = int(hmac_sha512[-1], 16)
    binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

def TOTP(K, digits=10, timeref = 0, timestep = 30):
    """TOTP, time-based variant of HOTP
    digits control the response length
    the C in HOTP is replaced by ( (currentTime - timeref) / timestep )
    """
    C = int ( time.time() - timeref ) // timestep
    return HOTP(K, C, digits = digits)

data =  {
    "github_url": "https://gist.github.com/Rsiu95/8fb37bef00708b5edf88bcb58c243138",
    "contact_email": "rsiu95@gmail.com",
    "solution_language": "python"
}

passwd = TOTP(shared_secret, 10, T0, timestep).zfill(10) 
resp = requests.post(root, auth=HTTPBasicAuth(userid, passwd), data=json.dumps(data))
print(resp.json())


