#!/bin/bash

foamListTimes -rm
blockMesh | tee log.blockMesh
checkMesh | tee log.checkMesh
pyFoamPlotRunner.py --with-courant pisoFoam
pyFoamRedoPlot.py --pickle-file Gnuplotting.analyzed/pickledPlots --picture-prefix=kEps1095_ 
postProcess -func CourantNo
foamToVTK
killall gnuplot_x11

