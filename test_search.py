from selene import browser, be, have


def test_google_search(browser_custom_window):
    browser.element('[name="q"]').should(be.blank).type('SDET - это').press_enter()
    browser.element('[id="rso"]').should(have.text('У SDET — сердце разработчика'))


def test_google_search_incorrect(browser_custom_window):
    browser.element('[name="q"]').clear().type('qqa1!2@3#7khbjgd+№;%:?*(278uhecihdydh&^%$#$$##').press_enter()
    browser.element('[id="botstuff"]').should(
        have.text('Your search - qqa1!2@3#7khbjgd+№;%:?*(278uhecihdydh&^%$#$$## - did not match any documents.'))
