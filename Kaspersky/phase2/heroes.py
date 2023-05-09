def check_mission(heroes, mission) -> tuple:
	ability_list = []
	hero_list = []
	for hero in heroes:
		hero_list.append(hero)
		ability_list.extend(hero[1])

	for stage in mission:
		if stage not in ability_list or mission.count(stage) > ability_list.count(stage):
			return ()

	hero_list.sort(key=lambda x: x[1])
	return tuple([i[0] for i in hero_list])


heroes = (("Илья М.", (1, 2, 3)),)
mission = (1,)

heroes2 = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)
mission2 = (1, 2)

heroes3 = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))
mission3 = (1, 1, 2)

heroes4 = (("Добрыня Н.", (2, 3)), ("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )))
mission4 = (1, 1, 2)

heroes5 = (("Добрыня Н.", (2, 3)), ("Илья М.", (2,)), ("Алёша П.", (1, )))
mission5 = (1, 1, 2)

heroes6 = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)
mission6 = (1, 5)

heroes7 = (("Добрыня Н.", (1, 2, 3, 4)), ("Илья М.", (1, 2, 4)), ("Алёша П.", (1, 2, 4)), ("----- П.", (1, 2, 4)))
mission7 = (1, 2, 3, 4)

heroes8 = (("Добрыня Н.", (1, 2, 3, 4)), ("Илья М.", (1, 2)), ("Алёша П.", (2, 4)), ("----- П.", (1, 4)))
mission8 = (1, 2, 3, 4)

# test Ok
# print(check_mission(heroes, mission))
print(check_mission(heroes2, mission2))
print(check_mission(heroes3, mission3))
print(check_mission(heroes4, mission4))
print(check_mission(heroes5, mission5))
print(check_mission(heroes6, mission6))
# test Fail
print(check_mission(heroes7, mission7))
print(check_mission(heroes8, mission8))
