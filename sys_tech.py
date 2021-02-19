print('hello\n')
fc = 79e9
T_r = 50e-6
FFT_v = 256
L = 256
c = 299792458.0
varray = 1
time_on_velocity = L*T_r
bin_on_velocity = 1/(varray*T_r *FFT_v )
v_factor = c/(2*fc)
v_resolution = 1/time_on_velocity * v_factor
v_accuracy = bin_on_velocity * v_factor/2
v_max = 1/(varray*T_r) * v_factor
print('m/s')
print('v_resolution= ',v_resolution)
print('v_accuracy= ',v_accuracy)
print('v_max=',v_max)
print('km/h')
print('v_resolution= ',v_resolution*3.6)
print('v_accuracy= ',v_accuracy*3.6)
print('v_max=',v_max*3.6)

#below is for giving spec
#v_max_need = 600/3.6
#T_r_need = v_factor/v_max_need
#print('max T_r= ',T_r_need)
#v_resolution_need = 0.2/3.6
#L_need = v_factor/v_resolution_need/T_r_need
#print('minmum L= ',L_need)
#v_accuracy_need = 0.1/3.6
#FFT_v_need = v_factor/(v_accuracy_need*2)/T_r_need
#print('minmum FFT_v= ',FFT_v_need)


fs = 40e6
B = 1200e6
T_u = 16e-6
FFT_r = 512
r_resolution = c/(2*B)
r_factor = (fs*T_u)/FFT_r
r_resolution = r_factor*r_resolution
r_accuracy = r_resolution/2
r_max = (fs*T_u)*c/(4*B)
print('r_resolution=',r_resolution)
print('r_accuracy=',r_accuracy)
print('r_max=',r_max)

#below is for giving spec
#r_resolution_need = 0.4
#B_need = c/r_resolution_need/2
#print('minmum B=',B_need)

#r_max_need = 250
#fs_need = r_max_need*4*B_need /(c*T_u)
#print('minmum fs=',fs_need)
#print('FFT_r need more than or equal to fs*Tu')

#below for translate R,V to index

V = -30.58
R = 16
v_idx = V/v_resolution
p_k_coe = FFT_r/FFT_v/T_r/fs
r_idx = R/r_resolution + v_idx*p_k_coe
if v_idx < 0:
    v_idx = v_idx + 256
print(r_idx)
print(v_idx)







