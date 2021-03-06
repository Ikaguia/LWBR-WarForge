from compiler import *
register_plugin(__name__)

from plugin_make_presentations import make_presentation,typ



def foo__lwbr_menu():
	def foo__sv_var(slot,load = [],change = []):
		slot = lwbr.sv_vars[slot].id
		load = [ (get_lwbr_sv_var, l.val, slot), ] + load
		change  = [ (get_lwbr_sv_var, l.val_old, slot), (eq, l.val_old, l.val_old), ] + change
		change += [ (set_lwbr_sv_var, slot, l.val, lwbr.sync_to_sv), ]
		return (load,change)
	def foo__cl_var(slot,load = [],change = []):
		slot = lwbr.cl_vars[slot].id
		load = [ (get_lwbr_var, l.val, slot), ] + load
		change  = [ (get_lwbr_var, l.val_old, slot), (eq, l.val_old, l.val_old), ] + change
		change += [ (set_lwbr_var, slot, l.val), ]
		return (load,change)
	is_wf = [(neg|troop_slot_eq,  trp.lwbr_sv_vars, lwbr.sv_vars["version"].id, lwbr.native),]
	is_nat = [(troop_slot_eq,  trp.lwbr_sv_vars, lwbr.sv_vars["version"].id, lwbr.native),]
	is_adm = [(multiplayer_get_my_player, l.player),(player_is_admin, l.player),]
	is_adm_wf = is_wf + is_adm
	lwbr_menu_list = [
		(typ.text,"LWBR WarForge menu v%.3f"%(lwbr.mod_version/1000),[]),
		(typ.blank,),
		(typ.text,"Server is not running LWBR WarForge",is_nat),
		(typ.text,"Server is running LWBR WarForge v{reg0}.{reg1}{reg2}{reg3}",is_wf + [
				(get_lwbr_sv_var, l.version, "version"),
				(store_mod, reg3, l.version, 10),
				(val_div, l.version, 10),
				(store_mod, reg2, l.version, 10),
				(val_div, l.version, 10),
				(store_mod, reg1, l.version, 10),
				(store_div, reg0, l.version, 10),
				]),
		(typ.open_container,400,350),
		# (typ.checkbox,"Dmg report:") + foo__cl_var("dmg_report"),
		# (typ.checkbox,"Keep selected items:") + foo__cl_var("keep_items"),
		# (typ.button,"Set Hotkeys",is_wf,[
				# (presentation_set_duration, 0),
				# (start_presentation,prsnt.lwbr_set_hotkeys),
				# ]),
		(typ.code,[(try_begin),]+is_adm_wf),
		(typ.blank,),
		# (typ.text,"Admin options:",[]),
		# (typ.button,"Admin Text",[],[
				# (presentation_set_duration, 0),
				# (start_presentation,prsnt.lwbr_admin_chat),
				# ]),
		# (typ.button,"Admin Cheats",[],[
				# (presentation_set_duration, 0),
				# (start_presentation,prsnt.lwbr_admin_cheats),
				# ]),
		# (typ.button,"Customize Maplist",[],[
				# (presentation_set_duration, 0),
				# (start_presentation,prsnt.lwbr_customize_maplist),
				# ]),
		# (typ.checkbox,"Firearms:") + foo__sv_var("firearms_en"),
		# (typ.checkbox,"Horses:") + foo__sv_var("horses_en"),
		# (typ.checkbox,"Peasants:") + foo__sv_var("peasants_en"),
		# (typ.checkbox,"Persistant Stats:") + foo__sv_var("persistant_stats"),
		# (typ.checkbox,"Jump from horse:") + foo__sv_var("horse_jump"),
		# (typ.checkbox,"Taunting:") + foo__sv_var("taunt"),
		# (typ.checkbox,"Cheering:") + foo__sv_var("cheer"),
		# (typ.checkbox,"Only one FREE weapon:") + foo__sv_var("free_wpn"),
		(typ.numbox,"Min Version required:") + foo__sv_var("min_version") + (lwbr.native,lwbr.mod_version+1),
		(typ.numbox,"Messages interval(seconds):") + foo__sv_var("msg_cd") + (1,1001),
		(-typ.numbox,"Messages count:") + foo__sv_var("msg_cnt") + (0,lwbr.msg_cnt_max+1),
		(-typ.numbox,"Editting Message:") + foo__cl_var("msg_edit",[
				(get_lwbr_sv_var, l.max, "msg_cnt"),
				(ge, l.max, 2),
				]) + (1,l.max+1),
		(typ.textbox,"Message #{reg0}:",[
				(get_lwbr_sv_var, l.cnt, "msg_cnt"),
				(ge, l.cnt, 1),
				(get_lwbr_var, l.cnt, "msg_edit"),
				(assign, reg0, l.cnt),
				(str_store_troop_name, s0, lwbr.msg_troops_begin+l.cnt-1),
				],[
				(get_lwbr_var, l.cnt, "msg_edit"),
				(store_add, l.trp, lwbr.msg_troops_begin-1, l.cnt),
				(troop_set_name, l.trp, s0),
				(send_str_to_server, "@{s0}", lwbr.str_event.set_troop_name, l.trp, 0, 0, lwbr.silent),
				]),
		# (typ.numbox,"Team 1 damage received(%):") + foo__sv_var("t1_dmg_r") + (0,1001),
		# (typ.numbox,"Team 1 damage dealt(%):") + foo__sv_var("t1_dmg_d") + (0,1001),
		# (typ.numbox,"Team 2 damage received(%):") + foo__sv_var("t2_dmg_r") + (0,1001),
		# (typ.numbox,"Team 2 damage dealt(%):") + foo__sv_var("t2_dmg_d") + (0,1001),
		(-typ.combo_button,"Custom Game Mode:") + foo__sv_var("game_mode") + ([gm for gm in lwbr.game_modes],),
		]
	for packi in xrange(len(lwbr.packs)):
		pack = lwbr.packs[packi]
		lo = [
			(get_lwbr_sv_var, l.gm, "game_mode"),
			(eq, l.gm, lwbr.game_modes["native"].id),
			(val_and, l.val, lwbr.packages[pack]),
			]
		ch = [
			# (assign, reg0, l.val_old),
			(try_begin),
				(eq, l.val, 0),
				(store_and, l.val, l.val_old, lwbr.packages['-' + pack]),
				# (assign, reg1, lwbr.packages['-' + pack]),
				# (assign, reg2, l.val),
				# (display_message, "@pack %s, {reg0} & {reg1} = {reg2}" % pack),
			(else_try),
				(store_or, l.val, l.val_old, lwbr.packages[pack]),
				# (assign, reg1, lwbr.packages[pack]),
				# (assign, reg2, l.val),
				# (display_message, "@pack %s, {reg0} | {reg1} = {reg2}" % pack),
			(try_end),
			# (call_script, script.lwbr_give_items_to_troops, l.val),
			]
		lwbr_menu_list += [(typ.checkbox,pack + " Items:") + foo__sv_var("items",load = lo,change = ch),]
	lwbr_menu_list += [
		(typ.combo_button,"Weather:") + foo__sv_var("weather_config") + ([
				"Based on Map",
				"Clear Sky",
				"Rainy",
				"Snowy",
				],),
		(typ.combo_button,"Time:") + foo__sv_var("time_config") + ([
				"Random",
				"Random - No night",
				"Dawn",
				"Noon",
				"Dusk",
				"Midnight",
				],),
		(typ.combo_button,"Fog:") + foo__sv_var("fog_config") + ([
				"Based on Map",
				"None",
				"Sparse",
				"Thick",
				"Random",
				],),
		(typ.code,[(try_end),]),
		(typ.close_container,),
		(typ.button,"Done",[],[(presentation_set_duration,0)]),
		]

	return lwbr_menu_list

def foo__debug_vars():
	s_cl_vars = sorted([(lwbr.cl_vars[var].id,var) for var in lwbr.cl_vars])
	s_sv_vars = sorted([(lwbr.sv_vars[var].id,var) for var in lwbr.sv_vars])
	s_scn_slots = sorted([(lwbr.scene_slots[slot].id,slot) for slot in lwbr.scene_slots])
	return sum([[
		(get_lwbr_var, reg0, _id),
		(display_message, "@var %s = {reg0}" % name),
		] for _id,name in s_cl_vars ],[])\
	+ sum([[
		(get_lwbr_sv_var, reg0, _id),
		(display_message, "@sv var %s = {reg0}" % name),
		] for _id,name in s_sv_vars ],[])\
	+ [ (store_current_scene, l.scn), ]\
	+ sum([[
		(scene_get_slot, reg0, l.scn, _id),
		(display_message, "@scene_slot %s = {reg0}" % name),
		] for _id,name in s_scn_slots ],[])

def foo__scn_names():
	from module_scenes import scenes as _scenes
	block = []
	for scene in _scenes:
		name = scene[0]
		if lwbr.scenes_name.has_key(name):
			block += [("scn_"+name,lwbr.scenes_name[name])]
		else:
			block += [("scn_"+name,name)]
	return block


presentations = [
	make_presentation("lwbr_menu", prsntf_manual_end_only, 0, foo__lwbr_menu()),
	("lwbr_admin_cheats", prsntf_manual_end_only, 0, []),
	("lwbr_customize_maplist", prsntf_manual_end_only, 0, []),
	("lwbr_admin_chat", prsntf_manual_end_only, 0, []),
	("lwbr_set_hotkeys", prsntf_manual_end_only, 0, []),
]

