trip={
    "trip_id":"123456",
    "pickup":"Chennai_central",
    "drop":["Airport","thambaram","medavakam"],
    "fare":430.45,
    "driver":"Ravi",
    "status":"Completed"
}
# lookup
# print(trip["pickup"])
# print(trip.get("Airport"))
# print(trip.keys())
# print(trip.values())

# for key,value in trip.items():
#     print(key,":",value)
#
# trip.update({"car_modal":"Benz"})
# print(trip)


# trip.pop("status")
# print(trip)

print(trip["drop"][2])

for location in trip["drop"]:
    print(location)

