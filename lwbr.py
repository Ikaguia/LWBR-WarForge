from compiler import *

mod_version	= 2000 #2.000
debug_mode	= 0 #add debug messages ingame
edit_scenes = 0 #replace custom battle with edit scenes menu


native = -1 #mod version
wt_event_limit = 30 #how many weather events can be run per second



#used for item packs selection
packages = {'full': 0}
packs = ('Native','WarForge','Arena','Peasant','Event','Event2')
for pack in packs:
	packages[pack] = 1 << (len(packages)-1)
	packages['full'] += packages[pack]
for pack in packs:
	packages['-'+pack] = packages['full'] ^ packages[pack]

#used to select all players that match all restrictions that are set
#i.e: "Admin|WarForge" will select all admins that are using this mod)
player_types = {
	"Any"		: 0,
	"Admin"		: 1,
	"NotAdmin"	: 2,
	"NotServer"	: 4,
	"Native"	: 8,
	"WarForge"	: 16,
}
player_types["All"]			= player_types["Any"]
player_types["-Admin"]		= player_types["NotAdmin"]
player_types["-Server"]		= player_types["NotServer"]
player_types["-WarForge"]	= player_types["Native"]
player_types["-Native"]		= player_types["WarForge"]
def player_filter(filters):
	filters = filters.split("|")
	val = 0
	for f in filters:
		f = f.replace(" ","")
		# print "val = ",val
		# print "player_types[f] = ",player_types[f]
		val |= player_types[f]
	return val


multiplayer_event_server			= 125
multiplayer_event_client			= 126
multiplayer_event_server_str		= 127
multiplayer_event_client_str		= 49 #128 is invalid

sync_to_cl = 1
sync_to_sv = 2

verbose = 0
silent = 1

msg_troops_begin = trp.trainer_1
msg_string_begin = s.sv_msg_1
msg_cnt_max = 30

class _action:#player action
	count = 0
	def __init__(self,script,cd=0,hk=-1,adm=False):
		self.id = _action.count
		self.cd = cd
		self.hk = hk
		self.adm = adm
		self.script = script
		_action.count += 1
actions = {
	"taunt":		_action(script.lwbr_action_taunt,		cd=3,hk=key_comma),
	"cheer":		_action(script.lwbr_action_cheer,		cd=6,hk=key_period),
	"jumphorse":	_action(script.lwbr_action_jumphorse,	cd=5,hk=key_k),
	"msg_to_adm":	_action(script.lwbr_action_msg_to_adm,	cd=5,hk=key_back_space),
	"msg_from_adm":	_action(script.lwbr_action_msg_from_adm,cd=5,hk=key_u,adm=True),
	"kdown":		_action(script.lwbr_action_kdown,		cd=5,hk=key_delete,adm=True),
	}

class sv_event:#events that run on the server
	start = 0
	end = start + 4

	set_sv_var,ask_sv_var,return_var,\
	action = xrange(start,end)
class cl_event:#events that run on the client
	start = 0
	end = start + 15

	set_var,ask_var,return_sv_var,\
	set_faction_slot,set_item_slot,set_party_slot,set_pt_slot,set_quest_slot,set_sp_slot,\
	set_scene_slot,set_team_slot,set_agent_slot,set_troop_slot,set_player_slot,\
	clear_items = xrange(start,end)
class str_event:#options on sending strings
	start = 0
	end = start + 1

	set_troop_name, = xrange(start,end)

class _var:
	count = {
		"cl": 0,
		"sv": 0,
	}
	def __init__(self,typ,deff=None,deff_sv=None,sync=False,reset=True):
		if not _var.count.has_key(typ):
			print "Error: count not set for event type",typ
			exit(1)
		self.id = _var.count[typ]
		self.deff = deff
		self.deff_sv = deff_sv
		self.sync = sync
		self.reset = reset
		_var.count[typ] += 1
cl_vars = {#personal settings
	"version":			_var("cl",deff=mod_version,reset=False),
	"dmg_report":		_var("cl",deff=0,reset=False),
	"keep_items":		_var("cl",deff=1,reset=False),

	"nxt_scn_info":		_var("cl",deff=0), #next scene to receive info from server
	"msg_edit":			_var("cl",deff=1), #id of msg being edited

	"str_sending1":		_var("cl",deff=-1),
	"str_sending2":		_var("cl",deff=-1),
	"str_sending3":		_var("cl",deff=-1),
	"str_sending4":		_var("cl",deff=-1),
	"str_receiving1":	_var("cl",deff=-1),
	"str_receiving2":	_var("cl",deff=-1),
	"str_receiving3":	_var("cl",deff=-1),
	"str_receiving4":	_var("cl",deff=-1),
	}