scripts = [
	## INITIALIZATION ##
	#script.lwbr_server_start
	("lwbr_server_start",[
			(try_begin),
				(multiplayer_is_server),
				] + lwbr.sv_version([
					] + lwbr.debug([(display_message, "@running script lwbr_server_start"),]) + [

					(eq, g.lwbr_server_initiallized, 0),

					(call_script, script.lwbr_init_cl_vars),
					(call_script, script.lwbr_init_sv_vars),
					(call_script, script.lwbr_init_slots),
					(call_script, script.lwbr_init_hotkeys),

					(try_for_range, l.scn, 0, scn.end),
						(call_script, script.lwbr_calc_weather, l.scn),
					(try_end),

					(get_lwbr_sv_var, l.itms, "items"),
					(call_script, script.lwbr_give_items_to_troops, l.itms),

					(try_for_range, l.msg, 0, lwbr.msg_cnt_max),
						(str_store_string, s0, l.msg+lwbr.msg_string_begin),
						(troop_set_name, l.msg+lwbr.msg_troops_begin, s0),
					(try_end),

					(assign, g.lwbr_server_initiallized, 1),
				]) + [#end lwbr.sv_version
			(try_end),
			]),
	#script.lwbr_player_start
	("lwbr_player_start",[
			(try_begin),
				(neg|multiplayer_is_server),
				] + lwbr.cl_version([
					] + lwbr.debug([(display_message, "@running script lwbr_player_start"),]) + [

					(call_script, script.lwbr_init_cl_vars),
					(call_script, script.lwbr_init_sv_vars),
					(call_script, script.lwbr_init_slots),
					(call_script, script.lwbr_init_hotkeys),

					(try_for_range, l.scn, 0, scn.end),
						(call_script, script.lwbr_calc_weather, l.scn),
					(try_end),

					(get_lwbr_sv_var, l.itms, "items"),
					(call_script, script.lwbr_give_items_to_troops, l.itms),
				]) + [#end lwbr.cl_version
			(try_end),
			]),
	#script.lwbr_init_slots
	("lwbr_init_slots",[
			#players
			(try_for_players, l.pl),
				(call_script, script.lbwr_init_player, l.pl),
			(try_end),
			#troops
			(try_for_range, l.trp, 0, trp.end),
				(neq, l.trp, trp.lwbr_sv_vars),
				(neq, l.trp, trp.lwbr_vars),
				(neq, l.trp, trp.lwbr_hotkeys),
				] + [(troop_set_slot, l.trp, lwbr.troop_slots[slot].id, lwbr.troop_slots[slot].deff) for slot in lwbr.troop_slots] + [
			(try_end),
			#scenes
			(try_for_range, l.scn, 0, scn.end),
				] + [(scene_set_slot, l.scn, lwbr.scene_slots[slot].id, lwbr.scene_slots[slot].deff) for slot in lwbr.scene_slots] + [
			(try_end),
			] + sum(sum([[[(scene_set_slot, _s, _o, _os[_o]) for _o in _os] for _s in _ss] for _ss,_os in lwbr.scenes_opt],[]),[]) + [
			#items
			(try_for_range, l.itm, 0, itm.end),
				(call_script, script.lwbr_init_item, l.itm),
			(try_end),
			]),
	#script.lwbr_init_item
	("lwbr_init_item",[
			(store_script_param_1, l.item),
			(item_set_slot, l.item, slot_item_multiplayer_item_class, 0),
			(item_get_type, l.type, l.item),
			(try_begin),#1h
				(eq,l.type,itp_type_one_handed_wpn),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_cleavers),

				(item_get_thrust_damage,     l.dmg,      l.item),
				(item_get_swing_damage_type, l.dmg_type, l.item),
				(try_begin),
					(eq, l.dmg_type, blunt),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_blunt),
				(else_try),
					(gt, l.dmg, 0),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_sword),
				(else_try),
					(item_has_property, l.item, itp_bonus_against_shield),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_axe),
				(try_end),
				#multi_item_class_type_war_picks
			(else_try),#2h
				(eq,l.type,itp_type_two_handed_wpn),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
				(try_begin),
					(item_has_property, l.item, itp_bonus_against_shield),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
				(try_end),
			(else_try),#polearm
				(eq,l.type,itp_type_polearm),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_spear),
				(try_begin),
					(item_has_property, l.item, itp_bonus_against_shield),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
				# (else_try),
					# (item_has_property, l.item, itp_couchable),
					# (item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_lance),
				(try_end),
			(else_try),#shield
				(eq,l.type,itp_type_shield),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_small_shield),

				# (item_get_shield_height, l.h, l.item),
				# (try_begin),
					# (gt, l.h, 100),
					# (item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_large_shield),
				# (try_end),
			(else_try),#bow
				(eq,l.type,itp_type_bow),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_bow),
			(else_try),#xbow
				(eq,l.type,itp_type_crossbow),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_crossbow),
			(else_try),#arrow
				(eq,l.type,itp_type_arrows),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_arrow),
			(else_try),#bolt
				(eq,l.type,itp_type_bolts),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_bolt),
			(else_try),#throw
				(eq,l.type,itp_type_thrown),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_throwing),
				# (try_begin),
					# (item_has_property, l.item, itp_bonus_against_shield),
					# (item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
				# (try_end),
			(else_try),#head armor
				(eq, l.type, itp_type_head_armor),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_light_helm),

				(item_get_head_armor, l.armor, l.item),
				(try_begin),
					(gt, l.armor, 25),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_heavy_helm),
				(try_end),
			(else_try),#body armor
				(eq, l.type, itp_type_body_armor),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_light_armor),

				(item_get_body_armor, l.armor, l.item),
				(try_begin),
					(gt, l.armor, 40),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_heavy_armor),
				(else_try),
					(gt, l.armor, 25),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_medium_armor),
				(try_end),
			(else_try),#foot armor
				(eq, l.type, itp_type_foot_armor),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_light_foot),

				(item_get_leg_armor, l.armor, l.item),
				(try_begin),
					(gt, l.armor, 25),
					(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_heavy_foot),
				(try_end),
			(else_try),#hand armor
				(eq,l.type,itp_type_hand_armor),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_glove),
			(else_try),#horse
				(eq,l.type,itp_type_horse),
				(item_set_slot, l.item, slot_item_multiplayer_item_class, multi_item_class_type_horse),
			(try_end),
			]),
	#script.lbwr_init_player
	("lbwr_init_player",[
			(store_script_param_1, l.pl),
			(try_begin),
				(player_is_active, l.pl),
				] + [(player_set_slot, l.pl, lwbr.player_slots[slot].id, lwbr.player_slots[slot].deff) for slot in lwbr.player_slots] + [
			(try_end),
			]),
	#script.lwbr_init_hotkeys
	("lwbr_init_hotkeys",[
			(try_begin),
				(eq, g.lwbr_hotkeys_initialized, 0),
				] + [(set_lwbr_hotkey, lwbr.actions[action].id) for action in lwbr.actions] + [
				(assign, g.lwbr_hotkeys_initialized, 1),
			(try_end),
			]),
	#script.lwbr_ask_player_info
	("lwbr_ask_player_info",[
			] + lwbr.debug([ (display_message, "@asking info from player"), ]) + [
			] + lwbr.sv_version([
				(store_script_param, l.player, 1),
				] + [ (send_event_to_player, l.player, lwbr.multiplayer_event_client, lwbr.cl_event.ask_var, var)\
					for var in (lwbr.cl_vars["version"].id, lwbr.cl_vars["nxt_scn_info"].id) ] + [
			]) + [#end lwbr.sv_version
			]),
	#script.lwbr_send_player_info
	("lwbr_send_player_info",[
			] + lwbr.debug([ (display_message, "@sending info to player"), ]) + [
			] + lwbr.sv_version([
				(store_script_param, l.player, 1),
				] + sum([ [
						(get_lwbr_sv_var, l.val, lwbr.sv_vars[var].id),
						(send_event_to_player, l.player, lwbr.multiplayer_event_client,
							lwbr.cl_event.return_sv_var, lwbr.sv_vars[var].id, l.val, 0, "-Server", lwbr.verbose),
					] for var in lwbr.sv_vars if lwbr.sv_vars[var].sync ],[]) + [
				(store_current_scene, l.scn),
				(call_script, script.lwbr_send_scene_weather_info, l.player, l.scn),
			]) + [#end lwbr.sv_version
			]),

	## SEND EVENTS TO SV/PLAYER ##
	#script.cf_lwbr_filter_player
	("cf_lwbr_filter_player",[
			(store_script_param, l.player, 1),
			(store_script_param, l.filter, 2),
			#player is active
			(player_is_active, l.player),
			#player is admin
			(store_and, l.req, l.filter, lwbr.player_filter("Admin")),
			(this_or_next|eq, l.req, 0),
			(player_is_admin, l.player),
			#player is not admin
			(store_and, l.req, l.filter, lwbr.player_filter("-Admin")),
			(this_or_next|eq, l.req, 0),
			(neg|player_is_admin, l.player),
			#player is not server
			(assign, l.me, -1),
			(try_begin),
				(neg|multiplayer_is_dedicated_server),
				(multiplayer_get_my_player, l.me),
			(try_end),
			(store_and, l.req, l.filter, lwbr.player_filter("-Server")),
			(this_or_next|eq, l.req, 0),
			(neq, l.player, l.me),
			#player is using Native
			(store_and, l.req, l.filter, lwbr.player_filter("Native")),
			(this_or_next|eq, l.req, 0),
			(player_slot_eq, l.player, lwbr.player_slots["version"].id, lwbr.native),
			#player is using WarForge
			(store_and, l.req, l.filter, lwbr.player_filter("WarForge")),
			(this_or_next|eq, l.req, 0),
			(player_slot_ge, l.player, lwbr.player_slots["version"].id, lwbr.native+1),
			]),
	#script.lwbr_send_event_to_players
	("lwbr_send_event_to_players",[
			(try_begin),
				(multiplayer_is_server),
				] + lwbr.sv_version([
					(store_script_param, l.event_type, 1),
					(store_script_param, l.par1, 2),
					(store_script_param, l.par2, 3),
					(store_script_param, l.par3, 4),
					(store_script_param, l.par4, 5),
					(store_script_param, l.filter, 6),
					(store_script_param, l.silent, 7),
					(try_begin),
						(eq, l.silent, 0),
						] + lwbr.debug_func("lwbr_send_event_to_players", [l.event_type, l.par1, l.par2, l.par3, l.par4, l.filter]) + [
					(try_end),
					(try_for_players, l.player),
						(filter_player, l.player, l.filter),
						] + lwbr.debug([
							(try_begin),
								(eq, l.silent, 0),
								(assign, reg42, l.player),
								(display_message, "@sending to player {reg42}"),
							(try_end),
						]) + [#end lwbr.debug
						(multiplayer_send_4_int_to_player, l.player, l.event_type, l.par1, l.par2, l.par3, l.par4),
				(try_end),
				]) + [#end lwbr.sv_version
			(try_end),
			]),
	#script.lwbr_send_event_to_player
	("lwbr_send_event_to_player",[
			(try_begin),
				(multiplayer_is_server),
				] + lwbr.sv_version([
					(store_script_param,l.player,1),
					(store_script_param,l.event_type,2),
					(store_script_param,l.par1,3),
					(store_script_param,l.par2,4),
					(store_script_param,l.par3,5),
					(store_script_param,l.par4,6),
					(store_script_param,l.filter,7),
					(store_script_param,l.silent,8),
					(try_begin),
						(eq, l.silent, 0),
						] + lwbr.debug_func("lwbr_send_event_to_player", [l.player, l.event_type, l.par1, l.par2, l.par3, l.par4, l.filter]) + [
					(try_end),
					(filter_player, l.player, l.filter),
					(multiplayer_send_4_int_to_player, l.player, l.event_type, l.par1, l.par2, l.par3, l.par4),
				]) + [#end lwbr.sv_version
			(try_end),
			]),
	#script.lwbr_send_event_to_server
	("lwbr_send_event_to_server",[
			(try_begin),
				(neg|multiplayer_is_dedicated_server),
				] + lwbr.cl_version([
					(store_script_param,l.event_type,1),
					(store_script_param,l.par1,2),
					(store_script_param,l.par2,3),
					(store_script_param,l.par3,4),
					(store_script_param,l.par4,5),
					(store_script_param,l.silent,6),
					(try_begin),
						(eq, l.silent, 0),
						] + lwbr.debug_func("lwbr_send_event_to_server", [l.event_type, l.par1, l.par2, l.par3, l.par4]) + [
					(try_end),
					(multiplayer_send_4_int_to_server, l.event_type, l.par1, l.par2, l.par3, l.par4),
				]) + [#end lwbr.cl_version
			(try_end),
			]),
	#script.lwbr_log_action
	("lwbr_log_action",[
			(store_script_param_1, l.player),
			(store_script_param_2, l.silent),
			(try_begin),
				(player_is_active, l.player),
				(player_get_unique_id, reg42, l.player),
				(str_store_player_username, s44, l.player),
				(try_begin),
					(player_is_admin, l.player),
					(str_store_string, s45, "@Admin {s44}: {s42}"),
					(str_store_string, s46, "@Admin {s44} #{reg42}: {s42}"),
					(str_store_string, s47, "@Admin {s44} #{reg42}: {s43}"),
				(else_try),
					(str_store_string, s45, "@Player {s44}: {s42}"),
					(str_store_string, s46, "@Player {s44} #{reg42}: {s42}"),
					(str_store_string, s47, "@Player {s44} #{reg42}: {s43}"),
				(try_end),
			(else_try),
				(eq, l.player, lwbr.console),
				(str_store_string, s45, "@Console: {s42}"),
				(str_store_string, s46, "@Console: {s42}"),
				(str_store_string, s47, "@Console: {s43}"),
			(else_try),
				(str_store_string, s45, "@{s42}"),
				(str_store_string, s46, "@{s42}"),
				(str_store_string, s47, "@{s43}"),
			(try_end),
			(try_begin),
				(multiplayer_is_dedicated_server),
				(server_add_message_to_log, s46),
				(display_message, s47),
			(try_end),
			(try_begin),
				(neq, l.silent, lwbr.silent),
				(try_for_players, l.pl),
					(filter_player, l.pl, "Admin"),
					(multiplayer_send_string_to_player, l.pl, multiplayer_event_show_server_message, s46),
				(else_try),
					(player_is_active, l.pl),
					(multiplayer_send_string_to_player, l.pl, multiplayer_event_show_server_message, s45),
				(try_end),
			(try_end),
			]),

	## VARs and SV_VARs
	#script.lwbr_init_cl_vars
	("lwbr_init_cl_vars",[
			# (try_begin),
			# 	(eq, g.lwbr_cl_vars_initialized, 0),
			# 	] + [ (set_lwbr_var, lwbr.cl_vars[var].id, lwbr.cl_vars[var].deff) for var in lwbr.cl_vars if not lwbr.cl_vars[var].reset] + [
			# (try_end),
			# ] + [ (set_lwbr_var, lwbr.cl_vars[var].id, lwbr.cl_vars[var].deff) for var in lwbr.cl_vars if lwbr.cl_vars[var].reset] + [
			] + [ (set_lwbr_var, lwbr.cl_vars[var].id, lwbr.cl_vars[var].deff) for var in lwbr.cl_vars] + [
			(assign, g.lwbr_cl_vars_initialized, 1),
			]),
	#script.lwbr_init_sv_vars
	("lwbr_init_sv_vars",[
			(try_begin),
				(multiplayer_is_server),
				] + lwbr.sv_version([
					# (try_begin),
					# 	(eq, g.lwbr_sv_vars_initialized, 0),
					# 	] + [ (set_lwbr_sv_var, lwbr.sv_vars[var].id, lwbr.sv_vars[var].deff_sv) for var in lwbr.sv_vars if not lwbr.sv_vars[var].reset] + [
					# (try_end),
					# ] + [ (set_lwbr_sv_var, lwbr.sv_vars[var].id, lwbr.sv_vars[var].deff_sv) for var in lwbr.sv_vars if lwbr.sv_vars[var].reset] + [
					] + [ (set_lwbr_sv_var, lwbr.sv_vars[var].id, lwbr.sv_vars[var].deff_sv) for var in lwbr.sv_vars] + [
					(assign, g.lwbr_sv_vars_initialized, 1),
				]) + [#end lwbr.sv_version
			(else_try),
				] + lwbr.cl_version([
					# (try_begin),
					# 	(eq, g.lwbr_sv_vars_initialized, 0),
					# 	] + [ (set_lwbr_sv_var, lwbr.sv_vars[var].id, lwbr.sv_vars[var].deff) for var in lwbr.sv_vars if not lwbr.sv_vars[var].reset] + [
					# (try_end),
					# ] + [ (set_lwbr_sv_var, lwbr.sv_vars[var].id, lwbr.sv_vars[var].deff) for var in lwbr.sv_vars if lwbr.sv_vars[var].reset] + [
					] + [ (set_lwbr_sv_var, lwbr.sv_vars[var].id, lwbr.sv_vars[var].deff) for var in lwbr.sv_vars] + [
					(assign, g.lwbr_sv_vars_initialized, 1),
				]) + [#end lwbr.cl_version
				(try_end),
			]),
	#script.lwbr_set_var
	("lwbr_set_var",[
			(store_script_param, l.var, 1),
			(store_script_param, l.val, 2),
			(store_script_param, l.sync, 3),
			(get_slot, l.pre, trp.lwbr_vars, l.var),
			(set_slot, trp.lwbr_vars, l.var, l.val),
			(try_begin),
				(neq, l.pre, l.val),
				(try_begin),
					(eq, l.sync, lwbr.sync_to_cl),
					(multiplayer_is_server),
					] + lwbr.sv_version([
						(send_event_to_players, lwbr.multiplayer_event_client, lwbr.cl_event.set_var, l.var, l.val),
					]) + [#end lwbr.sv_version
				(else_try),
					(eq, l.sync, lwbr.sync_to_sv),
					(neg|multiplayer_is_dedicated_server),
					] + lwbr.cl_version([
						(send_event_to_server, lwbr.multiplayer_event_server, lwbr.sv_event.return_var, l.var, l.val),
					]) + [#end lwbr.cl_version
				(try_end),
			(try_end),
			]),
	#script.lwbr_set_sv_var
	("lwbr_set_sv_var",[
			(store_script_param, l.var, 1),
			(store_script_param, l.val, 2),
			(store_script_param, l.sync, 3),
			(get_slot, l.pre, trp.lwbr_sv_vars, l.var),
			(set_slot, trp.lwbr_sv_vars, l.var, l.val),
			(try_begin),
				(neq, l.pre, l.val),
				(try_begin),
					(eq, l.sync, lwbr.sync_to_cl),
					(multiplayer_is_server),
					] + lwbr.sv_version([
						(send_event_to_players, lwbr.multiplayer_event_client,
							lwbr.cl_event.return_sv_var, l.var, l.val, 0, lwbr.player_filter("-Server|WarForge")),
					]) + [#end lwbr.sv_version
				(else_try),
					(eq, l.sync, lwbr.sync_to_sv),
					(neg|multiplayer_is_dedicated_server),
					] + lwbr.cl_version([
						(send_event_to_server, lwbr.multiplayer_event_server, lwbr.sv_event.set_sv_var, l.var, l.val),
					]) + [#end lwbr.cl_version
				(try_end),
			(try_end),
			]),
	#script.lwbr_get_var
	("lwbr_get_var",[
			(store_script_param, l.var, 1),
			(get_slot, reg42, trp.lwbr_vars, l.var),
			]),
	#script.lwbr_get_sv_var
	("lwbr_get_sv_var",[
			(store_script_param, l.var, 1),
			(get_slot, reg42, trp.lwbr_sv_vars, l.var),
			]),

	## WEATHER ##
	#script.lwbr_calc_weather
	("lwbr_calc_weather",[
			#(store_current_scene, l.scn),
			(store_script_param, l.scn, 1),
			(scene_get_slot, l.rain_min,	l.scn, lwbr.scene_slots["rain_min"].id),
			(scene_get_slot, l.rain_max,	l.scn, lwbr.scene_slots["rain_max"].id),
			(scene_get_slot, l.rain_chance,	l.scn, lwbr.scene_slots["rain_chance"].id),
			(scene_get_slot, l.snow_chance,	l.scn, lwbr.scene_slots["snow_chance"].id),
			(scene_get_slot, l.fog_min,		l.scn, lwbr.scene_slots["fog_min"].id),
			(scene_get_slot, l.fog_max,		l.scn, lwbr.scene_slots["fog_max"].id),
			(scene_get_slot, l.fog_color1,	l.scn, lwbr.scene_slots["fog_color1"].id),
			(scene_get_slot, l.fog_color2,	l.scn, lwbr.scene_slots["fog_color2"].id),

			(store_random_in_range, l.rnd, 0, 100),
			(try_begin),
				(lt, l.rnd, l.rain_chance),
				(scene_set_slot, l.scn, lwbr.scene_slots["cur_wt_typ"].id, 1),
			(else_try),
				(lt, l.rnd, l.snow_chance),
				(scene_set_slot, l.scn, lwbr.scene_slots["cur_wt_typ"].id, 2),
			(else_try),
				(scene_set_slot, l.scn, lwbr.scene_slots["cur_wt_typ"].id, 0),
			(try_end),

			(store_random_in_range, l.rnd, l.rain_min, l.rain_max),
			(scene_set_slot, l.scn, lwbr.scene_slots["cur_wt_str"].id, l.rnd),

			(store_random_in_range, l.rnd, l.fog_min, l.fog_max),
			(scene_set_slot, l.scn, lwbr.scene_slots["cur_wt_fgD"].id, l.rnd),

			(try_begin),
				(eq, l.fog_color1, l.fog_color2),
				(assign, l.rgb, l.fog_color1),
			(else_try),
				(store_and, l.r1, l.fog_color1, 0xFF0000),#get the R,G,B components of each color
				(store_and, l.r2, l.fog_color2, 0xFF0000),
				(store_and, l.g1, l.fog_color1, 0x00FF00),
				(store_and, l.g2, l.fog_color2, 0x00FF00),
				(store_and, l.b1, l.fog_color1, 0x0000FF),
				(store_and, l.b2, l.fog_color2, 0x0000FF),

				(val_div, l.r1, 0x010000),#normalize them
				(val_div, l.r2, 0x010000),
				(val_div, l.g1, 0x000100),
				(val_div, l.g2, 0x000100),
				#(val_div, l.b1, 0x000001),
				#(val_div, l.b2, 0x000001),

				(store_random_in_range, l.r, l.r1, l.r2),#get a random in between each
				(store_random_in_range, l.g, l.g1, l.g2),
				(store_random_in_range, l.b, l.b1, l.b2),

				(store_mul, l.R, l.r, 0x010000),#multiply them back
				(store_mul, l.G, l.g, 0x000100),
				(store_mul, l.B, l.b, 0x000001),

				(store_or, l.rg, l.R, l.G),#and combine them
				(store_or, l.rgb, l.rg, l.B),
				] + lwbr.debug([
					(try_begin),
						(is_between, l.scn, multiplayer_scenes_begin, multiplayer_scenes_end),

						(call_script, script.game_get_scene_name, l.scn),

						(display_message, "@l.scn = {s0}"),

						(assign, reg0, l.r1),
						(assign, reg1, l.r2),
						(assign, reg2, l.r),
						(display_message, "@fog r = random_in_range({reg0},{reg1}) = {reg2}"),

						(assign, reg0, l.g1),
						(assign, reg1, l.g2),
						(assign, reg2, l.g),
						(display_message, "@fog g = random_in_range({reg0},{reg1}) = {reg2}"),

						(assign, reg0, l.b1),
						(assign, reg1, l.b2),
						(assign, reg2, l.b),
						(display_message, "@fog b = random_in_range({reg0},{reg1}) = {reg2}"),

						(assign, reg0, l.fog_color1),
						(assign, reg1, l.fog_color2),
						(assign, reg2, l.rgb),
						(display_message, "@fog rgb = random_in_range({reg0},{reg1}) = {reg2}"),
					(try_end),
				]) + [#end lwbr.debug
			(try_end),
			(scene_set_slot, l.scn, lwbr.scene_slots["cur_wt_fgC"].id, l.rgb),

			(try_begin),
				(multiplayer_is_server),
				] + lwbr.sv_version([
					(try_for_players, l.player_no),
						(call_script, script.lwbr_send_scene_weather_info, l.player_no, l.scn),
					(try_end),
				]) + [#end lwbr.sv_version
			(try_end),
			]),
	#script.lwbr_set_weather
	("lwbr_set_weather",[
			#(store_current_scene, l.scn),
			(store_script_param_1, l.scn),
			(get_lwbr_sv_var, l.weather_config,	"weather_config"),
			(get_lwbr_sv_var, l.time_config,	"time_config"),
			(get_lwbr_sv_var, l.fog_config,		"fog_config"),
			#rain/snow
			(try_begin),
				(eq, l.weather_config, 0),
				(scene_get_slot, l.typ, l.scn, lwbr.scene_slots["cur_wt_typ"].id),
				(scene_get_slot, l.str, l.scn, lwbr.scene_slots["cur_wt_str"].id),
			(else_try),
				(eq, l.weather_config, 1),
				(assign, l.typ, 0),
				(assign, l.str, 0),
			(else_try),
				(eq, l.weather_config, 2),
				(assign, l.typ, 1),
				(store_random_in_range, l.str, 30, 100),
			(else_try),
				(eq, l.weather_config, 3),
				(assign, l.typ, 2),
				(store_random_in_range, l.str, 30, 100),
			(try_end),
			#time
			(try_begin),
				(eq, l.time_config, 0),
				(store_random_in_range, l.tim, 0, 24),
			(else_try),
				(eq, l.time_config, 1),
				(store_random_in_range, l.tim, 6, 18),
			(else_try),
				(eq, l.time_config, 2),
				(assign, l.tim, 6),
			(else_try),
				(eq, l.time_config, 3),
				(assign, l.tim, 12),
			(else_try),
				(eq, l.time_config, 4),
				(assign, l.tim, 18),
			(else_try),
				(eq, l.time_config, 5),
				(assign, l.tim, 24),
			(try_end),
			#fog
			(try_begin),
				(this_or_next|ge, l.tim, 18),
				(lt, l.tim, 6),
				(store_random_in_range, l.rnd, 0, 2),
				(eq, l.rnd, 0),
				(assign, l.fgC, 0x0F0F0F),
			(else_try),
				(scene_get_slot, l.fgC, l.scn, lwbr.scene_slots["cur_wt_fgC"].id),
			(try_end),
			(try_begin),
				(eq, l.fog_config, 0),
				(scene_get_slot, l.fgD, l.scn, lwbr.scene_slots["cur_wt_fgD"].id),
			(else_try),
				(eq, l.fog_config, 1),
				(assign, l.fgD, 1000),
			(else_try),
				(eq, l.fog_config, 2),
				(store_random_in_range, l.fgD, 300, 700),
			(else_try),
				(eq, l.fog_config, 3),
				(store_random_in_range, l.fgD, 10, 150),
			(else_try),
				(eq, l.fog_config, 4),
				(store_random_in_range, l.fgD, 0, 1000),
			(try_end),
			] + lwbr.debug_func("lwbr_set_weather",[l.weather_config,l.fog_config,l.time_config,l.typ,l.str,l.fgD,l.fgC,l.tim]) + [
			(try_begin),
				(is_between, l.tim, 0, 24),
				(is_between, l.typ, 0, 3),
				(is_between, l.str, 0, 100),
				(neq, l.fgD, -1),
				(neq, l.fgC, -1),
				(scene_set_day_time, l.tim),
				(set_rain, l.typ, l.str),
				(set_fog_distance, l.fgD, l.fgC),
			(else_try),
				(call_script, script.lwbr_calc_weather, l.scn),
				(call_script, script.lwbr_set_weather, l.scn),
			(try_end),
			]),
	#script.lwbr_send_scene_weather_info
	("lwbr_send_scene_weather_info",[
			] + lwbr.sv_version([
				(store_script_param_1, l.player),
				(store_script_param_2, l.scn),
				(player_is_active, l.player),
				(store_add, l.end, lwbr.scene_slots["cur_wt_fgC"].id, 1),
				# (try_for_range, l.slot, lwbr.scene_slots["cur_wt_typ"].id, l.end),
				(try_for_range, l.slot, lwbr.scene_slots["available_dm"].id, l.end),
					(scene_get_slot, l.val, l.scn, l.slot),
					(send_event_to_player, l.player, lwbr.multiplayer_event_client,
						lwbr.cl_event.set_scene_slot, l.scn, l.slot, l.val, "WarForge", 1),
					(val_add, g.lwbr_wt_events_sent, 1),
					# (ge, g.lwbr_wt_events_sent, lwbr.wt_event_limit),
					# (assign, l.end, 0),
				(try_end),
			]) + [#end lwbr.sv_version
			]),
	#script.lwbr_send_weather_info
	("lwbr_send_weather_info",[
			] + lwbr.sv_version([
				(store_script_param_1, l.player),
				(try_begin),
					(filter_player, l.player, "-Server"),
					(player_get_slot, l.start, l.player, lwbr.player_slots["nxt_scn_info"].id),
					(neq, l.start, -1),
					(lt, l.start, scn.end),
					(store_add, l.end, l.start, 10),
					(val_min, l.end, scn.end),
					(try_for_range, l.scn, l.start, l.end),
						(player_is_active, l.player),
						(call_script, script.lwbr_send_scene_weather_info, l.player, l.scn),

						(lt, g.lwbr_wt_events_sent, lwbr.wt_event_limit),
					(else_try),
						(assign, l.end, l.scn),
					(try_end),
					(player_is_active, l.player),
					(player_set_slot, l.player, lwbr.player_slots["nxt_scn_info"].id, l.end),
				(try_end),
			]) + [#end lwbr.sv_version
			]),

	## ITEMS ##
	#script.lwbr_set_item_for_troop
	("lwbr_set_item_for_troop",[
			(store_script_param, l.itm, 1),
			(store_script_param, l.trp, 2),
			(store_script_param, l.val, 3),
			(store_add, l.slot, l.trp, slot_item_multiplayer_availability_linked_list_begin - multiplayer_troops_begin),
			(item_set_slot, l.itm, l.slot, l.val),
			]),
	#script.lwbr_get_item_for_troop
	("lwbr_get_item_for_troop",[
			(store_script_param, l.itm, 1),
			(store_script_param, l.trp, 2),
			(store_add, l.slot, l.trp, slot_item_multiplayer_availability_linked_list_begin - multiplayer_troops_begin),
			(item_get_slot, reg42, l.itm, l.slot),
			]),
	#script.lwbr_force_change_weapons
	("lwbr_force_change_weapons",[
			] + lwbr.cl_version([
				(multiplayer_get_my_player, l.me),
				# (call_script, script.multiplayer_clear_player_selected_items, l.me),
				(player_get_troop_id, l.trp, l.me),
				(try_begin),
					(gt, l.trp, -1),
					(try_for_range, l.slot, lwbr.troop_slots["sel_head"].id, lwbr.troop_slots["sel_wpn4"].id+1),
						(troop_set_slot, l.trp, l.slot, -2),
					(try_end),
					(call_script, script.multiplayer_set_default_item_selections_for_troop, l.trp),
				(try_end),
			]) + [#end lwbr.cl_version
			]),
	#script.lwbr_add_rnd_itm_of_type
	("lwbr_add_rnd_itm_of_type",[
			(store_script_param, l.trp, 1),
			(store_script_param, l.itp, 2),
			(store_script_param, l.cnt, 3),
			(store_script_param, l.ek,  4),
			(store_script_param, l.pl,  5),
			(try_begin),
				(gt, l.cnt, 0),
				(store_random_in_range, l.rnd, 0, l.cnt),
				(try_for_troop_items, l.itm, l.trp),
					(item_get_type, l.type, l.itm),
					(eq, l.type, l.itp),
					(try_begin),
						(eq, l.rnd, 0),
						] + lwbr.debug([
							(str_store_item_name, s0, l.itm),
							(str_store_player_username, s1, l.pl),
							(display_message,"@Adding itm.{s0} to player {s1}"),
						]) + [
						(player_add_spawn_item, l.pl, l.ek, l.itm),
						(try_for_troop_items_break),
					(try_end),
					(val_sub, l.rnd, 1),
				(try_end),
			(try_end),
			]),

	## ACTIONS ##
	#script.lwbr_do_action
	("lwbr_do_action",[
			(store_script_param_1, l.action),
			(store_script_param_2, l.player_no),

			(assign, l.error, -1),

			(try_begin),#check if it is a valid action
				] + [ (neq, l.action, lwbr.actions[act].id) for act in lwbr.actions] + [
				(assign, l.error, 1),
			(else_try),#check if it is a valid player
				(neg|player_is_active, l.player_no),
				(assign, l.error, 2),
			(else_try),#check if the player has the privileges to do it
				(neg|player_is_admin, l.player_no),
				(call_script, script.cf_lwbr_is_adm_action, l.action),
				(assign, l.error, 3),
			(else_try),#check the player cooldown for the action
				(eq, 1, 0),##TODO
				(assign, l.error, 4),
			] + sum([[
				(else_try),
					(eq, l.action, lwbr.actions[act].id),
					(call_script, lwbr.actions[act].script, l.player_no),
					(assign, l.error, 0),
			] for act in lwbr.actions ],[]) + [
			(try_end),
			(assign, reg42, l.error),
			]),
	#script.cf_lwbr_is_adm_action
	("cf_lwbr_is_adm_action",[
			(store_script_param_1, l.action),
			] + [ (this_or_next|eq, l.action, lwbr.actions[act].id) for act in lwbr.actions if lwbr.actions[act].adm] + [
			(eq, 1, 0),
			]),
	#script.lwbr_action_taunt
	("lwbr_action_taunt",[
			(store_script_param_1, l.player_no),
			(try_begin),
				(player_is_active, l.player_no),
				(player_get_agent_id, l.agent, l.player_no),
				(agent_is_active, l.agent),
				(agent_is_alive, l.agent),
				#play sound
				(player_get_gender, l.gender, l.player_no),
				(try_chance, 5, 1000),#0,5%
					(agent_play_sound, l.agent, snd.cow_moo),
				(else_try_chance, 5, 1000),#0,5%
					(agent_play_sound, l.agent, snd.cow_slaughter),
				(else_try),
					(eq, l.gender, 1),#female
					(agent_play_sound, l.agent, snd.woman_yell),
				(else_try),
					(store_random_in_range, l.sound, snd.man_warcry, snd.encounter_vaegirs_enemy+1),
					(agent_play_sound, l.agent, l.sound),
				(try_end),
			(try_end),
			]),
	#script.lwbr_action_cheer
	("lwbr_action_cheer",[
			(store_script_param_1, l.player_no),
			(try_begin),
				(player_is_active, l.player_no),
				(player_get_agent_id, l.agent, l.player_no),
				(agent_is_active, l.agent),
				(agent_is_alive, l.agent),
				#play cheer animation
				(agent_get_animation, l.anim, l.agent, 1),
				(try_begin),
					(neq, l.anim, anim.cheer),
					(agent_set_animation, l.agent, anim.cheer, 1),
				(try_end),
				#(agent_get_animation, l.anim, l.agent, 0),
				# (try_begin),
				# 	(this_or_next|eq, l.anim, anim.stand),
				# 	(this_or_next|eq, l.anim, anim.stand_man),
				# 	(eq, 0, 1),
				# 	(agent_set_animation, l.agent, anim.cheer_stand, 1),
				# (else_try),
				# 	(agent_set_animation, l.agent, anim.cheer, 1),
				# (try_end),
				#play sound
				(player_get_gender, l.gender, l.player_no),
				(try_begin),
					(eq, l.gender, 1),#female
					(agent_play_sound, l.agent, snd.woman_yell),
				(else_try),
					(agent_play_sound, l.agent, snd.man_yell),
				(try_end),
			(try_end),
			]),
	#script.lwbr_action_jumphorse
	("lwbr_action_jumphorse",[
			(store_script_param_1, l.player_no),
			(try_begin),
				(player_is_active, l.player_no),
				(player_get_agent_id, l.agent, l.player_no),
				(agent_is_active, l.agent),
				(agent_is_alive, l.agent),
				(agent_get_horse, l.horse, l.agent),
				(agent_is_active, l.horse),
				(agent_is_alive, l.horse),
				(agent_start_running_away, l.horse),
				(agent_stop_running_away, l.horse),
			(try_end),
			]),
	#script.lwbr_action_msg_to_adm
	("lwbr_action_msg_to_adm",[
			(store_script_param_1, l.player_no),
			(try_begin),
				(player_is_active, l.player_no),
				(str_store_player_username, s0, l.player_no),
				(try_for_players, l.pl),
					(filter_player, l.pl, "Admin"),
					(multiplayer_send_string_to_player, l.pl, multiplayer_event_show_server_message, "@{s0}: test"),
				(try_end),
			(try_end),
			]),
	#script.lwbr_action_msg_from_adm
	("lwbr_action_msg_from_adm",[
			(store_script_param_1, l.player_no),
			(try_begin),
				(player_is_active, l.player_no),
				(log_action, "@test", l.player_no, lwbr.verbose),
			(try_end),
			]),
	#script.lwbr_action_kdown
	("lwbr_action_kdown",[
			(store_script_param_1, l.player_no),
			(try_begin),
				(player_is_active, l.player_no),
			(try_end),
			]),

	## OTHER ##
	#script.lwbr_get_key_name
	("lwbr_get_key_name",[
			(store_script_param_1,l.key),
			(try_begin),
				(eq,l.key,-1),
				(str_store_string,s1,"@Disabled"),
			(else_try),
				(eq,l.key,key_1),
				(str_store_string,s1,"@1"),
			(else_try),
				(eq,l.key,key_2),
				(str_store_string,s1,"@2"),
			(else_try),
				(eq,l.key,key_3),
				(str_store_string,s1,"@3"),
			(else_try),
				(eq,l.key,key_4),
				(str_store_string,s1,"@4"),
			(else_try),
				(eq,l.key,key_5),
				(str_store_string,s1,"@5"),
			(else_try),
				(eq,l.key,key_6),
				(str_store_string,s1,"@6"),
			(else_try),
				(eq,l.key,key_7),
				(str_store_string,s1,"@7"),
			(else_try),
				(eq,l.key,key_8),
				(str_store_string,s1,"@8"),
			(else_try),
				(eq,l.key,key_9),
				(str_store_string,s1,"@9"),
			(else_try),
				(eq,l.key,key_0),
				(str_store_string,s1,"@0"),
			(else_try),
				(eq,l.key,key_a),
				(str_store_string,s1,"@A"),
			(else_try),
				(eq,l.key,key_b),
				(str_store_string,s1,"@B"),
			(else_try),
				(eq,l.key,key_c),
				(str_store_string,s1,"@C"),
			(else_try),
				(eq,l.key,key_d),
				(str_store_string,s1,"@D"),
			(else_try),
				(eq,l.key,key_e),
				(str_store_string,s1,"@E"),
			(else_try),
				(eq,l.key,key_f),
				(str_store_string,s1,"@F"),
			(else_try),
				(eq,l.key,key_g),
				(str_store_string,s1,"@G"),
			(else_try),
				(eq,l.key,key_h),
				(str_store_string,s1,"@H"),
			(else_try),
				(eq,l.key,key_i),
				(str_store_string,s1,"@I"),
			(else_try),
				(eq,l.key,key_j),
				(str_store_string,s1,"@J"),
			(else_try),
				(eq,l.key,key_k),
				(str_store_string,s1,"@K"),
			(else_try),
				(eq,l.key,key_l),
				(str_store_string,s1,"@L"),
			(else_try),
				(eq,l.key,key_m),
				(str_store_string,s1,"@M"),
			(else_try),
				(eq,l.key,key_n),
				(str_store_string,s1,"@N"),
			(else_try),
				(eq,l.key,key_o),
				(str_store_string,s1,"@O"),
			(else_try),
				(eq,l.key,key_p),
				(str_store_string,s1,"@P"),
			(else_try),
				(eq,l.key,key_q),
				(str_store_string,s1,"@Q"),
			(else_try),
				(eq,l.key,key_r),
				(str_store_string,s1,"@R"),
			(else_try),
				(eq,l.key,key_s),
				(str_store_string,s1,"@S"),
			(else_try),
				(eq,l.key,key_t),
				(str_store_string,s1,"@T"),
			(else_try),
				(eq,l.key,key_u),
				(str_store_string,s1,"@U"),
			(else_try),
				(eq,l.key,key_v),
				(str_store_string,s1,"@V"),
			(else_try),
				(eq,l.key,key_w),
				(str_store_string,s1,"@W"),
			(else_try),
				(eq,l.key,key_x),
				(str_store_string,s1,"@X"),
			(else_try),
				(eq,l.key,key_y),
				(str_store_string,s1,"@Y"),
			(else_try),
				(eq,l.key,key_z),
				(str_store_string,s1,"@Z"),
			(else_try),
				(eq,l.key,key_numpad_0),
				(str_store_string,s1,"@Numpad 0"),
			(else_try),
				(eq,l.key,key_numpad_1),
				(str_store_string,s1,"@Numpad 1"),
			(else_try),
				(eq,l.key,key_numpad_2),
				(str_store_string,s1,"@Numpad 2"),
			(else_try),
				(eq,l.key,key_numpad_3),
				(str_store_string,s1,"@Numpad 3"),
			(else_try),
				(eq,l.key,key_numpad_4),
				(str_store_string,s1,"@Numpad 4"),
			(else_try),
				(eq,l.key,key_numpad_5),
				(str_store_string,s1,"@Numpad 5"),
			(else_try),
				(eq,l.key,key_numpad_6),
				(str_store_string,s1,"@Numpad 6"),
			(else_try),
				(eq,l.key,key_numpad_7),
				(str_store_string,s1,"@Numpad 7"),
			(else_try),
				(eq,l.key,key_numpad_8),
				(str_store_string,s1,"@Numpad 8"),
			(else_try),
				(eq,l.key,key_numpad_9),
				(str_store_string,s1,"@Numpad 9"),
			(else_try),
				(eq,l.key,key_num_lock),
				(str_store_string,s1,"@Num Lock"),
			(else_try),
				(eq,l.key,key_numpad_slash),
				(str_store_string,s1,"@Numpad /"),
			(else_try),
				(eq,l.key,key_numpad_multiply),
				(str_store_string,s1,"@Numpad *"),
			(else_try),
				(eq,l.key,key_numpad_minus),
				(str_store_string,s1,"@Numpad -"),
			(else_try),
				(eq,l.key,key_numpad_plus),
				(str_store_string,s1,"@Numpad +"),
			(else_try),
				(eq,l.key,key_numpad_enter),
				(str_store_string,s1,"@Numpad Enter"),
			(else_try),
				(eq,l.key,key_numpad_period),
				(str_store_string,s1,"@Numpad ."),
			(else_try),
				(eq,l.key,key_insert),
				(str_store_string,s1,"@Insert"),
			(else_try),
				(eq,l.key,key_delete),
				(str_store_string,s1,"@Delete"),
			(else_try),
				(eq,l.key,key_home),
				(str_store_string,s1,"@Home"),
			(else_try),
				(eq,l.key,key_end),
				(str_store_string,s1,"@End"),
			(else_try),
				(eq,l.key,key_page_up),
				(str_store_string,s1,"@Pg Up"),
			(else_try),
				(eq,l.key,key_page_down),
				(str_store_string,s1,"@Pg Down"),
			(else_try),
				(eq,l.key,key_up),
				(str_store_string,s1,"@Up Arrow"),
			(else_try),
				(eq,l.key,key_down),
				(str_store_string,s1,"@Down Arrow"),
			(else_try),
				(eq,l.key,key_left),
				(str_store_string,s1,"@Left Arrow"),
			(else_try),
				(eq,l.key,key_right),
				(str_store_string,s1,"@Right Arrow"),
			(else_try),
				(eq,l.key,key_f1),
				(str_store_string,s1,"@F1"),
			(else_try),
				(eq,l.key,key_f2),
				(str_store_string,s1,"@F2"),
			(else_try),
				(eq,l.key,key_f3),
				(str_store_string,s1,"@F3"),
			(else_try),
				(eq,l.key,key_f4),
				(str_store_string,s1,"@F4"),
			(else_try),
				(eq,l.key,key_f5),
				(str_store_string,s1,"@F5"),
			(else_try),
				(eq,l.key,key_f6),
				(str_store_string,s1,"@F6"),
			(else_try),
				(eq,l.key,key_f7),
				(str_store_string,s1,"@F7"),
			(else_try),
				(eq,l.key,key_f8),
				(str_store_string,s1,"@F8"),
			(else_try),
				(eq,l.key,key_f9),
				(str_store_string,s1,"@F9"),
			(else_try),
				(eq,l.key,key_f10),
				(str_store_string,s1,"@F10"),
			(else_try),
				(eq,l.key,key_f11),
				(str_store_string,s1,"@F11"),
			(else_try),
				(eq,l.key,key_f12),
				(str_store_string,s1,"@F12"),
			(else_try),
				(eq,l.key,key_space),
				(str_store_string,s1,"@Spacebar"),
			(else_try),
				(eq,l.key,key_escape),
				(str_store_string,s1,"@Esc"),
			(else_try),
				(eq,l.key,key_enter),
				(str_store_string,s1,"@Enter"),
			(else_try),
				(eq,l.key,key_tab),
				(str_store_string,s1,"@Tab"),
			(else_try),
				(eq,l.key,key_back_space),
				(str_store_string,s1,"@Backspace"),
			(else_try),
				(eq,l.key,key_open_braces),
				(str_store_string,s1,"@ [ "),
			(else_try),
				(eq,l.key,key_close_braces),
				(str_store_string,s1,"@ ] "),
			(else_try),
				(eq,l.key,key_comma),
				(str_store_string,s1,"@ , "),
			(else_try),
				(eq,l.key,key_period),
				(str_store_string,s1,"@ . "),
			(else_try),
				(eq,l.key,key_slash),
				(str_store_string,s1,"@ / "),
			(else_try),
				(eq,l.key,key_back_slash),
				(str_store_string,s1,"@ \ "),
			(else_try),
				(eq,l.key,key_equals),
				(str_store_string,s1,"@ = "),
			(else_try),
				(eq,l.key,key_minus),
				(str_store_string,s1,"@ - "),
			(else_try),
				(eq,l.key,key_semicolon),
				(str_store_string,s1,"@ ; "),
			(else_try),
				(eq,l.key,key_apostrophe),
				(str_store_string,s1,"@ ' "),
			(else_try),
				(eq,l.key,key_tilde),
				(str_store_string,s1,"@ ~ "),
			(else_try),
				(eq,l.key,key_caps_lock),
				(str_store_string,s1,"@Caps Lock"),
			(else_try),
				(eq,l.key,key_left_shift),
				(str_store_string,s1,"@Left Shift"),
			(else_try),
				(eq,l.key,key_right_shift),
				(str_store_string,s1,"@Right Shift"),
			(else_try),
				(eq,l.key,key_left_control),
				(str_store_string,s1,"@Left Cntrl"),
			(else_try),
				(eq,l.key,key_right_control),
				(str_store_string,s1,"@Right Cntrl"),
			(else_try),
				(eq,l.key,key_left_alt),
				(str_store_string,s1,"@Left Alt"),
			(else_try),
				(eq,l.key,key_right_alt),
				(str_store_string,s1,"@Right Alt"),
			(else_try),
				(eq,l.key,key_left_mouse_button),
				(str_store_string,s1,"@Left Mouse Button"),
			(else_try),
				(eq,l.key,key_right_mouse_button),
				(str_store_string,s1,"@Right Mouse Button"),
			(else_try),
				(eq,l.key,key_middle_mouse_button),
				(str_store_string,s1,"@Middle Mouse Button"),
			(else_try),
				(eq,l.key,key_mouse_button_4),
				(str_store_string,s1,"@Mouse Button 4"),
			(else_try),
				(eq,l.key,key_mouse_button_5),
				(str_store_string,s1,"@Mouse Button 5"),
			(else_try),
				(eq,l.key,key_mouse_button_6),
				(str_store_string,s1,"@Mouse Button 6"),
			(else_try),
				(eq,l.key,key_mouse_button_7),
				(str_store_string,s1,"@Mouse Button 7"),
			(else_try),
				(eq,l.key,key_mouse_button_8),
				(str_store_string,s1,"@Mouse Button 8"),
			(else_try),
				(eq,l.key,key_mouse_scroll_up),
				(str_store_string,s1,"@Mouse Scroll Up"),
			(else_try),
				(eq,l.key,key_mouse_scroll_down),
				(str_store_string,s1,"@Mouse Scroll Down"),
			(else_try),
				(eq,l.key,key_xbox_a),
				(str_store_string,s1,"@xBox A"),
			(else_try),
				(eq,l.key,key_xbox_b),
				(str_store_string,s1,"@xBox B"),
			(else_try),
				(eq,l.key,key_xbox_x),
				(str_store_string,s1,"@xBox X"),
			(else_try),
				(eq,l.key,key_xbox_y),
				(str_store_string,s1,"@xBox Y"),
			(else_try),
				(eq,l.key,key_xbox_dpad_up),
				(str_store_string,s1,"@xBox dPad Up"),
			(else_try),
				(eq,l.key,key_xbox_dpad_down),
				(str_store_string,s1,"@xBox dPad Down"),
			(else_try),
				(eq,l.key,key_xbox_dpad_right),
				(str_store_string,s1,"@xBox dPad Right"),
			(else_try),
				(eq,l.key,key_xbox_dpad_left),
				(str_store_string,s1,"@xBox dPad Left"),
			(else_try),
				(eq,l.key,key_xbox_start),
				(str_store_string,s1,"@xBox Start"),
			(else_try),
				(eq,l.key,key_xbox_back),
				(str_store_string,s1,"@xBox Back"),
			(else_try),
				(eq,l.key,key_xbox_rbumper),
				(str_store_string,s1,"@xBox Right Bumper"),
			(else_try),
				(eq,l.key,key_xbox_lbumper),
				(str_store_string,s1,"@xBox Left Bumper "),
			(else_try),
				(eq,l.key,key_xbox_ltrigger),
				(str_store_string,s1,"@xBox Right Trigger"),
			(else_try),
				(eq,l.key,key_xbox_rtrigger),
				(str_store_string,s1,"@xBox Left Trigger"),
			(else_try),
				(eq,l.key,key_xbox_rstick),
				(str_store_string,s1,"@xBox Right Stick"),
			(else_try),
				(eq,l.key,key_xbox_lstick),
				(str_store_string,s1,"@xBox Left Stick"),
			(try_end),
			]),
	#script.lwbr_knock_down_from_horse
	("lwbr_knock_down_from_horse",[
			(store_script_param_1,l.agent_no),
			(try_begin),
				(agent_is_active,l.agent_no),
				(agent_get_horse,l.horse,l.agent_no),
				(agent_is_active,l.horse),
				(agent_start_running_away,l.horse),
				(agent_stop_running_away,l.horse),
				(store_agent_hit_points, l.hp, l.agent_no, 1),
				(store_random_in_range, l.dmg, 4, 15),#4-14 dmg
				(val_sub, l.hp, l.dmg),
				(val_max, l.hp, 1),
				(agent_set_hit_points, l.agent_no, l.hp, 1),
				(agent_deliver_damage_to_agent,l.horse,l.agent_no,1),
				(store_random_in_range,l.anim,"anim_rider_fall_right","anim_strike_chest_front_stop"),
				(try_begin),
					(agent_get_player_id,l.player_no, l.agent_no),
					(agent_is_active,l.agent_no),
					(assign,reg1,l.anim),
					(str_store_player_username, s1, l.player_no),
					(str_store_string, s1, "@Player {s1} fell from horse with anim = {reg1}."),
					(server_add_message_to_log, s1),
				(try_end),
				(try_begin),
					(gt, lwbr.debug_mode, 1),
					(multiplayer_send_string_to_player, l.player_no, multiplayer_event_show_server_message,
						"@Falling anim is {reg1}."),
				(try_end),
				(agent_set_animation,l.agent_no,l.anim, 0),
				(agent_set_animation,l.agent_no,l.anim, 1),
			(try_end),
			]),
	#script.lwbr_drop_shield ##TODO
	# ("lwbr_drop_shield",[
			# #(store_script_param_1,l.agent_no),
			# #(try_begin),
			# 	#(agent_is_active, l.agent_no),
			# 	#(agent_get_player_id, l.player_no, l.agent_no),
			# 	#(player_is_active, l.player_no),
			# 	#(agent_is_alive, l.agent_no),
			# 	#(str_store_player_username, s1, l.player_no),
			# 	#(try_begin),
			# 		#(agent_get_wielded_item, l.shield, l.agent_no, 1),
			# 		#(neq, l.shield, -1),
			# 		#(item_get_type, l.type, l.shield),
			# 		#(eq, l.type, itp_type_shield),
			# 		###TODO: drop shield
			# 		#(str_store_string, s1, "@Player dropped his shield."),
			# 		#(server_add_message_to_log, s1),
			# 	#(try_end),
			# 	#(try_begin),
			# 		#(eq, lwbr.debug_mode, 1),
			# 		#(multiplayer_send_string_to_player, l.player_no, multiplayer_event_show_server_message,
			# 			"@{s2} sound is {reg1} and anim is {reg2}"),
			# 	#(try_end),
			# #(try_end),
			# ]),
	#script.lwbr_crouch ##TODO
	# ("lwbr_crouch",[
			# #(store_script_param_1,l.agent_no),
			# #(try_begin),
			# 	#(agent_is_active, l.agent_no),
			# 	#(neg|agent_is_non_player, l.agent_no),
			# 	#(agent_get_player_id, l.player_no, l.agent_no),
			# 	#(player_is_active, l.player_no),
			# 	#(agent_is_alive, l.agent_no),
			# 	#(agent_get_horse, l.horse, l.agent_no),
			# 	#(str_store_player_username, s1, l.player_no),
			# 	##(agent_get_crouch_mode, reg1, l.agent_no),
			# 	#(try_begin),
			# 		##(eq, reg1, 0),
			# 		##(agent_set_crouch_mode, l.agent_no, 1),
			# 		#(agent_slot_eq, l.agent_no, slot_agent_crouch, 0),
			# 		#(agent_set_animation, l.agent_no, "anim_stand_to_crouch", 0),
			# 		#(agent_set_slot, l.agent_no, slot_agent_crouch, 1),
			# 		#(str_store_string, s1, "@CROUCH TEST: Player {s1} crouched."),
			# 		#(server_add_message_to_log, s1),
			# 	#(else_try),
			# 		##(agent_set_crouch_mode, l.agent_no, 0),
			# 		#(agent_slot_eq, l.agent_no, slot_agent_crouch, 1),
			# 		##(agent_set_animation, l.agent_no, "anim_crouch_to_stand", 0),
			# 		#(agent_set_slot, l.agent_no, slot_agent_crouch, 0),
			# 		#(str_store_string, s1, "@CROUCH TEST: Player {s1} stood up."),
			# 		#(server_add_message_to_log, s1),
			# 	#(try_end),
			# 	#(try_begin),
			# 		#(eq, lwbr.debug_mode, 1),
			# 		#(multiplayer_send_string_to_player, l.player_no, multiplayer_event_show_server_message,
			# 			"@DEBUG: You just {reg20?stood up:crouched}."),
			# 	#(try_end),
			# #(try_end),
			# ]),
	#script.lwbr_get_crouch_anim ##TODO
	# ("lwbr_get_crouch_anim",[
			# #(store_script_param_1,l.agent_no),
			# #(assign, l.anim, "anim_crouch_unarmed"),
			# #(try_begin),
			# 	#(agent_is_active, l.agent_no),
			# 	#(agent_is_human, l.agent_no),
			# 	#(agent_get_wielded_item, l.item, l.agent_no),
			# 	#(try_begin),
			# 		#(ge, l.item, 0),
			# 		#(item_get_type, l.item_type, l.item),
			# 		#(try_begin),
			# 			#(eq, l.item_type, itp_type_one_handed_wpn),
			# 			#(assign, l.anim, "anim_crouch_single"),
			# 		#(else_try),
			# 			#(eq, l.item_type, itp_type_two_handed_wpn),
			# 			#(assign, l.anim, "anim_crouch_greatsword"),
			# 		#(else_try),
			# 			#(eq, l.item_type, itp_type_polearm),
			# 			#(assign, l.anim, "anim_crouch_staff"),
			# 		#(else_try),
			# 			#(eq, l.item_type, itp_type_crossbow),
			# 			#(assign, l.anim, "anim_crouch_crossbow"),
			# 		#(else_try),
			# 			#(eq, l.item_type, itp_type_pistol),
			# 			#(assign, l.anim, "anim_crouch_ready_pistol"),
			# 		#(try_end),
			# 	#(try_end),
			# #(try_end),
			# #(assign, reg0, l.anim),
			# ]),
	#script.lwbr_quit_server
	# ("lwbr_quit_server",[
			# (set_rain, 0, 0),
			# (scene_set_day_time, 12),
			# (set_fog_distance, 10000),
			# (call_script,script.lwbr_initialize_variables),
			# ]),
	#script.lwbr_store_troop_stats_all
	# ("lwbr_store_troop_stats_all",[
			# (try_for_range, l.troop, trp.swadian_crossbowman_multiplayer, trp.multiplayer_end),
			# 	(call_script, script.lwbr_store_troop_stats, l.troop),
			# (try_end),
			# ]),
	#script.lwbr_store_troop_stats
	# ("lwbr_store_troop_stats",[
			# (store_script_param_1, l.troop),
			# #
			# (try_for_range, l.slot, slot_troop_stats_begin, slot_troop_stats_end),
			# 	(store_sub, l.value, l.slot, slot_troop_stats_begin),
			# 	(store_attribute_level, l.value2, l.troop, l.value),
			# 	(troop_set_slot, l.troop, l.slot, l.value2),
			# 	(try_begin),
			# 		(eq, lwbr.debug_mode, 1),
			# 		(eq, l.troop, trp.swadian_crossbowman_multiplayer),
			# 		(assign, reg1, l.value),
			# 		(assign, reg2, l.value2),
			# 		(str_store_troop_name, s2, l.troop),
			# 		(str_store_string, s1, "@DEBUG: Troop {s2} stat '{reg1}' default is {reg2}"),
			# 		#(call_script, script.lwbr_send_msg_to_all_players),
			# 		(server_add_message_to_log, s1),
			# 	(try_end),
			# (try_end),
			# #
			# (try_for_range, l.slot, slot_troop_proficiences_begin, slot_troop_proficiences_end),
			# 	(store_sub, l.value, l.slot, slot_troop_proficiences_begin),
			# 	(store_proficiency_level, l.value2, l.troop, l.value),
			# 	(troop_set_slot, l.troop, l.slot, l.value2),
			# 	(try_begin),
			# 		(eq, lwbr.debug_mode, 1),
			# 		(eq, l.troop, trp.swadian_crossbowman_multiplayer),
			# 		(assign, reg1, l.value),
			# 		(assign, reg2, l.value2),
			# 		(str_store_troop_name, s2, l.troop),
			# 		(str_store_string, s1, "@DEBUG: Troop {s2} proficience '{reg1}' default is {reg2}"),
			# 		#(call_script, script.lwbr_send_msg_to_all_players),
			# 		(server_add_message_to_log, s1),
			# 	(try_end),
			# (try_end),
			# #
			# (try_for_range, l.slot, slot_troop_skills_begin, slot_troop_skills_end),
			# 	(store_sub, l.value, l.slot, slot_troop_skills_begin),
			# 	(store_skill_level, l.value2, l.value, l.troop),
			# 	(troop_set_slot, l.troop, l.slot, l.value2),
			# 	(try_begin),
			# 		(eq, lwbr.debug_mode, 1),
			# 		(eq, l.troop, trp.swadian_crossbowman_multiplayer),
			# 		(assign, reg1, l.value),
			# 		(assign, reg2, l.value2),
			# 		(str_store_troop_name, s2, l.troop),
			# 		(str_store_string, s1, "@DEBUG: Troop {s2} skill '{reg1}' default is {reg2}"),
			# 		#(call_script, script.lwbr_send_msg_to_all_players),
			# 		(server_add_message_to_log, s1),
			# 	(try_end),
			# (try_end),
			# #
			# ]),
	#script.lwbr_restore_troop_stats_all
	# ("lwbr_restore_troop_stats_all",[
			# (try_for_range, l.troop, trp.swadian_crossbowman_multiplayer, trp.multiplayer_end),
			# 	(call_script, script.lwbr_restore_troop_stats, l.troop),
			# (try_end),
			# ]),
	#script.lwbr_restore_troop_stats
	# ("lwbr_restore_troop_stats",[
			# (store_script_param_1, l.troop),
			# #
			# (try_begin),
			# 	(eq, lwbr.debug_mode, 1),
			# 	(eq, l.troop, trp.swadian_crossbowman_multiplayer),
			# 	(str_store_troop_name, s1, l.troop),
			# 	(str_store_string, s1, "@Restoring '{s1}' stats"),
			# 	(server_add_message_to_log, s1),
			# (try_end),
			# #
			# (try_for_range, l.slot, slot_troop_stats_begin, slot_troop_stats_end),
			# 	(store_sub, l.value, l.slot, slot_troop_stats_begin),
			# 	(troop_get_slot, l.value2, l.troop, l.slot),
			# 	(call_script, script.lwbr_set_troop_attribute_level, l.troop, l.value, l.value2),
			# (try_end),
			# #
			# (try_for_range, l.slot, slot_troop_proficiences_begin, slot_troop_proficiences_end),
			# 	(store_sub, l.value, l.slot, slot_troop_proficiences_begin),
			# 	(troop_get_slot, l.value2, l.troop, l.slot),
			# 	(call_script, script.lwbr_set_troop_wpn_proficience_level, l.troop, l.value, l.value2),
			# (try_end),
			# #
			# (try_for_range, l.slot, slot_troop_skills_begin, slot_troop_skills_end),
			# 	(store_sub, l.value, l.slot, slot_troop_skills_begin),
			# 	(troop_get_slot, l.value2, l.troop, l.slot),
			# 	(call_script, script.lwbr_set_troop_skill_level, l.troop, l.value, l.value2),
			# (try_end),
			# #
			# (try_begin),
			# 	(eq, lwbr.debug_mode, 1),
			# 	(eq, l.troop, trp.swadian_crossbowman_multiplayer),
			# 	(str_store_troop_name, s1, l.troop),
			# 	(str_store_string, s1, "@'{s1}' stats restored"),
			# 	(server_add_message_to_log, s1),
			# (try_end),
			# #
			# ]),
	#script.lwbr_set_troop_skill_level
	# ("lwbr_set_troop_skill_level",[
			# (store_script_param, l.troop, 1),
			# (store_script_param, l.skill, 2),
			# (store_script_param, l.skl_lvl, 3),
			# (try_begin),
			# 	(store_skill_level,l.old_lvl,l.skill,l.troop),
			# 	(neq, l.skl_lvl, l.old_lvl),
			# 	(val_sub, l.skl_lvl, l.old_lvl),
			# 	(troop_raise_skill,l.troop,l.skill,l.skl_lvl),
			# 	(store_skill_level,l.new_lvl,l.skill,l.troop),
			# 	(try_begin),
			# 		(eq, lwbr.debug_mode, 1),
			# 		(eq, l.troop, trp.swadian_crossbowman_multiplayer),
			# 		(assign, reg1, l.old_lvl),
			# 		(assign, reg2, l.new_lvl),
			# 		(assign, reg3, l.skill),
			# 		(str_store_troop_name, s2, l.troop),
			# 		(str_store_string, s1, "@DEBUG: Troop {s2} skill '{reg3}' changed from {reg1} to {reg2}"),
			# 		#(call_script, script.lwbr_send_msg_to_all_players),
			# 		(server_add_message_to_log, s1),
			# 	(try_end),
			# (try_end),
			# ]),
	#script.lwbr_set_troop_all_skills_level
	# ("lwbr_set_troop_all_skills_level",[
			# (store_script_param, l.troop, 1),
			# (store_script_param, l.skl_lvl, 2),
			# (try_for_range, l.skill, 0, len(skills)),
			# 	(call_script, script.lwbr_set_troop_skill_level, l.troop, l.skill, l.skl_lvl),
			# (try_end),
			# ]),
	#script.lwbr_set_troop_attribute_level
	# ("lwbr_set_troop_attribute_level",[
			# (store_script_param, l.troop, 1),
			# (store_script_param, l.attribute, 2),
			# (store_script_param, l.attribute_lvl, 3),
			# (try_begin),
			# 	(store_attribute_level,l.old_lvl,l.troop,l.attribute),
			# 	(neq, l.attribute_lvl, l.old_lvl),
			# 	(val_sub, l.attribute_lvl, l.old_lvl),
			# 	(troop_raise_attribute_linear,l.troop,l.attribute,l.attribute_lvl),
			# 	(store_attribute_level,l.new_lvl,l.troop,l.attribute),
			# 	(try_begin),
			# 		(eq, lwbr.debug_mode, 1),
			# 		(eq, l.troop, trp.swadian_crossbowman_multiplayer),
			# 		(assign, reg1, l.old_lvl),
			# 		(assign, reg2, l.new_lvl),
			# 		(assign, reg3, l.attribute),
			# 		(str_store_troop_name, s2, l.troop),
			# 		(str_store_string, s1, "@DEBUG: Troop {s2} attribute '{reg3}' changed from {reg1} to {reg2}"),
			# 		#(call_script, script.lwbr_send_msg_to_all_players),
			# 		(server_add_message_to_log, s1),
			# 	(try_end),
			# (try_end),
			# ]),
	#script.lwbr_set_troop_all_attributes_level
	# ("lwbr_set_troop_all_attributes_level",[
			# (store_script_param, l.troop, 1),
			# (store_script_param, l.attribute_lvl, 2),
			# (try_for_range, l.attribute, 0, 4),
			# 	(call_script, script.lwbr_set_troop_attribute_level, l.troop, l.attribute, l.attribute_lvl),
			# (try_end),
			# ]),
	#script.lwbr_set_troop_wpn_proficience_level
	# ("lwbr_set_troop_wpn_proficience_level",[
			# (store_script_param, l.troop, 1),
			# (store_script_param, l.proficience, 2),
			# (store_script_param, l.proficience_lvl, 3),
			# (store_proficiency_level,l.old_lvl,l.troop,l.proficience),
			# (try_begin),
			# 	(neq, l.proficience_lvl, l.old_lvl),
			# 	(val_sub, l.proficience_lvl, l.old_lvl),
			# 	(troop_raise_proficiency_linear,l.troop,l.proficience,l.proficience_lvl),
			# 	(store_proficiency_level,l.new_lvl,l.troop,l.proficience),
			# 	(try_begin),
			# 		(eq, lwbr.debug_mode, 1),
			# 		(eq, l.troop, trp.swadian_crossbowman_multiplayer),
			# 		(assign, reg1, l.old_lvl),
			# 		(assign, reg2, l.new_lvl),
			# 		(assign, reg3, l.proficience),
			# 		(str_store_troop_name, s2, l.troop),
			# 		(str_store_string, s1, "@DEBUG: Troop {s2} proficience '{reg3}' changed from {reg1} to {reg2}"),
			# 		#(call_script, script.lwbr_send_msg_to_all_players),
			# 		(server_add_message_to_log, s1),
			# 	(try_end),
			# (try_end),
			# ]),
	#script.lwbr_set_troop_all_wpn_proficiences_level
	# ("lwbr_set_troop_all_wpn_proficiences_level",[
			# (store_script_param, l.troop, 1),
			# (store_script_param, l.proficience_lvl, 2),
			# (try_for_range, l.proficience, 0, 4),
			# 	(call_script, script.lwbr_set_troop_wpn_proficience_level, l.troop, l.proficience, l.proficience_lvl),
			# (try_end),
			# ]),
	#script.lwbr_change_troop_stats_if_needed
	# ("lwbr_change_troop_stats_if_needed",[
			# (try_begin),
			# 	(eq, lwbr.debug_mode, 1),
			# 	(str_store_string, s1, "@Restoring troop stats"),
			# 	(server_add_message_to_log, s1),
			# (try_end),
			# (call_script, script.lwbr_restore_troop_stats_all),
			# (try_begin),
			# 	(eq, lwbr.debug_mode, 1),
			# 	(str_store_string, s1, "@Troop stats restored"),
			# 	(server_add_message_to_log, s1),
			# (try_end),
			# (try_begin),
			# 	(eq, "$g_lwbr_new_items", lwbr_new_items__peasant_items),
			# 	(try_for_range, l.troop, multiplayer_troops_begin, multiplayer_troops_end),
			# 		(call_script, script.lwbr_set_troop_all_attributes_level, l.troop, 10),
			# 		(call_script, script.lwbr_set_troop_all_wpn_proficiences_level, l.troop, 50),
			# 		(call_script, script.lwbr_set_troop_all_skills_level, l.troop, 0),
			# 	(try_end),
			# (else_try),
			# 	(eq, "$g_lwbr_new_items", lwbr_new_items__arena_items),
			# 	(try_for_range, l.troop, multiplayer_troops_begin, multiplayer_troops_end),
			# 		(call_script, script.lwbr_set_troop_all_attributes_level, l.troop, 20),
			# 		(call_script, script.lwbr_set_troop_all_wpn_proficiences_level, l.troop, 125),
			# 		(call_script, script.lwbr_set_troop_all_skills_level, l.troop, 5),
			# 	(try_end),
			# (try_end),
			# ]),
	#script.lwbr_get_mt_name_from_slot
	("lwbr_get_mt_name_from_slot",[
			(store_script_param, l.slot, 1),
			(store_add, l.val, l.slot, multiplayer_game_type_deathmatch - lwbr.scene_slots["available_dm"].id),
			(call_script, script.game_get_mission_template_name, l.val),
			]),
]

