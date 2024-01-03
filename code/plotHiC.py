###------ Packages that you need

#pip install fanc==0.9.27
#pip uninstall -y biopython
#pip install biopython==1.75

###------End


import fanc
import fanc.plotting as fancplot

def plotHiC(hic_file_path, name, region_start, region_end):
    fc = fancplot.SquareMatrixPlot(hic_file_path, flip=True, vmax=0.05)
    fc.plot('f{}:{}-{}'.format(name, region_start,region_end))
    fc.show()

    print("Diagram is done.")