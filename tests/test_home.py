from selene import browser

from home_8_10.page.registration_page import RegistrationPage
from home_8_10.data.users import User
import allure




def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    with allure.step("Заполнить форму регистрации тестовыми данными"):
        student = User(first_name='Anton',
                   last_name='Fomin',
                   email='catman@mail.ru',
                   gender='Other',
                   phone_number='9694840725',
                   day_birth='019',
                   month_birth='3',
                   year_birth='90',
                   subject='Computer Science',
                   hobby='Sports, Reading',
                   picture='sun.jpg',
                   current_address='Krasnodar',
                   state='NCR',
                   city='Delhi')


    # WHEN
    registration_page.register(student)
    with allure.step("Проверка, что пользователь зарегистрирован"):
        registration_page.student_should_by_registred(student)