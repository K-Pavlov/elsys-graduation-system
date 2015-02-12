# -*- coding: utf-8 -*-
from teacher import Teacher
from season import Season
from firm import Firm

def create_mentor_referee(type, item_dict):
    DEFAULT = 'ТУЕС'
    try:
        first_name = item_dict['fname']
        if(not first_name): 
            return
    except KeyError:
        return
    try:
        middle_name = item_dict['mname']
    except KeyError:
        middle_name = ''
    try: 
        last_name = item_dict['lname']
        if(not last_name):
            return
    except KeyError:
        return

    model = type()
    try:
       teacher = Teacher.objects.get(first_name= first_name, middle_name= middle_name,
                               last_name= last_name)
       try:
           return type.objects.get(teacher=teacher)
       except type.DoesNotExist:
           pass
    except Teacher.DoesNotExist:
        teacher = Teacher()

        teacher.first_name = first_name
        teacher.middle_name = middle_name
        teacher.last_name = last_name

        firm = {}
        try:
            firm_name = item_dict['firm']
            try:
                firm = Firm.objects.get(name=firm_name)
            except Firm.DoesNotExist:
                firm = Firm()
                firm.name = firm_name
                firm.save()
        except KeyError:
            try:
                firm = Firm.objects.get(name=DEFAULT)
            except Firm.DoesNotExist:
                firm = Firm()
                firm.name = DEFAULT
                firm.save()                 

        try:
            model.season = Season.objects.get(is_active=True)
        except Season.DoesNotExist:
            pass

        teacher.firm = firm
        teacher.save()

    try:
        model.season = Season.objects.get(is_active=True)
    except Season.DoesNotExist:
        pass

    model.teacher = teacher
    return model