from compiler import *
register_plugin(__name__)

class typ:
	blank,open_container,close_container,text,checkbox,numbox,button,combo_button,code = xrange(9)

	def_y_sz = 30
	y_sz = {
		open_container: 0,
		close_container: 1.33 * def_y_sz,
		code: 0,
		combo_button: 2.5 * def_y_sz,
	}
def y_sz(tp):
	if typ.y_sz.has_key(tp): return typ.y_sz[tp]
	return typ.def_y_sz
def get_x(in_container):
	if in_container: return 10
	return 300



def make_presentation(name,flags,args,opts):

	load = [
		(set_fixed_point_multiplier, 1000),
		(create_mesh_overlay, reg0, mesh.mp_ingame_menu),
		(overlay_set_pos, reg0, 250, 80),
		(overlay_set_sz, reg0, 1000, 1000),
		(presentation_set_duration, 999999),
		(assign,l.cur_y,600),
		#Little Pos Helper by Kuba begin
		(create_text_overlay, g.lwbr_little_pos_helper, "@00,00"),
			(overlay_set_color, g.lwbr_little_pos_helper, 0xFFFFFFFF),
			(overlay_set_pos, g.lwbr_little_pos_helper, 10, 700),
		#Little Pos Helper by Kuba end
	]
	in_container = False
	for opti in xrange(len(opts)):
		opt = opts[opti]

		load += [(assign,l.cur_overlay,0),]

		if opt[0] in (typ.blank,typ.code,typ.open_container,typ.close_container):
			if opt[0] == typ.open_container:
				if in_container:
					print "\n\nError: opening container inside another container at plugin_make_presentations, option #%d, presentation %s\n" % (opti,name)
					exit(1)

				tot = 0
				for optj in xrange(opti,len(opts)):
					if opts[optj][0] == typ.close_container: break
					tot += y_sz(opts[optj][0])
				tot = max(tot,opt[2]-50)

				load += [
					(val_sub,l.cur_y,opt[2]),
					(str_clear,s0),
					(create_text_overlay, l.cur_overlay, s0, tf_scrollable),
					(overlay_set_pos, l.cur_overlay, get_x(in_container), l.cur_y),
					(overlay_set_area_sz, l.cur_overlay, opt[1], opt[2]),
					(set_container_overlay, l.cur_overlay),
					(assign,l.out_y,l.cur_y),
					(assign,l.cur_y,tot),
				]
				in_container = True
			elif opt[0] == typ.close_container:
				if not in_container:
					print "\n\nError: closing container outside of any container at plugin_make_presentations, option #%d, presentation %s\n" % (opti,name)
					exit(1)
				load += [
					(set_container_overlay, -1),
					(assign,l.cur_y,l.out_y),
				]
				in_container = False
			elif opt[0] == typ.code:
				#
				load += opt[1]
			load += [(val_sub,l.cur_y,y_sz(opt[0])),]
		else:
			load += [
				(try_begin),
					(assign, l.val, 0),
			] + opt[2]

			if opt[0] == typ.text:
				load += [
					(create_text_overlay, l.cur_overlay, "@"+opt[1]),
					(overlay_set_color, l.cur_overlay, 0xFFFFFF),
					(overlay_set_pos, l.cur_overlay, get_x(in_container), l.cur_y),
				]
			elif opt[0] == typ.checkbox:
				load += [
					(create_text_overlay, l.cur_overlay, "@"+opt[1]),
					(overlay_set_color, l.cur_overlay, 0xFFFFFF),
					(overlay_set_pos, l.cur_overlay, get_x(in_container) + 30, l.cur_y),
					(create_check_box_overlay, l.cur_overlay, mesh.checkbox_off, mesh.checkbox_on),
					(overlay_set_pos, l.cur_overlay, get_x(in_container), l.cur_y+5),
					(overlay_set_val, l.cur_overlay, l.val),
				]
			elif opt[0] == typ.numbox:
				load += [
					(create_text_overlay, l.cur_overlay, "@"+opt[1]),
					(overlay_set_color, l.cur_overlay, 0xFFFFFF),
					(overlay_set_pos, l.cur_overlay, get_x(in_container) + 75, l.cur_y),
					(create_number_box_overlay, l.cur_overlay, opt[4], opt[5]),
					(overlay_set_pos, l.cur_overlay, get_x(in_container), l.cur_y),
					(overlay_set_val, l.cur_overlay, l.val),
				]
			elif opt[0] == typ.button:
				load += [
					(create_button_overlay, l.cur_overlay, "@"+opt[1]),
					(overlay_set_color, l.cur_overlay, 0xFFFFFF),
					(overlay_set_pos, l.cur_overlay, get_x(in_container), l.cur_y),
				]
			elif opt[0] == typ.combo_button:
				load += [(try_begin),]
				load += opt[3]
				load += [
					(create_text_overlay, l.cur_overlay, "@"+opt[1]),
					(overlay_set_color, l.cur_overlay, 0xFFFFFF),
					(overlay_set_pos, l.cur_overlay, get_x(in_container), l.cur_y),

					(create_combo_button_overlay, l.cur_overlay),
					(overlay_set_color, l.cur_overlay, 0xFFFFFF),
					(overlay_set_pos, l.cur_overlay, get_x(in_container)+140, l.cur_y - (1.25*y_sz(typ.text))),
				]
				for combo_opt in opt[4]: load += [(overlay_add_item, l.cur_overlay, "@"+combo_opt),]
				load += [(try_end),]
			load += [
					(val_sub,l.cur_y,y_sz(opt[0])),
				(try_end),
			]

		load += [(troop_set_slot,trp.lwbr_prsnt_vars,opti,l.cur_overlay),]

	change = [
		(store_trigger_param_1, l.obj),
		(store_trigger_param_2, l.val),
		(try_begin),
			(eq,1,0),
		#
	]
	for opti in xrange(len(opts)):
		opt = opts[opti]
		change += [
			(else_try),
				(troop_get_slot, l.check, trp.lwbr_prsnt_vars, opti),
				(eq, l.obj, l.check)
		]
		if opt[0] in (typ.checkbox,typ.numbox,typ.button,typ.combo_button):
			change += opt[3]
		else:
			change += [(display_message,"@This should never appear: %d"%opti),]

	change += [(try_end),]

	run = [
		#Little Pos Helper by Kuba begin
		(mouse_get_position, pos1),
		(position_get_x, reg1, pos1),
		(position_get_y, reg2, pos1),
		(overlay_set_text, g.lwbr_little_pos_helper, "@{reg1},{reg2}"),
		#Little Pos Helper by Kuba end
		(try_begin),
			(key_is_down,key_escape),
			(presentation_set_duration, 0),
		(try_end),
	]

	body = [
		(ti_on_presentation_load,load),
		(ti_on_presentation_event_state_change,change),
		(ti_on_presentation_run,run),
	]
	return (name, flags, args, body)


troops = [
	["lwbr_prsnt_vars","{!}lwbr_prsnt_vars","{!}lwbr_prsnt_vars", 0, 0, 0, fac.kingdom_1, [], 0, 0, 0, 0, 0],
]

