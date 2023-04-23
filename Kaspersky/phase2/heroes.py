def check_mission(heroes, mission) -> tuple:
	set_man = set()
	set_power = set()
	for man, superpowers in heroes:
		for i in superpowers:
			set_power.add(i)
			if i in mission:
				set_man.add(man)
		for i in mission:
			if i not in set_power:
				return ()
	return tuple(set_man)


heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))
mission = (1, 1, 2)

heroes2 = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)
mission2 = (1, 5)

heroes3 = (("Илья М.", (1, 2, 3)),)
mission3 = (1,)


print(check_mission(heroes, mission))
print(check_mission(heroes2, mission2))
print(check_mission(heroes3, mission3))
