import sys, os, shelve
stops = {}
stops_name = {} #fetches name of stop
trips = {}
routes = {}
routes_name = {}
flag = 0
shelfFile = shelve.open('myData')
with open('stops.txt') as fin:
    for line in fin:
        if flag == 0:
        	flag = 1
        	continue
        my_list = line.split(",")
        stops[my_list[2]] = int(my_list[0])
        stops_name[int(my_list[0])] = my_list[2]

flag = 0
with open('trips.txt') as fin:
    for line in fin:
        if flag == 0:
        	flag = 1
        	continue
        my_list = line.split(",")
        trips[int(my_list[2])] = int(my_list[0])

flag = 0
with open('stop_times.txt') as fin:
    for line in fin:
        if flag == 0:
        	flag = 1
        	continue
        my_list = line.split(",")

        if trips[int(my_list[0])] not in routes:
        	routes[trips[int(my_list[0])]] = []
        if int(my_list[3]) not in routes[trips[int(my_list[0])]]:
        	routes[trips[int(my_list[0])]].append(int(my_list[3]))
flag = 0
with open('routes.txt') as fin:
    for line in fin:
        if flag == 0:
        	flag = 1
        	continue
        my_list = line.split(",")
        routes_name[int(my_list[3])] = my_list[1]
shelfFile['stops'] = stops;
shelfFile['routes'] = routes;
shelfFile['trips'] = trips;
shelfFile['stops_name'] = stops_name;
shelfFile['routes_name'] = routes_name;
shelfFile.close()
