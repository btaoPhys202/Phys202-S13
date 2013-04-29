

def pointPotential(x,y,q,posx,posy):
	"""Takes point(s), the size and direction of charge, and the position of that charge to return the electric potential due to that charge."""
	k = (8.987551787)*(10**9)
	Vxy = (k*q)/(((x-posx)**2)+((y-posy)**2))**(1/2.)
	return Vxy

def dipolePotential(x,y,q,d):
	"""Takes point(s), the size and direction of charge, and the position of that charge to return the dipole potential due to that charge."""
	k = (8.987551787)*(10**9)
	Vxy = (k*q)/(((x+d)**2)+((y-0.)**2))**(1/2.)-((k*q)/(((x-d)**2)+((y-0.)**2))**(1/2.))
	return Vxy

