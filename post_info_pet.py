import requests

put_info_headers = {
    "auth_key": "0063dc59a50de8093253304eb1b96eb487e9b1ca1cd7ca9280ac6db3",
    "pet_id": "588734bd-742c-4b32-b021-b89259037ea7"
}

put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "588734bd-742c-4b32-b021-b89259037ea7"


def put_pet_info(link, p_params, p_headers):
    response = requests.put(link,
                            params=p_params,
                            headers=p_headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(put_pet_info(put_info_link, put_info_params, put_info_headers))