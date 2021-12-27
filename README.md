Лабораторная работа №3

Для начала нужно зарегестрироваться на сайте PetFriends:

![image](https://user-images.githubusercontent.com/72302486/147510922-35521dae-9b5e-489c-a891-74b89283db80.png)

![image](https://user-images.githubusercontent.com/72302486/147510943-85f87d02-37d2-46e5-a898-8c2f8220f5d7.png)

Перейдя на сайт Flasgger, нужно изучить API для сайта PetFriends. Указанные ниже функции были реализованы на Python 3.8:

![image](https://user-images.githubusercontent.com/72302486/147510976-ec373f13-a823-4a49-9963-c36337ff8a28.png)

Далее будут представлены результаты нужных нам функций:

GET API key:

![image](https://user-images.githubusercontent.com/72302486/147511004-2d434ec6-be65-47ca-b244-7e0dbb4fe72d.png)

POST new pet:

![image](https://user-images.githubusercontent.com/72302486/147511027-cc64cc42-e93a-40d8-aa7c-07558bf76b4a.png)

GET pets list:

![image](https://user-images.githubusercontent.com/72302486/147511040-5f8709fc-167a-4757-b88b-c5a27903f565.png)

POST photo of the pet:

![image](https://user-images.githubusercontent.com/72302486/147511048-26fc95c1-3313-41ab-80d2-666d57ff5539.png)

PUT info about pet:

![image](https://user-images.githubusercontent.com/72302486/147511058-2fe6cda7-7a74-41ae-8a3b-549325a44ef8.png)

DELETE pet from database:

![image](https://user-images.githubusercontent.com/72302486/147511071-725f5e75-c891-4f60-83da-6f314b40a830.png)

После выполнения всех функций на Python с помощью библиотеки "requests", были проведены тесты. Была использована библиотеку PyTest (мы научились пользоваться ей в предыдущей ЛР№2). Фикстуры были использованы для всех функций, а параметризация подойдет для функции "POST".

![image](https://user-images.githubusercontent.com/72302486/147511174-25f7d851-1cb7-443c-9d9b-8998a18f21d0.png)

Фикстура для удаления питомца:

![image](https://user-images.githubusercontent.com/72302486/147511188-1c69ef22-a202-42ba-ba5b-f3774ecba92b.png)

Отрицательные кейсы "marks=pytest.mark.xfail":

![image](https://user-images.githubusercontent.com/72302486/147511210-a9ace867-529d-4fbf-8da7-6fc7024e9d53.png)
