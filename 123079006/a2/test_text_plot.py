import text_plot

def test_init_blank_plot_with_axis():
   assert text_plot.init_blank_plot_with_axis(80,30)==([' ']*39+['|']+[' ']*40+['\n'])*14  + (['-']*39+['+']+['-']*40+['\n']) +([' ']*39+['|']+[' ']*40+['\n'])*15,"init_blank_plot_with_axis(80,30) improper"
   assert text_plot.init_blank_plot_with_axis(121,31)==([' ']*60+['|']+[' ']*60+['\n'])*15  + (['-']*60+['+']+['-']*60+['\n']) +([' ']*60+['|']+[' ']*60+['\n'])*15,"init_blank_plot_with_axis(121,31) improper"

def test_autorange_data(x,y,X_range,Y_range):
   pass


def test_rastering():
   assert text_plot.rastering([],[],80,30,text_plot.init_blank_plot_with_axis(80,30)) == text_plot.init_blank_plot_with_axis(80,30),"rastering() failed no data plot"
   
   plotlist = text_plot.init_blank_plot_with_axis(80,30)
   plotlist[0]='*'
   assert text_plot.rastering([-39],[14],80,30,text_plot.init_blank_plot_with_axis(80,30)) == plotlist,"rastering() failed -39,14 plot"

   plotlist = text_plot.init_blank_plot_with_axis(80,30)
   plotlist[14*81+40-1]='*'
   assert text_plot.rastering([0],[0],80,30,text_plot.init_blank_plot_with_axis(80,30)) == plotlist,"rastering() failed origin plot"

   plotlist = text_plot.init_blank_plot_with_axis(11,11)
   plotlist[0*12+11-1]='*'
   assert text_plot.rastering([5],[5],11,11,text_plot.init_blank_plot_with_axis(11,11)) == plotlist,"rastering() failed non-origin plot"

   plotlist = text_plot.init_blank_plot_with_axis(11,11)
   plotlist[5*12+6-1]='*'
   plotlist[5*12+11-1]='*'
   assert text_plot.rastering([0,5],[0,0],11,11,text_plot.init_blank_plot_with_axis(11,11)) == plotlist,"rastering() failed multi-point plot"

   plotlist = text_plot.init_blank_plot_with_axis(11,11)
   plotlist[5*12+11-1]='*'
   assert text_plot.rastering([4.4999999999999999999999999999999999999999999999999999999999999999],[0],11,11,text_plot.init_blank_plot_with_axis(11,11)) == plotlist,"rastering() failed floating-point plot"

   plotlist = text_plot.init_blank_plot_with_axis(11,11)
   plotlist[5*12+6-1]='*'
   plotlist[5*12+10-1]='*'
   assert text_plot.rastering([0,4.3333333],[0,0],11,11,text_plot.init_blank_plot_with_axis(11,11)) == plotlist,"rastering() failed multi-floating-point plot"

def test_plot(x,y,X_range,Y_range):
   pass
   #test for default size and nothing to plot

#test for default size and rastering single point

#test for default size and rastering multiple points

#test for default size and rastering out of orfer points

#test for cahnge dim and all of the above if needed??

#test for autorange with single point(take other point as origin)

#test for autorange with multiple points

#




















#plot(x,y,X=80,Y=30) ---> "*"

def test_text_plot():
   test_init_blank_plot_with_axis()
   test_rastering()
   #test_autorange_data()
   #test_plot()
   print "Good JOB"

test_text_plot()

