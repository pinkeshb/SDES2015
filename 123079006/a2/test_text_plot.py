import text_plot
import sys
import filecmp

def test_init_blank_plot_with_axis():
   assert text_plot.init_blank_plot_with_axis(80,30)==([' ']*39+['|']+[' ']*40+['\n'])*14  + (['-']*39+['+']+['-']*40+['\n']) +([' ']*39+['|']+[' ']*40+['\n'])*15,"init_blank_plot_with_axis(80,30) improper"
   assert text_plot.init_blank_plot_with_axis(80,31)==([' ']*39+['|']+[' ']*40+['\n'])*15  + (['-']*39+['+']+['-']*40+['\n']) +([' ']*39+['|']+[' ']*40+['\n'])*15,"init_blank_plot_with_axis(80,31) improper"
   assert text_plot.init_blank_plot_with_axis(81,30)==([' ']*40+['|']+[' ']*40+['\n'])*14  + (['-']*40+['+']+['-']*40+['\n']) +([' ']*40+['|']+[' ']*40+['\n'])*15,"init_blank_plot_with_axis(81,30) improper"
   assert text_plot.init_blank_plot_with_axis(121,31)==([' ']*60+['|']+[' ']*60+['\n'])*15  + (['-']*60+['+']+['-']*60+['\n']) +([' ']*60+['|']+[' ']*60+['\n'])*15,"init_blank_plot_with_axis(121,31) improper"

def test_autorange_data():
   assert text_plot.autorange_data([],[],80,30)==([],[]),"autorange without data"
   assert text_plot.autorange_data([0],[0],80,30)==([0],[0]),"autorange with (0,0)"
   assert text_plot.autorange_data([30],[10],80,30)==([39],[13]),"autorange with (30,10) data"
   assert text_plot.autorange_data([5],[5],11,11)==([5],[5]),"autorange wuth (5,5) data"
   assert text_plot.autorange_data([-10],[10],11,11)==([-5],[5]),"autorange with (10,10) data"
   assert text_plot.autorange_data([10.9],[-10.9],11,11)==([5],[-5]),"autorange with (10.9,10.9) data"
   assert text_plot.autorange_data([-4.5],[10],11,11)==([-2],[5]),"autorange with (4.5,10) data"
   assert text_plot.autorange_data([-10,0,-15.5],[10,0,-10.5],11,11)==([-3,0,-5],[3,0,-3]),"autorange with [-10,0,-15.5],[10,0,-10.5] data"
   assert text_plot.autorange_data([10],[-10],10,20)==([4],[-4]),"autorange with (10,-10) data"
   assert text_plot.autorange_data([1,0,4.3,5.4],[-1,0,8.5,3.1],10,20)==([1,0,3,4],[-1,0,6,2]),"autorange with [1,0,4.3,5.4],[-1,0,8.5,3.1] data"
   assert text_plot.autorange_data((100,4,2),[100,4,1],10,20)==([4,0,0],[4,0,0]),"autorange with [100,4,2],[100,4,1] data"
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

def test_plot():
   #test for default size and nothing to plot
   s=sys.stdout
   sys.stdout = open('testcase_output_of_plot.txt', 'w')
   text_plot.plot([0.5,-3.5,0,-3.8,2.1],[5,-1,0,+2.5,-1.9],50,55) 
   sys.stdout=s
   assert filecmp.cmp('expected_output_of_plot.txt','testcase_output_of_plot.txt'),"plot not working as expected"



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
   test_autorange_data()
   test_plot()
   print "Good JOB"

test_text_plot()

