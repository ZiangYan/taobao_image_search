#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import re
import time
import random


def wait_for_page_load(old):
    def _wait_for(condition_function):
        start_time = time.time()
        while time.time() < start_time + 10:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception('Timeout waiting for %s' % condition_function.__name__)
    def _elem_has_gone_stale():
        try:
            old.find_element_by_id('I-am-nothing-at-all')
            return False
        except StaleElementReferenceException:
            return True
        except NoSuchElementException:
            return False
    _wait_for(_elem_has_gone_stale)


def main(image_list_fname, result_fname):
    #driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://s.taobao.com/search')
    with open(image_list_fname, 'r') as image_list_f, \
            open(result_fname, 'w') as result_f:
        images_fname = [line.strip() for line in image_list_f.readlines()]
        for idx, image_fname in enumerate(images_fname):
            success = False
            old = driver.find_element_by_id('J_SiteNav')
            elem = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'J_IMGSeachUploadBtn')))
            elem.send_keys(os.path.abspath(image_fname))
            wait_for_page_load(old)
            h4 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'collection-title')))
            labels = re.findall(r'[^{]"title":"[^"]+"', driver.page_source)
            joined_label = '_'.join([label[10:-1] for label in labels]).encode('utf-8')
            result_f.write('%s: %s\n' % (image_fname, joined_label))
            print 'processing %d/%d...' % (idx, len(images_fname))
    driver.quit()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: '
        print '    ./get_tb_description.py image_list.txt result.txt'
        exit(1)
    else:
        main(sys.argv[1], sys.argv[2])
