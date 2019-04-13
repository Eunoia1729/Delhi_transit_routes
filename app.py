from flask import Flask, render_template, request
import shelve
app = Flask(__name__)

@app.route('/send', methods = ['GET','POST'])

def send():
	
	shelfFile = shelve.open('myData')
	stops = shelfFile['stops']
	routes = shelfFile['routes']
	trips = shelfFile['trips']
	routes_name = shelfFile['routes_name']
	stops_name = shelfFile['stops_name']
    

	if request.method == 'POST':
		#tv_series = request.form['tv_series']
		source = request.form.get('source')
		destination = request.form.get('destination')
		src_id = stops[source]
		dest_id = stops[destination]
		hop0 = []
		hop1 = []
		
		for route_id, route_list in routes.items():
			if src_id in route_list and dest_id in route_list:
				hop0.append(str(routes_name[route_id]))
		if len(hop0) == 0:
			hop0.append(str('No 0-hop routes found ! '))
		

		for route_id, route_list in routes.items():
			if src_id in route_list and dest_id not in route_list:
				for inter_stop in route_list:
					if inter_stop == src_id:
						continue
					else:
						for route_id2, route_list2 in routes.items():
							if route_id == route_id2:
								continue
							elif dest_id in route_list2 and inter_stop in route_list2:
								hop1.append(str(routes_name[route_id])+" -> change at "+stops_name[inter_stop]+" -> "+str(routes_name[route_id2]))
		if len(hop1) == 0:
			hop1.append(str('No 1-hop routes found ! '))
		
		return render_template('results.html', source = source, destination = destination, hop0 = hop0, hop1 = hop1)


	stops1 = list(stops.keys())
	stops1.sort()
	return render_template('index.html', stops=stops1)
@app.route('/about')

def about():
	return render_template('about.html')

if __name__ == "__main__":
   app.run() 	