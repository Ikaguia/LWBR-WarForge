from compiler import *

mod_version	= 2000 #2.000
debug_mode	= 0
edit_scenes = 1


packages = {'full': 0}
packs = ('Native','WarForge','Arena','Peasant','Event','Event2')
for pack in packs:
	packages[pack] = 1 << (len(packages)-1)
	packages['full'] += packages[pack]
for pack in packs: packages['-'+pack] = packages['full'] ^ packages[pack]


multiplayer_event_server			= 200
multiplayer_event_client			= 201


class sv_event:#events that run on the server
	start,end = 2000,2005

	set_sv_var,ask_sv_var,return_var,\
	action,\
	count = xrange(start,end)
class cl_event:#events that run on the client
	start,end = 3000,3016

	set_var,ask_var,return_sv_var,\
	set_faction_slot,set_item_slot,set_party_slot,set_pt_slot,set_quest_slot,set_sp_slot,\
	set_scene_slot,set_team_slot,set_agent_slot,set_troop_slot,set_player_slot,\
	clear_items,\
	count = xrange(start,end)
class var:#personal settings
	version,dmg_report,keep_items,count = xrange(4)
	default = {
		version : mod_version,
		dmg_report : 0,
		keep_items : 1,
	}
class sv_var:#settings of the server
	items,version,firearms_en,horses_en,peasants_en,persistant_stats,\
	horse_jump,taunt,cheer,free_wpn,min_version,msg_cd,\
	t1_dmg_r,t1_dmg_d,t2_dmg_r,t2_dmg_d,weather_config,time_config,fog_config,\
	cur_wt_typ,cur_wt_str,cur_wt_fog,cur_wt_tim,count = xrange(24)
	default = {
		#assume the server is Native at start
		items: packages["Native"],
		version: 0,
		firearms_en: 0,
		horses_en: 1,
		peasants_en: 0,
		persistant_stats: 0,
		horse_jump: 0,
		taunt: 0,
		cheer: 0,
		free_wpn: 0,
		min_version: -1,
		msg_cd: -1,
		t1_dmg_d: 100,
		t1_dmg_r: 100,
		t2_dmg_d: 100,
		t2_dmg_r: 100,
		weather_config: 0,
		time_config: 0,
		fog_config: 0,
		cur_wt_typ: -1,
		cur_wt_str: -1,
		cur_wt_fog: -1,
		cur_wt_tim: -1,
	}
	default_sv = {
		items: packages["Native"] | packages["WarForge"],
		# items: packages["Peasant"],
		version: mod_version,
		firearms_en: 0,
		horses_en: 1,
		peasants_en: 0,
		persistant_stats: 0,
		horse_jump: 1,
		taunt: 1,
		cheer: 1,
		free_wpn: 0,
		min_version: -1,#-1 for none
		msg_cd: 120,#in seconds
		t1_dmg_d: 100,
		t1_dmg_r: 100,
		t2_dmg_d: 100,
		t2_dmg_r: 100,
		weather_config: 0,#based on map
		time_config: 0,#random
		fog_config: 0,#based on map
		cur_wt_typ: -1,#unitialized
		cur_wt_str: -1,#unitialized
		cur_wt_fog: -1,#unitialized
		cur_wt_tim: -1,#unitialized
	}

class slot_player:
	start = 80
	version,count = xrange(start,start+2)
	default = {
		version: 0,#0 for native
	}
class slot_troop:
	start = 0
	sel_head,sel_body,sel_foot,sel_hand,sel_horse,sel_wpn1,sel_wpn2,sel_wpn3,sel_wpn4,count = xrange(start,start+10)
	default = {
		sel_head: -2,#-2 for unknown, -1 for none
		sel_body: -2,#-2 for unknown, -1 for none
		sel_foot: -2,#-2 for unknown, -1 for none
		sel_hand: -2,#-2 for unknown, -1 for none
		sel_horse: -2,#-2 for unknown, -1 for none
		sel_wpn1: -2,#-2 for unknown, -1 for none
		sel_wpn2: -2,#-2 for unknown, -1 for none
		sel_wpn3: -2,#-2 for unknown, -1 for none
		sel_wpn4: -2,#-2 for unknown, -1 for none
	}
