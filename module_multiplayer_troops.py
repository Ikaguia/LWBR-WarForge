from compiler import *

infantry,archer,crossbowman,cavalry,ranged_cavalry = 0,1,1,2,3

multi_troops = [
	[fac.kingdom_1,[#swadia
		[trp.swadian_infantry_multiplayer,infantry,[
			["Native",
				[#free items
					itm.sword_medieval_a,itm.tab_shield_heater_a,itm.red_tunic,itm.ankle_boots
				],[#paid items
					itm_awlpike,itm_awlpike_long,itm_sword_medieval_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_sword_medieval_c,
					itm_sword_medieval_c_small,itm_bastard_sword_a,itm_bastard_sword_b,itm_sword_two_handed_a,itm_sword_two_handed_b,itm_darts,
					itm_war_darts,itm_tab_shield_heater_a,itm_tab_shield_heater_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_red_tunic,
					itm_red_gambeson,itm_leather_armor,itm_haubergeon,itm_brigandine_red,itm_ankle_boots,itm_leather_boots,itm_mail_chausses,
					itm_splinted_greaves,itm_arming_cap,itm_norman_helmet,itm_helmet_with_neckguard,itm_flat_topped_helmet,itm_guard_helmet,
					itm_great_helmet,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm_dagger,itm_fighting_pick,itm_hammer,itm_sword_medieval_d_long,itm_military_hammer,itm_pickaxe,itm_mace_4,itm_voulge,
					itm_morningstar,itm_battle_fork,itm_military_fork,itm_pitch_fork,itm_padded_cloth,itm_coat_of_plates_red,
					itm_heraldic_mail_with_tunic_b,itm_heraldic_mail_with_tabard,itm_light_mail_and_plate,itm_mail_with_surcoat,
					itm_tabard,itm_bascinet,itm_mail_coif,itm_winged_great_helmet,itm_plate_armor,itm_throwing_daggers,
					itm_throwing_knives,itm_woolen_hose,
				]]
			]],
		[trp.swadian_crossbowman_multiplayer,crossbowman,[
			["Native",
				[#free items
					itm.bolts,itm.crossbow,itm.sword_medieval_b_small,itm.tab_shield_heater_a,itm.red_shirt,itm.ankle_boots
				],[#paid items
					itm.bolts,itm.steel_bolts,itm.crossbow,itm.heavy_crossbow,itm.sniper_crossbow,itm.sword_medieval_a,
					itm.sword_medieval_b,itm.sword_medieval_b_small,itm.tab_shield_heater_a,itm.tab_shield_heater_b,
					itm.tab_shield_heater_c,itm.red_shirt,itm.padded_cloth,itm.leather_armor,itm.haubergeon,itm.ankle_boots,
					itm.leather_boots,itm.mail_chausses,itm.leather_gloves,itm.arming_cap,itm.norman_helmet,itm.helmet_with_neckguard,
					itm.flat_topped_helmet,itm.guard_helmet,
				]],
			["WarForge",[],
				[#paid items
					itm.dagger,itm.fighting_pick,itm.hammer,itm.pickaxe,itm.mace_4,itm.bastard_sword_a,itm.heraldic_mail_with_tunic,itm.tabard,
					itm.bascinet,itm.mail_coif,itm.hunting_crossbow,itm.light_crossbow,itm.woolen_hose,
				]]
			]],
		[trp.swadian_man_at_arms_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.lance,itm.sword_medieval_a,itm.tab_shield_heater_a,itm.red_tunic,itm.ankle_boots,itm.saddle_horse
				],[#paid items
					itm_saddle_horse,itm_courser,itm_hunter,itm_warhorse,itm_darts,itm_war_darts,itm_lance,itm_heavy_lance,
					itm_great_lance,itm_sword_medieval_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_sword_medieval_c,
					itm_sword_medieval_c_small,itm_bastard_sword_a,itm_bastard_sword_b,itm_tab_shield_heater_a,itm_tab_shield_heater_b,
					itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_red_tunic,itm_padded_cloth,itm_leather_armor,itm_mail_with_surcoat,
					itm_coat_of_plates_red,itm_ankle_boots,itm_leather_boots,itm_mail_chausses,itm_splinted_greaves,itm_plate_boots,
					itm_arming_cap,itm_norman_helmet,itm_helmet_with_neckguard,itm_flat_topped_helmet,itm_guard_helmet,itm_great_helmet,
					itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm_charger,itm_dagger,itm_hammer,itm_sword_medieval_d_long,itm_military_hammer,itm_mace_4,itm_sword_two_handed_a,
					itm_sword_two_handed_b,itm_morningstar,itm_battle_fork,itm_double_sided_lance,itm_jousting_lance,itm_light_lance,
					itm_military_fork,itm_pitch_fork,itm_brigandine_red,itm_haubergeon,itm_heraldic_mail_with_surcoat,itm_light_mail_and_plate,
					itm_tabard,itm_bascinet,itm_mail_coif,itm_winged_great_helmet,itm_plate_armor,itm_woolen_hose,
				]]
			]],
		#[trp.swadian_mounted_crossbowman_multiplayer,ranged_cavalry,[
			#["Native",
				#[#free items
					#itm.bolts,itm.light_crossbow,itm.tab_shield_heater_cav_a,itm.bastard_sword_a,itm.red_shirt,itm.hide_boots,itm.saddle_horse
				#],[#paid items
					#itm_saddle_horse,itm_courser,itm_hunter,itm_bolts,itm_light_crossbow,itm_crossbow,itm_heavy_crossbow,
					#itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_b,itm_bastard_sword_a,itm_red_shirt,itm_padded_cloth,
					#itm_leather_armor,itm_mail_with_surcoat,itm_coat_of_plates_red,itm_hide_boots,itm_arming_cap,itm_norman_helmet,
					#itm_helmet_with_neckguard,itm_flat_topped_helmet,itm_guard_helmet,itm_leather_gloves,
				#]],
			#["WarForge",[],[]]
			#]],
		]],
	[fac.kingdom_2,[#vaegir
		[trp.vaegir_spearman_multiplayer,infantry,[
			["Native",
				[#free items
					itm.spear, itm.tab_shield_kite_a, itm.mace_1, itm.linen_tunic, itm.hide_boots
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.vaegir_archer_multiplayer,archer,[
			["Native",
				[#free items
					itm.arrows,itm.mace_1,itm.nomad_bow,itm.linen_tunic,itm.hide_boots
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.vaegir_horseman_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.scimitar,itm.lance,itm.tab_shield_kite_cav_a,itm.linen_tunic,itm.hide_boots,itm.saddle_horse
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		]],
	[fac.kingdom_3,[#khergit khanate
		[trp.khergit_infantry_multiplayer,infantry,[
			["Native",
				[#free items
					itm.sword_khergit_1,itm.spear,itm.tab_shield_small_round_a,itm.steppe_armor,itm.hide_boots,itm.leather_gloves
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.khergit_veteran_horse_archer_multiplayer,ranged_cavalry,[
			["Native",
				[#free items
					itm.sword_khergit_1,itm.nomad_bow,itm.arrows,itm.khergit_armor,itm.leather_steppe_cap_a,itm.hide_boots,itm.steppe_horse
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.khergit_lancer_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.sword_khergit_1,itm.lance,itm.tab_shield_small_round_a,itm.khergit_armor,itm.leather_steppe_cap_a,itm.hide_boots,itm.steppe_horse
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		]],
	[fac.kingdom_4,[#nords
		[trp.nord_veteran_multiplayer,infantry,[
			["Native",
				[#free items
					itm.sword_viking_1,itm.one_handed_war_axe_a,itm.tab_shield_round_a,itm.blue_tunic,itm.leather_boots
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.nord_archer_multiplayer,archer,[
			["Native",
				[#free items
					itm.arrows,itm.sword_viking_2_small,itm.short_bow,itm.blue_tunic,itm.leather_boots
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.nord_scout_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.javelin,itm.sword_viking_1,itm.spear,itm.tab_shield_small_round_a,itm.blue_tunic,itm.leather_boots,itm.saddle_horse
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		]],
	[fac.kingdom_5,[#rhodoks
		[trp.rhodok_sergeant_multiplayer,infantry,[
			["Native",
				[#free items
					itm.fighting_pick,itm.tab_shield_pavise_a,itm.spear,itm.green_tunic,itm.ankle_boots
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.rhodok_veteran_crossbowman_multiplayer,crossbowman,[
			["Native",
				[#free items
					itm.crossbow,itm.bolts,itm.fighting_pick,itm.tab_shield_pavise_a,itm.tunic_with_green_cape,itm.ankle_boots
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.rhodok_horseman_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.sword_medieval_a,itm.tab_shield_heater_cav_a, itm.light_lance,itm.green_tunic,itm.ankle_boots,itm.saddle_horse
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		]],
	[fac.kingdom_6,[#sarranid sultanate
		[trp.sarranid_footman_multiplayer,infantry,[
			["Native",
				[#free items
					itm.bamboo_spear, itm.tab_shield_kite_a, itm.arabian_sword_a,itm.sarranid_cloth_robe, itm.sarranid_boots_b
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.sarranid_archer_multiplayer,archer,[
			["Native",
				[#free items
					itm.arrows,itm.arabian_sword_a,itm.nomad_bow,itm.sarranid_cloth_robe, itm.sarranid_boots_b
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		[trp.sarranid_mamluke_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.arabian_sword_a,itm.lance,itm.tab_shield_small_round_a,itm.sarranid_cloth_robe, itm.sarranid_boots_b,itm.saddle_horse
				],[#paid items
				]],
			["WarForge",[],
				[#paid items
				]]
			]],
		]],
]