troops = [
	["lwbr_vars",   "{!}lwbr_vars",   "{!}lwbr_vars",   tf_hero|tf_inactive, 0, 0, 0, [], 0, 0, 0, 0, 0],
	["lwbr_sv_vars","{!}lwbr_sv_vars","{!}lwbr_sv_vars",tf_hero|tf_inactive, 0, 0, 0, [], 0, 0, 0, 0, 0],
	["lwbr_hotkeys","{!}lwbr_hotkeys","{!}lwbr_hotkeys",tf_hero|tf_inactive, 0, 0, 0, [], 0, 0, 0, 0, 0],
]

strings = [
	("sv_msg_1", "This server is running LWBR WarForge v%.3f"%(lwbr.mod_version/1000))
	] + [ ("sv_msg_%d"%i,"Default msg %d"%i) for i in xrange(2, lwbr.msg_cnt_max+1) ] + [
	] + foo__scn_names() + [
]

injection = {
	'lwbr_inject_escape_presentation_load' : [
		(create_button_overlay, g.lwbr_open_menu_overlay, "@LWBR WarForge menu"),
		(overlay_set_color, g.lwbr_open_menu_overlay, 0xFFFFFF),
		(overlay_set_pos, g.lwbr_open_menu_overlay, 10, 10),
		] + lwbr.debug([
			(create_button_overlay, g.lwbr_debug_overlay, "@LWBR debug"),
			(overlay_set_color, g.lwbr_debug_overlay, 0xFFFFFF),
			(overlay_set_pos, g.lwbr_debug_overlay, 250, 10),
		]) + [#end lwbr.debug
		],
	'lwbr_inject_escape_presentation_state_change' : [
		(else_try),
			(eq, l.object, g.lwbr_open_menu_overlay),
			(presentation_set_duration, 0),
			(start_presentation, prsnt.lwbr_menu),
			] + lwbr.debug([
				(else_try),
					(eq, l.object, g.lwbr_debug_overlay),
				] + foo__debug_vars() + [
			]) + [#end lwbr.debug
		],
	'lwbr_inject_events' : [
		(else_try),
			(assign, l.done, 0),
			(try_begin),
				# (eq, l.event_type, __),
				# (store_script_param, l.par1, 3),
				# ] + lwbr.debug_func("game_receive_network_message", [l.player_no, l.event_type, l.par1]) + [
				# (do_something),
				# (assign, l.done, 1),
			# (else_try),
				(eq, l.event_type, lwbr.multiplayer_event_server_str),
				(player_get_slot, l.par1, l.player_no, lwbr.player_slots["str_sending1"].id),(eq, l.par1, l.par1),
				(player_get_slot, l.par2, l.player_no, lwbr.player_slots["str_sending2"].id),(eq, l.par2, l.par2),
				(player_get_slot, l.par3, l.player_no, lwbr.player_slots["str_sending3"].id),(eq, l.par3, l.par3),
				(player_get_slot, l.par4, l.player_no, lwbr.player_slots["str_sending4"].id),(eq, l.par4, l.par4),
				(player_set_slot, l.player_no, lwbr.player_slots["str_sending1"].id, -1),
				(send_event_to_player, l.player_no, lwbr.multiplayer_event_client,#lwbr.sync_to_cl
					lwbr.cl_event.set_var, lwbr.cl_vars["str_sending1"].id, -1, 0, "WarForge"),
				(player_set_slot, l.player_no, lwbr.player_slots["str_sending2"].id, -1),
				(send_event_to_player, l.player_no, lwbr.multiplayer_event_client,#lwbr.sync_to_cl
					lwbr.cl_event.set_var, lwbr.cl_vars["str_sending2"].id, -1, 0, "WarForge"),
				(player_set_slot, l.player_no, lwbr.player_slots["str_sending3"].id, -1),
				(send_event_to_player, l.player_no, lwbr.multiplayer_event_client,#lwbr.sync_to_cl
					lwbr.cl_event.set_var, lwbr.cl_vars["str_sending3"].id, -1, 0, "WarForge"),
				(player_set_slot, l.player_no, lwbr.player_slots["str_sending4"].id, -1),
				(send_event_to_player, l.player_no, lwbr.multiplayer_event_client,#lwbr.sync_to_cl
					lwbr.cl_event.set_var, lwbr.cl_vars["str_sending4"].id, -1, 0, "WarForge"),
				] + lwbr.debug_func("multiplayer_event_server_str", [l.player_no, l.par1, l.par2, l.par3, l.par4]) + [
				] + lwbr.debug([(display_message, "@string is {s0}")]) + [
				(try_begin),
				    (eq, l.par1, lwbr.str_event.set_troop_name),
				    (troop_set_name, l.par2, s0),
				(try_end),
				(assign, l.done, 1),
			(else_try),
				(eq, l.event_type, lwbr.multiplayer_event_client_str),
				(get_lwbr_var, l.par1, "str_receiving1"),(eq, l.par1, l.par1),
				(get_lwbr_var, l.par2, "str_receiving2"),(eq, l.par2, l.par2),
				(get_lwbr_var, l.par3, "str_receiving3"),(eq, l.par3, l.par3),
				(get_lwbr_var, l.par4, "str_receiving4"),(eq, l.par4, l.par4),
				(set_lwbr_var, "str_receiving1", -1, lwbr.sync_to_sv),
				(set_lwbr_var, "str_receiving2", -1, lwbr.sync_to_sv),
				(set_lwbr_var, "str_receiving3", -1, lwbr.sync_to_sv),
				(set_lwbr_var, "str_receiving4", -1, lwbr.sync_to_sv),
				] + lwbr.debug_func("multiplayer_event_client_str", [l.player_no, l.par1, l.par2, l.par3, l.par4]) + [
				] + lwbr.debug([(display_message, "@string is {s0}")]) + [
				(try_begin),
				    (eq, l.par1, lwbr.str_event.set_troop_name),
				    (troop_set_name, l.par2, s0),
				(try_end),
				(assign, l.done, 1),
			(else_try),
				] + lwbr.debug_func("game_receive_network_message", [l.player_no, l.event_type]) + [
			(try_end),
			(neq, l.done, 0),
		],
	'lwbr_inject_server_only_events' : [
		(else_try),#set_sv_var
			(eq, l.type, lwbr.sv_event.set_sv_var),
			(store_script_param, l.slot, 4),
			(store_script_param, l.val, 5),
			] + lwbr.debug_func("sv_event.set_sv_var", [l.slot, l.val]) + [
			(try_begin),
				(try_begin),#invalid player
					(neg|player_is_active, l.player_no),
					(assign, reg0, l.player_no),
					(log_action, "@Error: invalid player id #{reg0} at sv_event.set_sv_var #{reg0} -> {reg1}", -1, lwbr.silent),
				(else_try),#not admin
					(neg|player_is_admin, l.player_no),
					(str_store_player_username, s0, l.player_no),
					(assign, reg0, l.slot),
					(assign, reg1, l.val),
					(log_action, "@Error: non-admin player {s0} at sv_event.set_sv_var #{reg0} -> {reg1}", -1, lwbr.silent),
				(else_try),#invalid var
					(neg|is_between, l.slot, 0, lwbr._var.count["sv"]),
					(assign, reg0, l.slot),
					(log_action, "@Error: invalid or unrecognized sv_var #{reg0} at sv_event.set_sv_var", -1, lwbr.silent),
				(else_try),#valid
					(get_lwbr_sv_var, l.old_val, l.slot),
					(set_lwbr_sv_var, l.slot, l.val, lwbr.sync_to_cl),
					(assign, l.logged, 0),
					(try_begin),#items
						(eq, l.slot, lwbr.sv_vars["items"].id),
						(call_script, script.lwbr_give_items_to_troops, l.val),
						(try_for_players, l.pl),#force players to reselect items
							(player_is_active, l.pl),
							(send_event_to_player, l.pl, lwbr.multiplayer_event_client, lwbr.cl_event.clear_items),
							(multiplayer_get_my_player, l.me),
							(neq, l.pl, l.me),
							(send_event_to_player, l.pl, multiplayer_event_force_start_team_selection),
						(try_end),
					(else_try),#msg_cont
						(eq, l.slot, lwbr.sv_vars["msg_cnt"].id),
						(store_add, l.end, l.val, lwbr.msg_troops_begin),
						(store_add, l.begin, l.old_val, lwbr.msg_troops_begin),
						(try_for_range, l.trp, l.begin, l.end),
							(str_store_troop_name, s0, l.trp),
							(send_str_to_players, "@{s0}", lwbr.multiplayer_event_client_str,
								lwbr.str_event.set_troop_name, l.trp, 0, "-Server|WarForge|Admin", lwbr.silent),
						(try_end),
						(assign, reg0, l.val),
						(log_action, "@Changing # of server messages to #{reg0}", l.player_no, lwbr.verbose),
						(assign, l.logged, 1),
					(try_end),
					(try_begin),
						(eq, l.logged, 0),
						(assign, reg0, l.slot),
						(assign, reg1, l.old_val),
						(assign, reg2, l.val),
						(log_action, "@Changing server var #{reg0} from {reg1} to {reg2}", l.player_no, lwbr.verbose),
					(try_end),
				(try_end),
			(try_end),
		(else_try),#ask_sv_var
			(eq, l.type, lwbr.sv_event.ask_sv_var),
			(store_script_param, l.slot, 4),
			] + lwbr.debug_func("sv_event.ask_sv_var", [l.slot]) + [
			(try_begin),
				(neg|is_between, l.slot, 0, lwbr._var.count["sv"]),
				(assign, reg0, l.slot),
				(log_action, "@Error: invalid or unrecognized sv_var #{reg0} at sv_event.ask_sv_var", l.player_no, lwbr.silent),
			(else_try),
				(get_lwbr_sv_var, l.val, l.slot),
				(send_event_to_player, l.player_no, lwbr.multiplayer_event_client,
					lwbr.cl_event.return_sv_var, l.slot, l.val, 0, "-Server|WarForge"),
			(try_end),
		(else_try),#return_var
			(eq, l.type, lwbr.sv_event.return_var),
			(store_script_param, l.slot, 4),
			(store_script_param, l.val, 5),
			] + lwbr.debug_func("sv_event.return_var", [l.slot, l.val]) + [
			(try_begin),
				(eq, l.slot, lwbr.cl_vars["version"].id),
				(player_set_slot, l.player_no, lwbr.player_slots["version"].id, l.val),
			(else_try),
				(eq, l.slot, lwbr.cl_vars["nxt_scn_info"].id),
				(player_set_slot, l.player_no, lwbr.player_slots["nxt_scn_info"].id, l.val),
			(else_try),
				(is_between, l.slot, lwbr.cl_vars["str_sending1"].id, lwbr.cl_vars["str_receiving4"].id+1),
				(val_add, l.slot, lwbr.player_slots["str_sending1"].id - lwbr.cl_vars["str_sending1"].id),
				(player_set_slot, l.player_no, l.slot, l.val),
			(else_try),
				(assign, reg0, l.slot),
				(log_action, "@Error: invalid or unrecognized returned var #{reg0} at sv_event.return_var", l.player_no, lwbr.silent),
			(try_end),
		(else_try),#action
			(eq, l.type, lwbr.sv_event.action),
			(store_script_param, l.action, 4),
			(try_begin),
				(call_script, script.lwbr_do_action, l.action, l.player_no),
				(assign, l.error, reg42),
				(try_begin),
					(eq, l.error, 0),
					(try_begin),
						(call_script, script.cf_lwbr_is_adm_action, l.action),
						(assign, reg0, l.action),
						(log_action, "@Doing admin action #{reg0}", l.player_no, lwbr.verbose),
						# (log_action, "@Doing admin action #{reg0}", l.player_no, lwbr.verbose),
					(else_try),
						(assign, reg0, l.action),
						(log_action, "@Doing action #{reg0}", l.player_no, lwbr.verbose),
					(try_end),
				(else_try),
					(eq, l.error, 1),
					(assign, reg0, l.action),
					(log_action, "@Error: invalid or unrecognized action #{reg0} at sv_event.action", l.player_no, lwbr.verbose),
				(else_try),
					(eq, l.error, 2),
					(assign, reg0, l.action),
					(log_action, "@Error: invalid player at sv_event.action", -1, lwbr.verbose),
				(else_try),
					(eq, l.error, 3),
					(assign, reg0, l.action),
					(log_action, "@Error: admin only action #{reg0}", l.player_no, lwbr.verbose),
				(else_try),
					(eq, l.error, 4),
					(assign, reg0, l.action),
					(log_action, "@Error: action #{reg0} still in cooldown", l.player_no, lwbr.verbose),
				(try_end),
			(try_end),
		],
	'lwbr_inject_client_only_events' : [
		(else_try),#set_var
			(eq, l.type, lwbr.cl_event.set_var),
			(store_script_param, l.slot, 4),
			(store_script_param, l.val, 5),
			] + lwbr.debug_func("cl_event.set_var", [l.slot, l.val]) + [
			(try_begin),
				(neg|is_between, l.slot, 0, lwbr._var.count["cl"]),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid or unrecognized var #{reg0} at cl_event.set_var"),
			(else_try),
				(set_lwbr_var, l.slot, l.val),
				# (try_begin),
				# 	(eq, l.slot, lwbr.cl_vars["---"]..idid),
				# 	---
				# (try_end),
			(try_end),
		(else_try),#ask_var
			(eq, l.type, lwbr.cl_event.ask_var),
			(store_script_param, l.slot, 4),
			] + lwbr.debug_func("cl_event.ask_var", [l.slot]) + [
			(try_begin),
				(neg|is_between, l.slot, 0, lwbr._var.count["cl"]),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid or unrecognized var #{reg0} at cl_event.ask_var"),
			(else_try),
				(get_lwbr_var, l.val, l.slot),
				(send_event_to_server, lwbr.multiplayer_event_server, lwbr.sv_event.return_var, l.slot, l.val),
			(try_end),
		(else_try),#return_sv_var
			(eq, l.type, lwbr.cl_event.return_sv_var),
			(store_script_param, l.slot, 4),
			(store_script_param, l.val, 5),
			] + lwbr.debug_func("cl_event.return_sv_var", [l.slot,l.val]) + [
			(try_begin),
				(neg|is_between, l.slot, 0, lwbr._var.count["sv"]),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid or unrecognized sv_var #{reg0} at cl_event.return_sv_var"),
			(else_try),
				(set_lwbr_sv_var, l.slot, l.val),
				(try_begin),
					(eq, l.slot, lwbr.sv_vars["items"].id),
					(call_script, script.lwbr_give_items_to_troops, l.val),
				(try_end),
			(try_end),
		(else_try),#set_faction_slot
			(eq, l.type, lwbr.cl_event.set_faction_slot),
			(store_script_param, l.faction, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_faction_slot", [l.faction, l.slot, l.slot]) + [
			(try_begin),
				(is_between, l.faction, 0, fac.end),
				(faction_set_slot, l.faction, l.slot, l.val),
			(else_try),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid faction #{reg0} at cl_event.set_faction_slot"),
			(try_end),
		(else_try),#set_item_slot
			(eq, l.type, lwbr.cl_event.set_item_slot),
			(store_script_param, l.item, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_item_slot", [l.item, l.slot, l.slot]) + [
			(try_begin),
				(is_between, l.item, 0, itm.end),
				(item_set_slot, l.item, l.slot, l.val),
			(else_try),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid item #{reg0} at cl_event.set_item_slot"),
			(try_end),
		(else_try),#set_party_slot
			(eq, l.type, lwbr.cl_event.set_party_slot),
			(store_script_param, l.party, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_party_slot", [l.party, l.slot, l.slot]) + [
			(try_begin),
				(is_between, l.party, 0, p.end),
				(party_set_slot, l.party, l.slot, l.val),
			(else_try),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid party #{reg0} at cl_event.set_party_slot"),
			(try_end),
		(else_try),#set_pt_slot
			(eq, l.type, lwbr.cl_event.set_pt_slot),
			(store_script_param, l.pt, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_pt_slot", [l.pt, l.slot, l.slot]) + [
			(try_begin),
				(is_between, l.pt, 0, pt.end),
				(party_template_set_slot, l.pt, l.slot, l.val),
			(else_try),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid pt #{reg0} at cl_event.set_pt_slot"),
			(try_end),
		(else_try),#set_quest_slot
			(eq, l.type, lwbr.cl_event.set_quest_slot),
			(store_script_param, l.quest, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_quest_slot", [l.quest, l.slot, l.slot]) + [
			(try_begin),
				(is_between, l.quest, 0, qst.end),
				(quest_set_slot, l.quest, l.slot, l.val),
			(else_try),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid quest #{reg0} at cl_event.set_quest_slot"),
			(try_end),
		(else_try),#set_sp_slot
			(eq, l.type, lwbr.cl_event.set_sp_slot),
			(store_script_param, l.sp, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_sp_slot", [l.sp, l.slot, l.slot]) + [
			(try_begin),
				(is_between, l.sp, 0, spr.end),
				(scene_prop_set_slot, l.sp, l.slot, l.val),
			(else_try),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid sp #{reg0} at cl_event.set_sp_slot"),
			(try_end),
		(else_try),#set_scene_slot
			(eq, l.type, lwbr.cl_event.set_scene_slot),
			(store_script_param, l.scene, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			(try_begin),
				(neg|is_between, l.slot, lwbr.scene_slots["available_dm"].id, lwbr.scene_slots["cur_wt_fgC"].id+1),
				] + lwbr.debug_func("cl_event.set_scene_slot", [l.scene, l.slot, l.slot]) + [
			(try_end),
			(try_begin),
				(is_between, l.scene, 0, scn.end),
				(scene_set_slot, l.scene, l.slot, l.val),
				(try_begin),
					(is_between, l.slot, lwbr.scene_slots["available_dm"].id, lwbr.scene_slots["cur_wt_fgC"].id+1),
					(get_lwbr_var, l.val, "nxt_scn_info"),
					(val_max, l.val, l.scene+1),
					(set_lwbr_var, "nxt_scn_info", l.val),
				(try_end),
			(else_try),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid scene #{reg0} at cl_event.set_scene_slot"),
			(try_end),
		(else_try),#set_team_slot
			(eq, l.type, lwbr.cl_event.set_team_slot),
			(store_script_param, l.team, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_team_slot", [l.team, l.slot, l.slot]) + [
			# (try_begin),
				# (is_between, l.team, 0, tm.end),
				(team_set_slot, l.team, l.slot, l.val),
			# (else_try),
				# (assign, reg0, l.slot),
				# (display_message, "@Error: invalid team #{reg0} at cl_event.set_team_slot"),
			# (try_end),
		(else_try),#set_agent_slot
			(eq, l.type, lwbr.cl_event.set_agent_slot),
			(store_script_param, l.agent, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_agent_slot", [l.agent, l.slot, l.slot]) + [
			# (try_begin),
				# (is_between, l.agent, 0, ag.end),
				(agent_set_slot, l.agent, l.slot, l.val),
			# (else_try),
				# (assign, reg0, l.slot),
				# (display_message, "@Error: invalid agent #{reg0} at cl_event.set_agent_slot"),
			# (try_end),
		(else_try),#set_troop_slot
			(eq, l.type, lwbr.cl_event.set_troop_slot),
			(store_script_param, l.troop, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_troop_slot", [l.troop, l.slot, l.slot]) + [
			(try_begin),
				(is_between, l.troop, 0, trp.end),
				(troop_set_slot, l.troop, l.slot, l.val),
			(else_try),
				(assign, reg0, l.slot),
				(display_message, "@Error: invalid troop #{reg0} at cl_event.set_troop_slot"),
			(try_end),
		(else_try),#set_player_slot
			(eq, l.type, lwbr.cl_event.set_player_slot),
			(store_script_param, l.player, 4),
			(store_script_param, l.slot, 5),
			(store_script_param, l.val, 6),
			] + lwbr.debug_func("cl_event.set_player_slot", [l.player, l.slot, l.slot]) + [
			# (try_begin),
				# (is_between, l.player, 0, pl.end),
				(player_set_slot, l.player, l.slot, l.val),
			# (else_try),
				# (assign, reg0, l.slot),
				# (display_message, "@Error: invalid player #{reg0} at cl_event.set_player_slot"),
			# (try_end),
		(else_try),#clear_items
			(eq, l.type, lwbr.cl_event.clear_items),
			] + lwbr.debug_func("cl_event.clear_items") + [
			(call_script, script.lwbr_force_change_weapons),
		],
	'lwbr_inject_server_before_mission_start' : [
		(call_script, script.lwbr_server_start, 0),
		(call_script, script.lwbr_player_start, 0),
		(store_current_scene, l.scn),
		(call_script, script.lwbr_set_weather, l.scn),
		],
	'lwbr_inject_on_non_player_spawn' : [],
	'lwbr_inject_on_player_spawn' : [],
	'lwbr_inject_player_join' : [
		] + lwbr.sv_version([
			(log_action, "@Joined the server", l.player_no, lwbr.verbose),

			(call_script, script.lbwr_init_player, l.player_no),
			(call_script, script.lwbr_ask_player_info, l.player_no),
			(try_begin),
				(filter_player, l.player_no, "-Server"),
				(call_script, script.lwbr_send_player_info, l.player_no),
			(try_end),
			(store_current_scene, l.scn),
			(call_script, script.game_get_scene_name, l.scn),
			(multiplayer_send_string_to_player, l.player_no, multiplayer_event_show_server_message, "@Current map is '{s0}'"),
		]) + [#end lwbr.sv_version
		],
	'lwbr_inject_once_at_first_frame' : [
		(call_script, script.lwbr_player_start, 1),
		(call_script, script.lwbr_server_start, 1),
		],
	'lwbr_inject_mt_common' : [
		] + lwbr.cl_version(
			[#actions
				(0, 0, lwbr.actions[act].cd, [
					(multiplayer_get_my_player, l.me),
					(neg|player_is_busy_with_menus, l.me),
					(get_lwbr_hotkey, l.hk, lwbr.actions[act].id),
					(key_clicked, l.hk),
					(display_message, "@doing action %d"%lwbr.actions[act].id),
					], [ (send_event_to_server, lwbr.multiplayer_event_server, lwbr.sv_event.action, lwbr.actions[act].id), ])\
				for act in lwbr.actions if not lwbr.actions[act].adm
			] + [#admin actions
				(0, 0, lwbr.actions[act].cd, [
					(multiplayer_get_my_player, l.me),
					(neg|player_is_busy_with_menus, l.me),
					(player_is_admin, l.me),
					(get_lwbr_hotkey, l.hk, lwbr.actions[act].id),
					(key_clicked, l.hk),
					] + lwbr.debug([(display_message, "@doing admin action %d"%lwbr.actions[act].id),]) + [
					], [ (send_event_to_server, lwbr.multiplayer_event_server, lwbr.sv_event.action, lwbr.actions[act].id), ])\
				for act in lwbr.actions if lwbr.actions[act].adm
			]
		) + [#end cl_version
		] + lwbr.sv_version([
			(1, 0, 0, [],[#send weather
					(try_begin),
						(multiplayer_is_server),
						] + lwbr.sv_version([
							(get_max_players, l.mx),
							(val_mod, g.lwbr_wt_send_pl_iter, l.mx),
							(assign, g.lwbr_wt_events_sent, 0),
							# ] + lwbr.debug([
							# 	(assign, reg0, g.lwbr_wt_send_pl_iter),
							# 	(assign, reg1, l.mx),
							# 	(display_message, "@send weather: starting at player {reg0}/{reg1}"),
							# ]) + [#end lwbr.debug
							(try_for_range, g.lwbr_wt_send_pl_iter, g.lwbr_wt_send_pl_iter, l.mx),
								(player_is_active, g.lwbr_wt_send_pl_iter),
								(filter_player, g.lwbr_wt_send_pl_iter, "-Server"),
								] + lwbr.debug([
									(assign, reg0, g.lwbr_wt_send_pl_iter),
									(display_message, "@send weather: sending to player {reg0}/{reg1}"),
								]) + [#end lwbr.debug
								(call_script, script.lwbr_send_weather_info, g.lwbr_wt_send_pl_iter),

								(ge, g.lwbr_wt_events_sent, lwbr.wt_event_limit),
								(assign, l.mx, 0),
							(try_end),
							(val_add, g.lwbr_wt_send_pl_iter, 1),
							# ] + lwbr.debug([
							# 	(assign, reg0, g.lwbr_wt_events_sent),
							# 	(assign, reg1, lwbr.wt_event_limit),
							# 	(display_message, "@send weather: sent {reg0}/{reg1} events"),
							# ]) + [#end lwbr.debug
						]) + [#end lwbr.sv_version
					(try_end),
					]),
			(1, 0, 0, [],[#show server messages
					(get_lwbr_sv_var, l.cur_tm, "msg_cur_tm"),
					(get_lwbr_sv_var, l.max_tm, "msg_cd"),
					(get_lwbr_sv_var, l.cur_id, "msg_cur_id"),
					(get_lwbr_sv_var, l.max_id, "msg_cnt"),
					(gt, l.max_tm, 0),
					(try_begin),
						(ge, l.cur_tm, l.max_tm),
						(assign, l.cur_tm, 0),
						(str_store_troop_name, s0, lwbr.msg_troops_begin+l.cur_id),
						(try_for_players, l.pl),
							(multiplayer_send_string_to_player, l.pl, multiplayer_event_show_server_message, "@{s0}"),
						(try_end),
						(val_add, l.cur_id, 1),
						(val_mod, l.cur_id, l.max_id),
					(try_end),
					(val_add, l.cur_tm, 1),
					(set_lwbr_sv_var, "msg_cur_tm", l.cur_tm),
					(set_lwbr_sv_var, "msg_cur_id", l.cur_id),
					]),
			(ti_on_multiplayer_mission_end, 0, 0, [],[#recalc weather for cur scn
					(try_begin),
						(multiplayer_is_server),
						] + lwbr.sv_version([
							(store_current_scene, l.scn),
							(call_script, script.lwbr_calc_weather, l.scn),
						]) + [#end lwbr.sv_version
					(try_end),
					]),
			(5, 0, 0, [], [#min version
					(try_begin),
						(multiplayer_is_server),
						] + lwbr.sv_version([
							(get_lwbr_sv_var, l.min_version, "min_version"),
							(gt, l.min_version, 0),
							(try_for_players, l.pl),
								(player_get_slot, l.version, l.pl,  lwbr.player_slots["version"].id),
								(lt, l.version, l.min_version),
								(try_begin),
									(eq, l.version, lwbr.native),
									(str_store_string, s0, "@Native"),
								(else_try),
									(store_div, reg0, l.version, 1000),
									(store_mod, reg1, l.version, 1000),
									(str_store_string, s1, "@v{reg0}.{reg1}"),
								(try_end),
								(store_mission_timer_a, l.cur_time),
								(player_get_slot, l.join_time, l.pl, slot_player_join_time),
								(store_div, reg0, l.min_version, 1000),
								(store_mod, reg1, l.min_version, 1000),
								(str_store_string, s0, "@This server requires LWBR WarForge v{reg0}.{reg1}, you seem to be using {s0}"),
								(str_store_player_username, s1, l.pl),
								(try_begin),
									(store_add, l.join_time8, l.join_time, 8),
									(gt, l.cur_time, l.join_time8),
									(multiplayer_send_string_to_player, l.pl, multiplayer_event_show_server_message,
										"@{s0}, you will be kicked now"),
									(server_add_message_to_log, "@Player {s1} has been kicked due to not using the required WarForge version({s1}, needs {s0})"),
									(kick_player, l.pl),
								(else_try),
									(store_add, l.join_time4, l.join_time, 4),
									(gt, l.cur_time, l.join_time4),
									(multiplayer_send_string_to_player, l.pl, multiplayer_event_show_server_message,
										"@{s0}, you will be kicked within 5 seconds"),
								(try_end),
							(try_end),
						]) + [#end lwbr.sv_version
					(try_end),
					]),
			(ti_on_player_exit, 0, 0, [],[#player exited message
					(try_begin),
						(multiplayer_is_server),
						(store_trigger_param_1, l.player_no),
						(log_action, "@Left the server", l.player_no, lwbr.verbose),
					(try_end),
					]),
		]) + [#end sv_version
		],
	'lwbr_inject_mt_deathmatch' : [],
	'lwbr_inject_mt_t_deathmatch' : [],
	'lwbr_inject_mt_headquarters' : [],
	'lwbr_inject_mt_capture_the_flag' : [],
	'lwbr_inject_mt_siege' : [],
	'lwbr_inject_mt_battle' : [],
	'lwbr_inject_mt_fight_and_destroy' : [],
	'lwbr_inject_mt_coop' : [],
	'lwbr_inject_mt_duel' : [],
	'lwbr_inject_buy_equipment' : [
		(get_lwbr_sv_var, l.gm, "game_mode"),
		] + lwbr.debug_func("lwbr_inject_buy_equipment", [l.player_no, l.packs]) + [
		# try_begin # lwbr_buy_peasant_items
			(eq, l.gm, lwbr.game_modes["peasantWars"].id),
			] + lwbr.debug_func("lwbr_buy_peasant_items") + [
			(try_begin),
				(player_get_troop_id, l.trp, l.player_no),
				(gt, l.trp, 0),
				(troop_get_type_counts,l.cnt_horses,
									   l.cnt_1h,l.cnt_2h,l.cnt_pole,
									   l.cnt_arrow,l.cnt_bolt,
									   l.cnt_shield,
									   l.cnt_bow,l.cnt_xbow,l.cnt_th,
									   l.rest,
									   l.cnt_helm,l.cnt_armor,l.cnt_boots,l.cnt_gloves,
									   l.rest,l.rest,l.rest,l.rest,l.rest,
									   l.trp),
				(try_chance,80),#80%
					] + lwbr.debug_func("bought_head_armor", [l.player_no, l.cnt_helm]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_head_armor,	l.cnt_helm,  ek_head,   l.player_no),
				(try_end),
				(try_chance,90),#90%
					] + lwbr.debug_func("bought_body_armor", [l.player_no, l.cnt_armor]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_body_armor,	l.cnt_armor, ek_body,   l.player_no),
				(try_end),
				(try_chance,95),#95%
					] + lwbr.debug_func("bought_foot_armor", [l.player_no, l.cnt_boots]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_foot_armor,	l.cnt_boots, ek_foot,   l.player_no),
				(try_end),
				(try_chance,25),#25%
					] + lwbr.debug_func("bought_hand_armor", [l.player_no, l.cnt_gloves]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_hand_armor,	l.cnt_gloves,ek_gloves, l.player_no),
				(try_end),
				(try_chance,3),#3%
					] + lwbr.debug_func("bought_horse", [l.player_no, l.cnt_horses]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_horse,			l.cnt_horses,ek_horse,  l.player_no),
				(try_end),
				(try_chance,50),#50%
					] + lwbr.debug_func("bought_1h", [l.player_no, l.cnt_1h]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_one_handed_wpn,l.cnt_1h,    ek_item_0, l.player_no),
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_shield,		l.cnt_shield,ek_item_1, l.player_no),
				# (else_try_chance),
				# 	] + lwbr.debug_func("bought_2h", [l.player_no, l.cnt_2h]) + [
				# 	(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_two_handed_wpn,l.cnt_2h,    ek_item_0, l.player_no),
				(else_try),#50%
					] + lwbr.debug_func("bought_pole", [l.player_no, l.cnt_pole]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_polearm,		l.cnt_pole,  ek_item_0, l.player_no),
				(try_end),
				(try_chance,75),#75%
					] + lwbr.debug_func("bought_thrown", [l.player_no, l.cnt_th]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_thrown,		l.cnt_th,    ek_item_2, l.player_no),
				(else_try_chance, 20),#5%
					] + lwbr.debug_func("bought_bow", [l.player_no, l.cnt_bow]) + [
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_bow,			l.cnt_bow,   ek_item_2, l.player_no),
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_arrows,		l.cnt_arrow, ek_item_3, l.player_no),
				(try_end),
			(try_end),
		(else_try),# lwbr_buy_tournament_items
			(eq, l.gm, lwbr.game_modes["tournament"].id),
			] + lwbr.debug_func("lwbr_buy_tournament_items") + [
			(try_begin),
				(player_get_troop_id, l.trp, l.player_no),
				(gt, l.trp, 0),
				(troop_get_type_counts,l.cnt_horses,
									   l.cnt_1h,l.cnt_2h,l.cnt_pole,
									   l.cnt_arrow,l.cnt_bolt,
									   l.cnt_shield,
									   l.cnt_bow,l.cnt_xbow,l.cnt_th,
									   l.rest,
									   l.cnt_helm,l.cnt_armor,l.cnt_boots,l.cnt_gloves,
									   l.rest,l.rest,l.rest,l.rest,l.rest,
									   l.trp),

				#add armor
				(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_head_armor, l.cnt_helm,  ek_head,  l.player_no),
				(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_body_armor, l.cnt_armor, ek_body,  l.player_no),
				(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_hand_armor, l.cnt_gloves,ek_gloves,l.player_no),
				(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_foot_armor, l.cnt_boots, ek_foot,  l.player_no),

				(try_begin),#horse
					(player_get_slot, l.horse, l.player_no, slot_player_selected_item_indices_begin + 8),#horse slot
					(ge, l.horse, 0),
					] + lwbr.debug_func("picked_mounted_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_horse, itm.practice_horse),
				(try_end),

				(player_get_slot, l.wpn, l.player_no, slot_player_selected_item_indices_begin),#1st wpn slot
				(assign, l.itm_type, -1),
				(assign, l.itm_class, -1),
				(try_begin),
					(ge, l.wpn, 0),
					(item_get_type, l.itm_type, l.wpn),
					(item_get_slot, l.itm_class, l.wpn, slot_item_multiplayer_item_class),
				(try_end),

				(try_begin),#lance/shield/dagger
					(eq, l.wpn, itm.practice_lance),
					] + lwbr.debug_func("picked_lancer_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_item_0, itm.practice_lance),
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_shield, l.cnt_shield, ek_item_1, l.player_no),
					(player_add_spawn_item, l.player_no, ek_item_2, itm.practice_dagger),
				(else_try),#staff/throwing dagger
					(this_or_next|eq, l.wpn, itm.practice_staff),
					(eq, l.wpn, itm.practice_throwing_daggers),
					] + lwbr.debug_func("picked_staff_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_item_0, itm.practice_staff),
					(player_add_spawn_item, l.player_no, ek_item_1, itm.practice_throwing_daggers),
				(else_try),#javelin/shield/dagger
					(eq, l.wpn, itm.practice_javelin),
					] + lwbr.debug_func("picked_javelin_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_item_0, itm.practice_javelin),
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_shield, l.cnt_shield, ek_item_1, l.player_no),
					(player_add_spawn_item, l.player_no, ek_item_1, itm.practice_dagger),
				(else_try),#bow/dagger
					(this_or_next|eq, l.itm_type, itp_type_bow),
					(eq, l.itm_type, itp_type_arrows),
					] + lwbr.debug_func("picked_bow_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_item_0, itm.practice_bow),
					(player_add_spawn_item, l.player_no, ek_item_1, itm.practice_arrows),
					(player_add_spawn_item, l.player_no, ek_item_2, itm.practice_dagger),
				(else_try),#xbow/dagger
					(this_or_next|eq, l.itm_type, itp_type_crossbow),
					(eq, l.itm_type, itp_type_bolts),
					] + lwbr.debug_func("picked_xbow_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_item_0, itm.practice_crossbow),
					(player_add_spawn_item, l.player_no, ek_item_1, itm.practice_bolts),
					(player_add_spawn_item, l.player_no, ek_item_2, itm.practice_dagger),
				(else_try),#2h
					(eq, l.itm_type, itp_type_two_handed_wpn),
					] + lwbr.debug_func("picked_2h_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_item_0, itm.heavy_practice_sword),
				(else_try),#1h axe/shield
					(eq, l.itm_type, itp_type_one_handed_wpn),
					(eq, l.itm_class, multi_item_class_type_axe),
					] + lwbr.debug_func("picked_axe_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_item_0, itm.practice_axe),
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_shield, l.cnt_shield, ek_item_1, l.player_no),
				(else_try),#1h sword/shield -> default
					# (this_or_next|eq, l.itm_type, itp_type_one_handed_wpn),
					# (eq, l.type, itp_type_shield),
					] + lwbr.debug_func("picked_1h_kit", [l.player_no]) + [
					(player_add_spawn_item, l.player_no, ek_item_0, itm.practice_sword),
					(call_script, script.lwbr_add_rnd_itm_of_type, l.trp, itp_type_shield, l.cnt_shield, ek_item_1, l.player_no),
				(try_end),
			(try_end),
		(else_try),# normal
			(neq, l.gm, lwbr.game_modes["native"].id),
			(assign, reg0, l.gm),
			(display_message, "@Error: invalid 'game mode' selected: #{reg0}"),
		(else_try),# normal
			] + lwbr.debug_func("lwbr_buy_normal_items") + [
			] + lwbr.debug([
				(try_for_range, l.slot, slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
					(player_get_slot, l.itm, l.player_no, l.slot),
					(ge, l.itm, 0),
					(str_store_item_name, s0, l.itm),
					(display_message, "@buying item '{s0}'"),
				(try_end),
			]) + [
		# try_end
		],
	'lwbr_inject_get_scene_name' : [
			(str_store_string, s0, l.scene_no + s.scn_random_scene),#first scene is scn.random_scene
		(else_try),
		]
}



#LWBR WarForge 2.0 --- BEGIN
#LWBR WarForge 2.0 --- END

