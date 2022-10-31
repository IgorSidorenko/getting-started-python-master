from selene.support.shared import browser
from selene import be, have


browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('ecosia').press_enter()
browser.element('[id="search"]').should(have.text('Ecosia - the search engine that plants trees'))
