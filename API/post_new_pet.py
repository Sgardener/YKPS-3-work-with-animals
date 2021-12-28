import requests

post_new_pet_headers = {
    "auth_key": "0063dc59a50de8093253304eb1b96eb487e9b1ca1cd7ca9280ac6db3",
    "name": "Rich",
    "animal_type": "cat",
    "age": '2',
    "pet_photo": ""
}

post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"


def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('kot.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_new_pet(new_pet_POST_link, post_new_pet_params, post_new_pet_headers))