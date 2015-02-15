import test_plot

def test_init_blank_plot_with_axis():
	assert "".join(init_blank_plot_with_axis(80,30))=="""                                       |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
   ---------------------------------------|----------------------------------------
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        
                                          |                                        ""","init_blank_plot_with_axis(80,30) improper"

   assert "".join(init_blank_plot_with_axis(121,31))=="""                                                            |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
   ------------------------------------------------------------+------------------------------------------------------------
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            
                                                               |                                                            ""","init_blank_plot_with_axis(121,31) improper"

def test_autorange_data(x,y,X_range,Y_range):
   pass


def test_ploting():
   assert ploting([],[],init_blank_plot_with_axis(80,30)) == init_blank_plot_with_axis(80,30),"ploting() failed no data plot"
 
   plotlist = init_blank_plot_with_axis(80,30)
   plotlist[14*81+40-1]='*'
   assert ploting([0],[0],init_blank_plot_with_axis(80,30)) == plotlist,"ploting() failed origin plot"

   plotlist = init_blank_plot_with_axis(11,11)
   plotlist[0*12+11-1]='*'
   assert ploting([5],[5],init_blank_plot_with_axis(11,11)) == plotlist,"ploting() failed non-origin plot"

   plotlist = init_blank_plot_with_axis(11,11)
   plotlist[5*12+6-1]='*'
   plotlist[5*12+11-1]='*'
   assert ploting([0,5],[0,0],init_blank_plot_with_axis(11,11)) == plotlist,"ploting() failed multi-point plot"



def test_plot(x,y,X_range,Y_range):
   pass
   #test for default size and nothing to plot

#test for default size and ploting single point

#test for default size and ploting multiple points

#test for default size and ploting out of orfer points

#test for cahnge dim and all of the above if needed??

#test for autorange with single point(take other point as origin)

#test for autorange with multiple points

#




















#plot(x,y,X=80,Y=30) ---> "*"

def test_text_plot():
   test_init_blank_plot_with_axis()
   test_ploting()
   #test_autorange_data()
   #test_plot()

	

