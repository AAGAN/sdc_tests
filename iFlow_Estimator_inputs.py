#server to test
server = "http://10.16.74.48/sdc/" 
#server = "http://www.suppressiondesigncenter.com"

#login page https://www.suppressiondesigncenter.com/sdc/
fUsername = 'aagan2'
fPassword = 'Jci8124@agan'

#New Project page https://www.suppressiondesigncenter.com/fsdc/add_project.php
addProject = {
    'cboUnits' : 'Metric',
    'projectname': 'Test',
    'cboSystem' : 'Inert Gas',
    'address1' : '1467 Elmwood Ave.',
    'address2': ' ',
    'projectcity' : 'Cranston',
    'projectref' : 'Test Case',
    'customer' : 'JCI',
    'cboCountry' : 'United States',
    'cboState' : 'Rhode Island',
    'projectzip' : '02910'
}

#System Details https://www.suppressiondesigncenter.com/fsdc/systems/inert/iflow/systemdetails.php
systemDetails = {
    'cboBrand'  : 'ANSUL',
    'cboSystype' : 'iFlow System',
    'cboSysApproval' : 'UL/ULC/FM',
    'cboAgenttype' : 'IG-541 (Inergen)',
    'cboDesignStandards' : 'NFPA 2001',
    'cboFireClasses' : 'Surface Class A',
    'cboReserve' : 'No',
    'txtMinTemp' : '20',
    'txtMaxTemp' : '100',
    'txtAltitude' : '0',
    'txtPressureChange' : '250',
    'txtDesignConcentration' : '34.2',
    'txtDischargeTime' : '120 s',
    'cboSystemPressures' : '300 bar',
    'cboContainerApproval' : 'TPED',
    'cboContainerSizes' : '80 L',
    'cboNozzles' : 'Inert Acoustic',
    'cboMulti' : 'Simultaneous',
}

#Hazard Management page
Hazards = [
    {
        'hazardname' : 'Haz1',
        'designconcentration' : '34.2',
        'maxpressurechange' : '250',
        'cboNozzle' : 'Inert 360° (UL/FM - NPT)',
        'roomexits' : '2',
        'Enclosures': [
            {
                'vlabel1' : 'Enc1',
                'cLength' : '10',
                'cWidth' : '5',
                'cHeight' : '5',
                'cFloor' : '25',
                'cVolRed' : '10'
            }#,
#             {
#                 'vlabel2' : 'Enc2',
#                 'rLength' : '5',
#                 'rWidth' : '5',
#                 'rHeight' : '5',
#                 'rFloor' : '25',
#                 'rVolRed' : '10'
#             },
#             {
#                 'vlabel3' : 'Enc3',
#                 'fLength' : '5',
#                 'fWidth' : '5',
#                 'fHeight' : '5',
#                 'fFloor' : '25',
#                 'fVolRed' : '10'
#             }
        ]
    }#,
#     {
#         'hazardname' : 'Haz2',
#         'designconcentration' : '34.2',
#         'maxpressurechange' : '250',
#         'cboNozzle' : 'Inert 360° (UL/FM - NPT)',
#         'roomexits' : '2',
#         'Enclosures': [
#             {
#                 'vlabel1' : 'Enc1',
#                 'cLength' : '5',
#                 'cWidth' : '5',
#                 'cHeight' : '5',
#                 'cFloor' : '25',
#                 'cVolRed' : '10'
#             },
#             {
#                 'vlabel2' : 'Enc2',
#                 'rLength' : '5',
#                 'rWidth' : '5',
#                 'rHeight' : '5',
#                 'rFloor' : '25',
#                 'rVolRed' : '10'
#             },
#             {
#                 'vlabel3' : 'Enc3',
#                 'fLength' : '5',
#                 'fWidth' : '5',
#                 'fHeight' : '5',
#                 'fFloor' : '25',
#                 'fVolRed' : '10'
#             }
#         ]
#     }
]

#Hazard Review page (https://www.suppressiondesigncenter.com/fsdc/systems/inert/iflow/hazardreview.php)
cboContainerSizes = '80 L' #'140 L'

#system options page (https://www.suppressiondesigncenter.com/fsdc/systems/inert/iflow/systemreview.php)
systemOptions={
    'cboGauges' : 'Contacted Gauge', #'Standard Gauge'
    'cboThreadType' : 'NPT', #'BSP'
    'cboActuation' : 'Pilot Container',
    'cboBracketing' : 'iFlow 80 L Matrix', # 'iFlow 80 L Upright (Floor Mount)'
    'cboArrangement' : '1-row', #'2-row' , '3-row'
}

#Vent BOM page (https://www.suppressiondesigncenter.com/fsdc/systems/inert/iflow/ventbom.php)
cboVenttype = 'Internal Mount'

#Hydraulic Options page
hydraulicsOptions = {
    'txtPipeTemp' : '20',
    'txtDischargeTime' : '120',
    'txtCylQty' : '3',
    'cboNozzleType' : 'Fixed Nozzle', #'Agent Quantity', #'Fixed Nozzle'
    'cboFVAType' : 'Ansul' # 'FIA'
}

# Acoustic Nozzle Calculator
# New Room page
BOMEnclosure = {
    'vroomname' : 'Enc1',
    'cboHardware' : 'iFlow',
    'vlength' : '5',
    'vwidth' : '5',
    'vheight' : '5',
    'vvolume' : '115',
    'vreceiverdist' : '2',
    'vtargetpress' : '100',
    'vdatarackcount' : '5',
    'vhumidity' : '50',
    'vpressure' : '250',
    'vtemp' : '25'
}

#add Nozzle window
addNozzle = {
    #'cboRun' , 'NameOfRun',
    'cboNozzType' : '1-1/2 Acoustic Nozzle - INERT', #'3/4 Acoustic Nozzle - INERT' 'Standard Nozzle - INERT'
    'cboPeakRate' : '41-62',
    'vNozzleCount' : '2'
}