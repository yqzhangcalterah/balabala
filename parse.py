#!/tools/bootstrap/gentoo/usr/bin python3 

import re
import os
import argparse
import matplotlib.pyplot as plt
import numpy as np



# get DUT.f
def get_dut(path,dif_ang) :
    for index in range(len(path)):
        dut_i = open(path[index])
        fileList = dut_i.readlines()
        list = []
        for fileLine in fileList :
            mo = re.search('DoAEstimator\((\d+)\):.*\[\s*(.*),\s*(.*)\]\: .* = (.*);', fileLine)
            if mo :
                ID, k, p, rem = mo.groups()
                rem = rem.split(";")
                cnt=0
                for pw, b in eval('[%s]' % rem[0]) :
                    tmp = -60.0+ float(b)/3
                    list.append(tmp)
            else :
                err = 'An error occurs when parse results: ' + fileLine
        dut_i.close()
        #f = open('out_result.dat','w+')
        #f.write(str(list))
        #f.close()
        #  matplotlib.axes.Axes.hist() 方法的接口
        d = np.array(list, dtype=float)
        n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                                    alpha=0.7, rwidth=0.85)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Angle Value (deg)')
        plt.ylabel('Counts')
        plt.title('Hist of angle')
        #plt.text(23, 45, r'$\mu=15, b=3$')
        maxfreq = n.max()
        # 设置y轴的上限
        plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
        filename = 'dif_%sdeg.pdf' % dif_ang
        plt.savefig(filename)
        #plt.show()



if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description='Script to generate file list for FPGA project')
    parser.add_argument('infile', metavar='infile', type=str, nargs=1, help='input DUT file')
    parser.add_argument('dif_ang', metavar='dif_ang', type=float,help='dif_b_indx')
    args = parser.parse_args()
    get_dut(args.infile,args.dif_ang);
    
