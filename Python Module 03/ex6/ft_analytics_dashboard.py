scores = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 2050
}
achs = {
    "alice": ["first_kill", "level_10", "boss_slayer", "speedrun", "mvp"],
    "bob": ["first_kill", "level_10", "collector"],
    "charlie": ["first_kill", "boss_slayer", "marathon", "level_10",
                "explorer", "warrior", "veteran"],
    "diana": ["first_kill", "level_10", "boss_slayer"]
}
p_is_act = {
    "alice": True,
    "bob": True,
    "charlie": True,
    "diana": False
}
p_reg = {
    "alice": "north",
    "bob": "east",
    "charlie": "central",
    "diana": "west"
}

print("=== Game Analytics Dashboard ===")
print()
print("=== List Comprehension Examples ===")
high_scores = [name for name, score in scores.items() if score > 2000]
print(f"High scorers (>2000): {high_scores}")
doubled_scores = [score * 2 for score in scores.values()]
print(f"Scores doubled: {doubled_scores}")
active_players = [name for name, is_active in p_is_act.items() if is_active]
print(f"Active players: {active_players}")
print()
print("=== Dict Comprehension Examples ===")
pscore = {n: scores[n] for n, is_active in p_is_act.items() if is_active}
print(f"PLayer Scores: {pscore}")
list_score_cat = [('high' if s > 2200 else 'medium' if s > 2000 else 'low')
                  for s in scores.values()]
dict_score_cat = {cat: list_score_cat.count(cat)
                  for cat in ['high', 'medium', 'low']}
print(f"Score categories: {dict_score_cat}")
achievements_count = {name: len(achs[name])
                      for name, is_active in p_is_act.items() if is_active}
print(f"Achievement counts: {achievements_count}")
print()
print("=== Set Comprehension Examples ===")
unique_players = {name for name in scores.keys()}
print(f"Unique players {unique_players}")
unique_achievements = {achievement for achievements in achs.values()
                       for achievement in achievements}
print(f"Unique achievements {unique_achievements}")
regions = {p_reg[name] for name, is_active in p_is_act.items() if is_active}
print(f"active regions: {regions}")
print()
print("=== Combined Analysis === ")
total_players = len(scores)
print(f"Total players: {total_players}")
total_unique_achievements = len(unique_achievements)
print(f"Total unique achievements: {total_unique_achievements}")
average_score = sum(list(scores.values()))/total_players
print(f"Average score: {average_score:.1f}")
top_performer = max(scores, key=lambda name: scores[name])
top_performer_achievements = len(achs["alice"])
print(f"Top performer: {top_performer} ({scores['alice']} points, "
      f"{top_performer_achievements} achievements)")
