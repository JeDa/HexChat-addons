"""
This script tests the addons.

You ***SHOULDN'T*** load this on your HexChat. :)
"""

if __name__ == "__main__":
    import os
    import sys
    import pytest
    returnlist = []
    for val in os.listdir("addons"):
        returnlist.append(pytest.main(["addons/{0}".format(val), "-s", '--tb', 'native']))
    if 1 in returnlist:
        print("There's a broken addon.")
        sys.exit(1)
    else:
        print("All is fine. :)")
        sys.exit(0)
