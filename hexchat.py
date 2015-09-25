"""
Ignore this file.

It's just part of the testing script.

This doesn't do nothing that you might want. :P
"""

def hook_command(name, function, help):
    function(help.split(" "), [help, help.split(" ")[1]], None)
    
def command(command):
    split = command.split(" ")
    if split[0] == "say":
        print("<testuser> {0}".format(command.replace(split[0] + " ", "")))
    elif split[0] == "me":
        print("* testuser {0}".format(command.replace(split[0] + " ", "")))
    elif split[0] == "msg" or split[0] == "privmsg":
        print(">{0}< {1}".format(split[1], command.replace(split[0] + " ", "").replace(split[1] + " ", "")))
    elif split[0] == "notice":
        print("->{0}<- {1}".format(split[1], command.replace(split[0] + " ", "").replace(split[1] + " ", "")))
