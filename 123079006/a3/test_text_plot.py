import unittest	
import text_plot
class Test_Plot_class(unittest.TestCase):
	def setUp(self):
		print "In setup"
	def tearDown(self):
		print "In teardown"
	def test_init_blank_plot_with_axis(self):
		self.assertEqual(text_plot.Plot().plot_list,([' ']*39+['|']+[' ']*40+['\n'])*14  + (['-']*39+['+']+['-']*40+['\n']) +([' ']*39+['|']+[' ']*40+['\n'])*15)
		self.assertEqual(text_plot.Plot((80,31)).plot_list,([' ']*39+['|']+[' ']*40+['\n'])*15  + (['-']*39+['+']+['-']*40+['\n']) +([' ']*39+['|']+[' ']*40+['\n'])*15)
		self.assertEqual(text_plot.Plot((121,31)).plot_list,([' ']*60+['|']+[' ']*60+['\n'])*15  + (['-']*60+['+']+['-']*60+['\n']) +([' ']*60+['|']+[' ']*60+['\n'])*15)
		self.assertEqual(text_plot.Plot((81,30)).plot_list,([' ']*40+['|']+[' ']*40+['\n'])*14  + (['-']*40+['+']+['-']*40+['\n']) +([' ']*40+['|']+[' ']*40+['\n'])*15)
	def test_rastering(self):
		# output_list=text_plot.rastering([],[],80,30,text_plot.init_blank_plot_with_axis(80,30))
		# self.assertEqual(output_list,text_plot.init_blank_plot_with_axis(80,30),"rastering() failed no data plot"      	output_list = text_plot.Plot((80,30))
		# plotlist = text_plot.Plot((80,30)).plot_list
		# plotlist[0]='*'
		# self/.assertEqual(output_list,plotlist)

		output_list=text_plot.Plot((80,30)).rastering(text_plot.Points([0],[0])).plot_list
		plotlist = text_plot.Plot((80,30)).init_blank_plot_with_axis(80,30).plot_list
		plotlist[14*81+40-1]='*'
		self.assertEqual(output_list,plotlist)
 
       #  output_list=text_plot.rastering([5],[5],11,11,text_plot.init_blank_plot_with_axis(11,11)) 
       #  plotlist = text_plot.init_blank_plot_with_axis(11,11)
       #  plotlist[0*12+11-1]='*'
       #  self.assertEqual(output_list,plotlist)

       #  output_list=text_plot.rastering([0,5],[0,0],11,11,text_plot.init_blank_plot_with_axis(11,11)) 
       #  plotlist = text_plot.init_blank_plot_with_axis(11,11)
       #  plotlist[5*12+6-1]='*'
       #  plotlist[5*12+11-1]='*'
       #  self.assertEqual(output_list,plotlist)

       #  output_list=text_plot.rastering([4.4999999999999999999999999999999999999999999999999999999999999999],[0],11,11,text_plot.init_blank_plot_with_axis(11,11))
       #  plotlist = text_plot.init_blank_plot_with_axis(11,11)
       #  plotlist[5*12+11-1]='*'
      	# self.assertEqual(output_list,plotlist)

      	# output_list=text_plot.rastering([0,4.3333333],[0,0],11,11,text_plot.init_blank_plot_with_axis(11,11))
      	# plotlist = text_plot.init_blank_plot_with_axis(11,11)
      	# plotlist[5*12+6-1]='*'
      	# plotlist[5*12+10-1]='*'
      	# self.assertEqual(output_list,plotlist)

class Test_Points_class(unittest.TestCase):
	pass
class Test_plot_function(unittest.TestCase):
	pass
unittest.main()