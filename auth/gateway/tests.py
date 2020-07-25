from django.test import APITestCase

class userProfileTestCase(APITestCase):
    profile_list_url=reverse('all-profiles')
    def setUp(self):
        # создайте нового пользователя, отправив запрос к конечной точке djoser
        self.user=self.client.post('/auth/users/',data={'username':'mario','password':'i-keep-jumping'})
        # получить веб-токен JSON для вновь созданного пользователя
        response=self.client.post('/auth/jwt/create/',data={'username':'mario','password':'i-keep-jumping'})
        self.token=response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

    # получить список всех профилей пользователей во время аутентификации пользователя запроса
    def test_userprofile_list_authenticated(self):
        response=self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    # получить список всех профилей пользователей, пока запрос пользователя не прошел проверку подлинности
    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response=self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    # проверьте, чтобы получить данные профиля аутентифицированного пользователя
    def test_userprofile_detail_retrieve(self):
        response=self.client.get(reverse('profile',kwargs={'pk':1}))
        # print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    # заполнить профиль пользователя, который был автоматически создан с использованием сигналов
    def test_userprofile_profile(self):
        profile_data={'description':'I am a very famous game character','location':'nintendo world','is_creator':'true',}
        response=self.client.put(reverse('profile',kwargs={'pk':1}),data=profile_data)
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)