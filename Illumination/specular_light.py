import numpy as np 

#specular light I = k_d*I_0(R*V)^N
# I = specular_light(P, N, color, cam_pos, ks , n, light_positions, light_intensities)
def specular_light(P,N,color,cam_pos, k_s, n, l_p,l_i):
	N_u = N/np.absolute(N)
	#calculate R vector
	L = l_p - P
	L_u = L/np.absolute(L)
	R = 2*Nu*np.dot(N,L_u)-L_u
	V = P - cam_pos
	V_u = V/np.absolute(V)
	#R*V
	sl_coeff = np.dot(R,V_u)
	specular_light_val = (sl_coeff*l_i*k_s)^n
	return specular_light_val
	