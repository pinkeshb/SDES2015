import math
import time
def init_blank_plot_with_axis(X_range,Y_range):
	if X_range%2 == 1:
		blank_line=[' ']*(X_range/2)+['|']+[' ']*(X_range/2)+['\n']
		blank_line_middle=['-']*(X_range/2)+['+']+['-']*(X_range/2)+['\n']
	else:
		blank_line=[' ']*((X_range-1)/2)+['|']+[' ']*(X_range/2)+['\n']
		blank_line_middle=['-']*((X_range-1)/2)+['+']+['-']*(X_range/2)+['\n']	
	if Y_range%2 == 1:
		blank_plot_with_axis=blank_line*(Y_range/2)+blank_line_middle+blank_line*(Y_range/2)
	else:
		blank_plot_with_axis=blank_line*((Y_range-1)/2)+blank_line_middle+blank_line*(Y_range/2)
	return blank_plot_with_axis

def autorange_data(x,y,X_range,Y_range):
	no_of_point=len(x)
	if no_of_point==0:
		return ([],[])
	max_x=x[0]
	max_y=y[0]
	for i in range(0,no_of_point):
		if max_x<abs(x[i]):
			max_x=abs(x[i])
		if max_y<abs(y[i]):
			max_y=abs(y[i])
	if max_x==0:
		max_x=(X_range-1)/2
	if max_y==0:
		max_y=(Y_range-1)/2
	scaling_factor = 1.0/max([float(max_x)/((X_range-1)/2),float(max_y)/((Y_range-1)/2)])
	x_scaled=[]
	y_scaled=[]
	for i in range(0,no_of_point):
		x_scaled.append(round(x[i]*scaling_factor))
		y_scaled.append(round(y[i]*scaling_factor))
	return (x_scaled,y_scaled)

def rastering(x_scaled,y_scaled,X_range,Y_range,plot_list):
	no_of_point=len(x_scaled)
	if no_of_point==0:
		return plot_list
	for i in range(0,no_of_point):
		column=int(round(x_scaled[i]-1+(X_range+1)/2))
		row=int(round(-y_scaled[i]-1+(Y_range+1)/2))
		plot_list[row*(X_range+1)+column]='*'
	return plot_list

def plot(x,y,X_range=80,Y_range=30):
	Blank_plot_with_axis=init_blank_plot_with_axis(X_range,Y_range)
	(x_scaled,y_scaled)=autorange_data(x,y,X_range,Y_range)
	plot_list=rastering(x_scaled,y_scaled,X_range,Y_range,Blank_plot_with_axis)
	print "".join(plot_list)

def print_sine():
	x=[0]
	y=[0]
	for i in range(1,31):
		x.append(x[i-1]+2*math.pi/30)
		y.append(math.sin(x[i]))
	plot(x,y,121,31)

if __name__=="__main__":
	print_sine()