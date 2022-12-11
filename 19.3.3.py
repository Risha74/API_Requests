import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

status = 'available'
base_url = 'https://petstore.swagger.io/v2'
api_key = 'special-key'
headers = {'accept': 'application/json'}
object = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data_photo = MultipartEncoder(
            fields={
                'file': ('image/dog.jpg', open('image/dog.jpg', 'rb'), 'image/jpeg')
            })

res = requests.get(f'{base_url}/pet/findByStatus?status={status}', headers=headers)
res_post = requests.post(f'{base_url}/pet', headers=headers, json=object)
res_put = requests.put(f'{base_url}/pet', json=object)

pet_id = str(json.loads(res.content)[0]['id'])

res_get_id = requests.get(f'{base_url}/pet/{pet_id}', headers=headers)
res_post_id = requests.post(f'{base_url}/pet/{pet_id}', headers=headers, data={'name': 'Rex', 'status': 'available'})
res_post_photo = requests.post(f'{base_url}/pet/{pet_id}/uploadImage', headers={'accept': 'application/json', 'Content-Type': 'multipart/form-data'}, data=data_photo)
res_delete = requests.delete(f'{base_url}/pet/{pet_id}', headers={'api_key': api_key})

print(res.text)
print('')
print(res_post.text)
print('')
print(res_put.text)
print(pet_id)
print('')
print(res_get_id.text)
print('')
print(res_post_id.text)
print('')
print(res_post_photo.text)
print('')
print(res_delete.text)

