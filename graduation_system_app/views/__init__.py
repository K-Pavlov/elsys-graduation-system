from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

def create_from_form(request, model_form, redir_view_name, template, context_data):
    if request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(redir_view_name))
    else:
        form = model_form()

    context_data['form'] = form
    return render(
        request,
        template,
        context_instance = RequestContext(request, context_data)
    )