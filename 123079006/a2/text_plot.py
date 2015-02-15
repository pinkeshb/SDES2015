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
	pass
def rastering(x_scaled,y_scaled,X_range,Y_range,plot_list):
	no_of_point=len(x_scaled)
	if no_of_point==0:
		return plot_list
	for i in range(0,no_of_point):
		column=int(round(x_scaled[i]-1+(X_range+1)/2))
		row=int(round(-y_scaled[i]-1+(Y_range+1)/2))
		plot_list[row*(X_range+1)+column]='*'
	return plot_list

def plot(x,y,X_range,Y_range):
	pass
