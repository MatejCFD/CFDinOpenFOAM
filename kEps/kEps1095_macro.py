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

    animationScene1.GoToLast()

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

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.3499999940395355, 0.0, 0.6309901114002235]
    renderView1.CameraFocalPoint = [0.3499999940395355, 0.0, 0.0]
    renderView1.CameraParallelScale = 0.35007432900271984

    # save screenshot
    SaveScreenshot('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_Ux.png', renderView1, ImageResolution=[4232, 1932],
        TransparentBackground=1, 
        # PNG options
        CompressionLevel='0')

    # destroy renderView1
    Delete(renderView1)
    del renderView1

    # load state
    LoadState('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/Re1095_postPlot.pvsm', LoadStateDataFileOptions='Choose File Names',
        DataDirectory='/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095',
        kEps_config1_FileNames=['/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_0.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_1900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_2900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_3900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_4900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_5900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_6900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_7900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_8900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9000.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9100.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9200.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9300.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9400.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9500.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9600.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9700.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9800.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_9900.vtk', '/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/VTK/'+i+'_10000.vtk'])

    # find view
    lineChartView1 = FindViewOrCreate('LineChartView1', viewtype='XYChartView')
    # uncomment following to set a specific view size
    # lineChartView1.ViewSize = [524, 483]

    # set active view
    SetActiveView(lineChartView1)

    # get layout
    layout1 = GetLayout()

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
    kEps_config1_Display = Show(kEps_config1_, spreadSheetView1)

    # set active view
    SetActiveView(lineChartView1)

    # destroy lineChartView1
    Delete(lineChartView1)
    del lineChartView1

    # close an empty frame
    layout1.Collapse(5)

    # set active view
    SetActiveView(spreadSheetView1)

    # find source
    plotOverLine2 = FindSource('PlotOverLine2')

    # set active source
    SetActiveSource(plotOverLine2)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=plotOverLine2.Source)

    # show data in view
    plotOverLine2Display = Show(plotOverLine2, spreadSheetView1)

    # export view
    ExportView('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_023.csv', view=spreadSheetView1)

    # find source
    plotOverLine1 = FindSource('PlotOverLine1')

    # set active source
    SetActiveSource(plotOverLine1)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=plotOverLine1.Source)

    # show data in view
    plotOverLine1Display = Show(plotOverLine1, spreadSheetView1)

    # export view
    ExportView('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_019.csv', view=spreadSheetView1)

    # find source
    plotOverLine3 = FindSource('PlotOverLine3')

    # set active source
    SetActiveSource(plotOverLine3)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=plotOverLine3.Source)

    # show data in view
    plotOverLine3Display = Show(plotOverLine3, spreadSheetView1)

    # export view
    ExportView('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_029.csv', view=spreadSheetView1)

    # find source
    plotOverLine4 = FindSource('PlotOverLine4')

    # set active source
    SetActiveSource(plotOverLine4)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=plotOverLine4.Source)

    # show data in view
    plotOverLine4Display = Show(plotOverLine4, spreadSheetView1)

    # export view
    ExportView('/home/matej/Desktop/LearnCFD/OpenFOAM_ja/transientReport/transientBFS/RANS/Re_1095/kEps_1095/'+i+'/'+i+'_055.csv', view=spreadSheetView1)

    #### uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
