from .base_page import BasePage
from .locators import ProductPageLocators as PPL

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*PPL.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*PPL.SUCCESS_MESSAGE), 'Success message is not presented'

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*PPL.PRODUCT_NAME).text
        message_txt = self.browser.find_element(*PPL.SUCCESS_MESSAGE).text

        assert product_name == message_txt, 'Product name in message is different'

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*PPL.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*PPL.BASKET_PRICE).text

        assert product_price == basket_price, "Basket price is different"





