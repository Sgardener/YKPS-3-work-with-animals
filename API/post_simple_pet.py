import requests

post_simple_headers = {
    "auth_key": "0063dc59a50de8093253304eb1b96eb487e9b1ca1cd7ca9280ac6db3",
    "name": "Richard",
    "animal_type": "dog",
    "age": '1,5'
}

post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"


def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    print(type(response), type(response.ok))
    return response.ok


print(post_simple_pet(create_pet_simple_POST_link, post_simple_params, post_simple_headers))