class slot_scene:
	start = 0
	available_dm,available_tdm,available_hq,available_cf,available_sg,available_bt,available_fd,available_duel,available_coop,\
	rain_min,rain_max,\
	rain_chance,snow_chance,\
	fog_min,fog_max,fog_color,\
	count = xrange(start,start+17)
	default = {
		available_dm : 0,
		available_tdm : 0,
		available_bt : 0,
		available_fd : 0,
		available_cf : 0,
		available_hq : 0,
		available_sg : 0,
		available_duel : 0,
		available_coop : 0,
		#default is plains weather
		rain_min : 15,
		rain_max : 50,
		rain_chance : 40,#00-40 = 40% chance
		snow_chance : 60,#40-60 = 20% chance
		fog_min : 100,
		fog_max : 700,
		fog_color : 0x8F8F8F
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
			slot_scene.available_dm : 0,
			slot_scene.available_tdm : 0,
			slot_scene.available_bt : 0,
			slot_scene.available_fd : 0,
			slot_scene.available_cf : 0,
			slot_scene.available_hq : 0,
			slot_scene.available_duel : 0,
			slot_scene.available_coop : 0,
		}),
	(#random
		[
			scn.random_multi_plain_medium,
			scn.random_multi_plain_large,
			scn.random_multi_steppe_medium,
			scn.random_multi_steppe_large,
		],{
			slot_scene.available_dm : 0,
			slot_scene.available_tdm : 0,
			slot_scene.available_bt : 0,
			slot_scene.available_cf : 0,
			slot_scene.available_duel : 0,
		}),
	(#not in fight and destroy
		[
			scn.multi_scene_11,
			scn.multi_scene_17,
			scn.multi_scene_18,
		],
		{slot_scene.available_fd : 0}),
	(#not in coop
		[scn.multi_scene_2,],
		{slot_scene.available_coop : 0}
		),
	(#random
		[
			scn.random_multi_plain_medium,
			scn.random_multi_plain_large,
			scn.random_multi_steppe_medium,
			scn.random_multi_steppe_large,
		],{
			slot_scene.available_dm : 0,
			slot_scene.available_tdm : 0,
			slot_scene.available_bt : 0,
			slot_scene.available_cf : 0,
			slot_scene.available_duel : 0,
		}),
	(#desert
		[
			] + ["scn_town_%d_center"%x for x in xrange(19,23)] + [
			] + ["scn_town_%d_castle"%x for x in xrange(19,23)] + [
			] + ["scn_town_%d_tavern"%x for x in xrange(19,23)] + [
			] + ["scn_town_%d_store"%x for x in xrange(19,23)] + [
			] + ["scn_town_%d_arena"%x for x in xrange(19,23)] + [
			] + ["scn_town_%d_prison"%x for x in xrange(19,23)] + [
			] + ["scn_town_%d_walls"%x for x in xrange(19,23)] + [
			] + ["scn_town_%d_alley"%x for x in xrange(19,23)] + [
			] + ["scn_castle_%d_exterior"%x for x in xrange(41,49)] + [
			] + ["scn_castle_%d_interior"%x for x in xrange(41,49)] + [
			] + ["scn_castle_%d_prison"%x for x in xrange(41,49)] + [
			] + ["scn_village_%d"%x for x in xrange(91,111)] + [
			scn.multi_scene_15,
			scn.multi_scene_16,
			scn.multi_scene_20,
			scn.lair_desert_bandits,
			scn.quick_battle_scene_2,
			scn.quick_battle_scene_4,
			scn.meeting_scene_desert,
			scn.meeting_scene_desert_forest,
			#
			#scn.lwbr_multi_16,
			#scn.lwbr_new_de_dust,
			#scn.lwbr_new_2desert,
			#scn.lwbr_new_,
			#
			scn.enterprise_linen_weavery,#lwbr_multi_random_desert_small
			scn.enterprise_wool_weavery,#lwbr_multi_random_desert_medium
			scn.enterprise_brewery,#lwbr_multi_random_desert_large
		],{
			slot_scene.rain_min		: 1,
			slot_scene.rain_max		: 15,
			slot_scene.rain_chance	: 3,# 3%
			slot_scene.snow_chance	: 4,# 1%
			slot_scene.fog_min		: 300,
			slot_scene.fog_max		: 1000,
			slot_scene.fog_color	: 0xFF8400,
		}),
	(#steppe
		[
			] + ["scn_town_%d_center"%x for x in 10,14,16,17,18] + [
			] + ["scn_town_%d_castle"%x for x in 10,14,16,17,18] + [
			] + ["scn_town_%d_tavern"%x for x in 10,14,16,17,18] + [
			] + ["scn_town_%d_store"%x for x in 10,14,16,17,18] + [
			] + ["scn_town_%d_arena"%x for x in 10,14,16,17,18] + [
			] + ["scn_town_%d_prison"%x for x in 10,14,16,17,18] + [
			] + ["scn_town_%d_walls"%x for x in 10,14,16,17,18] + [
			] + ["scn_town_%d_alley"%x for x in 10,14,16,17,18] + [
			] + ["scn_castle_%d_exterior"%x for x in 1,9,10,17,38,40] + [
			] + ["scn_castle_%d_interior"%x for x in 1,9,10,17,38,40] + [
			] + ["scn_castle_%d_prison"%x for x in 1,9,10,17,38,40] + [
			] + ["scn_village_%d"%x for x in 11,12,25,28,37,40,41,42,43,44,45,52,76,88,89,90] + [
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
			# #new maps begin
			# scn.lwbr_new_combat_sur_glace_advenced,
			# scn.lwbr_new_tharlak_fortress,
			# #new maps end
			scn.multi_scene_2,
			scn.random_multi_steppe_medium,
			scn.random_multi_steppe_large,
			scn.lair_steppe_bandits,
			scn.meeting_scene_steppe,
			scn.meeting_scene_steppe_forest,
			scn.enterprise_winery,#lwbr_multi_random_steppe_small
		],{
			slot_scene.rain_min		: 1,
			slot_scene.rain_max		: 40,
			slot_scene.rain_chance	: 15,# 15%
			slot_scene.snow_chance	: 30,# 30%
			slot_scene.fog_min		: 150,
			slot_scene.fog_max		: 500,
			slot_scene.fog_color	: 0xFF8400,
		}),
	(#taiga
		[
			] + ["scn_town_%d_center"%x for x in 9,11] + [
			] + ["scn_town_%d_castle"%x for x in 9,11] + [
			] + ["scn_town_%d_tavern"%x for x in 9,11] + [
			] + ["scn_town_%d_store"%x for x in 9,11] + [
			] + ["scn_town_%d_arena"%x for x in 9,11] + [
			] + ["scn_town_%d_prison"%x for x in 9,11] + [
			] + ["scn_town_%d_walls"%x for x in 9,11] + [
			] + ["scn_town_%d_alley"%x for x in 9,11] + [
			] + ["scn_castle_%d_exterior"%x for x in 7,18,19,29,39] + [
			] + ["scn_castle_%d_interior"%x for x in 7,18,19,29,39] + [
			] + ["scn_castle_%d_prison"%x for x in 7,18,19,29,39] + [
			] + ["scn_village_%d"%x for x in 16,18,19,20,21,22,49,50,62,75,85,86] + [
			scn.multi_scene_9,
			scn.multi_scene_14,
			scn.lair_taiga_bandits,
			scn.meeting_scene_snow,
			scn.meeting_scene_snow_forest,
			scn.random_scene_snow,
			scn.random_scene_snow_forest,
			scn.quick_battle_3,
			scn.training_ground_horse_track_3,
			scn.training_ground_ranged_melee_3,
			scn.multi_scene_9,
			scn.multi_scene_14,
			#
			# scn.lwbr_multi_29,
			# scn.lwbr_new_combat_sur_glace_advenced,
			# scn.lwbr_new_snow_fight,
			# scn.lwbr_new_ice_age,
			# scn.lwbr_new_,
			#
			scn.enterprise_mill,#lwbr_multi_random_snow_small
			scn.enterprise_smithy,#lwbr_multi_random_snow_medium
			scn.enterprise_dyeworks,#lwbr_multi_random_snow_large
		],{
			slot_scene.rain_min		: 15,
			slot_scene.rain_max		: 50,
			slot_scene.rain_chance	: 5,  #  5%
			slot_scene.snow_chance	: 100,# 95%
			slot_scene.fog_min		: 150,
			slot_scene.fog_max		: 500,
			slot_scene.fog_color	: 0xFFFFFF,
		}),
	(#mountains
		[
			# ] + ["scn_town_%d_center"%x for x in ] + [
			# ] + ["scn_town_%d_castle"%x for x in ] + [
			# ] + ["scn_town_%d_tavern"%x for x in ] + [
			# ] + ["scn_town_%d_store"%x for x in ] + [
			# ] + ["scn_town_%d_arena"%x for x in ] + [
			# ] + ["scn_town_%d_prison"%x for x in ] + [
			# ] + ["scn_town_%d_walls"%x for x in ] + [
			# ] + ["scn_town_%d_alley"%x for x in ] + [
			# ] + ["scn_castle_%d_exterior"%x for x in ] + [
			# ] + ["scn_castle_%d_interior"%x for x in ] + [
			# ] + ["scn_castle_%d_prison"%x for x in ] + [
			scn.multi_scene_4,
			#
			# scn.lwbr_new_tharlak_fortress,
			# scn.lwbr_new_land_of_conflict,
			# scn.lwbr_multi_7,
			# scn.lwbr_multi_11,
			# scn.lwbr_new_sky_castle,
			# scn.lwbr_new_,
			#
			scn.lair_mountain_bandits,
		],{
			slot_scene.rain_min		: 20,
			slot_scene.rain_max		: 60,
			slot_scene.rain_chance	: 15,# 15%
			slot_scene.snow_chance	: 55,# 40%
			slot_scene.fog_min		: 10,
			slot_scene.fog_max		: 120,
			slot_scene.fog_color	: 0x8F8F8F,
		}),
	(#forest
		[
		scn.meeting_scene_plain_forest,
		scn.lair_forest_bandits,
		#
		# scn.lwbr_multi_12,
		# scn.lwbr_multi_24,
		# scn.lwbr_multi_25,
		# scn.lwbr_multi_30,
		# scn.lwbr_multi_32,
		# scn.lwbr_new_,
		#
		scn.multi_scene_18,
		],{
			slot_scene.rain_min		: 10,
			slot_scene.rain_max		: 70,
			slot_scene.rain_chance	: 35,# 35%
			slot_scene.snow_chance	: 40,#  5%
			slot_scene.fog_min		: 10,
			slot_scene.fog_max		: 500,
			slot_scene.fog_color	: 0x8F8F8F,
		}),
	(#coast
		[
			scn.multi_scene_12,
			scn.lair_sea_raiders,
			scn.four_ways_inn,
			#
			# scn.lwbr_multi_8,
			# scn.lwbr_multi_21,
			# scn.lwbr_new_sea,
			# scn.lwbr_new_sea_battle,
			# scn.lwbr_new_desert_isle,
			# scn.lwbr_new_cutthroat_isle,
			# scn.lwbr_new_,
			#
		],{
			slot_scene.rain_min		: 20,
			slot_scene.rain_max		: 100,
			slot_scene.rain_chance	: 55,# 55%
			slot_scene.snow_chance	: 60,#  5%
			slot_scene.fog_min		: 0,
			slot_scene.fog_max		: 250,
			slot_scene.fog_color	: 0x9798AB,
		}),
]
