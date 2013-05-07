def pointPotential(x,y,q,posx,posy):
	"""Takes point(s), the size and direction of charge, and the position of that charge to return the electric potential due to that charge."""
	k = (8.9875551787)*(10**9)
	Vxy = (k*q)/(((x-posx)**2)+((y-posy)**2))**(1/2.)
	return Vxy

def dipolePotential(x,y,q,d):
	"""Take point(s), the size and direction of charge, and the position of that charge to return the dipole potential due to that charge."""
	Vxy = pointPotential(x,y,q,-d,0.)-pointPotential(x,y,q,d,0.)
	return Vxy

def pointField(x,y,q,Xq,Yq):
	"""Takes as arguments the arrays (x,y), charge (q), and position (Xq, Yq), and returns the electric field components (Ex, Ey)."""
	Ex = (k*q*(x-Xq))/(((x-Xq)**2)+((y-Yq)**2)**(1/2))
	Ey = (k*q*(y-Yq))/(((x-Xq)**2)+((y-Yq)**2)**(1/2))
