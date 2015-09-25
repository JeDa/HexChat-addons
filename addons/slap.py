# -*- coding: utf-8 -*-
import hexchat
import random

__module_name__ = 'Slap'
__module_version__ = '1.0.0'
__module_description__ = 'Slaps people.'
__module_author__ = 'JeDa (based off Frankity\'s code)'

def slap_cb(word, word_eol, userdata):
  actions = ["slaps", "whacks", "ˢᵉʳᶦᵒᵘˢ ᵗʳᵒᵘᵇᶫᵉs", "eats", "Timsons", "13r12a11i10n9b8o7w ᵗʳᵒᵘᵇᶫᵉs"]
  modifiers = [" around a bit", " around a lot", ""]
  items = ["your hero", "Apple", "Donald Trump's combover", "Lizard's food", "a MobiusLizard4", "Tintle", "MJ94's brain", "fish's food", "a dead forum", "NetOpsBot's trout", "1a 2r3a4i5n6b7o8w 9s10h11i12t", "JeDa's laptop", "your ass", "X-Chat v0.1 beta", "LuminolBlue's cat", "Wikipedia trolls", "a Beancounter's broken line", "a cursed [-1] Aperture Science Weighted Companion Cube", "a Sagittarius A*, the black hole at the center of the galaxy, with a talking Aperture Science Weighted Companion Cube", "an atomic diamond hoe", "an atomic whale", "Donald Trump's cursed [-1] combover", "a wolf", "a Werewolf's 15-player failgame", "a bridge with a cursed [-1] whale", "a feisty rolled-up comic", "a quantum fish", "Python", "a bug", "a SlowLizard8", "Java", "Cloudflare", "a large fishbot", "a OVH's VPS", "a GitHub empty repo", "Avast! Antivirus", "a bot", "the life without HexChat"]
  if len(word) > 1:
    hexchat.command('me {0} {1}{2} with {3}'.format(random.choice(actions), word[1], random.choice(modifiers), random.choice(items)))
  else:
    hexchat.command('help slap')

hexchat.hook_command('slap', slap_cb, help='/slap <nick>')
print("{0} module version {1} by {2} loaded.".format(__module_name__, __module_version__, __module_author__))
