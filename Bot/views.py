# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbot import Chat,reflections,multiFunctionCall
from Bot.botUtil import pairs,whoIs,getQues
from django.template.response import TemplateResponse



@csrf_exempt 
def chat(request):
	try:
		client=str(request.GET["q"])
	except:
		msg="hi"
	call = multiFunctionCall({"whoIs":whoIs,"getQues":getQues})
	bot=Chat(pairs, reflections,call=call)
	bot.conversation["general"].append("Hi, I am your stackExchange bot. What can I do for you?")
	bot.conversation["general"].append(client)
	reply = bot.respond(client,sessionID="general")
	bot.conversation["general"].append(reply)
	return HttpResponse(reply)



@csrf_exempt
def home(request):
	return TemplateResponse(request,'chat.html',)


