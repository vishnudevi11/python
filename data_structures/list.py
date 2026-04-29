# Creating lists for different apps
# mutable,index based,multiple datatypes
playlist=["Shape of You","Naa Ready","Maligapoo","Tum Hi Ho"]
favourite_foods=["Momos","Grill","Briyani","Dosa"]
recent_locations=["Home","PG","Work","Mall"]

# print("Playlist:",playlist)
# print("Zomato Foods:",favourite_foods)
# print("Uber Locations:",recent_locations)

# list methods
# playlist.append("Oo antava")
# playlist.insert(3,"mama mama")
# playlist.remove("Naa Ready")
# playlist.pop()
# playlist.reverse()

# print(playlist.count("Maligapoo"))

# List silicing
# print("top 2 songs",playlist[2:4])

# List iteration
# for food in favourite_foods:
#     print(food)

# for song in playlist:
#     print(song+" by vishnu")

# check if
# if "Dosa" in favourite_foods:
#     print("yes")
# else:
#     print("no")

# print(favourite_foods)
# favourite_foods[1]="shawarma"
# print(favourite_foods)

# mixed=["vishnu",26,1.56]
# for i in mixed:
#     print(i)


# index position
for i,location in enumerate(recent_locations):
    print(i,location)



