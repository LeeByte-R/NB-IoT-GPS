import http.client
import json
import mimetypes
from codecs import encode


def ini():
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=email;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("acs106128@gm.ntcu.edu.tw"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=password;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("acs106128"))
    dataList.append(encode('--'+boundary+'--'))
    dataList.append(encode(''))


conn = http.client.HTTPSConnection("campus.kits.tw")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
body = b'\r\n'.join(dataList)
payload = body
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjhhZjU3YzY3Mjc4MTU3NWIzMmM0M2MxYWNmY2NmNTc5Y2U5NzhkNjAxYTExYWYwNzM3YWJjODU5ZjJlMWY4OWQzMTRmMWQwMzU1NWExZDMwIn0.eyJhdWQiOiIyIiwianRpIjoiOGFmNTdjNjcyNzgxNTc1YjMyYzQzYzFhY2ZjY2Y1NzljZTk3OGQ2MDFhMTFhZjA3MzdhYmM4NTlmMmUxZjg5ZDMxNGYxZDAzNTU1YTFkMzAiLCJpYXQiOjE2MTA0MzU5MTQsIm5iZiI6MTYxMDQzNTkxNCwiZXhwIjoxNjQxOTcxOTE0LCJzdWIiOiI3NDgiLCJzY29wZXMiOltdfQ.UCz96BZEmXFdbJtPUZtC8aoPqTHH7NZ_jj0svbesjLQT6AYJoqx2X6XydiHlPR5jgfV62vhTGvivHcxVemE0Czm74nAWC3zq2i_RgmTGHA6ZMiGyWf2tav2J8i-BYa6xQx-nETUFx4efzCpHv1qVVSZWzZ7gyXXafSRr8SDBSC9Kx1vcWDfbWqj348GQK-22nWhdYwe-jdlotu1YKgB4yrQEViXEZfLSl9YszjLXSVZUiu-tT5rfuIlYzren-Ns3pR8iFIuTeHHqVJslY0Che2DIxKoUV5SI2FmaGCQERhWMCD6BT-zBjDzwQEKhzAeLhVtDOIwesoV8ILKe0YpnCweEJxzXiazWxJs2-Puv8KMHZl5_O5DiOjvgBsRJ6KIQoL1jPjtqLN9mVfuY6TY2W9jlDSOyeOzCV92hG2zfY9hUu7dObnXmjvJcY9VGpIskxHVVwmxKMKKmqecI2bvSpS-F0iQGa1DUjg57OuoWYkCDSNC7R21ylzguc6miNBUyOG3aSN1WVKpUCukXT-6pHC7uShebm9aTb8l-NcGjkVrwsu2OkQRthy-0l3_ND-0CtVetjRXrYVhNMLtZDWqoU6fiYcHcn0TaxHmH4kMt5fWBR6oMflJxBl8LO_OzCFs0YBuJM5FhDiN_dYc5jIITdqw8bOhQdLGGWnh_h7aDgCI',
    'Accept': 'application/json',
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}


def get_data(start, current):
    url = f"/api/get/data/AAA8DF07?date_filter=" \
          f"{start.year}-{start.month}-{start.day}%20{start.hour}:{start.minute}:{start.second}%20+-+" \
          f"%20{current.year}-{current.month}-{current.day}%20{current.hour}:{current.minute}:{current.second}"
    conn.request("POST", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data)
    # print(json_data)
    return json_data