sv_vars = {#settings of the server
	"items":			_var("sv",deff=packages["Native"],deff_sv=packages["Native"]|packages["WarForge"],sync=True),
	"version": 			_var("sv",deff=native,deff_sv=mod_version,sync=True),
	"firearms_en":		_var("sv",deff=0,deff_sv=0,sync=True),
	"horses_en":		_var("sv",deff=1,deff_sv=1,sync=True),
	"peasants_en":		_var("sv",deff=0,deff_sv=0,sync=True),
	"persistant_stats":	_var("sv",deff=0,deff_sv=0,sync=True),
	"horse_jump":		_var("sv",deff=0,deff_sv=1,sync=True),
	"taunt":			_var("sv",deff=0,deff_sv=1,sync=True),
	"cheer":			_var("sv",deff=0,deff_sv=1,sync=True),
	"free_wpn":			_var("sv",deff=1,deff_sv=1,sync=True),
	"min_version":		_var("sv",deff=native,deff_sv=native,sync=True),
	"msg_cd":			_var("sv",deff=-1,deff_sv=120,sync=True), #cooldown in seconds
	"msg_cnt":			_var("sv",deff=0,deff_sv=1,sync=True), #how many different messages
	"msg_cur_tm":		_var("sv",deff=0,deff_sv=0), #counter
	"msg_cur_id":		_var("sv",deff=0,deff_sv=0), #counter
	"t1_dmg_d":			_var("sv",deff=100,deff_sv=100,sync=True), #team 1 damage dealt
	"t1_dmg_r":			_var("sv",deff=100,deff_sv=100,sync=True), #team 1 damage received
	"t2_dmg_d":			_var("sv",deff=100,deff_sv=100,sync=True), #team 2 damage dealt
	"t2_dmg_r":			_var("sv",deff=100,deff_sv=100,sync=True), #team 2 damage received
	"weather_config":	_var("sv",deff=0,deff_sv=0,sync=True), #0 = based on map
	"time_config":		_var("sv",deff=0,deff_sv=0,sync=True), #0 = random
	"fog_config":		_var("sv",deff=0,deff_sv=0,sync=True), #0 = based on map
	}

class _slot:
	count = {
		"player": 80,
		"troop": 0,
		"scene": 0,
	}
	def __init__(self,typ,deff=None):
		self.id = _slot.count[typ]
		self.deff = deff
		_slot.count[typ] += 1
player_slots = {
	"version":			_slot("player",native),
	"nxt_scn_info":		_slot("player",-1), #unknown/native player
	"str_sending1":		_slot("player",-1), #none
	"str_sending2":		_slot("player",-1), #none
	"str_sending3":		_slot("player",-1), #none
	"str_sending4":		_slot("player",-1), #none
	"str_receiving1":	_slot("player",-1), #none
	"str_receiving2":	_slot("player",-1), #none
	"str_receiving3":	_slot("player",-1), #none
	"str_receiving4":	_slot("player",-1), #none
	}
troop_slots = {
	"sel_head":			_slot("troop",-2), #-2 for unset, -1 for none
	"sel_body":			_slot("troop",-2), #-2 for unset, -1 for none
	"sel_foot":			_slot("troop",-2), #-2 for unset, -1 for none
	"sel_hand":			_slot("troop",-2), #-2 for unset, -1 for none
	"sel_horse":		_slot("troop",-2), #-2 for unset, -1 for none
	"sel_wpn1":			_slot("troop",-2), #-2 for unset, -1 for none
	"sel_wpn2":			_slot("troop",-2), #-2 for unset, -1 for none
	"sel_wpn3":			_slot("troop",-2), #-2 for unset, -1 for none
	"sel_wpn4":			_slot("troop",-2), #-2 for unset, -1 for none
	}
