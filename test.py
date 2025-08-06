import base64
import json
import jwt 
import hmac
import hashlib
from jwcrypto import jwe, jwk
from jwcrypto.common import json_decode


def decode_base64url(base64url):
    # Add padding if necessary
    padding = '=' * (4 - len(base64url) % 4)
    base64url += padding
    # Decode from base64url to base64
    return base64.urlsafe_b64decode(base64url.encode('utf-8'))

jwt_token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImZkNjE4NzMzLTAxYTMtNDAwMC1iMzc0LWYyMDYwYjQyMWJlNSIsIm9yZy5hcGVyZW8uY2FzLnNlcnZpY2VzLlJlZ2lzdGVyZWRTZXJ2aWNlIjoiMTAwMDAwMDEifQ.ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1qVTJRMEpETFVoVE5URXlJaXdpWTNSNUlqb2lTbGRVSWl3aWRIbHdJam9pU2xkVUlpd2lhMmxrSWpvaU5ETmxOakl4WlRBdFlqQmhaQzAwWlRJd0xXRmhPREV0TmpjeU16UXdabVV4WVRRMElpd2liM0puTG1Gd1pYSmxieTVqWVhNdWMyVnlkbWxqWlhNdVVtVm5hWE4wWlhKbFpGTmxjblpwWTJVaU9pSXhNREF3TURBd01TSjkuLnpSYjRmRFpkWTFpMlFfVDQyWnRTVEEua1RwbXJqMzV2YnpTSUdGczh2bXlDc3pyU3U4OEVmd2M4cUJvVE5xeWhDbWxqM1NDeUhJQlRwOGtablFVUEZyRU43QWhiMXBlTTZCSmtLZENaX0pGN3VNeTlTZVlON05kSFVhWlFjQzBiSHREYUd1ZXVlcGRUOW40dzcwc3RqdjhuaXJSdFB1ZjV3OV9UaUxKX2VxZk9ab0dSYmxBY3A1dUJDQXZXS3FyZ29LY0RHMS10dEhDNzlCUmI0VGtNZWNicnA2ZWdNMzRlZC1JemR2VFZ6TnhoWFUzZ1hSLWNlX1F3QlFldmlfUHh4bUFiMy0zQWtUQmtYNXlZM0JPMDZyTUxaTmNzdjVScjdXNGw4OTFENHh5RWhyRm1yUmp1UGhSbGh4X1ZxYXVoekQySTdqMWJBdS12RHdNRkdQTkNKTExwNTZUSjRCbnp3elJmREhiV1FYcllRS21VYmdjZU5yU0hCM2REeU1VYWlIM3BkLTRrUFNKM0dFcGt2cGI3Z04yUEhpVThtRmMzbnZwMDVvOEdHMldyWEt1SG5rS3J6YmF3V2U2WnBTZmNYazZVZnFwcmtjNHpmY2txczBya0FqVG1rR1RxMUlFMkExd0wzWlFadldBSG1tS2VEcGZIM25NTFBCU3hSQjUtTVBwMWV6SWR4WjJKMGNaTFVzTE4yeXNhVDFtOTV3UjlXWlR2YWppOWtQRG5GdFY4eG12MVN0NnkyVEFnY3VyNi1RcUhpdmtkSm9yYjFyNkZuZ2hPSS1YSy15OUNMd1lYYlQ0NUxPREFSVkR1QkdtTjdJZ1VQMDNVVllqejdmSHpVMTF6QWlrZk9YU1ZiMXVDb0RmUWV2Rmd2WmNscmpqZFFyMmVnVllCQmZBZkUxYWpJcXhYZXI1V0FDU0otb3FoYURPY2owaGtQeVBNcU1UeWREUThiam1VWUNiRDRHVGNpQmxXV2lQZkVhSnNaNFpyZ3FvTkhnWjVha0hzSkQtUFdab1YwRlE5LVNQMi02TUZrb05DWXA5eDhqcFhHNzB1UklaLU1LcnJXM1lXdy5BV3pTVFdtd0Q1Y0JVRUszbTRQTEJpeVFmZnFsMTAwMWpNdGhYbXNrSTdn.DPxbyLZ9yX5KcsmJaUqv4OhBtmuI0wy_w9xDU7pUu4ryhss_WaaputY8XXxJ68PcZduXdxnEmsdT7SCavsH4Tw"
header_b64, payload_b64, signature_b64 = jwt_token.split('.')

header = decode_base64url(header_b64)
print("Header:", header)
payload = decode_base64url(payload_b64)
print("Payload:", payload)


# Assuming 'header_b64' and 'payload_b64' are already defined
message = header_b64 + '.' + payload_b64
secret_key = b"WAayJAF/KaUxlVC5hwTsXzZiixYCQNnFItaXQlyEdgsydDZaqWPjY+nTZcVEJmJvrHhYlb7syMLRwHMTbd/5XQ=="

# Create the HMAC SHA-512 signature
signature = hmac.new(secret_key, message.encode(), hashlib.sha512).digest()

# Decode the base64url encoded signature from the JWT
expected_signature = base64.urlsafe_b64decode(signature_b64 + '==')

# Compare the two signatures
if signature == expected_signature:
    print("Signature is valid.")
else:
    print("Signature is invalid.")


# Your encryption key (ensure it's 256 bits for A256CBC-HS512)
encryption_key = b"qt5FuyB+sTHKyQjmTT2MH4FKBxgMvh2/KcE1ja2HgxSbUCF/3nhBMuif6GHNpPJYVCMv1S7MppCm4U7fTxlhGA=="

# Nested JWE token extracted from the JWS payload
nested_jwe_token = payload_b64

# Proceed with deserialization
jwetoken = jwe.JWE()
jwetoken.deserialize(nested_jwe_token)

# Decrypt the token (ensure you have the correct decryption key)
jwetoken.decrypt(encryption_key)

# Access the decrypted payload
decrypted_payload = jwetoken.payload.decode('utf-8')
print("Decrypted Payload:", decrypted_payload)
