import sys,os

# print "Write module file name:"
# sys.stdout.flush()
# file = raw_input()

files = [
	"animations",
	"constants",
	"dialogs",
	"factions",
	"game_menus",
	"info_pages",
	"items",
	"map_icons",
	"meshes",
	"mission_templates",
	"music",
	"particle_systems",
	"parties",
	"party_templates",
	"postfx",
	"presentations",
	"quests",
	"scene_props",
	"scenes",
	"scripts",
	"simple_triggers",
	"skills",
	"skins",
	"sounds",
	"strings",
	"tableau_materials",
	"triggers",
	"troops",
	"ui_strings",
]

for file in files:
	print "fixing",file,"..."
	sys.stdout.flush()
	with open("module_" + file + ".py",'r') as inputF:
		with open("module_" + file + '_new.py','w') as outputF:
			inStr = False
			ident_level  = 0
			#lastLine = None
			for iLine in inputF:
				wasInStr = inStr
				iLine = iLine.lstrip().rstrip()
				oLine = iLine

				#if iLine == "" and lastLine == "": continue

				comment = len(iLine)+1
				open_level = 0
				close_level = 0
				for i in xrange(len(iLine)):
					c = iLine[i]
					if c == '"': inStr = not inStr
					if not inStr:
						if c == '#':
							comment = i
							break
						if c in ['[','(','{']: open_level += 1
						if c in [']',')','}']: close_level += 1

				iLine = iLine[:comment]

				for pattern in ["else_try","try_end","end_try"]:
					ident_level -= iLine.count(pattern)

				if not wasInStr:
					for _ in xrange(ident_level): oLine = "\t" + oLine

				for pattern in ["try_begin","try_for_range","try_for_parties","try_for_agents","try_for_prop_instances","try_for_players","else_try"]:
					ident_level += iLine.count(pattern)
				if iLine.startswith("def "):
					ident_level += 1
				if iLine.startswith("return "):
					ident_level -= 1

				ident_level += open_level
				ident_level -= close_level

				oLine += "\n"

				outputF.write(oLine)
			outputF.close()
		inputF.close()
	os.system("rm module_" + file + ".py")
	os.system("mv module_" + file + "_new.py module_" + file + ".py")
print "\ndone"
