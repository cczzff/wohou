# coding=utf-8
import datetime
from celery import shared_task

from module.sms_md import send_verify_code_msg, send_todolist_msg
from todolist.models import Todo


# 此处使用了 shared_task 装饰器，用于设置不与具体 celery 应用绑定的 task
@shared_task
def celery_send_verify_code(phone, code):
    send_verify_code_msg(mobile=phone, verify_code=code)


@shared_task
def celery_send_todolist_msg():
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(minutes=10)
    wait_remid_todos = Todo.objects.filter(sms_remid=True, already_remid=False,
                                           todo_time__gte=start_time, todo_time__lt=end_time).all()

    for todo in wait_remid_todos:
        send_todolist_msg(mobile=todo.account.username, content=todo.note)
        todo.already_remid = False
        todo.save()
