def calculate_coffee_stats(office_stats_list):
    hello = sorted(office_stats_list)
    new_list = []
    for i in hello:
        new_list.append(i.split(","))
    print(new_list)

calculate_coffee_stats(["Hawke's Bay,Jan,542", "Hawke's Bay,Feb,348", "Auckland,Apr,6744"])
