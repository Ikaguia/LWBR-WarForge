from compiler import *

infantry,archer,crossbowman,cavalry,ranged_cavalry = 0,1,1,2,3

packages = {}
for pack in ('Native','WarForge','Arena','Peasant'):
	packages[pack] = 1 << len(packages)


multi_troops = [
	[fac.kingdom_1,[#swadia
		[trp.swadian_infantry_multiplayer,infantry,[
			["Native",
				[#free items
					itm.sword_medieval_a,itm.tab_shield_heater_a,itm.red_tunic,itm.ankle_boots
				],[#paid items
					itm.awlpike,itm.awlpike_long,itm.sword_medieval_a,itm.sword_medieval_b,itm.sword_medieval_b_small,itm.sword_medieval_c,
					itm.sword_medieval_c_small,itm.bastard_sword_a,itm.bastard_sword_b,itm.sword_two_handed_a,itm.sword_two_handed_b,itm.darts,
					itm.war_darts,itm.tab_shield_heater_a,itm.tab_shield_heater_b,itm.tab_shield_heater_c,itm.tab_shield_heater_d,itm.red_tunic,
					itm.red_gambeson,itm.leather_armor,itm.haubergeon,itm.brigandine_red,itm.ankle_boots,itm.leather_boots,itm.mail_chausses,
					itm.splinted_greaves,itm.arming_cap,itm.norman_helmet,itm.helmet_with_neckguard,itm.flat_topped_helmet,itm.guard_helmet,
					itm.great_helmet,itm.leather_gloves,itm.mail_mittens,itm.scale_gauntlets,itm.gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.dagger,itm.fighting_pick,itm.hammer,itm.sword_medieval_d_long,itm.military_hammer,itm.pickaxe,itm.mace_4,itm.voulge,
					itm.morningstar,itm.battle_fork,itm.military_fork,itm.pitch_fork,itm.padded_cloth,itm.coat_of_plates_red,
					itm.heraldic_mail_with_tunic_b,itm.heraldic_mail_with_tabard,itm.light_mail_and_plate,itm.mail_with_surcoat,
					itm.tabard,itm.bascinet,itm.mail_coif,itm.winged_great_helmet,itm.plate_armor,itm.throwing_daggers,
					itm.throwing_knives,itm.woolen_hose,
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
					itm.saddle_horse,itm.courser,itm.hunter,itm.warhorse,itm.darts,itm.war_darts,itm.lance,itm.heavy_lance,
					itm.great_lance,itm.sword_medieval_a,itm.sword_medieval_b,itm.sword_medieval_b_small,itm.sword_medieval_c,
					itm.sword_medieval_c_small,itm.bastard_sword_a,itm.bastard_sword_b,itm.tab_shield_heater_a,itm.tab_shield_heater_b,
					itm.tab_shield_heater_c,itm.tab_shield_heater_d,itm.red_tunic,itm.padded_cloth,itm.leather_armor,itm.mail_with_surcoat,
					itm.coat_of_plates_red,itm.ankle_boots,itm.leather_boots,itm.mail_chausses,itm.splinted_greaves,itm.plate_boots,
					itm.arming_cap,itm.norman_helmet,itm.helmet_with_neckguard,itm.flat_topped_helmet,itm.guard_helmet,itm.great_helmet,
					itm.leather_gloves,itm.mail_mittens,itm.scale_gauntlets,itm.gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.charger,itm.dagger,itm.hammer,itm.sword_medieval_d_long,itm.military_hammer,itm.mace_4,itm.sword_two_handed_a,
					itm.sword_two_handed_b,itm.morningstar,itm.battle_fork,itm.double_sided_lance,itm.jousting_lance,itm.light_lance,
					itm.military_fork,itm.pitch_fork,itm.brigandine_red,itm.haubergeon,itm.heraldic_mail_with_surcoat,itm.light_mail_and_plate,
					itm.tabard,itm.bascinet,itm.mail_coif,itm.winged_great_helmet,itm.plate_armor,itm.woolen_hose,
				]]
			]],
		#[trp.swadian_mounted_crossbowman_multiplayer,ranged_cavalry,[
			#["Native",
				#[#free items
					#itm.bolts,itm.light_crossbow,itm.tab_shield_heater_cav_a,itm.bastard_sword_a,itm.red_shirt,itm.hide_boots,itm.saddle_horse
				#],[#paid items
					#itm.saddle_horse,itm.courser,itm.hunter,itm.bolts,itm.light_crossbow,itm.crossbow,itm.heavy_crossbow,
					#itm.tab_shield_heater_cav_a,itm.tab_shield_heater_cav_b,itm.bastard_sword_a,itm.red_shirt,itm.padded_cloth,
					#itm.leather_armor,itm.mail_with_surcoat,itm.coat_of_plates_red,itm.hide_boots,itm.arming_cap,itm.norman_helmet,
					#itm.helmet_with_neckguard,itm.flat_topped_helmet,itm.guard_helmet,itm.leather_gloves,
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
					itm.spear,itm.war_spear,itm.awlpike,itm.tab_shield_kite_a,itm.tab_shield_kite_b,itm.tab_shield_kite_c,itm.tab_shield_kite_d,
					itm.mace_1,itm.mace_2,itm.mace_3,itm.mace_4,itm.long_hafted_spiked_mace,itm.long_spiked_club,itm.scimitar,itm.scimitar_b,
					itm.bardiche,itm.great_bardiche,itm.long_bardiche,itm.great_long_bardiche,itm.javelin,itm.linen_tunic,itm.leather_jerkin,
					itm.leather_vest,itm.lamellar_vest,itm.lamellar_armor,itm.vaegir_elite_armor,itm.hide_boots,itm.nomad_boots,
					itm.splinted_leather_greaves,itm.splinted_greaves,itm.vaegir_fur_cap,itm.vaegir_fur_helmet,itm.vaegir_spiked_helmet,
					itm.vaegir_lamellar_helmet,itm.vaegir_noble_helmet,itm.vaegir_war_helmet,itm.leather_gloves,itm.mail_mittens,itm.scale_gauntlets,
					#itm.spiked_helmet,itm.nasal_helmet,
				]],
			["WarForge",[],
				[#paid items
					itm.sword_khergit_4,itm.falchion,itm.sword_khergit_2,itm.mace_3,itm.battle_axe,itm.sword_of_war,itm.khergit_sword_two_handed_b,
					itm.war_axe,itm.boar_spear,itm.hunting_bow,itm.light_lance,itm.throwing_daggers,itm.throwing_spears,itm.banded_armor,
					itm.coat_of_plates,itm.fur_coat,itm.gambeson,itm.heraldic_mail_with_tunic_b,itm.heraldic_mail_with_tabard,itm.lamellar_vest_khergit,
					itm.leather_jacket,itm.nomad_vest,itm.studded_leather_coat,itm.tribal_warrior_outfit,itm.lamellar_gauntlets,itm.khergit_elite_armor,
					itm.fur_hat,itm.nasal_helmet,itm.nomad_cap,itm.spiked_helmet,itm.vaegir_mask,itm.khergit_leather_boots,
				]]
			]],
		[trp.vaegir_archer_multiplayer,archer,[
			["Native",
				[#free items
					itm.arrows,itm.mace_1,itm.nomad_bow,itm.linen_tunic,itm.hide_boots
				],[#paid items
					itm.arrows,itm.barbed_arrows,itm.mace_1,itm.mace_2,itm.falchion,itm.nomad_bow,itm.khergit_bow,itm.strong_bow,itm.war_bow,
					itm.linen_tunic,itm.leather_jerkin,itm.leather_vest,itm.lamellar_vest,itm.hide_boots,itm.nomad_boots,itm.splinted_leather_greaves,
					itm.nomad_cap,itm.vaegir_fur_cap,itm.vaegir_fur_helmet,itm.vaegir_spiked_helmet,itm.vaegir_lamellar_helmet,
				]],
			["WarForge",[],
				[#paid items
					itm.falchion,itm.sword_khergit_2,itm.mace_3,itm.hunting_bow,itm.short_bow,itm.khergit_arrows,itm.fur_coat,itm.gambeson,
					itm.heraldic_mail_with_tunic,itm.lamellar_vest_khergit,itm.leather_jacket,itm.nomad_vest,itm.tribal_warrior_outfit,
					itm.fur_hat,itm.nasal_helmet,itm.nomad_cap,itm.spiked_helmet,itm.khergit_leather_boots,
				]]
			]],
		[trp.vaegir_horseman_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.scimitar,itm.lance,itm.tab_shield_kite_cav_a,itm.linen_tunic,itm.hide_boots,itm.saddle_horse
				],[#paid items
					itm.saddle_horse,itm.courser,itm.hunter,itm.warhorse_steppe,itm.darts,itm.war_darts,itm.bardiche,itm.scimitar,itm.scimitar_b,
					itm.lance,itm.heavy_lance,itm.tab_shield_kite_cav_a,itm.tab_shield_kite_cav_b,itm.tab_shield_kite_c,itm.tab_shield_kite_d,
					itm.linen_tunic,itm.leather_vest,itm.lamellar_vest,itm.studded_leather_coat,itm.lamellar_armor,itm.vaegir_elite_armor,
					itm.hide_boots,itm.nomad_boots,itm.splinted_leather_greaves,itm.splinted_greaves,itm.plate_boots,itm.vaegir_fur_cap,
					itm.vaegir_fur_helmet,itm.vaegir_spiked_helmet,itm.vaegir_lamellar_helmet,itm.vaegir_noble_helmet,itm.vaegir_war_helmet,
					itm.vaegir_mask,itm.leather_gloves,itm.mail_mittens,itm.scale_gauntlets,
					#itm.great_bardiche,itm.spiked_helmet,itm.nasal_helmet,
				]],
			["WarForge",[],
				[#paid items
					itm.sword_khergit_4,itm.falchion,itm.sword_khergit_2,itm.mace_3,itm.battle_axe,itm.sword_of_war,itm.khergit_sword_two_handed_b,
					itm.war_axe,itm.morningstar,itm.boar_spear,itm.war_spear,itm.spear,itm.light_lance,itm.throwing_daggers,itm.throwing_spears,
					itm.banded_armor,itm.coat_of_plates,itm.fur_coat,itm.gambeson,itm.heraldic_mail_with_surcoat,itm.lamellar_vest_khergit,
					itm.leather_jacket,itm.nomad_vest,itm.tribal_warrior_outfit,itm.lamellar_gauntlets,itm.khergit_elite_armor,itm.fur_hat,
					itm.nasal_helmet,itm.nomad_cap,itm.spiked_helmet,itm.khergit_leather_boots,
				]]
			]],
		]],
	[fac.kingdom_3,[#khergit khanate
		[trp.khergit_infantry_multiplayer,infantry,[
			["Native",
				[#free items
					itm.sword_khergit_1,itm.spear,itm.tab_shield_small_round_a,itm.steppe_armor,itm.hide_boots,itm.leather_gloves
				],[#paid items
					itm.javelin,itm.jarid,itm.sword_khergit_1,itm.sword_khergit_2,itm.sword_khergit_3,itm.sword_khergit_4,itm.tab_shield_small_round_a,
					itm.tab_shield_small_round_b,itm.tab_shield_small_round_c,itm.tab_shield_round_b,itm.tab_shield_round_c,itm.spear,itm.hafted_blade_a,
					itm.hafted_blade_b,itm.mace_1,itm.mace_2,itm.mace_3,itm.nomad_cap_b,itm.leather_steppe_cap_b,itm.steppe_cap,itm.khergit_war_helmet,
					itm.khergit_guard_helmet,itm.steppe_armor,itm.tribal_warrior_outfit,itm.lamellar_armor,itm.khergit_elite_armor,itm.hide_boots,
					itm.nomad_boots,itm.khergit_leather_boots,itm.splinted_leather_greaves,itm.splinted_greaves,itm.leather_gloves,itm.mail_mittens,
					itm.scale_gauntlets,itm.lamellar_gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.strange_short_sword,itm.strange_great_sword,itm.strange_sword,itm.light_lance,itm.sickle,itm.club,itm.throwing_spears,
					itm.fur_coat,itm.heraldic_mail_with_tabard,itm.khergit_guard_armor,itm.lamellar_vest,itm.lamellar_vest_khergit,itm.nomad_robe,
					itm.strange_armor,itm.headcloth,itm.khergit_cavalry_helmet,itm.strange_helmet,itm.strange_boots,itm.winged_mace,itm.spiked_club,
					itm.bamboo_spear,itm.heraldic_mail_with_tunic_b,
				]]
			]],
		[trp.khergit_veteran_horse_archer_multiplayer,ranged_cavalry,[
			["Native",
				[#free items
					itm.sword_khergit_1,itm.nomad_bow,itm.arrows,itm.khergit_armor,itm.leather_steppe_cap_a,itm.hide_boots,itm.steppe_horse
				],[#paid items
					itm.steppe_horse,itm.sword_khergit_1,itm.sword_khergit_2,itm.sword_khergit_3,itm.sword_khergit_4,itm.nomad_bow,itm.khergit_bow,
					itm.strong_bow,itm.arrows,itm.khergit_arrows,itm.leather_steppe_cap_a,itm.nomad_cap_b,itm.leather_steppe_cap_b,itm.steppe_cap,
					itm.khergit_armor,itm.steppe_armor,itm.tribal_warrior_outfit,itm.lamellar_vest_khergit,itm.hide_boots,itm.nomad_boots,
					itm.khergit_leather_boots,itm.splinted_leather_greaves,itm.splinted_greaves,itm.leather_gloves,
				]],
			["WarForge",[],
				[#paid items
					itm.strange_short_sword,itm.sickle,itm.club,itm.hunting_bow,itm.barbed_arrows,itm.fur_coat,itm.heraldic_mail_with_tunic,
					itm.lamellar_vest,itm.nomad_robe,itm.headcloth,itm.khergit_cavalry_helmet,
				]]
			]],
		[trp.khergit_lancer_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.sword_khergit_1,itm.lance,itm.tab_shield_small_round_a,itm.khergit_armor,itm.leather_steppe_cap_a,itm.hide_boots,itm.steppe_horse
				],[#paid items
					itm.steppe_horse,itm.courser,itm.hunter,itm.warhorse_steppe,itm.javelin,itm.sword_khergit_1,itm.sword_khergit_2,itm.sword_khergit_3,
					itm.sword_khergit_4,itm.tab_shield_small_round_a,itm.tab_shield_small_round_b,itm.tab_shield_small_round_c,itm.lance,itm.heavy_lance,
					itm.hafted_blade_a,itm.hafted_blade_b,itm.one_handed_war_axe_a,itm.leather_steppe_cap_a,itm.nomad_cap_b,itm.leather_steppe_cap_b,
					itm.steppe_cap,itm.khergit_war_helmet,itm.khergit_armor,itm.steppe_armor,itm.tribal_warrior_outfit,itm.lamellar_armor,itm.hide_boots,
					itm.nomad_boots,itm.khergit_leather_boots,itm.splinted_leather_greaves,itm.splinted_greaves,itm.leather_gloves,itm.mail_mittens,
					itm.scale_gauntlets,itm.lamellar_gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.strange_short_sword,itm.strange_great_sword,itm.strange_sword,itm.light_lance,itm.sickle,itm.club,itm.throwing_spears,
					itm.fur_coat,itm.heraldic_mail_with_tabard,itm.khergit_guard_armor,itm.lamellar_vest,itm.lamellar_vest_khergit,itm.nomad_robe,
					itm.strange_armor,itm.headcloth,itm.khergit_cavalry_helmet,itm.strange_helmet,itm.strange_boots,itm.winged_mace,itm.spiked_club,
					itm.bamboo_spear,itm.heraldic_mail_with_tunic_b,
				]]
			]],
		]],
	[fac.kingdom_4,[#nords
		[trp.nord_veteran_multiplayer,infantry,[
			["Native",
				[#free items
					itm.sword_viking_1,itm.one_handed_war_axe_a,itm.tab_shield_round_a,itm.blue_tunic,itm.leather_boots
				],[#paid items
					itm.sword_viking_1,itm.darts,itm.war_darts,itm.javelin,itm.throwing_spears,itm.sword_viking_2,itm.sword_viking_2_small,
					itm.sword_viking_3,itm.sword_viking_3_small,itm.one_handed_war_axe_a,itm.one_handed_war_axe_b,itm.one_handed_battle_axe_a,
					itm.one_handed_battle_axe_b,itm.one_handed_battle_axe_c,itm.two_handed_axe,itm.two_handed_battle_axe_2,itm.great_axe,
					itm.long_axe,itm.long_axe_b,itm.long_axe_c,itm.spear,itm.war_spear,itm.tab_shield_round_a,itm.tab_shield_round_b,
					itm.tab_shield_round_c,itm.tab_shield_round_d,itm.tab_shield_round_e,itm.light_throwing_axes,itm.throwing_axes,
					itm.heavy_throwing_axes,itm.nordic_veteran_archer_helmet,itm.nordic_footman_helmet,itm.nordic_fighter_helmet,
					itm.nordic_huscarl_helmet,itm.nordic_warlord_helmet,itm.blue_tunic,itm.leather_jerkin,itm.mail_shirt,itm.mail_hauberk,
					itm.banded_armor,itm.leather_boots,itm.splinted_leather_greaves,itm.mail_chausses,itm.mail_boots,itm.leather_gloves,
					itm.mail_mittens,itm.scale_gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.cleaver,itm.dagger,itm.fighting_axe,itm.battle_axe,itm.war_axe,itm.ashwood_pike,itm.boar_spear,itm.cuir_bouilli,
					itm.heraldic_mail_with_tabard,itm.heraldic_mail_with_tunic_b,itm.light_leather,itm.rawhide_coat,itm.tribal_warrior_outfit,
					itm.axe,itm.light_lance,
				]]
			]],
		[trp.nord_archer_multiplayer,archer,[
			["Native",
				[#free items
					itm.arrows,itm.sword_viking_2_small,itm.short_bow,itm.blue_tunic,itm.leather_boots
				],[#paid items
					itm.arrows,itm.barbed_arrows,itm.bodkin_arrows,itm.sword_viking_1,itm.sword_viking_2,itm.sword_viking_2_small,itm.sword_viking_3,
					itm.sword_viking_3_small,itm.one_handed_war_axe_a,itm.one_handed_war_axe_b,itm.two_handed_axe,itm.short_bow,itm.long_bow,
					itm.blue_tunic,itm.leather_jerkin,itm.byrnie,itm.leather_boots,itm.splinted_leather_greaves,itm.mail_chausses,itm.mail_boots,
					itm.nordic_archer_helmet,itm.nordic_veteran_archer_helmet,itm.nordic_footman_helmet,itm.nordic_fighter_helmet,
				]],
			["WarForge",[],
				[#paid items
					itm.cleaver,itm.dagger,itm.heraldic_mail_with_tunic,itm.light_leather,itm.mail_shirt,itm.rawhide_coat,itm.tribal_warrior_outfit,
					itm.leather_gloves,itm.mail_mittens,itm.hunting_bow,itm.axe,
				]]
			]],
		[trp.nord_scout_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.javelin,itm.sword_viking_1,itm.spear,itm.tab_shield_small_round_a,itm.blue_tunic,itm.leather_boots,itm.saddle_horse
				],[#paid items
					itm.saddle_horse,itm.courser,itm.hunter,itm.darts,itm.war_darts,itm.javelin,itm.throwing_spears,itm.light_throwing_axes,
					itm.throwing_axes,itm.sword_viking_1,itm.sword_viking_2,itm.sword_viking_3,itm.two_handed_axe,itm.two_handed_battle_axe_2,
					itm.shortened_voulge,itm.spear,itm.war_spear,itm.light_lance,itm.lance,itm.tab_shield_small_round_a,itm.tab_shield_small_round_b,
					itm.tab_shield_small_round_c,itm.nordic_archer_helmet,itm.nordic_veteran_archer_helmet,itm.nordic_footman_helmet,
					itm.nordic_fighter_helmet,itm.nordic_huscarl_helmet,itm.blue_tunic,itm.leather_jerkin,itm.mail_shirt,itm.mail_hauberk,
					itm.leather_boots,itm.splinted_leather_greaves,itm.mail_chausses,itm.mail_boots,itm.leather_gloves,itm.mail_mittens,
					itm.scale_gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.cleaver,itm.dagger,itm.fighting_axe,itm.battle_axe,itm.ashwood_pike,itm.boar_spear,itm.heraldic_mail_with_surcoat,
					itm.light_leather,itm.rawhide_coat,itm.tribal_warrior_outfit,itm.stones,itm.throwing_daggers,itm.voulge,
				]]
			]],
		]],
	[fac.kingdom_5,[#rhodoks
		[trp.rhodok_sergeant_multiplayer,infantry,[
			["Native",
				[#free items
					itm.fighting_pick,itm.tab_shield_pavise_a,itm.spear,itm.green_tunic,itm.ankle_boots
				],[#paid items
					itm.darts,itm.war_darts,itm.javelin,itm.fighting_pick,itm.military_pick,itm.morningstar,itm.club_with_spike_head,
					itm.military_cleaver_b,itm.military_cleaver_c,itm.two_handed_cleaver,itm.military_sickle_a,itm.maul,itm.sledgehammer,
					itm.warhammer,itm.spear,itm.pike,itm.ashwood_pike,itm.war_spear,itm.glaive,itm.tab_shield_pavise_a,itm.tab_shield_pavise_b,
					itm.tab_shield_pavise_c,itm.tab_shield_pavise_d,itm.leather_cap,itm.padded_coif,itm.footman_helmet,itm.kettle_hat,itm.bascinet_2,
					itm.full_helm,itm.green_tunic,itm.aketon_green,itm.ragged_outfit,itm.leather_armor,itm.surcoat_over_mail,itm.ankle_boots,
					itm.leather_boots,itm.splinted_greaves,itm.iron_greaves,itm.leather_gloves,itm.mail_mittens,itm.scale_gauntlets,itm.gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.falchion,itm.winged_mace,itm.hammer,itm.military_hammer,itm.sword_medieval_c_small,itm.sword_medieval_b_small,
					itm.sword_medieval_a,itm.sword_medieval_b,itm.mace_4,itm.shortened_military_scythe,itm.bec_de_corbin_a,itm.blue_gambeson,
					itm.heraldic_mail_with_tunic_b,itm.heraldic_mail_with_tabard,itm.leather_apron,itm.mail_and_plate,itm.plate_armor,
					itm.scale_armor,itm.bascinet,itm.bascinet_3,itm.felt_hat,itm.felt_hat_b,itm.mail_coif,itm.skullcap,itm.segmented_helmet,
					itm.military_scythe,itm.padded_leather,itm.blue_hose,
				]]
			]],
		[trp.rhodok_veteran_crossbowman_multiplayer,crossbowman,[
			["Native",
				[#free items
					itm.crossbow,itm.bolts,itm.fighting_pick,itm.tab_shield_pavise_a,itm.tunic_with_green_cape,itm.ankle_boots
				],[#paid items
					itm.crossbow,itm.heavy_crossbow,itm.sniper_crossbow,itm.bolts,itm.steel_bolts,itm.fighting_pick,itm.military_pick,
					itm.club_with_spike_head,itm.maul,itm.sledgehammer,itm.sword_medieval_a,itm.sword_medieval_b,itm.sword_medieval_b_small,
					itm.tab_shield_pavise_a,itm.tab_shield_pavise_b,itm.tab_shield_pavise_c,itm.tab_shield_pavise_d,itm.leather_cap,
					itm.padded_coif,itm.footman_helmet,itm.kettle_hat,itm.tunic_with_green_cape,itm.aketon_green,itm.leather_armor,
					itm.ankle_boots,itm.leather_boots,itm.splinted_greaves,itm.leather_gloves,
				]],
			["WarForge",[],
				[#paid items
					itm.falchion,itm.winged_mace,itm.sword_medieval_c_small,itm.mace_4,itm.hunting_crossbow,itm.light_crossbow,itm.blue_gambeson,
					itm.heraldic_mail_with_tunic,itm.leather_apron,itm.bascinet,itm.felt_hat,itm.felt_hat_b,itm.mail_coif,itm.skullcap,
					itm.segmented_helmet,itm.padded_leather,itm.blue_hose,
				]]
			]],
		[trp.rhodok_horseman_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.sword_medieval_a,itm.tab_shield_heater_cav_a, itm.light_lance,itm.green_tunic,itm.ankle_boots,itm.saddle_horse
				],[#paid items
					itm.saddle_horse,itm.courser,itm.hunter,itm.warhorse,itm.darts,itm.war_darts,itm.javelin,itm.sword_medieval_a,
					itm.sword_medieval_b,itm.sword_medieval_c,itm.fighting_pick,itm.military_pick,itm.morningstar,itm.military_cleaver_b,
					itm.military_cleaver_c,itm.two_handed_cleaver,itm.shortened_military_scythe,itm.light_lance,itm.lance,itm.heavy_lance,
					itm.tab_shield_heater_cav_a,itm.tab_shield_heater_cav_b,itm.padded_coif,itm.footman_helmet,itm.kettle_hat,itm.bascinet_3,
					itm.green_tunic,itm.aketon_green,itm.ragged_outfit,itm.leather_armor,itm.surcoat_over_mail,itm.ankle_boots,itm.leather_boots,
					itm.splinted_greaves,itm.plate_boots,itm.leather_gloves,itm.mail_mittens,itm.scale_gauntlets,itm.gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.falchion,itm.winged_mace,itm.hammer,itm.sword_medieval_d_long,itm.military_hammer,itm.sword_medieval_c_small,
					itm.sword_medieval_b_small,itm.mace_4,itm.maul,itm.shortened_voulge,itm.sledgehammer,itm.bec_de_corbin_a,itm.blue_gambeson,
					itm.heraldic_mail_with_surcoat,itm.leather_apron,itm.mail_and_plate,itm.plate_armor,itm.scale_armor,itm.bascinet,
					itm.bascinet_2,itm.felt_hat,itm.felt_hat_b,itm.full_helm,itm.mail_coif,itm.skullcap,itm.segmented_helmet,itm.padded_leather,
					itm.blue_hose,
				]]
			]],
		]],
	[fac.kingdom_6,[#sarranid sultanate
		[trp.sarranid_footman_multiplayer,infantry,[
			["Native",
				[#free items
					itm.bamboo_spear, itm.tab_shield_kite_a, itm.arabian_sword_a,itm.sarranid_cloth_robe, itm.sarranid_boots_b
				],[#paid items
					itm.sarranid_cloth_robe,itm.skirmisher_armor,itm.archers_vest,itm.sarranid_leather_armor,itm.arabian_armor_b,
					itm.sarranid_elite_armor,itm.sarranid_felt_hat,itm.turban,itm.desert_turban,itm.sarranid_mail_coif,itm.sarranid_warrior_cap,
					itm.sarranid_veiled_helmet,itm.sarranid_boots_b,itm.sarranid_boots_c,itm.sarranid_boots_d,itm.arabian_sword_a,
					itm.arabian_sword_b,itm.arabian_sword_d,itm.sarranid_mace_1,itm.sarranid_axe_a,itm.sarranid_axe_b,itm.sarranid_two_handed_axe_a,
					itm.sarranid_two_handed_axe_b,itm.sarranid_two_handed_mace_1,itm.bamboo_spear,itm.spear,itm.jarid,itm.javelin,itm.tab_shield_kite_a,
					itm.tab_shield_kite_b,itm.tab_shield_kite_c,itm.tab_shield_kite_d,itm.leather_gloves,itm.mail_mittens,itm.scale_gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.sarranid_cavalry_robe,itm.heraldic_mail_with_tunic_b,itm.heraldic_mail_with_tabard,itm.sarranid_mail_shirt,
					itm.sarranid_cloth_robe,itm.lamellar_gauntlets,itm.sarranid_helmet1,itm.butchering_knife,itm.scimitar_b,itm.sword_khergit_1,
					itm.sword_khergit_2,itm.sarranid_cavalry_sword,itm.scimitar,itm.khergit_sword_two_handed_a,itm.khergit_sword_two_handed_b,
					itm.throwing_knives,itm.throwing_daggers,
				]]
			]],
		[trp.sarranid_archer_multiplayer,archer,[
			["Native",
				[#free items
					itm.arrows,itm.arabian_sword_a,itm.nomad_bow,itm.sarranid_cloth_robe, itm.sarranid_boots_b
				],[#paid items
					itm.sarranid_cloth_robe,itm.skirmisher_armor,itm.archers_vest,itm.arabian_armor_b,itm.sarranid_felt_hat,itm.turban,
					itm.desert_turban,itm.sarranid_mail_coif,itm.sarranid_horseman_helmet,itm.sarranid_warrior_cap,itm.sarranid_boots_b,
					itm.sarranid_boots_c,itm.short_bow,itm.nomad_bow,itm.arrows,itm.barbed_arrows,itm.scimitar,itm.mace_1,itm.arabian_sword_a,
					itm.arabian_sword_b,itm.leather_gloves,
				]],
			["WarForge",[],
				[#paid items
					itm.heraldic_mail_with_tunic,itm.sarranid_cloth_robe,itm.sarranid_helmet1,itm.butchering_knife,itm.sword_khergit_1,
					itm.sword_khergit_2,itm.hunting_bow,itm.khergit_bow,itm.strong_bow,
				]]
			]],
		[trp.sarranid_mamluke_multiplayer,cavalry,[
			["Native",
				[#free items
					itm.arabian_sword_a,itm.lance,itm.tab_shield_small_round_a,itm.sarranid_cloth_robe, itm.sarranid_boots_b,itm.saddle_horse
				],[#paid items
					itm.saddle_horse,itm.arabian_horse_a,itm.arabian_horse_b,itm.warhorse_sarranid,itm.sarranid_cloth_robe,itm.skirmisher_armor,
					itm.archers_vest,itm.sarranid_mail_shirt,itm.sarranid_cavalry_robe,itm.mamluke_mail,itm.sarranid_elite_armor,itm.turban,
					itm.desert_turban,itm.sarranid_horseman_helmet,itm.sarranid_mail_coif,itm.sarranid_veiled_helmet,itm.sarranid_boots_b,
					itm.sarranid_boots_c,itm.sarranid_boots_d,itm.arabian_sword_a,itm.arabian_sword_b,itm.sarranid_cavalry_sword,itm.arabian_sword_d,
					itm.sarranid_mace_1,itm.sarranid_axe_a,itm.sarranid_axe_b,itm.sarranid_two_handed_axe_a,itm.lance,itm.heavy_lance,itm.jarid,
					itm.javelin,itm.tab_shield_small_round_a,itm.tab_shield_small_round_b,itm.tab_shield_small_round_c,itm.leather_gloves,
					itm.mail_mittens,itm.scale_gauntlets,
				]],
			["WarForge",[],
				[#paid items
					itm.heraldic_mail_with_surcoat,itm.sarranid_leather_armor,itm.arabian_armor_b,itm.sarranid_cloth_robe,itm.lamellar_gauntlets,
					itm.sarranid_helmet1,itm.butchering_knife,itm.scimitar_b,itm.sword_khergit_4,itm.sword_khergit_1,itm.sword_khergit_2,itm.scimitar,
					itm.khergit_sword_two_handed_a,itm.khergit_sword_two_handed_b,itm.morningstar,itm.bamboo_spear,itm.throwing_knives,
					itm.throwing_daggers,
				]]
			]],
		]],
]

