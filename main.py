from Casing import *

casing1 = (casingBuilder()
           .set_inner_diameter(4.578*2)
           .set_outer_diameter(5.375*2)
           .set_yeld_limit(110000.0))


plt1 = plot_colapse(casing1,-20000,20000,-150000,150000)
plt2 = plot_burst(casing1,-20000,20000,-150000,150000)

plt1.append(plt2[0])
plt1.show()
