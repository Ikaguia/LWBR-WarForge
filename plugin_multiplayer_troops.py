from compiler import *
register_plugin(__name__)

infantry,archer,crossbowman,cavalry,ranged_cavalry = 0,1,1,2,3

multi_troops = [
	[fac.no_faction,[#all
		[trp.player,infantry,[#all troops
			["Peasant",[
				#2h/pole
				itm.pitch_fork,itm.long_spiked_club,itm.scythe,itm.military_fork,itm.battle_fork,
				itm.boar_spear,itm.staff,itm.quarter_staff,itm.shortened_spear,
				#1h
				itm.wooden_stick,itm.cudgel,itm.hammer,itm.club,itm.pickaxe,itm.spiked_club,itm.sickle,
				itm.butchering_knife,itm.cleaver,itm.knife,itm.dagger,itm.falchion,itm.hatchet,itm.mace_1,
				itm.torch,
				#thrown
				itm.stones,
				#bow
				itm.hunting_bow,itm.short_bow,
				itm.arrows,
				#head
				itm.straw_hat,itm.pilgrim_hood,itm.head_wrappings,itm.common_hood,itm.hood_b,itm.hood_c,
				itm.hood_d,itm.felt_hat,itm.felt_hat_b,itm.woolen_cap,itm.vaegir_fur_cap,itm.black_hood,
				#body
				itm.pilgrim_disguise,itm.fur_coat,itm.shirt,itm.linen_tunic,itm.short_tunic,itm.red_shirt,
				itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.coarse_tunic,itm.leather_apron,itm.tabard,
				itm.leather_vest,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.padded_cloth,
				itm.aketon_green,itm.leather_jerkin,itm.nomad_vest,itm.padded_leather,itm.nomad_robe,
				itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.robe,itm.burlap_tunic,
				itm.tunic_with_green_cape,
				#boots
				itm.wrapping_boots,itm.woolen_hose,itm.blue_hose,itm.hunter_boots,itm.hide_boots,
				itm.ankle_boots,itm.nomad_boots,itm.sarranid_boots_a,itm.sarranid_boots_b,itm.sarranid_boots_c,
				itm.leather_boots,
				#hands
				itm.leather_gloves,
				#horses
				itm.sumpter_horse,
				],[]],
			["Arena",
				[
					itm.practice_sword,
					itm.practice_boots,
					itm.leather_gloves,
				],[
					itm.heavy_practice_sword,
					# itm.practice_dagger,
					itm.practice_axe,
					itm.practice_staff,
					itm.practice_lance,
					itm.practice_bow,
					itm.practice_crossbow,
					itm.practice_javelin,
					itm.practice_throwing_daggers,
					itm.practice_horse,
					# itm.practice_arrows,
					# itm.practice_bolts,
				]],
			["WarForge",[],[
				itm.stones,itm.torch,
				]],
			]],
		]],
	[fac.kingdom_1,[#swadia
		[trp.player,infantry,[#all troops
			["Arena",
				[
					itm.arena_helmet_red,
					itm.arena_armor_red,
					itm.arena_shield_red,
				],[
					itm.arena_tunic_red,
					itm.arena_turban_red,
					itm.steppe_helmet_red,
				]],
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
				]],
			["Event",[itm.woolen_hose],
				[#paid items
					itm.gold_tourney_armor,itm.woolen_hose,itm.head_wrappings,itm.common_hood,itm.mail_coif,itm.segmented_helmet,
					itm.byzantion_helmet_a,itm.green_tourney_armor,
				]],
			["Event2",[],
				[#paid items
					itm.plate_armor,itm.plate_boots,
					itm.heraldic_mail_with_surcoat,itm.heraldic_mail_with_tabard,#cheaper cost
				]],
			]],
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
				]],
			["Event",[itm.woolen_hose],
				[#paid items
					itm.tutorial_shield,itm.red_tourney_armor,itm.gold_tourney_armor,itm.gold_tourney_helmet,itm.woolen_hose,itm.padded_cloth,
					itm.head_wrappings,itm.common_hood,itm.mail_coif,itm.military_hammer,itm.bec_de_corbin_a,itm.norman_shield_1,
					itm.norman_shield_6,itm.byzantion_helmet_a,itm.light_mail_and_plate,
				]],
			["Event2",[],
				[#paid items
					itm.plate_armor,itm.plate_boots,
					itm.heraldic_mail_with_surcoat,itm.heraldic_mail_with_tabard,#cheaper cost
				]],
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
				]],
			["Event",[],
				[#paid items
					itm.tutorial_shield,itm.red_tourney_armor,itm.tourney_helm_red,itm.mail_with_surcoat,itm.mail_coif,itm.sword_of_war,
					itm.light_mail_and_plate,
				]],
			["Event2",[],
				[#paid items
					itm.plate_armor,itm.plate_boots,itm.winged_great_helmet,
					itm.heraldic_mail_with_surcoat,itm.heraldic_mail_with_tabard,#cheaper cost
				]],
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
		[trp.player,infantry,[#all troops
			["Arena",
				[
					itm.arena_helmet_blue,
					itm.arena_armor_white,
					itm.arena_shield_blue,
				],[
					itm.arena_tunic_white,
					itm.arena_turban_blue,
					itm.steppe_helmet_white,
				]],
			]],
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
				]],
			["Event",[],
				[#paid items
					itm.hunter_boots,itm.fur_coat,itm.studded_leather_coat,itm.mail_shirt,itm.head_wrappings,itm.fur_hat,itm.nomad_cap,
					itm.leather_warrior_cap,itm.fighting_axe,itm.battle_axe,itm.war_axe,itm.mace_3,itm.mace_4,itm.rus_helmet_a,
					itm.throwing_spears,itm.nomad_armor,itm.byrnie,itm.tribal_warrior_outfit,itm.norman_shield_7,itm.magyar_helmet_a,
				]],
			["Event2",[],
				[#paid items
					itm.cuir_bouilli,
					itm.heraldic_mail_with_tunic,itm.heraldic_mail_with_tunic_b,#cheaper cost
				]],
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
				]],
			["Event",[],
				[#paid items
					itm.hunter_boots,itm.head_wrappings,itm.fur_hat,itm.nomad_cap,itm.leather_warrior_cap,itm.throwing_spears,
					itm.nomad_armor,itm.byrnie,
				]],
			["Event2",[],
				[#paid items
					itm.heraldic_mail_with_tunic,itm.heraldic_mail_with_tunic_b,#cheaper cost
				]],
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
				]],
			["Event",[],
				[#paid items
					itm.fur_coat,itm.sword_of_war,itm.rus_helmet_a,itm.banded_armor,itm.norman_shield_7,itm.magyar_helmet_a,
				]],
			["Event2",[],
				[#paid items
					itm.cuir_bouilli,
					itm.heraldic_mail_with_tunic,itm.heraldic_mail_with_tunic_b,#cheaper cost
				]],
			]],
		]],
	[fac.kingdom_3,[#khergit khanate
		[trp.player,infantry,[#all troops
			["Arena",
				[
					itm.arena_helmet_yellow,
					itm.arena_armor_yellow,
					itm.arena_shield_yellow,
				],[
					itm.arena_tunic_yellow,
					itm.arena_turban_yellow,
					itm.steppe_helmet_yellow,
				]],
			]],
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
		[trp.player,infantry,[#all troops
			["Arena",
				[
					itm.arena_helmet_blue,
					itm.arena_armor_blue,
					itm.arena_shield_blue,
				],[
					itm.arena_tunic_blue,
					itm.arena_turban_blue,
					itm.steppe_helmet_blue,
				]],
			]],
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
					itm.light_leather,itm.rawhide_coat,itm.tribal_warrior_outfit,itm.throwing_daggers,itm.voulge,
				]]
			]],
		]],
	[fac.kingdom_5,[#rhodoks
		[trp.player,infantry,[#all troops
			["Arena",
				[
					itm.arena_helmet_green,
					itm.arena_armor_green,
					itm.arena_shield_green,
				],[
					itm.arena_tunic_green,
					itm.arena_turban_green,
					itm.steppe_helmet_green,
				]],
			]],
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
		[trp.player,infantry,[#all troops
			["Arena",
				[
					itm.arena_helmet_yellow,
					itm.arena_armor_yellow,
					itm.arena_shield_yellow,
				],[
					itm.arena_tunic_yellow,
					itm.arena_turban_yellow,
					itm.steppe_helmet_yellow,
				]],
			]],
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
	foo = [ (store_script_param_1, l.value), ] + lwbr.debug_func("lwbr_give_items_to_troops", [l.value])
	for fact_id,fact_troops in multi_troops:
		if fact_id == fac.no_faction: continue
		for troop_id,troop_type,troop_packs in fact_troops:
			if troop_id == trp.player: continue
			foo += [ (call_script, script.lwbr_give_items_to_troop, l.value, troop_id), ]
	return ("lwbr_give_items_to_troops",foo)

def foo___lwbr_give_items_to_troop():
	foo = [
		(store_script_param_1, l.value),
		(store_script_param_2, l.troop),
		# (troop_clear_inventory,l.troop),#doesnt clear equiped items
		(troop_raise_skill, l.troop, skl.inventory_management, 10),
		(troop_get_inventory_capacity, l.slots, l.troop),
		(try_for_range, l.slot, 0, l.slots),
			(troop_set_inventory_slot, l.troop, l.slot, -1),
		(try_end),
		(store_troop_faction, l.troop_fac, l.troop),
		(eq, l.troop_fac, l.troop_fac),
		(try_for_range, l.cur_item, all_items_begin, all_items_end),
			(store_sub, l.item_troop_slot, l.troop, multiplayer_troops_begin),
			(val_add, l.item_troop_slot, slot_item_multiplayer_availability_linked_list_begin),
			(item_set_slot, l.cur_item, l.item_troop_slot, -1),
		(try_end),
		(try_begin),
	]

	for fact_id,fact_troops in multi_troops:
		for troop_id,troop_type,troop_packs in fact_troops:
			if troop_id == trp.player:
				if fact_id != fac.no_faction:
					foo += [(eq,l.troop_fac,fact_id),]
			else:
				foo += [(eq,l.troop,troop_id),]
			for pack_name,pack_free_items,pack_paid_items in troop_packs:
				foo += [
					(try_begin),
						(store_and,l.pack,l.value,lwbr.packages[pack_name]),
						(neq,l.pack,0),
				] + lwbr.debug([
						(try_begin),
							(eq, l.troop, trp.swadian_infantry_multiplayer),
							(display_message, "@pack.%s" % pack_name),
						(try_end),
				])
				for free_item in pack_free_items:
					foo += [
						(try_begin),
							(troop_has_item, l.troop, free_item),
					] + lwbr.debug([
							(try_begin),
								(eq, l.troop, trp.swadian_infantry_multiplayer),
								(str_store_troop_name, s0, l.troop),
								(str_store_item_name, s1, free_item),
								(display_message, "@Troop {s0} already had free item {s1}"),
							(try_end),
					]) + [
						(else_try),
							(troop_slot_eq, trp.lwbr_sv_vars, lwbr.sv_var.horses_en, 0),
							(eq, g.lwbr_horses_enabled ,0),
							(item_get_type, l.type, free_item),
							(eq, l.type, itp_type_horse),
					] + lwbr.debug([
							(try_begin),
								(eq, l.troop, trp.swadian_infantry_multiplayer),
								(str_store_troop_name, s0, l.troop),
								(str_store_item_name, s1, free_item),
								(display_message, "@Troop {s0} would get horse {s1} but horses are disabled"),
							(try_end),
					]) + [
						(else_try),
							(troop_add_item, l.troop, free_item),
							(call_script, script.multiplayer_set_item_available_for_troop,free_item, l.troop),
						(try_end),
					]
				for paid_item in pack_paid_items:
					foo += [ (call_script, script.multiplayer_set_item_available_for_troop,paid_item,l.troop), ]
				foo += [ (try_end), ]
			if troop_id == trp.player: foo += [(eq,1,0),]
			foo += [(else_try),]
	foo += [
			(str_store_troop_name, s0, l.troop),
			(display_message, "@Error: invalid or unrecognized troop '{s0}' for script.lwbr_give_items_to_troop"),
		(try_end),
	] + lwbr.debug([
			(try_begin),
				(eq, l.troop, trp.swadian_infantry_multiplayer),
				(str_store_troop_name, s0, l.troop),
				(display_message, "@trp.{s0} has itms:"),
				(try_for_troop_items, l.itm, l.troop),
					(str_store_item_name, s1, l.itm),
					(display_message, "@	itm.{s1}"),
				(try_end),
			(try_end),
	])

	return ("lwbr_give_items_to_troop",foo)

scripts = [
	foo___lwbr_give_items_to_troops(),
	foo___lwbr_give_items_to_troop(),
]
