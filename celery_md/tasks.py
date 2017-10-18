# coding=utf-8
from celery import shared_task
from module.sms_md import send_verify_code_msg, send_todolist_msg


# 此处使用了 shared_task 装饰器，用于设置不与具体 celery 应用绑定的 task
@shared_task
def celery_send_verify_code(phone, code):
    send_verify_code_msg(mobile=phone, verify_code=code)


@shared_task
def celery_send_todolist_msg(phone, content):
    send_todolist_msg(mobile=phone, content=content)