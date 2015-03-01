class Plot(object):
	def __init__(self,size=(80,30)):
		super(Plot, self).__init__()
		self.size=size
		self.plot_list=[]
		self.__init_blank_plot_with_axis__(self.size)

	def __init_blank_plot_with_axis__(self,(X_range,Y_range)):
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
		self.plot_list=blank_plot_with_axis

	def rastering(self,points_object):
		"""
		rastering(self,points_object)

		Plots data co-ordinates from points_object on plot_list. """
		no_of_point=len(points_object.pt_list_x)

		if no_of_point==0:
			return plot_list

		# finding row number and column number form co-ordinates x,y and ploting it on plot_list
		for i in range(0,no_of_point):
			column=int(round(points_object.pt_list_x[i]-1+(self.size[0]+1)/2))
			row=int(round(-points_object.pt_list_y[i]-1+(self.size[1]+1)/2))
			self.plot_list[row*(self.size[0]+1)+column]='*'
	def __repr__(self):

		return "".join(self.plot_list)



class Points(object):
	"""class holding Points of 2 dimensional plot with autorange feature to adapt data according to the plot size"""
	def __init__(self, pt_list_x,pt_list_y):
		super(Points, self).__init__()
		self.pt_list_x = pt_list_x
		self.pt_list_y=pt_list_y

	def autorange_data(self,(X_range,Y_range)):
		"""
		autorange_data(X_range,Y_range)

		set  scaled x & y list so as to cover the entire plot(X_range,Y_range).
		"""
		no_of_point=len(self.pt_list_x)

		if no_of_point==0:
			return 
		# find absolute max from both x and y
		max_x=self.pt_list_x[0]
		max_y=self.pt_list_y[0]
		for i in range(1,no_of_point):
			if max_x<abs(self.pt_list_x[i]):
				max_x=abs(self.pt_list_x[i])
			if max_y<abs(self.pt_list_y[i]):
				max_y=abs(self.pt_list_y[i])

		# if no data along x direction then no scaling in x direction
		if max_x==0:
			max_x=(X_range-1)/2
		# if no data along y direction then no scaling in y direction
		if max_y==0:
			max_y=(Y_range-1)/2

		# finding single scaling_factor to maintain aspect ratio of data
		scaling_factor = 1.0/max([float(max_x)/((X_range-1)/2),float(max_y)/((Y_range-1)/2)])

		#scaling the data
		x_scaled=[]
		y_scaled=[]
		for i in range(0,no_of_point):
			x_scaled.append(round(self.pt_list_x[i]*scaling_factor))
			y_scaled.append(round(self.pt_list_y[i]*scaling_factor))
		self.pt_list_x=x_scaled
		self.pt_list_y=y_scaled
		return 
def plot(x,y,X_range=80,Y_range=30):
	"""
	plot(x,y,X_range=80,Y_range=30) -> noneType

	Given two lists/tuples of floating point values x and y "plot(x, y)" produces a text-based scatter plot.
	That is, for each pair,	(x_i, y_i), it writes a "*" to the screen.

	screen has a default size of 30 rows by 80 columns (like your terminal window).
	This size is settable by the user to change the dimensions if needed but the default is 30x80. 
	The origin of plot is at (X_range+1)/2 and (Y_range+1)/2

	The range of the plot is automatically set to cover the entire plot.

	When text_plot.py is run as "python text_plot.py" it will show a sine plot (from 0 to 2*pi) as output.

	e.g.
	plot([2],[1],5,4)
	  | *
	--+--
	  |
	  |
	"""

	#creating instance of plot class with required size
	plot=Plot((X_range,Y_range))

	#creating instance of points initiated with points

	points=Points(x,y)

	#scaling the data acording to screen size
	points.autorange_data(plot.size)

	plot.rastering(points)

	print plot
	# # rastering the scaled data on plot_list
	# plot_list=rastering(x_scaled,y_scaled,X_range,Y_range,Blank_plot_with_axis)

	# #converting and printing plot form list "plot_list"
	# print "".join(plot_list)
# plot([0.5,-3.5,0,-3.8,2.1],[5,-1,0,+2.5,-1.9],50,55)