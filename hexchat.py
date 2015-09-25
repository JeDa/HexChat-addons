"""
This script tests the addons.

You *SHOULDN'T* load this on your HexChat. :)
"""

if __name__ == "__main__":
    import os
    import sys
    broken = 0
    print("HexChat addons test script.")
    print("There might been shown weird stuff. Don't worry. :)\n")
    for val in os.listdir("addons"):
        val = val.replace(".py", "")
        print("Testing {0}".format(val))
        try:
            __import__('addons.{0}'.format(val), globals=globals())
            print("{0} is WORKING.".format(val))
        except Exception as err:
            print("{0} is FAILING. ({1})".format(val, err))
            broken = 1
    if broken == 1:
        print("\nThere's broken addons. :(")
        sys.exit(1)
    else:
        print("\nAll is fine. :)")
        sys.exit(0)

def hook_command(name, function, help):
    function(help.split(" "), [help, help.split(" ")[1]], None)
    
def command(command):
    split = command.replace("\x034", "").split(" ")
    if split[0] == "say":
        print("<testuser> {0}".format(command.replace(split[0] + " ", "")))
    elif split[0] == "me":
        print("* testuser {0}".format(command.replace(split[0] + " ", "")))
    elif split[0] == "msg" or split[0] == "privmsg":
        print(">{0}< {1}".format(split[1], command.replace(split[0] + " ", "").replace(split[1] + " ", "")))
    elif split[0] == "notice":
        print("->{0}<- {1}".format(split[1], command.replace(split[0] + " ", "").replace(split[1] + " ", "")))

