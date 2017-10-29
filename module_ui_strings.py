from compiler import *

ui_strings = [
	
	("music_volume", "Music Volume:"),
	("sound_volume", "Sound Volume:"),
	("mouse_sensitivity", "Mouse Sensitivity:"),
	("invert_mouse_y_axis", "Invert Mouse Y Axis"),
	("enabled", "Enabled"),
	("disabled", "Disabled"),
	("damage_to_player", "Damage to Player:"),
	("reduced_to_1_over_4_easiest", "Reduced to 1/4 (Easiest)"),
	("reduced_to_1_over_2_easy", "Reduced to 1/2 (Easy)"),
	("damage_to_friends", "Damage to Friends:"),
	("reduced_to_1_over_2_easiest", "Reduced to 1/2 (Easiest)"),
	("reduced_to_3_over_4_easy", "Reduced to 3/4 (Easy)"),
	("normal", "Normal"),
	("combat_ai", "Combat AI:"),
	("combat_speed", "Combat Speed:"),
	("good", "Good"),
	("average_caps", "Average"),
	("poor", "Poor"),
	("faster", "Faster"),
	("slower", "Slower"),
	("control_block_direction", "Control Block Direction:"),
	("automatic_recommended", "Automatic"),
	("manual_easy", "Manual (Easy)"),
	("manual_hard", "Manual (Hard)"),
	("by_mouse_movement", "By mouse movement"),
	("control_attack_direction", "Control Attack Direction:"),
	("lance_control", "Lance Control:"),
	("by_relative_enemy_position", "By relative enemy position"),
	("by_inverse_mouse_movement", "By inverse mouse movement"),
	("battle_size", "Battle Size:"),
	("show_attack_direction", "Show Attack Direction"),
	("show_targeting_reticule", "Show Targeting Reticle"),
	("show_names_of_friendly_troops", "Show Banners on Friendly Troops"),
	("report_damage", "Report Damage"),
	("report_shot_difficulty", "Report Shot Difficulty"),
	("difficulty_rating_percentage", "Difficulty Rating = %d%%"),
	("controls", "Controls"),
	("video_options", "Video Options"),
	("done", "Done"),
	("factions", "Factions"),
	("item_itemname", "Item - %s"),
	("prop_propname", "Prop - %s"),
	("unknown_unknownname", "Unknown - %s"),
	("entry_point_entrypointname", "Entry Point %d"),
	("passage_menu_item_passagename", "Passage (menu item %d)"),
	("plant_plantname", "Plant - %s"),
	("export_file_for_character_playername_already_exists_overwrite_it", "Export file for character %s already exists. Overwrite it?"),
	("yes", "Yes"),
	("no", "No"),
	("set_save_file_name", "Enter a name for this save-game:"),
	("enter_new_name", "Enter a new name:"),
	("export_character", "Export Character"),
	("import_character", "Import Character"),
	("character_playername_exported_successfully", "Character %s exported successfully."),
	("character_playername_imported_successfully", "Character %s imported successfully."),
	("unable_to_open_import_file", "Unable to open import file."),
	("are_you_sure_you_want_to_import_the_character", "Are you sure you want to import the character?"),
	("unable_to_find_character_import_file", "Unable to find character import file."),
	("mount_and_blade_is_running_in_trial_mode_please_buy_the_game_for_importing_a_character", "Mount&Blade is running in trial mode. Please buy the game for importing a character."),
	("change_skin", "Skin"),
	("change_hair", "Hair"),
	("change_hair_color", "Hair Color"),
	("change_beard", "Beard"),
	("tutorial", "Tutorial"),
	("tutorial_face_generator", "Adjust your character's face using the buttons and the sliders. To rotate the head, click on it and drag the mouse."),
	("restore", "Load"),
	("cancel", "Cancel"),
	("delete", "Delete"),
	("confirm_delete_game", "Are you sure you want to delete this game?"),
	("error_removing_file", "Error removing file..."),
	("day_datedisplay", "Day %d (%d:%d%d)"),
	("reset_changes", "Reset Changes"),
	("weapon_proficiencies", "Proficiencies"),
	("skills", "Skills"),
	("attributes", "Attributes"),
	("enter_name_here", "*Enter Name Here*"),
	("edit_face", "Click to edit face"),
	("statistics", "Statistics"),
	("next", "Next"),
	("prev", "Prev"),
	("learn", "Learn"),
	("question_saving_policy", "What will the game's saving policy be?"),
	("saving_policy_realistic", "Realistic! No quitting without saving!"),
	("saving_policy_nonrealistic", "Allow me to quit without saving."),
	("tutorial_character_generation", "Now enter your name and distribute your attribute, skill and weapon points. You can click on various elements on the screen to learn how each one will affect your character."),
	("str", "STR"),
	("agi", "AGI"),
	("int", "INT"),
	("cha", "CHA"),
	("at_learning_limit", "(At learning limit)"),
	("not_enough_skill_points_to_learn", "(Not enough skill points to learn)"),
	("strength", "strength"),
	("agility", "agility"),
	("intelligence", "intelligence"),
	("charisma", "charisma"),
	("not_enough_attributetype_to_learn_this_skill", "(Not enough %s to learn this skill)"),
	("explanation_one_handed_weapon", "Covers usage of one handed swords, axes and blunt weapons."),
	("explanation_two_handed_weapon", "Covers usage of two handed swords, great axes and mauls."),
	("explanation_polearm", "Covers usage of pole weapons like spears, lances, staffs, etc."),
	("explanation_archery", "Covers usage of bows."),
	("explanation_crossbow", "Covers usage of crossbows."),
	("explanation_throwing", "Covers usage of thrown weapons like javelins, darts, stones etc."),
	("explanation_firearms", "Covers usage of pistols and muskets."),
	("explanation_strength", "Strength: Every point adds +1 to hit points. The following skills can not be developed beyond 1/3 of Strength: ironflesh, Power-strike, Power-throw, Power-draw."),
	("explanation_agility", "Agility: Each point gives five weapon points and slightly increases movement speed. The following skills can not be developed beyond 1/3 of Agility: weapon-master, Shield, Athletics, Riding, Horse archery, Looting."),
	("explanation_intelligence", "Intelligence: Every point to intelligence immediately gives one extra skill point. The following skills can not be developed beyond 1/3 of Intelligence: Trainer, Tracking, Tactics,  Path finding, Spotting, Inventory Management, Wound treatment, Surgery, First-aid, Engineer, Persuasion."),
	("explanation_charisma", "Charisma: Each point increases your party size limit by +1. The following skills can not be developed beyond 1/3 of Charisma: Prisoner Management, Leadership, Trade."),
	("level", "Level: %d"),
	("xp", "Experience: %d"),
	("next_level_at", "Next level at: %d"),
	("health_player", "Health: %d/%d"),
	("health", "Health: %d"),
	("attribute_points", "Attribute points: %d"),
	("skill_points", "Skill points: %d"),
	("weapon_points", "Weapon points: %d"),
	("mission_losses_none", " none."),
	("mission_losses_wounded", "wounded :"),
	("mission_losses_killed", "killed :"),
	("party_losses", "%s  : %d wounded --- %d killed of %d."),
	("casualties_sustained", "Casualties sustained:"),
	("advantage_change", "Advantage change = %c%d "),
	("overall_battle_casualties", "Overall battle causalties:"),
	("advantage_outnumbered", " You are hopelessly outnumbered."),
	("advantage_major_disadvantage", " You have a major disadvantage."),
	("advantage_slight_disadvantage", " You are slightly disadvantaged."),
	("advantage_balanced", " The situation is balanced."),
	("advantage_fair_advantage", " You have a fair advantage for winning."),
	("advantage_greatly_favored", " The odds of battle favor you greatly."),
	("tactical_advantage", "Tactical advantage: %d (%s)"),
	("order_group", "Order group:"),
	("question_save_changes", "You have made changes to the objects. Do you want to save changes?"),
	("yes_save", "Yes, save"),
	("no_discard_changes", "No, discard changes"),
	("everyone_control", "Everyone!"),
	("everyone_around_control", "Nearby Soldiers!"),
	("others_control", "Others!"),
	("question_give_up_fight", "Give up the fight?"),
	("give_up", "Give up"),
	("keep_fighting", "Keep fighting"),
	("question_leave_area", "Leave Area"),
	("cant_retreat_there_are_enemies_nearby", "Can't retreat. There are enemies nearby!"),
	("question_retreat_battle", "Retreat battle?"),
	("retreated_battle", "%s has been routed."),
	("retreated_battle", "%s has fled from the battlefield."),
	("retreat", "Retreat"),
	("talk", "Talk"),
	("duel", "Duel"),
	("mount", "Mount"),
	("riding_skill_not_adequate_to_mount", "(Riding skill not adequate to mount)"),
	("dismount", "Dismount"),
	("exit", "Exit"),
	("door_to", "Door to "),
	("open", "Open"),
	("equip", "Equip"),
	("baggage", "Baggage"),
	("access_inventory", "Access inventory"),
	("chest", "Chest"),
	("passage", "Passage"),
	("go", "Go"),
	("retreat_battle", "Retreat Battle"),
	("leave_area", "Leave Area"),
	("reports", "Reports"),
	("camp", "Camp"),
	("terrain", "Terrain"),
	("quests", "Notes"),
	("inventory", "Inventory"),
	("character", "Character"),
	("party", "Party"),
	("paused", "Paused"),
	("click_left_button_to_cancel_wait", "Waiting... (Left click to return)"),
	("midnight", "Midnight"),
	("late_night", "Late night"),
	("dawn", "Dawn"),
	("early_morning", "Early morning"),
	("morning", "Morning"),
	("noon", "Noon"),
	("afternoon", "Afternoon"),
	("late_afternoon", "Late afternoon"),
	("dusk", "Dusk"),
	("evening", "Evening"),
	("midnight", "Midnight"),
	("level_limit_reached", "Level Limit Reached!"),
	("explanation_level_limit", "Hail Adventurer, Mount&Blade has not been activated yet and is running in trial mode. In this mode, the game is limited to Level 8. In order to continue playing, please restart the game and activate it with your 16-digit serial key which is included in your boxed copy. After activating, you can continue playing right from here. Now, Mount&Blade will save your game and exit."),
	("time_limit_reached", "Time Limit Reached!"),
	("explanation_time_limit", "Hail Adventurer, Mount&Blade has not been activated yet and is running in trial mode. In this mode, the game is limited to 30 game days. In oder to continue playing, please restart the game and activate it with your 16-digit serial key which is included in your boxed copy. After activating, you can continue playing right from here. Now, Mount&Blade will save your game and exit."),
	("target_lost", "Target lost"),
	("waiting", "Waiting."),
	("travelling_to", "Travelling to "),
	("following", "Following "),
	("accompanying", "Accompanying "),
	("running_from", "Running from "),
	("patrolling", "Patrolling"),
	("patrolling_around", "Patrolling around "),
	("holding", "Holding"),
	("travelling", "Travelling"),
	("fighting_against", "Fighting against "),
	("speed_equals", "Speed = %2.1f"),
	("defenders", "Garrison:"),
	("prisoners", "Prisoners:"),
	("1_hour", "1 hour"),
	("n_hours", "%d hours"),
	("between_hours", "%d - %d hours"),
	("combatants", "Combatants: %d"),
	("party_size", "Party size: %d"),
	("party_size_between", "Party size: %d - %d"),
	("merchant", "Merchant"),
	("return", "Return"),
	("no_cost", "No cost"),
	("rename", "Rename"),
	("use", "Use"),
	("destroy", "Destroy"),
	("destructible_target", "Destructible target"),
	("tutorial_inventory", "This is the trade screen. Hold down control key while clicking on an item to quickly purchase or sell it."),
	("head_armor", "Head Armor: %d"),
	("body_armor", "Body Armor: %d"),
	("leg_armor", "Leg Armor: %d"),
	("encumbrance", "Encumbrance: %2.1f"),
	("you_dont_have_value", "You don't have %s."),
	("merchant_cant_afford_value", "%s: I can't afford %s. I have only %s."),
	("merchant_pay_whatever", "Allright, just pay whatever you can."),
	("merchant_think_of_something_else", "Hmm. Let us think of something else."),
	("dumping_value_items", "%d items will be permanently lost, are you sure?"),
	("dumping_value_item", "One item will be permanently lost, are you sure?"),
	("question_slaughter_food_and_eat", "Slaughter this %s and eat it?"),
	("money_value", "Money: %s"),
	("dump", "Discard"),
	("outfit", "Outfit"),
	("arms", "Arms"),
	("horse", "Horse"),
	("food", "Food"),
	("reclaim_your_sold_goods", "Reclaim your sold goods before buying that!"),
	("return_your_bought_goods", "Return your bought goods before selling that!"),
	("polearm_no_shield", "Polearm (No shield)"),
	("polearm", "Polearm"),
	("two_handed", "Two-handed"),
	("two_handed_one_handed", "Two-handed/One-handed"),
	("one_handed", "One-handed"),
	("return_price", "Return price: %d"),
	("sell_price", "Sell price: %d"),
	("reclaim_price", "Reclaim price: %d"),
	("buying_price", "Buying price: %d"),
	("default_item", "Default item"),
	("buying_price_free", "Buying price: Free"),
	("weight", "Weight: %2.1f"),
	("plus_value_to_head_armor", "+%d to head armor"),
	("plus_value_to_body_armor", "+%d to body armor"),
	("plus_value_to_leg_armor", "+%d to leg armor"),
	("swing", "Swing: %d%s"),
	("damage", "Damage: %d%s"),
	("thrust", "Thrust: %d%s"),
	("accuracy", "Accuracy: %d"),
	("speed_rating", "Speed rating: %d"),
	("value_to_damage", "%c%d to damage"),
	("value_to_morale", "+%1.1f to party morale"),
	("resistance", "Resistance: %d"),
	("size", "Size: %d"),
	("weapon_reach", "Weapon reach: %d"),
	("armor", "Armor: %d"),
	("speed", "Speed: %d"),
	("maneuver", "Maneuver: %d"),
	("charge", "Charge: %d"),
	("hit_points", "Hit Points: %d/%d"),
	("requires_value_difficulty", "Requires %s: %d"),
	("bonus_against_shields", "Bonus against shields"),
	("cant_be_used_to_block", "Can't be used to block"),
	("troop_cant_use_item", "%s: I can't use that item!"),
	("notification_riding_skill_not_enough", "Your riding skill is not high enough to mount this horse."),
	("notification_requirements_not_met", "You don't have the required skills or attributes for this weapon."),
	("notification_payment_value", "You must pay %s."),
	("notification_payment_receive_value", "You will receive %s."),
	("one_handed_weapons", "One Handed Weapons"),
	("two_handed_weapons", "Two Handed Weapons"),
	("polearms", "Polearms"),
	("archery", "Archery"),
	("crossbows", "Crossbows"),
	("throwing", "Throwing"),
	("firearms", "Firearms"),
	("reset", "Reset"),
	("release_one", "Release one"),
	("move_up", "Move Up"),
	("move_down", " Move Down "),
	("upgrade_one", "Upgrade one"),
	("party_skills", "Party Skills"),
	("morale", "Morale: %s"),
	("terrible", "Terrible"),
	("very_low", "Very low"),
	("low", "Low"),
	("below_average", "Below average"),
	("average", "Average"),
	("above_average", "Above average"),
	("high", "High"),
	("very_high", "Very high"),
	("excellent", "Excellent"),
	("starving", "Starving! %d%%"),
	("weekly_cost_value", "Weekly cost: %s"),
	("company", "Company: %d / %d"),
	("prisoners_equal_value", "Prisoners: %d / %d"),
	("choose_prisoners", "Choose Prisoners"),
	("choose_companions", "Choose Companions"),
	("rescued_prisoners", "Rescued Prisoners"),
	("captured_enemies", "Captured Enemies"),
	("disband", "Disband"),
	("take_prisoner", "Take prisoner"),
	("take_back", "Take back"),
	("give", "Give"),
	("take", "Take"),
	("sell", "Sell"),
	("hire", "Hire"),
	("notification_cant_hire", "(Can't hire: not enough money)"),
	("uncapture", "Release"),
	("capture", "Capture"),
	("party_capcity_reached", "(Party capacity reached)"),
	("all", " all"),
	("joining_cost_weekly_wage", "Joining cost: %d, Weekly wage: %d"),
	("weekly_wage", "Weekly wage: %d denars"),
	("price", "Price: %d"),
	("number_ready_to_upgrade", "%d ready to be upgraded."),
	("upgrade_to_value", " Upgrade to %s (%dd)"),
	("notification_no_slot_for_upgrade", "No slot for upgrading to %s!"),
	("shield_broken", "Shield broken."),
	("shield_cracked", "Shield cracked."),
	("shield_deformed", "Shield deformed."),
	("you_hit_a_friendly_troop", "You hit a friendly troop!"),
	("hit_shield_on_back", "Hit shield on back!"),
	("delivered_couched_lance_damage", "Delivered couched lance damage!"),
	("received_couched_lance_damage", "Received couched lance damage!"),
	("speed_bonus_plus", "Speed bonus: +%d%%"),
	("speed_bonus", "Speed bonus: %d%%"),
	("cant_reload_this_weapon_on_horseback", "Can't reload this weapon on horseback."),
	("no_more_bolts", "No more bolts..."),
	("you_are_not_carrying_any_bolts", "You are not carrying any bolts."),
	("no_more_arrows", "No more arrows..."),
	("you_are_not_carrying_any_arrows", "You are not carrying any arrows."),
	("head_shot", "Head shot!"),
	("delivered_number_damage", "Delivered %d damage."),
	("delivered_number_damage_to_horse", "Delivered %d damage to horse."),
	("horse_charged_for_number_damage", "Horse charged for %d damage."),
	("received_number_damage", "Received %d damage."),
	("horse_received_number_damage", "Horse received %d damage."),
	("value_killed_teammate", "%s has killed a teammate!"),
	("horse_fell_dead", "Horse fell dead..."),
	("horse_crippled", "Horse crippled..."),
	("shot_difficulty", "Shot difficulty: %2.1f"),
	("you_have_improved_your_proficiency_in_value_to_number", "You have improved your proficiency in %s to %d."),
	("your_proficiency_in_value_has_improved_by_number_to_number", "Your proficiency in %s has improved by +%d to %d."),
	("value_killed_by_value", "%s killed by %s."),
	("value_fell_dead", "%s fell dead."),
	("value_knocked_unconscious_by_value", "%s knocked unconscious by %s."),
	("value_fell_unconscious", "%s fell unconscious."),
	("troop_routed", "%s has been routed."),
	("troop_panicked", "%s has panicked."),
	("troop_fled", "%s has fled the battle."),
	("you_got_number_experience", "You got %d experience."),
	("you_have_advanced_to_level_number", "You have advanced to level %d."),
	("value_has_advanced_to_level_number", "%s has advanced to level %d."),
	("you_got_value", "You got %s."),
	("new_quest_taken", "New quest taken: %s."),
	("quest_completed_value", "Quest completed: %s."),
	("quest_succeeded_value", "Quest succeeded: %s."),
	("quest_failed_value", "Quest failed: %s."),
	("quest_concluded_value", "Quest concluded: %s."),
	("quest_cancelled_value", "Quest cancelled: %s."),
	("lost_value", " (Lost: %s)"),
	("items_lost", " (Items lost:"),
	("party_has_nothing_to_eat", "Party has nothing to eat!"),
	("days_training_is_complete", "Day's training is complete..."),
	("total_experience_gained_through_training_number", "Total experience gained through training: %d"),
	("some_soldiers_are_ready_to_upgrade", "Some soldiers are ready to upgrade."),
	("number_of_companions_exceeds_leadership_limit", " Number of companions exceeds leadership limit."),
	("number_of_prisoners_exceeds_prisoner_management_limit", " Number of prisoners exceeds prisoner management limit."),
	("party_morale_is_low", " Party morale is low!"),
	("and_one_space", " and"),
	("has_deserted_the_party", " has deserted the party."),
	("have_deserted_the_party", " have deserted the party."),
	("weekly_report", "Weekly report"),
	("shared_number_experience_within_party", "Shared %d experience within party."),
	("got_item_value", "Got item: %s."),
	("game_saved_successfully", "Game saved successfully."),
	("autosaving", "Autosaving..."),
	("quick_saving", "Quick-saving..."),
	("cant_quick_save", "Can't Quick-save during battle..."),
	("screenshot_taken_to_value", "Screenshot is saved to %s"),
	("screenshot_failed", "Can't save screenshot."),
	("value_joined_your_party", "%s joined your party."),
	("value_joined_party_as_prisoner", "%s joined party as prisoner."),
	("value_has_joined_party", "%s has joined party."),
	("value_has_been_taken_prisoner", "%s has been taken prisoner."),
	("value_left_the_party", "%s left the party."),
	("number_values_left_the_party", "%d %s(s) left the party."),
	("number_value_left_the_party", "%d %s left the party."),
	("your_relations_with_value_has_improved_from_number_to_number", "Your relations with %s has improved from %d to %d."),
	("your_relations_with_value_has_deteriorated_from_number_to_number", "Your relations with %s has deteriorated from %d to %d."),
	("you_lost_value", "You lost %s."),
	("lost_item_value", "Lost item: %s."),
	("got_number_value", "Got %d %s."),
	("lost_number_value", "Lost %d %s."),
	("set_default_keys", "Set default keys"),
	("undo_changes", "Undo changes"),
	("press_a_key", "Press a key"),
	("return_to_game", "Return to Game"),
	("options", "Options"),
	("save_and_exit", "Save & Exit"),
	("save", "Save"),
	("save_as", "Save As"),
	("quit_without_saving", "Quit without Saving"),
	("empty_slot", "Empty Slot"),
	("game_saved", "Game saved..."),
	("confirm_overwrite", "Savegame for %s will be overwritten. Are you sure?"),
	("dynamic_lighting", "Dynamic Lighting"),
	("character_shadows", "Character Shadows"),
	("grass_density", "Grass Density:"),
	("environment_shadows", "Environment Shadows"),
	("realistic_shadows_on_plants", "Realistic Shadows on Plants:"),
	("particle_systems", "Particle Systems"),
	("gamma", "Monitor Gamma:"),
	("character_detail", "Character Detail:"),
	("character_shadow_detail", "Character Shadow Detail:"),
	("blood_stains", "Blood Stains:"),
	("on", "On"),
	("off", "Off"),
	("near_player_only", "Near player only"),
	("default", "Default"),
	("3d_grass", "3D Grass:"),
	("number_of_ragdolls", "Number of Rag Dolls:"),
	("number_of_corpses", "Number of Corpses:"),
	("unlimited", "Unlimited"),
	("anisotropic_filtering", "Anisotropic Filtering"),
	("fast_water_reflection", "Fast Water Reflections"),
	("maximum_framerate", "Max. Frame-rate:"),
	("show_framerate", "Show Frame-rate:"),
	("estimated_performance", "Estimated Performance: %d%%"),
	("change_graphics_settings_explanation", "Some changes you have made will take effect when you enter a new area."),
	("start_tutorial", "Play Tutorial"),
	("start_a_new_game", "Start a New Game"),
	("restore_a_saved_game", "Load Game"),
	("exit_to_windows", "Exit"),
	("credits", "Credits"),
	("version_value", "v%s"),
	("active_quests", "Active Quests"),
	("finished_quests", "Finished Quests"),
	("given_on_date", "Given on: %s"),
	("days_since_given", "Days since given: %d"),
	("quest_progression_number", "Quest progression: %d%%"),
	("too_many_quests", "Too many quests"),
	("ok", "OK"),
	("move_forward", "Move Forward"),
	("move_backward", "Move Backward"),
	("move_left", "Move Left"),
	("move_right", "Move Right"),
	("action", "Action"),
	("jump", "Jump"),
	("attack", "Attack"),
	("parry_then_attack", "Counter Attack"),
	("defend", "Defend"),
	("kick", "Kick"),
	("equip_weapon_1", "Equip Item 1"),
	("equip_weapon_2", "Equip Item 2"),
	("equip_weapon_3", "Equip Item 3"),
	("equip_weapon_4", "Equip Item 4"),
	("equip_next_weapon", "Equip Next Weapon"),
	("equip_next_shield", "Equip Next Shield"),
	("sheath_weapon", "Sheath Weapon"),
	("character_window", "Character Window"),
	("inventory_window", "Inventory Window"),
	("party_window", "Party Window"),
	("quests_window", "Quests Window"),
	("game_log_window", "Game Log Window"),
	("leave_location_retreat", "Leave Location/Retreat"),
	("zoom", "Zoom"),
	("view_outfit", "View Outfit"),
	("toggle_first_person_view", "Toggle First Person View"),
	("view_orders", "View Orders"),
	("quick_save", "Quick Save"),
	("no_key_assigned", "No key assigned"),
	("new_enemies_have_arrived", "New enemies have arrived."),
	("reinforcements_have_arrived", "Reinforcements have arrived."),
	("report_casualties", "Report Casualties"),
	("report_experience", "Report Experience"),
	("current_level_value", "Current Level: %d"),
	("base_attribute_value", "Base Attribute: %s"),
	("battle_controls", "Battle Controls"),
	("map_controls", "Map Controls"),
	("general_controls", "General Controls"),
	("zoom_in", "Zoom In"),
	("zoom_out", "Zoom Out"),
	("wait", "Wait"),
	("take_screenshot", "Take Screenshot"),
	("randomize", "Randomize"),
	("hint", "Hint"),
	("press_left_mouse_button_to_continue", "Press left mouse button to continue..."),
	("loot", "Loot"),
	("chest", "Chest"),
	("cut_short", "c"),
	("pierce_short", "p"),
	("blunt_short", "b"),
	("battle", "Battle"),
	("siege", "Siege"),
	("troops", "Troops:"),
	("loading_module_info_file", "Loading Module Info File..."),
	("processing_ini_file", "Processing INI File..."),
	("loading_music", "Loading Music..."),
	("loading_data", "Loading Data..."),
	("loading_setting_data", "Loading Setting Data..."),
	("loading_textures", "Loading Textures..."),
	("finished", "Finished."),
	("creating_game", "Creating Game..."),
	("loading_savegame_file", "Loading Savegame File..."),
	("loading_map_file", "Loading Map File..."),
	("initializing_map", "Initializing Map..."),
	("launching_game", "Launching Game..."),
	("capital_battle", "BATTLE:"),
	("capital_versus", "--VERSUS--"),
	("tracks", "Tracks"),
	("battleground", "Battleground"),
	("order_1", "Select Order 1"),
	("order_2", "Select Order 2"),
	("order_3", "Select Order 3"),
	("order_4", "Select Order 4"),
	("order_5", "Select Order 5"),
	("order_6", "Select Order 6"),
	("order_button_hold_this_position", "Hold this position"),
	("order_button_follow_me", "Follow me"),
	("order_button_charge", "Charge"),
	("order_button_stand_ground", "Stand ground"),
	("order_button_retreat", "Retreat"),
	("order_button_advance", "Advance ten paces"),
	("order_button_fall_back", "Fall back ten paces"),
	("order_button_spread_out", "Spread out"),
	("order_button_stand_closer", "Stand closer"),
	("order_button_mount_horses", "Mount horses"),
	("order_button_dismount", "Dismount"),
	("order_button_hold_fire", "Hold your fire"),
	("order_button_fire_at_will", "Fire at will"),
	("order_button_use_blunt_weapons", "Use only blunt weapons"),
	("order_button_use_any_weapon", "Use weapons at will"),
	("order_button_movement_orders", "Movement orders"),
	("order_button_formation_orders", "Formation orders"),
	("order_button_fire_orders", "Fire orders"),
	("follow_me_e_", "%s, follow me!"),
	("charge_e_", "%s, charge!!!"),
	("stand_ground_e_", "%s, stand ground!"),
	("retreat_e_", "%s, retreat!"),
	("mount_horses_e_", "%s, mount horses!"),
	("dismount_e_", "%s, dismount!"),
	("advance_e_", "%s, advance ten paces!"),
	("fall_back_e_", "%s, fall back ten paces!"),
	("stand_closer_e_", "%s, stand closer!"),
	("spread_out_e_", "%s, spread out!"),
	("use_blunt_weapons_e_", "%s, use only blunt weapons!"),
	("use_any_weapon_e_", "%s, use weapons at will!"),
	("hold_fire_e_", "%s, hold your fire!"),
	("fire_at_will_e_", "%s, fire at will!"),
	("hold_this_position_e_", "%s, hold this position!"),
	("infantry", "Infantry"),
	("archers", "Archers"),
	("cavalry", "Cavalry"),
	("companions", "Companions"),
	("everyone_hear_me", "Everyone, hear me!"),
	("everyone", "Everyone"),
	("everyone_around_me", "Nearby Soldiers"),
	("str_hear_me", "%s, hear me!"),
	("str_and_str", "%s and %s"),
	("str_comma_str", "%s, %s"),
	("need_to_learn_prisoner_management", "You need to learn Prisoner Management skill in order to take prisoners."),
	("game_log", "Game Log"),
	("recent_messages", "Recent Messages"),
	("custom_battle", "Custom Battle"),
	("player", "Player"),
	("value_denars", "%d denars"),
	("back", "Back"),
	("forward", "Forward"),
	("display_on_map", "Show On Map"),
	("info_pages", "Game Concepts"),
	("troops2", "Characters"),
	("locations", "Locations"),
	("click_button_to_view_note", "Click on a link to view the notes"),
	("this_page_contains_no_information", "This page contains no information"),
	("other_pages_that_link_here", "Other pages that link here: "),
	("report_is_value_days_old", " (Report is %d days old)"),
	("report_is_current", " (Report is current)"),
	("button_party_member_healthy_total", "%s (%d/%d)"),
	("button_party_member_total", "%s (%d)"),
	("button_party_member_hero_percentage_wounded", "%s (%d%% - Wounded)"),
	("button_party_member_hero_percentage", "%s (%d%%)"),
	("percentage_value", "%d%%"),
	("full", "Full"),
	("quick", "Quick"),
	("none", "None"),
	("change", "Change"),
	("how_to_change", "How to change this?"),
	("change_directx_explanation", "You can change the render method between DirectX 7 and DirectX 9 by clicking on the Configure button at the launch menu that comes up when you first start the game."),
	("dropping_picking_up", "Dropping %s; picking up %s."),
	("dropping", "Dropping %s."),
	("picking_up", "Picking up %s."),
	("unable_to_take", "Unable to take that."),
	("age", "Age"),
	("cannot_be_used_on_horseback", "Cannot be used on horseback"),
	("enable_vertex_shaders2", "Render Method:"),
	("screen_size2", "Screen Resolution:"),
	("use_desktop_resolution2", "Use Desktop Resolution"),
	("shadow_quality2", "Shadow Quality:"),
	("m_low2", "Low"),
	("m_high2", "High"),
	("m_ultra_high2", "Ultra High"),
	("off2", "Off"),
	("group_header", "Class of troop"),
	("group_rename", "Rename group"),
	("group_1", "Infantry"),
	("group_2", "Archers"),
	("group_3", "Cavalry"),
	("group_4", "Unnamed 1"),
	("group_5", "Unnamed 2"),
	("group_6", "Unnamed 3"),
	("group_7", "Unnamed 4"),
	("group_8", "Unnamed 5"),
	("group_9", "Unnamed 6"),
	("group_rename", "Rename Group"),
	("group_close", "Close"),
	("party_b_group_information", "%s belongs to %s group"),
	("thrown_or_s", "Thrown/%s"),
	("ranged_damage", "Ranged: %d%s"),
	("overall_quality", "Overall Quality"),
	("shader_quality", "Shader Quality:"),
	("flora_lod_detail", "Tree Detail:"),
	("flora_degrade_distance", "Tree Degrade Distance:"),
	("antialiasing", "AntiAliasing:"),
	("use_depth_effects", "Use Depth Effects"),
	("hdr_mode", "HDR Mode:"),
	("autoexpore", "Auto-exposure"),
	("choose_profile", "Choose Profile"),
	("create", "Create"),
	("edit", "Edit"),
	("join_game", "Join a Game"),
	("host_game", "Host a Game"),
	("custom", "Custom"),
	("medium", "Medium"),
	("male", "Male"),
	("female", "Female"),
	("gender", "Choose Gender:"),
	("edit_profile", "Edit Profile"),
	("new_profile", "New Profile"),
	("enter_username", "Enter Username:"),
	("invalid_username", "Usernames may only contain letters, numbers or _ - * [ ] ~ characters."),
	("confirmation", "Are you sure?"),
	("multiplayer", "Multiplayer"),
	("server_name", "Server"),
	("module_name", "Module"),
	("game_type", "Game Type"),
	("map_name", "Map"),
	("ping", "Ping"),
	("dedicated", "Dedicated"),
	("number_of_players", "Players"),
	("password_protected", "Password"),
	("connect", "Connect"),
	("local_area_network", "Local Area Network"),
	("internet", "Internet"),
	("favorites", "Favorites"),
	("source", "Source:"),
	("server_password", "Server Password:"),
	("refresh", "Refresh"),
	("start_search", "Start Search"),
	("add_to_favorites", "Add to Favorites"),
	("remove_from_favorites", "Remove from Favorites"),
	("use_speedtree", "Use Speedtree"),
	("use_instancing", "Use Instancing"),
	("error", "Error"),
	("error_server_full", "Server is full."),
	("error_server_full_for_non_private", "Server is full for players without a private member password."),
	("error_server_password_incorrect", "Incorrect password."),
	("error_incorrect_serial", "Incorrect serial number."),
	("error_incorrect_authorization_key", "Incorrect authorization key."),
	("error_banned_from_server", "You are banned from this server."),
	("error_username_taken", "Your profile name is used by another player."),
	("error_authentication_failed", "Authentication failed."),
	("unable_to_connect_to_server", "Unable to connect to server."),
	("connection_to_server_is_lost", "Connection to server is lost."),
	("kicked_from_server", "Kicked from server."),
	("switch_to_module_question", "This server is running another module than the one you are currently running. Do you want Mount&Blade to switch to this module?"),
	("download_module_question", "This server is running a module that is not installed on your computer. Would you like to visit the download site for this module now?"),
	("download_mb_new_version_question", "This server is running a newer version (%d.%d%d%d) of Mount&Blade than the one you are currently running (%d.%d%d%d). Would you like to visit TaleWorlds download site now?"),
	("download_mb_old_version_question", "This server is running an older version (%d.%d%d%d) of Mount&Blade and than the one you are currently running (%d.%d%d%d)."),
	("download_module_new_version_question", "This server is running a newer version (%d.%d%d%d) of the current module than the one you are running (%d.%d%d%d). Would you like to visit the download site for this module now?"),
	("download_module_old_version_question", "This server is running an older version (%d.%d%d%d) of the current module than the one you are running (%d.%d%d%d)."),
	("authenticating_with_steam", "Authenticating with Steam..."),
	("validating_serial_number", "Validating serial number..."),
	("scanning_lan", "Scanning local area network..."),
	("retrieving_servers", "Retrieving server list..."),
	("shield_size2", "Size: %dx%d"),
	("click_to_view_notes", "Click to view notes"),
	("retrieving_server_infos", "Retrieving information from servers (%d)..."),
	("connecting_to_server", "Connecting to server..."),
	("requesting_to_join_the_game", "Requesting to join the game..."),
	("loading", "Loading..."),
	("group_value_control", "Group %d!"),
	("drop_weapon", "Drop Weapon"),
	("multiplayer_message_all", "Send Message to Everyone"),
	("multiplayer_message_team", "Send Message to Team"),
	("command_line", "Command Line"),
	("use_ranged_weapon_as_melee", "Toggle Weapon Mode"),
	("send_message_all", "Send Message to Everyone"),
	("send_message_team", "Send Message to Team"),
	("select", "Select"),
	("context_menu", "Context Menu"),
	("round_starts_in_value_seconds", "Round starts in %d seconds..."),
	("watching_value", "Following %s"),
	("capital_spec", "SPEC"),
	("capital_dead", "DEAD"),
	("instancing_error1", "Could not lock Instance Buffer (size: %d), Disabled mesh-instancing (Error Code: %d)"),
	("instancing_error2", "Could not fit instanced objects, Disabled mesh-instancing"),
	("by_keyboard", "By movement keys"),
	("combat_speed_slowest", "Slowest"),
	("combat_speed_slower", "Slower"),
	("combat_speed_normal", "Normal"),
	("combat_speed_faster", "Faster"),
	("combat_speed_fastest", "Fastest"),
	("module_newer_than_application", "The module you have selected requires a newer version of the game."),
	("module_older_than_application", "The module you have selected requires an older version of the game."),
	("unbalanced", "Unbalanced"),
	("can_crush_through_blocks", "Can crush through blocks"),
	("turn_camera_with_horse", "Turn Camera with Horse in First Person:"),
	("widescreen_mode_on", "Multiple Screen Mode Enabled"),
	("widescreen_mode_off", "Multiple Screen Mode Disabled"),
	("notification_cant_upgrade", "(Can't upgrade: not enough money)"),
	("turn_never", "Never"),
	("turn_ranged_only", "Ranged only"),
	("turn_melee_only", "Melee only"),
	("turn_always", "Always"),
	("general_options", "General Options"),
	("vac_enabled", "Valve Anti Cheat Enabled"),
	("campaign_ai", "Campaign AI:"),
	("downloading_map", "Downloading map (%d KB)"),
	("download_completed", "Download completed."),
	("server_filter", "Server filter"),
	("has_players", "Has players"),
	("is_not_full", "Not full"),
	("is_password_free", "No password"),
	("native_only", "Native only"),
	("ping_limit", "Ping limit"),
	("filter_info", "%d games and %d players filtered"),
	("is_version_compatible", "Compatible with module"),
	("ttnet_account", "TTNET Oyun account"),
	("username", "Username"),
	("password", "Password"),
	("error_incorrect_username_or_password", "Incorrect username or password"),
	("validating_account", "Validating account..."),
	("plase_enter_your_serial_key", "Please enter your serial key"),
	("texture_detail2", "Texture Detail:"),
	("antialiasing2", "Antialiasing:"),
	("napoleonic_key_does_not_exist", "This mod requires the Napoleonic Wars DLC to play!"),
	("delete_module_workshop", "Are you sure you want to unsubscribe from this module?"),
	("delete_module", "Are you sure you want to delete the module?"),
	("delete_native_module", "You cannot delete native mods."),
	("incompatible_module", "This server is incompatible with your current module. You can use the configuration utility to change module."),
	
	]