def foo___lwbr_give_items_to_troops():
	foo = [ (store_script_param_1, l.value), ]
	for faction in multi_troops:
		for troop in faction[1]:
			foo += [ (call_script, script.lwbr_give_items_to_troop, l.value, troop[0]), ]
	return ("lwbr_give_items_to_troops",foo)

def foo___lwbr_give_items_to_troop():
	foo = [
		(store_script_param_1, l.value),
		(store_script_param_2, l.troop),
		(try_for_range, l.cur_item, all_items_begin, all_items_end),
			(store_sub, l.item_troop_slot, l.troop, multiplayer_troops_begin),
			(val_add, l.item_troop_slot, slot_item_multiplayer_availability_linked_list_begin),
			(item_set_slot, l.cur_item, l.item_troop_slot, -1),
		(try_end),
		(try_begin),
			(eq,1,0),
		# 	(this_or_next|eq,l.value, lwbr_new_items__peasant_items),
		# 	(this_or_next|eq,l.value, lwbr_new_items__no_items),
		# 	(eq,l.value, lwbr_new_items__arena_items),
		# 	(call_script, script.lwbr_add_arena_equip_to_troop, l.troop, l.value),
		# (else_try),
		# 	(eq,l.troop, trp.swadian_crossbowman_multiplayer),
		# 	(call_script, script.multiplayer_set_item_available_for_troop, "itm.bolts", "trp_swadian_crossbowman_multiplayer", 0),
		# 	(eq, l.value, lwbr_new_items__native_plus_warforge),
	]

	for fact in multi_troops[-1:]:
		for troop in fact[1][-1:]:
			foo += [
				(else_try),
					(eq,l.troop,troop[0]),
					(troop_clear_inventory,troop[0]),
			]
			for pack in troop[2]:
				foo += [
					(try_begin),
						(store_and,l.pack,l.value,packages[pack[0]]),
						(eq,l.pack,packages[pack[0]]),
				]
				free_horses,paid_horses = [],[]
				for item in pack[1]:
					if (item.flags & itp_type_horse) == itp_type_horse: free_horses += [item]
					else: foo += [ (troop_add_item, troop[0], item), ]
				for item in pack[2]:
					if (item.flags & itp_type_horse) == itp_type_horse: paid_horses += [item]
					else: foo += [ (call_script, script.multiplayer_set_item_available_for_troop,item,troop[0]), ]
				foo += [
						(try_begin),
							(eq,g.lwbr_horses_enabled,1),
				]
				for horse in free_horses: foo += [ (troop_add_item, troop[0], horse), ]
				for horse in paid_horses: foo += [ (call_script, script.multiplayer_set_item_available_for_troop,horse,troop[0]), ]
				foo += [
						(try_end),
					(try_end),
				]

	foo += [ (try_end), ]
	return ("lwbr_give_items_to_troop",foo)

