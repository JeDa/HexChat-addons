# -*- coding: utf-8 -*-
import hexchat
import random

__module_name__ = "Rainbow"
__module_author__ = "JeDa"
__module_version__ = "1.0.2b"
__module_description__ = "Generates rainbow-colored versions of the text you enter."

def TheRainbow(word, raintype):
	colorlist = ["\x034","\x037","\x038","\x039","\x0311","\x0312","\x0313","\x036","\x034"]
	rainbowed = ""
	if raintype == "chan":
		word.remove(word[0])
		text = str(" ".join(word), "utf-8")
	elif raintype == "privmsg":
    		word.remove(word[0])
    		word.remove(word[0])
	    	text = str(" ".join(word), "utf-8")
	for letter in text:
	    	rainbowed += random.choice(colorlist) + letter
	return rainbowed.encode("utf-8", "replace")

def rainbow(word,word_eol,userdata):
		hexchat.command("say " + TheRainbow(word, "chan"))

def rainbowme(word,word_eol,userdata):
		hexchat.command("me " + TheRainbow(word, "chan"))

def rainbowmsg(word,word_eol,userdata):
		hexchat.command("msg " + word[1] + " " + TheRainbow(word, "privmsg"))

def rainbownotice(word,word_eol,userdata):
		hexchat.command("notice " + word[1] + " " + TheRainbow(word, "privmsg"))

hexchat.hook_command("r", rainbow, help="/r (text)")
hexchat.hook_command("rme", rainbowme, help="/rme (text)")
hexchat.hook_command("rmsg", rainbowmsg, help="/rmsg (user) (text)")
hexchat.hook_command("rnotice", rainbownotice, help="/rnotice (user) (text)")
print("{0} module version {1} by {2} loaded.".format(__module_name__, __module_version__, __module_author__))
