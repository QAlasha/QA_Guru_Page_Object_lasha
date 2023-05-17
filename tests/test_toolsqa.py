from pages.register_page import RegistrationPage


def test_form_filling_submitting():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Lasha')
    registration_page.fill_last_name('Baslandze')
    registration_page.fill_email('lasha.bas@gmail.com')
    registration_page.select_gender('Male')
    registration_page.fill_phone_number('89263530000')
    registration_page.fill_date_of_birth('1991', 'July', '29')

    registration_page.fill_subject('English')
    registration_page.fill_subject('Accounting')
    registration_page.fill_hobbie('Music')
    registration_page.upload_picture('account.png')

    registration_page.fill_address('проспект Революции 285 - 45')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Agra')
    registration_page.submit()

    # THEN
    registration_page.should_registered_user_with(
        'Lasha Baslandze',
        'lasha.bas@gmail.com',
        'Male',
        '89263530000',
        '29 July,1991',
        'English, Accounting',
        'Music',
        'account.png',
        'проспект Революции 285 - 45',
        'Uttar Pradesh Agra',
    )
