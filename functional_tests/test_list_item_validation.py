from unittest import skip
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest





class ItemValidationTest(FunctionalTest):
    
    # @skip
    def test_cannot_add_empty_list_items(self):

        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: 
            self.browser.find_element_by_css_selector(
                '#id_text:invalid'
        ))

        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: 
            self.browser.find_element_by_css_selector(
                '#id_text:valid'
        ))

        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: 
            self.browser.find_element_by_css_selector(
                '#id_text:invalid'
        ))

        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: 
            self.browser.find_element_by_css_selector(
                '#id_text:valid'
        ))


        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
        # self.fail("finish this test!")


    def test_cannot_add_duplicate_items(self):
        # Edith goes to the gome page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('!: Buy wellies')


        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)


        # She sees a helpful error message
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You've already got this in your list"
        ))




        








