split_string="heyy you"
print(split_string.split(" "))
split_string2="heyy,you"
print(split_string2.split(","))
split_string3="heyy/you"
print(split_string3.split("/"))

center_string="heyy you"
print(center_string.center(20,"~"))
count_string="heyy heyy heyyou hai"
print(count_string.count("heyy"))
endswith_string="heyy."
print(endswith_string.endswith("."))
print(endswith_string.endswith(","))

find_string="please arrest dileep"
print(find_string.find("dileep"))
print(find_string.find("dilleep"))
print(find_string.find("dileep",4) )    #4 is starting.