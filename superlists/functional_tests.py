import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    '''тест нового посетителя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        # Эдит слышала про крутое новое онлайн-приложение со списком неотложные дел
        # Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби - вязание рыболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')

        # Когда она нажимает Enter, страница обновляется, и теперь страница содержит
        # "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Купить павлиньи перья' for row in rows),
                        'Новый элемент списка не появился в таблице')

        # Текстовое поле по-прежнему приглашает ее добавить ещё один элемент
        # Она вводит "Сделать мушку из павлиньих перьев" (Эдит очень методична)

        # Страница снова обновляется, и теперь показывает оба элемента её списка

        # Эдит интересно, запомнит ли сайт её список. Далее она видит, что сайт сгенерировал
        # для неё уникальный URL-адрес - об этов выводится небольшой текст с объяснениями

        # Она посещает этот URL-адрес - её список по-прежнему там

        # Удовлетворённая, она снова ложится спать


if __name__ == '__main__':
    unittest.main(warnings='ignore')
