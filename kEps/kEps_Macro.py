# trace generated using paraview version 5.6.3
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

l = ["kEps_config1", "kEps_config2", "kEps_config3", "kEps_config4"] 
for i in l:
# create a new 'Legacy VTK Reader'
    kEps_config1_ = LegacyVTKReader(FileNames=['/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_0.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_10000.vtk'])

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1058, 483]

    # show data in view
    kEps_config1_Display = Show(kEps_config1_, renderView1)

    # trace defaults for the display properties.
    kEps_config1_Display.Representation = 'Surface'
    kEps_config1_Display.ColorArrayName = [None, '']
    kEps_config1_Display.OSPRayScaleArray = 'U'
    kEps_config1_Display.OSPRayScaleFunction = 'PiecewiseFunction'
    kEps_config1_Display.SelectOrientationVectors = 'None'
    kEps_config1_Display.ScaleFactor = 0.06999999880790711
    kEps_config1_Display.SelectScaleArray = 'None'
    kEps_config1_Display.GlyphType = 'Arrow'
    kEps_config1_Display.GlyphTableIndexArray = 'None'
    kEps_config1_Display.GaussianRadius = 0.0034999999403953555
    kEps_config1_Display.SetScaleArray = ['POINTS', 'U']
    kEps_config1_Display.ScaleTransferFunction = 'PiecewiseFunction'
    kEps_config1_Display.OpacityArray = ['POINTS', 'U']
    kEps_config1_Display.OpacityTransferFunction = 'PiecewiseFunction'
    kEps_config1_Display.DataAxesGrid = 'GridAxesRepresentation'
    kEps_config1_Display.SelectionCellLabelFontFile = ''
    kEps_config1_Display.SelectionPointLabelFontFile = ''
    kEps_config1_Display.PolarAxes = 'PolarAxesRepresentation'
    kEps_config1_Display.ScalarOpacityUnitDistance = 0.02094899412691451
    #kEps_config1_Display.SelectInputVectors = ['POINTS', 'U']
    #kEps_config1_Display.WriteLog = ''

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    kEps_config1_Display.DataAxesGrid.XTitleFontFile = ''
    kEps_config1_Display.DataAxesGrid.YTitleFontFile = ''
    kEps_config1_Display.DataAxesGrid.ZTitleFontFile = ''
    kEps_config1_Display.DataAxesGrid.XLabelFontFile = ''
    kEps_config1_Display.DataAxesGrid.YLabelFontFile = ''
    kEps_config1_Display.DataAxesGrid.ZLabelFontFile = ''

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    kEps_config1_Display.PolarAxes.PolarAxisTitleFontFile = ''
    kEps_config1_Display.PolarAxes.PolarAxisLabelFontFile = ''
    kEps_config1_Display.PolarAxes.LastRadialAxisTextFontFile = ''
    kEps_config1_Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

    # reset view to fit data
    renderView1.ResetCamera()

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(kEps_config1_Display, ('POINTS', 'U', 'Magnitude'))

    # rescale color and/or opacity maps used to include current data range
    kEps_config1_Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    kEps_config1_Display.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'U'
    uLUT = GetColorTransferFunction('U')

    # get opacity transfer function/opacity map for 'U'
    uPWF = GetOpacityTransferFunction('U')

    # set scalar coloring
    ColorBy(kEps_config1_Display, ('POINTS', 'U', 'X'))

    # rescale color and/or opacity maps used to exactly fit the current data range
    kEps_config1_Display.RescaleTransferFunctionToDataRange(False, False)

    # Update a scalar bar component title.
    UpdateScalarBarsComponentTitle(uLUT, kEps_config1_Display)

    animationScene1.GoToLast()

    # create a new 'Plot Over Line'
    plotOverLine1 = PlotOverLine(Input=kEps_config1_,
        Source='High Resolution Line Source')

    # init the 'High Resolution Line Source' selected for 'Source'
    plotOverLine1.Source.Point1 = [0.0, -0.005200000014156103, -0.004999999888241291]
    plotOverLine1.Source.Point2 = [0.699999988079071, 0.005200000014156103, 0.004999999888241291]

    # Properties modified on plotOverLine1.Source
    plotOverLine1.Source.Point1 = [0.190848, 0.0, 0.0]
    plotOverLine1.Source.Point2 = [0.190848, 0.0052, 0.0]

    # show data in view
    plotOverLine1Display = Show(plotOverLine1, renderView1)

    # trace defaults for the display properties.
    plotOverLine1Display.Representation = 'Surface'
    plotOverLine1Display.ColorArrayName = ['POINTS', 'U']
    plotOverLine1Display.LookupTable = uLUT
    plotOverLine1Display.OSPRayScaleArray = 'Co'
    plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    plotOverLine1Display.SelectOrientationVectors = 'Co'
    plotOverLine1Display.ScaleFactor = 0.0005200000014156103
    plotOverLine1Display.SelectScaleArray = 'Co'
    plotOverLine1Display.GlyphType = 'Arrow'
    plotOverLine1Display.GlyphTableIndexArray = 'Co'
    plotOverLine1Display.GaussianRadius = 2.6000000070780518e-05
    plotOverLine1Display.SetScaleArray = ['POINTS', 'Co']
    plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
    plotOverLine1Display.OpacityArray = ['POINTS', 'Co']
    plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
    plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
    plotOverLine1Display.SelectionCellLabelFontFile = ''
    plotOverLine1Display.SelectionPointLabelFontFile = ''
    plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
    #plotOverLine1Display.SelectInputVectors = ['POINTS', 'U']
    #plotOverLine1Display.WriteLog = ''

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    plotOverLine1Display.DataAxesGrid.XTitleFontFile = ''
    plotOverLine1Display.DataAxesGrid.YTitleFontFile = ''
    plotOverLine1Display.DataAxesGrid.ZTitleFontFile = ''
    plotOverLine1Display.DataAxesGrid.XLabelFontFile = ''
    plotOverLine1Display.DataAxesGrid.YLabelFontFile = ''
    plotOverLine1Display.DataAxesGrid.ZLabelFontFile = ''

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    plotOverLine1Display.PolarAxes.PolarAxisTitleFontFile = ''
    plotOverLine1Display.PolarAxes.PolarAxisLabelFontFile = ''
    plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

    # Create a new 'Line Chart View'
    lineChartView1 = CreateView('XYChartView')
    lineChartView1.ViewSize = [524, 483]
    lineChartView1.ChartTitleFontFile = ''
    lineChartView1.LeftAxisTitleFontFile = ''
    lineChartView1.LeftAxisRangeMaximum = 6.66
    lineChartView1.LeftAxisLabelFontFile = ''
    lineChartView1.BottomAxisTitleFontFile = ''
    lineChartView1.BottomAxisRangeMaximum = 6.66
    lineChartView1.BottomAxisLabelFontFile = ''
    lineChartView1.RightAxisRangeMaximum = 6.66
    lineChartView1.RightAxisLabelFontFile = ''
    lineChartView1.TopAxisTitleFontFile = ''
    lineChartView1.TopAxisRangeMaximum = 6.66
    lineChartView1.TopAxisLabelFontFile = ''

    # get layout
    layout1 = GetLayout()

    # place view in the layout
    layout1.AssignView(2, lineChartView1)

    # show data in view
    plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)

    # trace defaults for the display properties.
    plotOverLine1Display_1.CompositeDataSetIndex = [0]
    plotOverLine1Display_1.UseIndexForXAxis = 0
    plotOverLine1Display_1.XArrayName = 'arc_length'
    plotOverLine1Display_1.SeriesVisibility = ['cellID', 'Co', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']
    plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'cellID', 'cellID', 'Co', 'Co', 'epsilon', 'epsilon', 'k', 'k', 'nut', 'nut', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'cellID', '0.89', '0.1', '0.11', 'Co', '0.22', '0.49', '0.72', 'epsilon', '0.3', '0.69', '0.29', 'k', '0.6', '0.31', '0.64', 'nut', '1', '0.5', '0', 'p', '0.65', '0.34', '0.16', 'U_X', '0', '0', '0', 'U_Y', '0.89', '0.1', '0.11', 'U_Z', '0.22', '0.49', '0.72', 'U_Magnitude', '0.3', '0.69', '0.29', 'vtkValidPointMask', '0.6', '0.31', '0.64', 'Points_X', '1', '0.5', '0', 'Points_Y', '0.65', '0.34', '0.16', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.89', '0.1', '0.11']
    plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'cellID', '0', 'Co', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine1Display_1.SeriesLabelPrefix = ''
    plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'cellID', '1', 'Co', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'cellID', '2', 'Co', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'cellID', '0', 'Co', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

    # update the view to ensure updated data information
    renderView1.Update()

    # update the view to ensure updated data information
    lineChartView1.Update()

    # Rescale transfer function
    uLUT.RescaleTransferFunction(-0.313605755568, 2.12118005753)

    # Rescale transfer function
    uPWF.RescaleTransferFunction(-0.313605755568, 2.12118005753)

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.XArrayName = 'U_X'

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['cellID', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']
    plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'cellID', '0.889998', '0.100008', '0.110002', 'Co', '0.220005', '0.489998', '0.719997', 'epsilon', '0.300008', '0.689998', '0.289998', 'k', '0.6', '0.310002', '0.639994', 'nut', '1', '0.500008', '0', 'p', '0.650004', '0.340002', '0.160006', 'U_X', '0', '0', '0', 'U_Y', '0.889998', '0.100008', '0.110002', 'U_Z', '0.220005', '0.489998', '0.719997', 'U_Magnitude', '0.300008', '0.689998', '0.289998', 'vtkValidPointMask', '0.6', '0.310002', '0.639994', 'Points_X', '1', '0.500008', '0', 'Points_Y', '0.650004', '0.340002', '0.160006', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.889998', '0.100008', '0.110002']
    plotOverLine1Display_1.SeriesPlotCorner = ['Co', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'cellID', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']
    plotOverLine1Display_1.SeriesLineStyle = ['Co', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'cellID', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'vtkValidPointMask', '1']
    plotOverLine1Display_1.SeriesLineThickness = ['Co', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'cellID', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'vtkValidPointMask', '2']
    plotOverLine1Display_1.SeriesMarkerStyle = ['Co', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'cellID', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['cellID', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'cellID', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'k', 'nut', 'p']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'nut', 'p']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'p']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['arc_length']

    # set active source
    SetActiveSource(kEps_config1_)

    # create a new 'Plot Over Line'
    plotOverLine2 = PlotOverLine(Input=kEps_config1_,
        Source='High Resolution Line Source')

    # init the 'High Resolution Line Source' selected for 'Source'
    plotOverLine2.Source.Point1 = [0.0, -0.005200000014156103, -0.004999999888241291]
    plotOverLine2.Source.Point2 = [0.699999988079071, 0.005200000014156103, 0.004999999888241291]

    # Properties modified on plotOverLine2.Source
    plotOverLine2.Source.Point1 = [0.236608, -0.0052, 0.0]
    plotOverLine2.Source.Point2 = [0.236608, 0.0052, 0.0]

    # show data in view
    plotOverLine2Display = Show(plotOverLine2, lineChartView1)

    # trace defaults for the display properties.
    plotOverLine2Display.CompositeDataSetIndex = [0]
    plotOverLine2Display.UseIndexForXAxis = 0
    plotOverLine2Display.XArrayName = 'arc_length'
    plotOverLine2Display.SeriesVisibility = ['cellID', 'Co', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']
    plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'cellID', 'cellID', 'Co', 'Co', 'epsilon', 'epsilon', 'k', 'k', 'nut', 'nut', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'cellID', '0.89', '0.1', '0.11', 'Co', '0.22', '0.49', '0.72', 'epsilon', '0.3', '0.69', '0.29', 'k', '0.6', '0.31', '0.64', 'nut', '1', '0.5', '0', 'p', '0.65', '0.34', '0.16', 'U_X', '0', '0', '0', 'U_Y', '0.89', '0.1', '0.11', 'U_Z', '0.22', '0.49', '0.72', 'U_Magnitude', '0.3', '0.69', '0.29', 'vtkValidPointMask', '0.6', '0.31', '0.64', 'Points_X', '1', '0.5', '0', 'Points_Y', '0.65', '0.34', '0.16', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.89', '0.1', '0.11']
    plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'cellID', '0', 'Co', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine2Display.SeriesLabelPrefix = ''
    plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'cellID', '1', 'Co', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'cellID', '2', 'Co', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'cellID', '0', 'Co', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

    # update the view to ensure updated data information
    lineChartView1.Update()

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.XArrayName = 'U_X'

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['cellID', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']
    plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'cellID', '0.889998', '0.100008', '0.110002', 'Co', '0.220005', '0.489998', '0.719997', 'epsilon', '0.300008', '0.689998', '0.289998', 'k', '0.6', '0.310002', '0.639994', 'nut', '1', '0.500008', '0', 'p', '0.650004', '0.340002', '0.160006', 'U_X', '0', '0', '0', 'U_Y', '0.889998', '0.100008', '0.110002', 'U_Z', '0.220005', '0.489998', '0.719997', 'U_Magnitude', '0.300008', '0.689998', '0.289998', 'vtkValidPointMask', '0.6', '0.310002', '0.639994', 'Points_X', '1', '0.500008', '0', 'Points_Y', '0.650004', '0.340002', '0.160006', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.889998', '0.100008', '0.110002']
    plotOverLine2Display.SeriesPlotCorner = ['Co', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'cellID', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']
    plotOverLine2Display.SeriesLineStyle = ['Co', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'cellID', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'vtkValidPointMask', '1']
    plotOverLine2Display.SeriesLineThickness = ['Co', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'cellID', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'vtkValidPointMask', '2']
    plotOverLine2Display.SeriesMarkerStyle = ['Co', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'cellID', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['cellID', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['arc_length', 'cellID', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['arc_length', 'cellID', 'epsilon', 'k', 'nut']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['arc_length', 'cellID', 'epsilon', 'k']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['arc_length', 'cellID', 'epsilon']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['arc_length', 'cellID']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['arc_length']

    # set active source
    SetActiveSource(kEps_config1_)

    # create a new 'Plot Over Line'
    plotOverLine3 = PlotOverLine(Input=kEps_config1_,
        Source='High Resolution Line Source')

    # init the 'High Resolution Line Source' selected for 'Source'
    plotOverLine3.Source.Point1 = [0.0, -0.005200000014156103, -0.004999999888241291]
    plotOverLine3.Source.Point2 = [0.699999988079071, 0.005200000014156103, 0.004999999888241291]

    # Properties modified on plotOverLine3.Source
    plotOverLine3.Source.Point1 = [0.29908, -0.0052, 0.0]
    plotOverLine3.Source.Point2 = [0.29908, 0.0052, 0.0]

    # show data in view
    plotOverLine3Display = Show(plotOverLine3, lineChartView1)

    # trace defaults for the display properties.
    plotOverLine3Display.CompositeDataSetIndex = [0]
    plotOverLine3Display.UseIndexForXAxis = 0
    plotOverLine3Display.XArrayName = 'arc_length'
    plotOverLine3Display.SeriesVisibility = ['cellID', 'Co', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']
    plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'cellID', 'cellID', 'Co', 'Co', 'epsilon', 'epsilon', 'k', 'k', 'nut', 'nut', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'cellID', '0.89', '0.1', '0.11', 'Co', '0.22', '0.49', '0.72', 'epsilon', '0.3', '0.69', '0.29', 'k', '0.6', '0.31', '0.64', 'nut', '1', '0.5', '0', 'p', '0.65', '0.34', '0.16', 'U_X', '0', '0', '0', 'U_Y', '0.89', '0.1', '0.11', 'U_Z', '0.22', '0.49', '0.72', 'U_Magnitude', '0.3', '0.69', '0.29', 'vtkValidPointMask', '0.6', '0.31', '0.64', 'Points_X', '1', '0.5', '0', 'Points_Y', '0.65', '0.34', '0.16', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.89', '0.1', '0.11']
    plotOverLine3Display.SeriesPlotCorner = ['arc_length', '0', 'cellID', '0', 'Co', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine3Display.SeriesLabelPrefix = ''
    plotOverLine3Display.SeriesLineStyle = ['arc_length', '1', 'cellID', '1', 'Co', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine3Display.SeriesLineThickness = ['arc_length', '2', 'cellID', '2', 'Co', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine3Display.SeriesMarkerStyle = ['arc_length', '0', 'cellID', '0', 'Co', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

    # update the view to ensure updated data information
    lineChartView1.Update()

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.XArrayName = 'U_X'

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['cellID', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']
    plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'cellID', '0.889998', '0.100008', '0.110002', 'Co', '0.220005', '0.489998', '0.719997', 'epsilon', '0.300008', '0.689998', '0.289998', 'k', '0.6', '0.310002', '0.639994', 'nut', '1', '0.500008', '0', 'p', '0.650004', '0.340002', '0.160006', 'U_X', '0', '0', '0', 'U_Y', '0.889998', '0.100008', '0.110002', 'U_Z', '0.220005', '0.489998', '0.719997', 'U_Magnitude', '0.300008', '0.689998', '0.289998', 'vtkValidPointMask', '0.6', '0.310002', '0.639994', 'Points_X', '1', '0.500008', '0', 'Points_Y', '0.650004', '0.340002', '0.160006', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.889998', '0.100008', '0.110002']
    plotOverLine3Display.SeriesPlotCorner = ['Co', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'cellID', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']
    plotOverLine3Display.SeriesLineStyle = ['Co', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'cellID', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'vtkValidPointMask', '1']
    plotOverLine3Display.SeriesLineThickness = ['Co', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'cellID', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'vtkValidPointMask', '2']
    plotOverLine3Display.SeriesMarkerStyle = ['Co', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'cellID', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['cellID', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['arc_length', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['arc_length', 'k', 'nut', 'p']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['arc_length', 'nut', 'p']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['arc_length', 'p']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['arc_length']

    # set active source
    SetActiveSource(kEps_config1_)

    # create a new 'Plot Over Line'
    plotOverLine4 = PlotOverLine(Input=kEps_config1_,
        Source='High Resolution Line Source')

    # init the 'High Resolution Line Source' selected for 'Source'
    plotOverLine4.Source.Point1 = [0.0, -0.005200000014156103, -0.004999999888241291]
    plotOverLine4.Source.Point2 = [0.699999988079071, 0.005200000014156103, 0.004999999888241291]

    # Properties modified on plotOverLine4.Source
    plotOverLine4.Source.Point1 = [0.550688, -0.0052, 0.0]
    plotOverLine4.Source.Point2 = [0.550688, 0.0052, 0.0]

    # show data in view
    plotOverLine4Display = Show(plotOverLine4, lineChartView1)

    # trace defaults for the display properties.
    plotOverLine4Display.CompositeDataSetIndex = [0]
    plotOverLine4Display.UseIndexForXAxis = 0
    plotOverLine4Display.XArrayName = 'arc_length'
    plotOverLine4Display.SeriesVisibility = ['cellID', 'Co', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']
    plotOverLine4Display.SeriesLabel = ['arc_length', 'arc_length', 'cellID', 'cellID', 'Co', 'Co', 'epsilon', 'epsilon', 'k', 'k', 'nut', 'nut', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'cellID', '0.89', '0.1', '0.11', 'Co', '0.22', '0.49', '0.72', 'epsilon', '0.3', '0.69', '0.29', 'k', '0.6', '0.31', '0.64', 'nut', '1', '0.5', '0', 'p', '0.65', '0.34', '0.16', 'U_X', '0', '0', '0', 'U_Y', '0.89', '0.1', '0.11', 'U_Z', '0.22', '0.49', '0.72', 'U_Magnitude', '0.3', '0.69', '0.29', 'vtkValidPointMask', '0.6', '0.31', '0.64', 'Points_X', '1', '0.5', '0', 'Points_Y', '0.65', '0.34', '0.16', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.89', '0.1', '0.11']
    plotOverLine4Display.SeriesPlotCorner = ['arc_length', '0', 'cellID', '0', 'Co', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine4Display.SeriesLabelPrefix = ''
    plotOverLine4Display.SeriesLineStyle = ['arc_length', '1', 'cellID', '1', 'Co', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine4Display.SeriesLineThickness = ['arc_length', '2', 'cellID', '2', 'Co', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine4Display.SeriesMarkerStyle = ['arc_length', '0', 'cellID', '0', 'Co', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

    # update the view to ensure updated data information
    lineChartView1.Update()

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.XArrayName = 'U_X'

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.SeriesVisibility = ['cellID', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']
    plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'cellID', '0.889998', '0.100008', '0.110002', 'Co', '0.220005', '0.489998', '0.719997', 'epsilon', '0.300008', '0.689998', '0.289998', 'k', '0.6', '0.310002', '0.639994', 'nut', '1', '0.500008', '0', 'p', '0.650004', '0.340002', '0.160006', 'U_X', '0', '0', '0', 'U_Y', '0.889998', '0.100008', '0.110002', 'U_Z', '0.220005', '0.489998', '0.719997', 'U_Magnitude', '0.300008', '0.689998', '0.289998', 'vtkValidPointMask', '0.6', '0.310002', '0.639994', 'Points_X', '1', '0.500008', '0', 'Points_Y', '0.650004', '0.340002', '0.160006', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.889998', '0.100008', '0.110002']
    plotOverLine4Display.SeriesPlotCorner = ['Co', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'cellID', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']
    plotOverLine4Display.SeriesLineStyle = ['Co', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'cellID', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'vtkValidPointMask', '1']
    plotOverLine4Display.SeriesLineThickness = ['Co', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'cellID', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'vtkValidPointMask', '2']
    plotOverLine4Display.SeriesMarkerStyle = ['Co', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'cellID', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.SeriesVisibility = ['arc_length', 'cellID', 'epsilon', 'k', 'nut', 'p', 'U_Magnitude']

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.SeriesVisibility = ['arc_length', 'cellID', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.SeriesVisibility = ['arc_length', 'epsilon', 'k', 'nut', 'p']

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.SeriesVisibility = ['arc_length', 'k', 'nut', 'p']

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.SeriesVisibility = ['arc_length', 'nut', 'p']

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.SeriesVisibility = ['arc_length', 'p']

    # Properties modified on plotOverLine4Display
    plotOverLine4Display.SeriesVisibility = ['arc_length']

    # split cell
    layout1.SplitHorizontal(2, 0.5)

    # set active view
    SetActiveView(None)

    # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024L
    # uncomment following to set a specific view size
    # spreadSheetView1.ViewSize = [400, 400]

    # place view in the layout
    layout1.AssignView(6, spreadSheetView1)

    # show data in view
    plotOverLine4Display_1 = Show(plotOverLine4, spreadSheetView1)

    # set active view
    SetActiveView(lineChartView1)

    # destroy lineChartView1
    Delete(lineChartView1)
    del lineChartView1

    # close an empty frame
    layout1.Collapse(5)

    # set active view
    SetActiveView(spreadSheetView1)

    # export view
    ExportView('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_055.csv', view=spreadSheetView1)

    # set active source
    SetActiveSource(plotOverLine3)

    # show data in view
    plotOverLine3Display = Show(plotOverLine3, spreadSheetView1)

    # export view
    ExportView('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_029.csv', view=spreadSheetView1)

    # set active source
    SetActiveSource(plotOverLine2)

    # show data in view
    plotOverLine2Display = Show(plotOverLine2, spreadSheetView1)

    # export view
    ExportView('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_023.csv', view=spreadSheetView1)

    # set active source
    SetActiveSource(plotOverLine1)

    # show data in view
    plotOverLine1Display_1 = Show(plotOverLine1, spreadSheetView1)

    # export view
    ExportView('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_019.csv', view=spreadSheetView1)

    #### saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.3499999940395355, 0.0, 1.3525833420181734]
    renderView1.CameraFocalPoint = [0.3499999940395355, 0.0, 0.0]
    renderView1.CameraParallelScale = 0.35007432900271984

    #### uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