scene_slots = {
	"available_dm":		_slot("scene",0),
	"available_tdm":	_slot("scene",0),
	"available_hq":		_slot("scene",0),
	"available_cf":		_slot("scene",0),
	"available_sg":		_slot("scene",0),
	"available_bt":		_slot("scene",0),
	"available_fd":		_slot("scene",0),
	"available_duel":	_slot("scene",0),
	"available_coop":	_slot("scene",0),
	#default is plains weather
	"rain_min":			_slot("scene",15),
	"rain_max":			_slot("scene",50),
	"rain_chance":		_slot("scene",40), #00-40 = 40% chance
	"snow_chance":		_slot("scene",60), #40-60 = 20% chance
	"fog_min":			_slot("scene",100),
	"fog_max":			_slot("scene",700),
	"fog_color1":		_slot("scene",0x8F8F8F),
	"fog_color2":		_slot("scene",0x8F8F8F),
	"cur_wt_typ":		_slot("scene",-1), #unset
	"cur_wt_str":		_slot("scene",-1), #unset
	"cur_wt_fgD":		_slot("scene",-1), #unset
	"cur_wt_fgC":		_slot("scene",-1), #unset
	}

scenes_opt = [
	(#common scenes
		[
			scn.multi_scene_1,
			scn.multi_scene_2,
			scn.multi_scene_4,
			scn.multi_scene_7,
			scn.multi_scene_9,
			scn.multi_scene_11,
			scn.multi_scene_12,
			scn.multi_scene_14,
			scn.multi_scene_17,
			scn.multi_scene_18,
			scn.multi_scene_19,
			scn.multi_scene_20,
		],{
			scene_slots["available_dm"].id : 0,
			scene_slots["available_tdm"].id : 0,
			scene_slots["available_bt"].id : 0,
			scene_slots["available_fd"].id : 0,
			scene_slots["available_cf"].id : 0,
			scene_slots["available_hq"].id : 0,
			scene_slots["available_duel"].id : 0,
			scene_slots["available_coop"].id : 0,
		}),
	(#random
		[
			scn.random_multi_plain_medium,
			scn.random_multi_plain_large,
			scn.random_multi_steppe_medium,
			scn.random_multi_steppe_large,
		],{
			scene_slots["available_dm"].id : 0,
			scene_slots["available_tdm"].id : 0,
			scene_slots["available_bt"].id : 0,
			scene_slots["available_cf"].id : 0,
			scene_slots["available_duel"].id : 0,
		}),
	(#not in fight and destroy
		[
			scn.multi_scene_11,
			scn.multi_scene_17,
			scn.multi_scene_18,
		],
		{scene_slots["available_fd"].id : 0}),
	(#not in coop
		[scn.multi_scene_2,],
		{scene_slots["available_coop"].id : 0}
		),
	(#random
		[
			scn.random_multi_plain_medium,
			scn.random_multi_plain_large,
			scn.random_multi_steppe_medium,
			scn.random_multi_steppe_large,
		],{
			scene_slots["available_dm"].id : 0,
			scene_slots["available_tdm"].id : 0,
			scene_slots["available_bt"].id : 0,
			scene_slots["available_cf"].id : 0,
			scene_slots["available_duel"].id : 0,
		}),
	(#desert
		[
			] + [(scn.town_1_walls      + x - 1)for x in xrange(19,23)] + [
			] + [(scn.castle_1_exterior + x - 1)for x in xrange(41,49)] + [
			] + [(scn.village_1         + x - 1)for x in xrange(91,111)] + [
			scn.lair_desert_bandits,
			scn.quick_battle_scene_2,
			scn.quick_battle_scene_4,
			scn.meeting_scene_desert,
			scn.meeting_scene_desert_forest,
			#
			scn.multi_scene_8,#Rudkhan Castle, Castle 2
			scn.multi_scene_15,#Mahdaar Castle, Castle 5
			scn.multi_scene_16,#Jameyyed Castle, Castle 6
		],{
			scene_slots["rain_min"].id		: 1,
			scene_slots["rain_max"].id		: 15,
			scene_slots["rain_chance"].id	: 3,# 3%
			scene_slots["snow_chance"].id	: 4,# 1%
			scene_slots["fog_min"].id		: 300,
			scene_slots["fog_max"].id		: 1000,
			scene_slots["fog_color1"].id	: 0xFF8400,
			scene_slots["fog_color2"].id	: 0xFF8400,
		}),
	(#desert close
		[
			] + [(scn.town_1_center      + x - 1)for x in xrange(23)] + [
			] + [(scn.town_1_castle      + x - 1)for x in xrange(23)] + [
			] + [(scn.town_1_tavern      + x - 1)for x in xrange(23)] + [
			] + [(scn.town_1_store       + x - 1)for x in xrange(23)] + [
			] + [(scn.town_1_arena       + x - 1)for x in xrange(23)] + [
			] + [(scn.town_1_prison      + x - 1)for x in xrange(23)] + [
			] + [(scn.town_1_alley       + x - 1)for x in xrange(23)] + [
			] + [(scn.castle_1_interior  + x - 1)for x in xrange(41,49)] + [
			] + [(scn.castle_1_prison    + x - 1)for x in xrange(41,49)] + [
			#
			scn.multi_scene_17,#The Arena
			scn.multi_scene_20,#Desert Town
		],{
			scene_slots["rain_min"].id		: 1,
			scene_slots["rain_max"].id		: 15,
			scene_slots["rain_chance"].id	: 3,# 3%
			scene_slots["snow_chance"].id	: 4,# 1%
			scene_slots["fog_min"].id		: 45,
			scene_slots["fog_max"].id		: 90,
			scene_slots["fog_color1"].id	: 0xFF8400,
			scene_slots["fog_color2"].id	: 0xAA2C00,
		}),
	(#steppe
		[
			] + [(scn.town_1_center     + x - 1)for x in 10,14,16,17,18] + [
			] + [(scn.town_1_castle     + x - 1)for x in 10,14,16,17,18] + [
			] + [(scn.town_1_tavern     + x - 1)for x in 10,14,16,17,18] + [
			] + [(scn.town_1_store      + x - 1)for x in 10,14,16,17,18] + [
			] + [(scn.town_1_arena      + x - 1)for x in 10,14,16,17,18] + [
			] + [(scn.town_1_prison     + x - 1)for x in 10,14,16,17,18] + [
			] + [(scn.town_1_walls      + x - 1)for x in 10,14,16,17,18] + [
			] + [(scn.town_1_alley      + x - 1)for x in 10,14,16,17,18] + [
			] + [(scn.castle_1_exterior + x - 1)for x in 1,9,10,17,38,40] + [
			] + [(scn.castle_1_interior + x - 1)for x in 1,9,10,17,38,40] + [
			] + [(scn.castle_1_prison   + x - 1)for x in 1,9,10,17,38,40] + [
			] + [(scn.village_1         + x - 1)for x in 11,12,25,28,37,40,41,42,43,44,45,52,76,88,89,90] + [
			scn.random_scene_steppe,
			scn.random_scene_steppe_forest,
			scn.quick_battle_2,
			scn.quick_battle_6,
			scn.salt_mine,
			scn.training_ground_horse_track_4,
			scn.training_ground_ranged_melee_4,
			scn.village_52,
			scn.village_76,
			scn.village_88,
			scn.village_89,
			scn.village_90,
			scn.field_2,
			scn.field_3,
			scn.field_4,
			scn.field_5,
			scn.test2,
			scn.lair_steppe_bandits,
			scn.meeting_scene_steppe,
			scn.meeting_scene_steppe_forest,
			#
			scn.multi_scene_2,#Village
			scn.random_multi_steppe_medium,#Random Steppe (Medium)
			scn.random_multi_steppe_large,#Random Steppe (Large)
		],{
			scene_slots["rain_min"].id		: 1,
			scene_slots["rain_max"].id		: 40,
			scene_slots["rain_chance"].id	: 15,# 15%
			scene_slots["snow_chance"].id	: 30,# 30%
			scene_slots["fog_min"].id		: 150,
			scene_slots["fog_max"].id		: 500,
			scene_slots["fog_color1"].id	: 0xFF8400,
			scene_slots["fog_color2"].id	: 0xFF8400,
		}),
	(#taiga
		[
			] + [scn.town_1_center     + x - 1 for x in 9,11] + [
			] + [scn.town_1_castle     + x - 1 for x in 9,11] + [
			] + [scn.town_1_tavern     + x - 1 for x in 9,11] + [
			] + [scn.town_1_store      + x - 1 for x in 9,11] + [
			] + [scn.town_1_arena      + x - 1 for x in 9,11] + [
			] + [scn.town_1_prison     + x - 1 for x in 9,11] + [
			] + [scn.town_1_walls      + x - 1 for x in 9,11] + [
			] + [scn.town_1_alley      + x - 1 for x in 9,11] + [
			] + [scn.castle_1_exterior + x - 1 for x in 7,18,19,29,39] + [
			] + [scn.castle_1_interior + x - 1 for x in 7,18,19,29,39] + [
			] + [scn.castle_1_prison   + x - 1 for x in 7,18,19,29,39] + [
			] + [scn.village_1         + x - 1 for x in 16,18,19,20,21,22,49,50,62,75,85,86] + [
			scn.lair_taiga_bandits,
			scn.meeting_scene_snow,
			scn.meeting_scene_snow_forest,
			scn.random_scene_snow,
			scn.random_scene_snow_forest,
			scn.quick_battle_3,
			scn.training_ground_horse_track_3,
			scn.training_ground_ranged_melee_3,
			#
			scn.multi_scene_9,#Snowy Village
			scn.multi_scene_14,#Battle on Ice
			scn.multi_scene_21,#Cold Coast
		],{
			scene_slots["rain_min"].id		: 15,
			scene_slots["rain_max"].id		: 50,
			scene_slots["rain_chance"].id	: 5,  #  5%
			scene_slots["snow_chance"].id	: 100,# 95%
			scene_slots["fog_min"].id		: 150,
			scene_slots["fog_max"].id		: 500,
			scene_slots["fog_color1"].id	: 0xFFFFFF,
			scene_slots["fog_color2"].id	: 0xFFFFFF,
		}),
	(#mountains
		[
			# ] + [scn.town_1_center     + x - 1 for x in ] + [
			# ] + [scn.town_1_castle     + x - 1 for x in ] + [
			# ] + [scn.town_1_tavern     + x - 1 for x in ] + [
			# ] + [scn.town_1_store      + x - 1 for x in ] + [
			# ] + [scn.town_1_arena      + x - 1 for x in ] + [
			# ] + [scn.town_1_prison     + x - 1 for x in ] + [
			# ] + [scn.town_1_walls      + x - 1 for x in ] + [
			# ] + [scn.town_1_alley      + x - 1 for x in ] + [
			# ] + [scn.castle_1_exterior + x - 1 for x in ] + [
			# ] + [scn.castle_1_interior + x - 1 for x in ] + [
			# ] + [scn.castle_1_prison   + x - 1 for x in ] + [
			scn.lair_mountain_bandits,
			#
			scn.multi_scene_3,#Hailes Castle, Castle 1
			scn.multi_scene_4,#Ruined Fort
			scn.multi_scene_10,#Turin Castle, Castle 3
		],{
			scene_slots["rain_min"].id		: 20,
			scene_slots["rain_max"].id		: 60,
			scene_slots["rain_chance"].id	: 15,# 15%
			scene_slots["snow_chance"].id	: 55,# 40%
			scene_slots["fog_min"].id		: 10,
			scene_slots["fog_max"].id		: 120,
			scene_slots["fog_color1"].id	: 0x8F8F8F,
			scene_slots["fog_color2"].id	: 0x8F8F8F,
		}),
	(#forest
		[
			scn.meeting_scene_plain_forest,
			scn.lair_forest_bandits,
			#
			scn.multi_scene_13,#Brunwud Castle, Castle 4
			scn.multi_scene_18,#Forest Hideout
		],{
			scene_slots["rain_min"].id		: 10,
			scene_slots["rain_max"].id		: 70,
			scene_slots["rain_chance"].id	: 35,# 35%
			scene_slots["snow_chance"].id	: 40,#  5%
			scene_slots["fog_min"].id		: 10,
			scene_slots["fog_max"].id		: 500,
			scene_slots["fog_color1"].id	: 0x8F8F8F,
			scene_slots["fog_color2"].id	: 0x8F8F8F,
		}),
	(#coast
		[
			scn.lair_sea_raiders,
			scn.four_ways_inn,
			#
			scn.multi_scene_11,#Nord Town
			scn.multi_scene_12,#Port Assault
		],{
			scene_slots["rain_min"].id		: 20,
			scene_slots["rain_max"].id		: 100,
			scene_slots["rain_chance"].id	: 55,# 55%
			scene_slots["snow_chance"].id	: 60,#  5%
			scene_slots["fog_min"].id		: 0,
			scene_slots["fog_max"].id		: 250,
			scene_slots["fog_color1"].id	: 0x9798AB,
			scene_slots["fog_color2"].id	: 0x9798AB,
		}),
]


def debug(block = []):
	if debug_mode == 0: return []
	return block

def debug_func(func_name="script_name", args=[]):
	if debug_mode == 0: return []
	block = [(str_store_string, s42, "@running script %s" % func_name),]
	if len(args) > 0:
		block += [(str_store_string, s42, "@{s42} with args"),]
		for argi in xrange(len(args)):
			block += [
				(assign, reg0, args[argi]),
				(str_store_string, s42, "@{s42} {reg0}"),
			]
	return block + [(display_message, s42),]

def cl_version(block = []):
	if IS_CLIENT: return block
	else: return []

def sv_version(block = []):
	if IS_SERVER: return block
	else: return []

