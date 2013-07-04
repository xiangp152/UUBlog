#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView

from django.db import models


class UBaseTemplateView(TemplateView):
    extraContext={}

    def post(self, request, *args, **kwargs):
        context = self.post_context_data(**kwargs)
        return self.render_to_response(context)

    def post_context_data(self, **kwargs):
        context=self.get_context_data(**kwargs)

        return context

    def get_context_data(self, **kwargs):
        context = super(UBaseTemplateView, self).get_context_data(**kwargs)

        if kwargs:
            for key, value in kwargs.items():
                if callable(value):
                    context[key]=value()
                else:
                    context[key]=value

        if self.extraContext is not None:
            for key, value in self.extraContext.items():
                if callable(value):
                    context[key]=value()
                else:
                    context[key]=value

        return context


    def AddVars(self,context,args={},**kwargs):
        if args:
            for key, value in args.items():
                if callable(value):
                    context[key]=value()
                else:
                    context[key]=value

        if kwargs:
            for key, value in kwargs.items():
                if callable(value):
                    context[key]=value()
                else:
                    context[key]=value
            

    def HasPostData(self,key):
        if self.request:
            return self.request.POST.has_key(key)
        return False

    def GetPostData(self,key,default=""):
        if self.HasPostData(key):
            return self.request.POST[key]
        return default

    def HasGetData(self,key):
        if self.request:
            return self.request.GET.has_key(key)
        return False

    def GetGetData(self,key,default=""):
        if self.HasGetData(key):
            return self.request.GET[key]
        return default

