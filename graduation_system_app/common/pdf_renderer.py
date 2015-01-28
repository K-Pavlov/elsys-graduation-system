# -*- coding: utf-8 -*-
#coding: utf-8
import os 
import cStringIO as StringIO
import ho.pisa as pisa

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context_dict['path'] = os.path.abspath("graduation_system_app/static/fonts/DejaVuSansMono.ttf")
    print(context_dict['path'])
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(html, result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('<pre>%s</pre>' % escape(html))