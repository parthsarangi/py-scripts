import pybase64 as base64
# from google.cloud import kms_v1
# google-cloud-kms
def start_encrypt(params):
    val = []
    for item in params["decrypt"]:
        val.append(base64.b64encode(item))
    return val


def start_decrypt(params):
    val = []
    for item in params["encrypt"]:
        val.append(base64.b64decode(item))
    return val


def decrypt_symmetric(project_id, location_id, key_ring_id, crypto_key_id,
                      ciphertext):
    """Decrypts input ciphertext using the provided symmetric CryptoKey."""

    from google.cloud import kms_v1

    # Creates an API client for the KMS API.
    client = kms_v1.KeyManagementServiceClient()

    # The resource name of the CryptoKey.
    name = client.crypto_key_path_path(project_id, location_id, key_ring_id,
                                       crypto_key_id)
    # Use the KMS API to decrypt the data.
    parameters = {"decrypt": [], "encrypt": ciphertext, "function": "decrypt"}
    ciphertext_resp = start_decrypt(parameters)
    iv_key = []
    for item in ciphertext_resp:
        # print()
        response = client.decrypt(name, item)
        iv_key.append(response.plaintext)
        print(response.plaintext)
    return iv_key


if __name__ == '__main__':
    text_decrypted = [b'hello world']

    # passed value of iv an key in tet_encrypted
    text_encrypted = [b'Q2lRQWR2MXA5UzJNUVR6Y25MVFNRd0I1M0VJQmhHU1BzNVc0Zk9kbGtJSnRJTkdvalNFU09RRG80YlVYZkQyazlYNjNvV0xvcjFSUTRBeU9sUjI5NUlYM2NGVkVINXlyRm5WZzEydVBzL3FLQkZNY3RHYXVYekVZamc3RzBmbERtZz09',
                      b'Q2lRQWR2MXA5UXV5NDRGWVI0bW1mQ2c3blZXTVZjcG9HbzFBSHN0SDMyN1JtYTBjemVvU1NRRG80YlVYTTlXd2JFTDlBK21pbGpsVlE3M01zZndub1pkTDF0eHByaFRXdW1pT1FjOEoxOXpsVEQ2RE1Vdi8xWHNDTEh2UmFGdjB1Q0daTk9pTmdObGo3aVFINUhIZXM2bz0=',
                      b'c291cmNlX2VxX2VuY3J5cHQ=',
                      b'ZGF0YXBsYXRmb3JtLTEzNjM=',
                      b'cHJvamVjdHMvZGF0YXBsYXRmb3JtLTEzNjMvbG9jYXRpb25zL3VzL2tleVJpbmdzL2FjbS1tbS11cy9jcnlwdG9LZXlzL2JxLWRlY3J5cHRlcg==']

    function = "decrypt"
    parameters = {"decrypt": text_decrypted, "encrypt": text_encrypted, "function": function}

    if parameters["function"] == "encrypt":
        val = start_encrypt(parameters)

    if parameters["function"] == "decrypt":
        val = start_decrypt(parameters)

    for item in val:
        print(item)

    # Pass the iv and key to ciphertext for decoding
    ciphertext = val[0:2]

    response = decrypt_symmetric("dataplatform-1363", "us", "acm-mm-us", "bq-decrypter",
                      ciphertext)
    print("iv :" + repr(response[0]) + ": \nkey:" + repr(response[1]))


