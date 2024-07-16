from selene import browser, have
import os


def test_complete_todo():

    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Anastasia')
    browser.element('#lastName').type('Strelnik')

    browser.element('#userEmail').type('n.str@mail.ru')

    browser.element('[for="gender-radio-2"]').click()

    browser.element('#userNumber').type('89222222222')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value = "2001"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value = "3"]').click()
    browser.all('.react-datepicker__month-select>option').element_by(have.exact_text("March")).click()
    browser.element('.react-datepicker__day.react-datepicker__day--029').click()

    browser.element('#subjectsInput').type('Maths').press_tab()

    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('test.png'))

    browser.element('#currentAddress').type('Kaliningrad')
    browser.element("#react-select-3-input").type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter()
    browser.element('#submit').click()

    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts(
            "Anastasia Strelnik",
            "n.str@mail.ru",
            "Female",
            "8922222222",
            "29 March,2001",
            "Maths",
            "Music",
            "test.png",
            "Kaliningrad",
            "NCR Gurgaon",
        )
    )