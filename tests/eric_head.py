# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 08:22:06
# @Last Modified time: 2018-01-04 09:30:07
"""Head checker.

Check, that all data in a head contains in packages for Eric's room.

"""
import os
# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from eric_config import all_txt_in_eric_room_wihtout_subfolders
from eric_config import log

# Flags, see https://www.computerhope.com/jargon/f/flag.htm
# https://stackoverflow.com/a/48052480/5951529
head_failure_tests = False

# Flags for all matches
description_failure_tests = False
training_process_failure_tests = False
first_example_failure_tests = False
first_answer_failure_tests = False
second_example_failure_tests = False
second_answer_failure_tests = False
proofs_failure_tests = False
authors_failure_tests = False
link_failure_tests = False
package_link_failure_tests = False

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529
for filename in all_txt_in_eric_room_wihtout_subfolders:

    filename_without_path = os.path.basename(filename)

    # Find head data
    if 'Описание пакета:' in open(filename, encoding='windows-1251').read():
        log.debug(
            '«Описание пакета:» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Описание пакета:»')
        description_failure_tests = True

    if 'Процесс тренировки:' in open(
            filename, encoding='windows-1251').read():
        log.debug(
            '«Процесс тренировки:» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Процесс тренировки:»')
        training_process_failure_tests = True

    if 'Пример вопроса 1:' in open(filename, encoding='windows-1251').read():
        log.debug(
            '«Пример вопроса 1:» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Пример вопроса 1:»')
        first_example_failure_tests = True

    if 'Ответ к примеру вопроса 1:' in open(
            filename, encoding='windows-1251').read():
        log.debug(
            '«Ответ к примеру вопроса 1:» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Ответ к примеру вопроса 1:»')
        first_answer_failure_tests = True

    if 'Пример вопроса 2:' in open(filename, encoding='windows-1251').read():
        log.debug(
            '«Пример вопроса 2:» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Пример вопроса 2:»')
        second_example_failure_tests = True

    if 'Ответ к примеру вопроса 2:' in open(
            filename, encoding='windows-1251').read():
        log.debug(
            '«Ответ к примеру вопроса 2:» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Ответ к примеру вопроса 2:»')
        second_answer_failure_tests = True

    if 'Источник(и):' in open(filename, encoding='windows-1251').read():
        log.debug(
            '«Источник(и):» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Источник(и):»')
        proofs_failure_tests = True

    if 'Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):' in open(
            filename, encoding='windows-1251').read():
        log.debug(
            '«Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):»')
        authors_failure_tests = True

    if 'Ссылка(и) на источник(и):' in open(
            filename, encoding='windows-1251').read():
        log.debug(
            '«Ссылка(и) на источник(и):» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Ссылка(и) на источник(и):»')
        link_failure_tests = True

    if 'Постоянный адрес пакета:' in open(
            filename, encoding='windows-1251').read():
        log.debug(
            '«Постоянный адрес пакета:» contains in ' +
            filename_without_path)
    else:
        log.error(
            filename_without_path +
            ' not contains «Постоянный адрес пакета:»')
        package_link_failure_tests = True

    if description_failure_tests \
            or training_process_failure_tests \
            or first_example_failure_tests \
            or first_answer_failure_tests \
            or second_example_failure_tests \
            or second_answer_failure_tests \
            or proofs_failure_tests \
            or authors_failure_tests \
            or link_failure_tests \
            or package_link_failure_tests \
            is True:
        head_failure_tests = True

if not head_failure_tests:
    log.notice('All files contains correct head data.')

if head_failure_tests:
    log.error('One or more packages not contains one or more head data. '
              'Please, add correct head data to your package.')
