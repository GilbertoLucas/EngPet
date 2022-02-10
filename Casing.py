from sympy import symbols, plot_implicit, Eq, Abs

class casingBuilder:
    def __init__(self):
        self.inner_diameter = None
        self.outer_diameter = None
        self.yeld_limit = None

    def set_inner_diameter(self,inner_diameter):
        self.inner_diameter = inner_diameter
        return self

    def set_outer_diameter(self,outer_diameter):
        self.outer_diameter = outer_diameter
        return self

    def set_yeld_limit(self,yeld_limit):
        self.yeld_limit = yeld_limit
        return self

    def get_inner_diameter(self):
        return self.inner_diameter 

    def get_outer_diameter(self):
        return self.outer_diameter 

    def get_yeld_limit(self):
        return self.yeld_limit 

def plot_colapse(casing,minimum_external_pressure,maximum_external_pressure,minimum_sigma_z,maximum_sigma_z):
    Ri = casing.inner_diameter/2
    Re = casing.outer_diameter/2
    y = casing.yeld_limit 
    Pe_min = minimum_external_pressure
    Pe_max = maximum_external_pressure
    Sz_min = minimum_sigma_z
    Sz_max = maximum_sigma_z

    Sz, Pe = symbols('Sz Pe')
    plot2 = plot_implicit(Eq((8*((-Pe)**2)*(Re**4))/(((Re**2)-(Ri**2))**2)+(4*Sz*(Re**2)*(-Pe))/((Re**2)-(Ri**2))+2*Sz**2, 2*(y**2)), 
                  (Sz, Sz_min, Sz_max), 
                  (Pe, Pe_min, Pe_max),
                  line_color='crimson',
                  label = 'colapse',
                  show=False)
    
    plot2.legend(True)
    plot2.show()

    return plot2

def plot_burst(casing,minimum_internal_pressure,maximum_internal_pressure,minimum_sigma_z,maximum_sigma_z):
    Ri = casing.inner_diameter/2
    Re = casing.outer_diameter/2
    y = casing.yeld_limit 
    Pi_min = minimum_internal_pressure
    Pi_max = maximum_internal_pressure
    Sz_min = minimum_sigma_z
    Sz_max = maximum_sigma_z
    
    Sz, Pi = symbols('Sz Pi')
    plot2 = plot_implicit(Eq( (2*(3*(Re**4)+(Ri**4))*(Pi**2))/(((Re**2)-(Ri**2))**2)  + (2*(-2*(Re**2)*(Ri**2)*Sz + 2*(Ri**4)*Sz)*(Pi))/(((Re**2)-(Ri**2))**2)  +  (2*((Re**4)*(Sz**2) - 2*(Re**2)*(Ri**2)*(Sz**2)+(Ri**4)*(Sz**2)))/(((Re**2)-(Ri**2))**2)  , 2*(y**2)), 
                  (Sz, Sz_min, Sz_max), 
                  (Pi, Pi_min, Pi_max),
                  line_color='blue',
                  label = 'burst',
                  show=False)


    plot2.show()

    return plot2

