import requests

post_set_photo_headers = {
    "auth_key": "0063dc59a50de8093253304eb1b96eb487e9b1ca1cd7ca9280ac6db3",
    "pet_id": "588734bd-742c-4b32-b021-b89259037ea7"
}

post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "588734bd-742c-4b32-b021-b89259037ea7"


def post_set_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('sobaka.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_set_photo(set_photo_POST_link, post_set_photo_params, post_set_photo_headers))