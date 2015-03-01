class plot(object):
	def __init__(self,size=(80,30)):
		super(plot, self).__init__()
		self.size=size
		self.plot_list=__init_blank_plot_with_axis__(self.size)

	def __init_blank_plot_with_axis__(X_range,Y_range):
		"""
		init_blank_plot_with_axis(X_range,Y_range) -> List of string

		Returns List of string which, when joined using "".join() returns string for 
		blank plot with axis with from -(X_range-1)/2 to X_range/2 and -Y_range/2 to (Y_range-1)/2.
		e.g.
		init_blank_plot_with_axis(5,4)
		  | 
		--+--
		  |
		  |
		"""
		
		blank_line=[' ']*((X_range-1)/2)+['|']+[' ']*(X_range/2)+['\n'] #creates row_list = "         |           "
		blank_line_middle=['-']*((X_range-1)/2)+['+']+['-']*(X_range/2)+['\n']	# creates middle_row_list = "----------+---------"
		blank_plot_with_axis=blank_line*((Y_range-1)/2)+blank_line_middle+blank_line*(Y_range/2) # creates plot_list by stacking rows	   
		return blank_plot_with_axis

	def rastering(self,points_object):
		"""
		rastering(self,points_object)

		Plots data co-ordinates from points_object on plot_list. """
		no_of_point=len(x_scaled)

		if no_of_point==0:
			return plot_list

		# finding row number and column number form co-ordinates x,y and ploting it on plot_list
		for i in range(0,no_of_point):
			column=int(round(points_object.pt_list_x[i]-1+(X_range+1)/2))
			row=int(round(-points_object.pt_list_y[i]-1+(Y_range+1)/2))
			self.plot_list[row*(X_range+1)+column]='*'

