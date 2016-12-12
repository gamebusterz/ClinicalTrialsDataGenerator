# -*- coding: utf-8 -*-
import random
import uuid
import csv
from datetime import datetime

## FACTOR THE INFLUENCE OF HEALTH IN COSTS
## ADD EITHINICITY
header = ['ID','Site_No.','Rank_of_PI','Study_Type','Country','Therapeutic_Area','Sponsor','No_of_sites','Req_Healthy_Volunteer','Gender','Min_Age','Max_Age','Study_Start_Date','Study_End_Date','Duration_of_study(days)','Phase_1_length','No_of_volunteers_1','Patient_Rec_1','Patient_Retention_1','RN/CRA_1','Physician_1','Procedure_1','Central_lab_1','Site_rec_1','Site_ret_1','Admin_staff_1','Site_Monitoring_1','Data_mgmt_1','IRB_Approval_1','IRB_Amendment_1','Source_data_verf_1','Subtotal_1','Site_overhead_1','Total_including_Overhead_1','Phase_2_length','No_of_volunteers_2','Patient_Rec_2','Patient_Retention_2','RN/CRA_2','Physician_2','Procedure_2','Central_lab_2','Site_rec_2','Site_ret_2','Admin_staff_2','Site_Monitoring_2','Data_mgmt_2','IRB_Approval_2','IRB_Amendment_2','Source_data_verf_2','Subtotal_2','Site_overhead_2','Total_including_Overhead_2','Phase_3_length','No_of_volunteers_3','Patient_Rec_3','Patient_Retention_3','RN/CRA_3','Physician_3','Procedure_3','Central_lab_3','Site_rec_3','Site_ret_3','Admin_staff_3','Site_Monitoring_3','Data_mgmt_3','IRB_Approval_3','IRB_Amendment_3','Source_data_verf_3','Subtotal_3','Site_overhead_3','Total_including_Overhead_3']
print("Total cost of study")

myfile = open('Generated3.csv','a')
wr = csv.writer(myfile,quoting = csv.QUOTE_ALL)
wr.writerow(header)

n = 10 #Change the Value of n to generate as many rows of data as you want

pi_ranks = ['Low','Mid','High']
age_min_max = [[18,30],[18,90],[12,18],[65,90],[40,65],[16,30],[8,14]] ######or in days ? ##########
                # instead of 'None' string, None value can be used but it will give a blank cell

def get_enrollments(no_of_sites):
    enrollments_dict =  {
                            1: [random.randint(25,80),random.randint(100,300),random.randint(900,2500)],
                            2: [random.randint(20,45),random.randint(90,150),random.randint(800,1300)],
                            3: [random.randint(20,30),random.randint(70,100),random.randint(600,800)],
                            4: [random.randint(15,25),random.randint(50,75),random.randint(400,650)],
                            5: [random.randint(15,20),random.randint(40,60),random.randint(300,550)]
                        }
    return enrollments_dict[no_of_sites]



country_names = {
                 'India':{
                            'Low':  0.4,
                            'Mid':  0.5,
                            'High': 0.6
                         },
                 'Canada':{
                            'Low':  0.8,
                            'Mid':  0.85,
                            'High': 0.9
                         },
                 'France':{
                            'Low':  0.75,
                            'Mid':  0.9,
                            'High': 0.95
                         },
                 'Japan':{
                            'Low':  0.6,
                            'Mid':  0.65,
                            'High': 0.8
                         },
                 'Australia':{
                            'Low':  1.05,
                            'Mid':  1.15,
                            'High': 1.2
                         },
                 'USA':{
                            'Low':  1,
                            'Mid':  1,
                            'High': 1
                         },
                 'UK':{
                            'Low':  1.1,
                            'Mid':  1.2,
                            'High': 1.3
                         },
                 'Brazil':{
                            'Low':  0.5,
                            'Mid':  0.6,
                            'High': 0.7
                         },
                 'China' :{
                            'Low':  0.45,
                            'Mid':  0.55,
                            'High': 0.65
                         },
                 'Mexico' :{
                             'Low':  0.45,
                             'Mid':  0.55,
                             'High': 0.65
                         }
                 }

# Get cost per day per volunteer
#def get_cost_pd_pv(t_area):

#    cost_perday_phase1 = {
#                            #patient_rec,patient_ret,nurse,physician,clinical_proc,central_lab,site_rec,site_ret,admin_staff,site_monitoring,data_mgmt,IRB_apr,IRB_amm,source_data_verf

#                            'Immunomodulation':[120,21,510,350,1420,750,70000,10000,11000,45000int(,72000,12000,1200,480000],
#                            'Ophthalmology':[110,19,480,300,1360,680,67000,8200,9100,42000,67000,12000,1200,410000],
#                            'Respiratory System':[100,16,450,270,1300,650,65000,8000,9000,40000,65000,12000,1200,400000],
#                            'Oncology':[90,14,430,250,1240,610,60000,7200,8000,35000,60000,12000,1200,360000],
#                            'Anti-Infective':[85,17,410,220,1200,590,57000,6800,7000,32000,57000,12000,1200,320000],
#                            'Central Nervous System':[80,16,390,200,1100,550,54000,6400,6800,30000,53000,12000,1200,300000],
#                            'Genitourinary System':[80,15,320,170,900,410,48000,5700,6100,24500,35000,12000,1200,140000],
#                            'Gastrointestinal':[78,14,210,170,530,190,14000,1400,1700,13000,26000,12000,1200,80000],
#                            'Cardiovascular':[75,14,180,120,450,210,18000,2000,2100,10500,19000,12000,1200,60000],
#                            'Dermatology':[65,12,140,90,320,150,14000,1500,1600,9000,15000,12000,1200,80000],
#                            'Hematology':[65,12,140,90,320,150,14000,1500,1600,9000,15000,12000,1200,80000],
#                            'Endocrine':[60,10,120,80,300,140,12000,1300,1400,7000,12000,12000,1200,60000],
#                            'Pain and Anesthesia':[60,10,120,80,300,140,12000,1300,1400,7000,12000,12000,1200,60000],

#                          }

#    cost_perday_phase2 = {
#                            #patient_rec,patient_ret,nurse,physician,clinical_proc,central_lab,site_rec,site_ret,admin_staff,site_monitoring,data_mgmt,IRB_apr,IRB_amm,source_data_verf
#                            'Hematology':[120,21,510,350,1420,750,70000,10000,11000,45000,72000,60000,1500,480000],
#                            'Pain and Anesthesia':[60,10,120,80,300,140,12000,1300,1400,7000,12000,60000,1500,60000],
#                            'Immunomodulation':[120,21,510,350,1420,750,70000,10000,11000,45000,72000,160000,1500,480000],
#                            'Gastrointestinal':[78,14,210,170,530,190,14000,1400,1700,13000,26000,60000,1500,80000],
#                            'Genitourinary System':[80,15,320,170,900,410,48000,5700,6100,24500,35000,60000,1500,140000],
#                            'Anti-Infective':[85,17,410,220,1200,590,57000,6800,7000,32000,57000,60000,1500,320000],
#                            'Central Nervous System':[80,16,390,200,1100,550,54000,6400,6800,30000,53000,60000,1500,300000],
#                            'Ophthalmology':[110,19,480,300,1360,680,67000,8200,9100,42000,67000,60000,1500,410000],
#                            'Respiratory System':[100,16,450,270,1300,650,65000,8000,9000,40000,65000,60000,1500,400000],
#                            'Endocrine':[60,10,120,80,300,140,12000,1300,1400,7000,12000,60000,1500,60000],
#                            'Oncology':[90,14,430,250,1240,610,60000,7200,8000,35000,60000,60000,1500,360000],
#                            'Dermatology':[65,12,140,90,320,150,14000,1500,1600,9000,15000,60000,1500,80000],
#                            'Cardiovascular':[75,14,180,120,450,210,18000,2000,2100,10500,19000,60000,1500,60000]

#                          }

################################################START OF FUNCTION
def get_cost(phase,t_area):
    cost_phase1 = {
                            #patient_rec,patient_ret,nurse,physician,clinical_proc,central_lab,site_rec,site_ret,admin_staff,site_monitoring,data_mgmt,IRB_apr,IRB_amm,source_data_verf

                            'Immunomodulation':      [int(37000*1.7),int(6145*1.7),int(178237*1.7),int(109681*1.7),int(475667*1.7),int(250000*1.7),int(51000*1.7),int(193000*1.7),int(237000*1.7),int(198000*1.7),int(50331*1.7),int(11962*1.7),int(1094*1.7),int(326000*1.7)],
                            'Ophthalmology':         [int(37000*1.35),int(6145*1.35),int(178237*1.35),int(109681*1.35),int(475667*1.35),int(250000*1.35),int(51000*1.35),int(193000*1.35),int(237000*1.35),int(198000*1.35),int(50331*1.35),int(11962*1.35),int(1094*1.35),int(326000*1.35)],
                            'Respiratory System':    [int(37000*1.3),int(6145*1.3),int(178237*1.3),int(109681*1.3),int(475667*1.3),int(250000*1.3),int(51000*1.3),int(193000*1.3),int(237000*1.3),int(198000*1.3),int(50331*1.3),int(11962*1.3),int(1094*1.3),int(326000*1.3)],
                            'Oncology':              [int(37000*1.15),int(6145*1.15),int(178237*1.15),int(109681*1.15),int(475667*1.15),int(250000*1.15),int(51000*1.15),int(193000*1.15),int(237000*1.15),int(198000*1.15),int(50331*1.15),int(11962*1.15),int(1094*1.15),int(326000*1.15)],
                            'Anti-Infective':        [int(37000*1.07),int(6145*1.07),int(178237*1.07),int(109681*1.07),int(475667*1.07),int(250000*1.07),int(51000*1.07),int(193000*1.07),int(237000*1.07),int(198000*1.07),int(50331*1.07),int(11962*1.07),int(1094*1.07),int(326000*1.07)],
                            'Central Nervous System':[37000,6145,178237,109681,475667,250000,51000,193000,237000,198000,50331,11962,1094,326000],
                            'Genitourinary System':  [int(37000*0.89),int(6145*0.89),int(178237*0.89),int(109681*0.89),int(475667*0.89),int(250000*0.89),int(51000*0.89),int(193000*0.89),int(237000*0.89),int(198000*0.89),int(50331*0.89),int(11962*0.89),int(1094*0.89),int(326000*0.89)],
                            'Gastrointestinal':      [int(37000*0.61),int(6145*0.61),int(178237*0.61),int(109681*0.61),int(475667*0.61),int(250000*0.61),int(51000*0.61),int(193000*0.61),int(237000*0.61),int(198000*0.61),int(50331*0.61),int(11962*0.61),int(1094*0.61),int(326000*0.61)],
                            'Cardiovascular':        [int(37000*0.56),int(6145*0.56),int(178237*0.56),int(109681*0.56),int(475667*0.56),int(250000*0.56),int(51000*0.56),int(193000*0.56),int(237000*0.56),int(198000*0.56),int(50331*0.56),int(11962*0.56),int(1094*0.56),int(326000*0.56)],
                            'Dermatology':           [int(37000*0.46),int(6145*0.46),int(178237*0.46),int(109681*0.46),int(475667*0.46),int(250000*0.46),int(51000*0.46),int(193000*0.46),int(237000*0.46),int(198000*0.46),int(50331*0.46),int(11962*0.46),int(1094*0.46),int(326000*0.46)],
                            'Hematology':            [int(37000*0.43),int(6145*0.43),int(178237*0.43),int(109681*0.43),int(475667*0.43),int(250000*0.43),int(51000*0.43),int(193000*0.43),int(237000*0.43),int(198000*0.43),int(50331*0.43),int(11962*0.43),int(1094*0.43),int(326000*0.43)],
                            'Endocrine':             [int(37000*0.35),int(6145*0.35),int(178237*0.35),int(109681*0.35),int(475667*0.35),int(250000*0.35),int(51000*0.35),int(193000*0.35),int(237000*0.35),int(198000*0.35),int(50331*0.35),int(11962*0.35),int(1094*0.35),int(326000*0.35)],
                            'Pain and Anesthesia':   [int(37000*0.35),int(6145*0.35),int(178237*0.35),int(109681*0.35),int(475667*0.35),int(250000*0.35),int(51000*0.35),int(193000*0.35),int(237000*0.35),int(198000*0.35),int(50331*0.35),int(11962*0.35),int(1094*0.35),int(326000*0.35)]
    }

    cost_phase2 = {
                            'Hematology':             [int(161140*1.41),int(15439*1.41),int(441053*1.41),int(381968*1.41),int(1476368*1.41),int(804821*1.41),int(233729*1.41),int(1127005*1.41),int(1347390*1.41),int(1083186*1.41),int(60000*1.41),int(60000*1.41),int(1700*1.41),int(406000*1.41)],
                            'Pain and Anesthesia':    [int(161140*1.22),int(15439*1.22),int(441053*1.22),int(381968*1.22),int(1476368*1.22),int(804821*1.22),int(233729*1.22),int(1127005*1.22),int(1347390*1.22),int(1083186*1.22),int(60000*1.22),int(60000*1.22),int(1700*1.22),int(406000*1.22)],
                            'Immunomodulation':       [int(161140*1.15),int(15439*1.15),int(441053*1.15),int(381968*1.15),int(1476368*1.15),int(804821*1.15),int(233729*1.15),int(1127005*1.15),int(1347390*1.15),int(1083186*1.15),int(60000*1.15),int(60000*1.15),int(1700*1.15),int(406000*1.15)],
                            'Gastrointestinal':       [int(161140*1.13),int(15439*1.13),int(441053*1.13),int(381968*1.13),int(1476368*1.13),int(804821*1.13),int(233729*1.13),int(1127005*1.13),int(1347390*1.13),int(1083186*1.13),int(60000*1.13),int(60000*1.13),int(1700*1.13),int(406000*1.13)],
                            'Genitourinary System':   [int(161140*1.05),int(15439*1.05),int(441053*1.05),int(381968*1.05),int(1476368*1.05),int(804821*1.05),int(233729*1.05),int(1127005*1.05),int(1347390*1.05),int(1083186*1.05),int(60000*1.05),int(60000*1.05),int(1700*1.05),int(406000*1.05)],
                            'Anti-Infective':         [int(161140*1.02),int(15439*1.02),int(441053*1.02),int(381968*1.02),int(1476368*1.02),int(804821*1.02),int(233729*1.02),int(1127005*1.02),int(1347390*1.02),int(1083186*1.02),int(60000*1.02),int(60000*1.02),int(1700*1.02),int(406000*1.02)],
                            'Central Nervous System': [161140,15439,441053,381968,1476368,804821,233729,1127005,1347390,1083186,60000,60000,1700,406000],
                            'Ophthalmology':          [161140,15439,441053,381968,1476368,804821,233729,1127005,1347390,1083186,60000,60000,1700,406000],
                            'Respiratory System':     [int(161140*0.87),int(15439*0.87),int(441053*0.87),int(381968*0.87),int(1476368*0.87),int(804821*0.87),int(233729*0.87),int(1127005*0.87),int(1347390*0.87),int(1083186*0.87),int(60000*0.87),int(60000*0.87),int(1700*0.87),int(406000*0.87)],
                            'Endocrine':              [int(161140*0.86),int(15439*0.86),int(441053*0.86),int(381968*0.86),int(1476368*0.86),int(804821*0.86),int(233729*0.86),int(1127005*0.86),int(1347390*0.86),int(1083186*0.86),int(60000*0.86),int(60000*0.86),int(1700*0.86),int(406000*0.86)],
                            'Oncology':               [int(161140*0.80),int(15439*0.80),int(441053*0.80),int(381968*0.80),int(1476368*0.80),int(804821*0.80),int(233729*0.80),int(1127005*0.80),int(1347390*0.80),int(1083186*0.80),int(60000*0.80),int(60000*0.80),int(1700*0.80),int(406000*0.80)],
                            'Dermatology':            [int(161140*0.64),int(15439*0.64),int(441053*0.64),int(381968*0.64),int(1476368*0.64),int(804821*0.64),int(233729*0.64),int(1127005*0.64),int(1347390*0.64),int(1083186*0.64),int(60000*0.64),int(60000*0.64),int(1700*0.64),int(406000*0.64)],
                            'Cardiovascular':         [int(161140*0.50),int(15439*0.50),int(441053*0.50),int(381968*0.50),int(1476368*0.50),int(804821*0.50),int(233729*0.50),int(1127005*0.50),int(1347390*0.50),int(1083186*0.50),int(60000*0.50),int(60000*0.50),int(1700*0.50),int(406000*0.50)]
    }

    cost_phase3 = {
                            'Pain and Anesthesia':   [int(308672*2.75),int(24727*2.75),int(939540*2.75),int(805508*2.75),int(2252208*2.75),int(849180*2.75),int(395182*2.75),int(1305361*2.75),int(2321628*2.75),int(1624874*2.75),int(39047*2.75),int(114118*2.75),int(1919*2.75),int(400173*2.75)],
                            'Ophthalmology':         [int(308672*1.59),int(24727*1.59),int(939540*1.59),int(805508*1.59),int(2252208*1.59),int(849180*1.59),int(395182*1.59),int(1305361*1.59),int(2321628*1.59),int(1624874*1.59),int(39047*1.59),int(114118*1.59),int(1919*1.59),int(400173*1.59)],
                            'Cardiovascular':        [int(308672*1.31),int(24727*1.31),int(939540*1.31),int(805508*1.31),int(2252208*1.31),int(849180*1.31),int(395182*1.31),int(1305361*1.31),int(2321628*1.31),int(1624874*1.31),int(39047*1.31),int(114118*1.31),int(1919*1.31),int(400173*1.31)],
                            'Respiratory System':    [int(308672*1.20),int(24727*1.20),int(939540*1.20),int(805508*1.20),int(2252208*1.20),int(849180*1.20),int(395182*1.20),int(1305361*1.20),int(2321628*1.20),int(1624874*1.20),int(39047*1.20),int(114118*1.20),int(1919*1.20),int(400173*1.20)],
                            'Anti-Infective':        [int(308672*1.18),int(24727*1.18),int(939540*1.18),int(805508*1.18),int(2252208*1.18),int(849180*1.18),int(395182*1.18),int(1305361*1.18),int(2321628*1.18),int(1624874*1.18),int(39047*1.18),int(114118*1.18),int(1919*1.18),int(400173*1.18)],
                            'Oncology':              [int(308672*1.15),int(24727*1.15),int(939540*1.15),int(805508*1.15),int(2252208*1.15),int(849180*1.15),int(395182*1.15),int(1305361*1.15),int(2321628*1.15),int(1624874*1.15),int(39047*1.15),int(114118*1.15),int(1919*1.15),int(400173*1.15)],
                            'Central Nervous System':[308672,24727,939540,805508,2252208,849180,395182,1305361,2321628,1624874,39047,114118,1919,400173],
                            'Genitourinary System':  [int(308672*0.91),int(24727*0.91),int(939540*0.91),int(805508*0.91),int(2252208*0.91),int(849180*0.91),int(395182*0.91),int(1305361*0.91),int(2321628*0.91),int(1624874*0.91),int(39047*0.91),int(114118*0.91),int(1919*0.91),int(400173*0.91)],
                            'Endocrine':             [int(308672*0.88),int(24727*0.88),int(939540*0.88),int(805508*0.88),int(2252208*0.88),int(849180*0.88),int(395182*0.88),int(1305361*0.88),int(2321628*0.88),int(1624874*0.88),int(39047*0.88),int(114118*0.88),int(1919*0.88),int(400173*0.88)],
                            'Hematology':            [int(308672*0.78),int(24727*0.78),int(939540*0.78),int(805508*0.78),int(2252208*0.78),int(849180*0.78),int(395182*0.78),int(1305361*0.78),int(2321628*0.78),int(1624874*0.78),int(39047*0.78),int(114118*0.78),int(1919*0.78),int(400173*0.78)],
                            'Gastrointestinal':      [int(308672*0.75),int(24727*0.75),int(939540*0.75),int(805508*0.75),int(2252208*0.75),int(849180*0.75),int(395182*0.75),int(1305361*0.75),int(2321628*0.75),int(1624874*0.75),int(39047*0.75),int(114118*0.75),int(1919*0.75),int(400173*0.75)],
                            'Immunomodulation':      [int(308672*0.62),int(24727*0.62),int(939540*0.62),int(805508*0.62),int(2252208*0.62),int(849180*0.62),int(395182*0.62),int(1305361*0.62),int(2321628*0.62),int(1624874*0.62),int(39047*0.62),int(114118*0.62),int(1919*0.62),int(400173*0.62)],
                            'Dermatology':           [int(308672*0.59),int(24727*0.59),int(939540*0.59),int(805508*0.59),int(2252208*0.59),int(849180*0.59),int(395182*0.59),int(1305361*0.59),int(2321628*0.59),int(1624874*0.59),int(39047*0.59),int(114118*0.59),int(1919*0.59),int(400173*0.59)]
    }

    if phase == 1:
        return cost_phase1[t_area]
    elif phase == 2:
        return cost_phase2[t_area]
    else:
        return cost_phase3[t_area]

############################################################END OF FUNCTION

#therapeutic_areas = ['Cardiology/Vascular','Dental and Oral','Dermatology','Endocrinology','Family Medicine','Gastroentology','Genetic Disease','Healthy Volunteers','Hematology','Hepatology','Immunology','Infections and Infectious Diseases','Musculoskeletal','Nephrology','Neurology','Nutrition and Weight Loss','Obstrensics/Gynecology','Oncology','Opthalmology','ENT','Pediatrics/Neonatology','Plastic Surgery','Pharmocology/Toxicology','Podiatry','Psychiatry/Psychology','Pulmonary/Respiratory','Rheumatology','Sleep','Trauma','Urology','Vaccines']
therapeutic_areas = ['Respiratory System','Pain and Anesthesia','Oncology','Ophthalmology','Hematology','Cardiovascular','Endocrine','Gastrointestinal','Immunomodulation','Anti-Infective','Central Nervous System','Dermatology','Genitourinary System']

pharma_companies = [
                '3M Pharmaceuticals',
                'Abbott Laboratories',
                'AbbVie',
                'Acadia Pharmaceuticals',
                'Acorda Therapeutics',
                'Actavis',
                'Actelion',
                'Adcock Ingram',
                'Advanced Chemical Industries',
                'Advaxis',
                'Ajanta Pharma',
                'Alcon',
                'Alexion Pharmaceuticals',
                'Alkaloid',
                'Alkermes',
                'Allergan',
                'Alliance Boots',
                'Almirall',
                'Alphapharm',
                'Altana Pharma AG',
                'Amgen',
                'Amico Laboratories',
                'Apotex Inc.',
                'Aspen Pharmacare',
                'Astellas Pharma',
                'AstraZeneca',
                'Aurobindo Pharma',
                'Avax Technologies',
                'Avella Specialty Pharmacy',
                'Axcan Pharma',
                'Bargn Farmaceutici Phils Co',
                'Barr Pharmaceuticals',
                'Laboratórios BASI',
                'Bausch & Lomb',
                'Baxalta',
                'Baxter International',
                'Bayer Schering Pharma AG',
                'Beximco Pharmaceuticals Ltd',
                'Bial',
                'Biocon',
                'Biogen',
                'Biolex',
                'BioMarin Pharmaceutical',
                'Bionovo',
                'Biotecnol',
                'Biovail',
                'Biovitrum',
                'Bluepharma',
                'Boehringer-Ingelheim',
                'Bosnalijek',
                'Bristol-Myers Squibb',
                'BTG plc',
                'Cadila Healthcare',
                'Canadian Plasma Resources',
                'Celgene',
                'Cephalon',
                'Chiesi Farmaceutici S.p.A.',
                'Chugai Pharmaceutical Co.',
                'CinnaGen',
                'Cipla',
                'CoCo Therapeutics',
                'Concordia Healthcare',
                'Continental Clinical Solutions',
                'Covance',
                'Crucell',
                'CSL Limited',
                'Dabur',
                'Daiichi Sankyo',
                'Dainippon Sumitomo Pharma',
                'Dawakhana Shifaul Amraz',
                'Debiopharm',
                'Diabetology Ltd',
                'Diffusion Pharmaceuticals',
                'Dr. Reddys Laboratories',
                'Ego Pharmaceuticals',
                'Eisai (company)',
                'Elder Pharmaceuticals',
                'Eli Lilly and Company',
                'Elorac, Inc.',
                'Emergent BioSolutions',
                'Endo Pharmaceuticals',
                'Eskayef Bangladesh Limited',
                'F. Hoffmann–La Roche Ltd.',
                'Fabre-Kramer Pharmaceuticals',
                'Ferring Pharmaceuticals',
                'Fresenius Kabi',
                'Fresenius Medical Care',
                'Galderma Laboratories',
                'Gedeon Richter Ltd.',
                'General Pharma',
                'Getz Pharma',
                'Gilead Sciences',
                'GlaxoSmithKline',
                'Glenmark Pharmaceuticals',
                'GPC Biotech',
                'Grifols',
                'Gulf Pharmaceutical Industries',
                'G.F. Harvey Company',
                'Help Remedies',
                'Hetero Drugs',
                'Hexal Australia',
                'Hikma Pharmaceuticals',
                'Hoffmann–La Roche',
                'Horizon Pharma',
                'Hovione',
                'Incepta Pharmaceuticals',
                'Institute for OneWorld Health',
                'Intas Biopharmaceuticals',
                'Interphil Laboratories',
                'Ionis Pharmaceuticals',
                'Ipca Laboratories',
                'Ipsen',
                'Janssen Pharmaceutica Products',
                'Jenapharm',
                'JN-International Medical Corporation',
                'Johnson & Johnson',
                'Julphar',
                'Juno Therapeutics',
                'Lundbeck',
                'Lupin Ltd.',
                'Mallinckrodt Pharmaceuticals',
                'MannKind Corporation',
                'McGuff Companies',
                'Medinfar',
                'Melior Discovery',
                'Menarini',
                'Merck & Co.',
                'Merck KGaA',
                'Mitsubishi Pharma',
                'Mylan',
                'NovaBay Pharmaceuticals',
                'Novartis',
                'Novo Nordisk',
                'Noxxon',
                'Octapharma',
                'Orexo',
                'Orion Pharma',
                'Ortho-McNeil Pharmaceutical',
                'Otsuka Pharmaceutical Co.',
                'Panacea Biotec',
                'Par Pharmaceutical',
                'Patheon',
                'Peregrine Pharmaceuticals',
                'Perrigo',
                'Pfizer',
                'Pharmaceutical Product Development',
                'Pharma Medica',
                'Pharma Nord',
                'Pharmacosmos',
                'Pharmascience',
                'Pierre Fabre Group',
                'Piramal Healthcare',
                'Pliva',
                'Procter & Gamble',
                'Purdue Pharma',
                'Ranbaxy Laboratories',
                'Reckitt Benckiser',
                'Regeneron Pharmaceuticals',
                'Renovo plc',
                'Repligen',
                'Rubicon Research',
                'Salix Pharmaceuticals',
                'Sanofi',
                'Serum Institute of India',
                'Servier Laboratories',
                'Shionogi',
                'Shire plc',
                'Sigma Pharmaceuticals',
                'Sinopharm Group',
                'Solvay',
                'Square Pharmaceuticals',
                'STADA Arzneimittel',
                'Strides Arcolab',
                'Sun Pharmaceutical',
                'Sunovion',
                'Takeda Pharmaceutical Co.',
                'Tasly',
                'Teva Pharmaceuticals',
                'Taro Pharmaceuticals',
                'Torrent Pharmaceuticals',
                'UCB',
                'Unichem Laboratories',
                'United Laboratories',
                'Valeant Pharmaceuticals International',
                'VAV Life Sciences',
                'Veloxis Pharmaceuticals',
                'Vertex Pharmaceuticals',
                'Vion Pharmaceuticals, Inc.',
                'Wallace Pharmaceuticals',
                'Wockhardt',
                'Yuhan Corporation',
                'Zandu Pharmaceuticals',
                'Zentiva'
]

for i in range(n):

    phase_1_site_total = []
    phase_2_site_total = []
    phase_3_site_total = []

    #Start date
    start_year = random.randint(2002, 2010)
    start_month = random.randint(1, 12)
    start_day = random.randint(1, 28)
    start_date = datetime(start_year, start_month, start_day)

    #End date
    end_year = random.randint(start_year+3, start_year+5)
    end_month = random.randint(1, 12)
    end_day = random.randint(1, 28)
    end_date = datetime(end_year, end_month, end_day)

    #total length of study
    delta = end_date - start_date
    study_length = delta.days

    #phase lengths
    phase1_length = random.randint(210,400)
    phase2_length = random.randint(400,800)
    phase3_length = study_length - phase1_length - phase2_length

    #random unique id
    id = uuid.uuid4()
    t_area = random.choice(therapeutic_areas)
    p_company = random.choice(pharma_companies)
    site_counter = random.randint(1,5)
    no_of_sites = site_counter - 1

    age_group = random.choice(age_min_max)
    gender = random.choice(['Male','Female','Both'])

    study_type = random.choice(['International','Local'])
    if no_of_sites == 1:
        study_type = 'Local'
    if study_type == 'Local':
        country_name = random.choice(country_names.keys())


    #pi_rank = random.choice(pi_ranks)
    #-----------moving the above to inside the loop for more variance-----------------

    ## Single PI rank and thus costs for a single study
    ## Add site specific costs
    ## Ethics committee can be added based on the country of trials or the country of Pharma company
    for j in range (1,site_counter):
        if study_type == 'International':
            country_name = random.choice(country_names.keys())

        pi_rank = random.choice(pi_ranks)
        healthy_volunteer = random.choice([True,False])
        enrollments = get_enrollments(no_of_sites) # returns a list of length 3 containing random enrollments for each site

        phase1_c = get_cost(1,t_area)
        #after country adjustment
        phase1_costs = [int(x*country_names[country_name][pi_rank]) for x in phase1_c]
        #Additional costs for non-healthy volunteer
        if healthy_volunteer == False:
            phase1_costs = [int(x*1.05) for x in phase1_costs]
        #Additional costs for younger and older age group
        if age_group == [65,90] or [8,14] :
            phase1_costs = [int(x*1.05) for x in phase1_costs]
        #Added cost based on Number of volunteers
        #phase1_costs = [x+(enrollments*1000) for x in phase1_c]

        Subtotal_for_one_site_p1 = phase1_costs[0]+phase1_costs[1]+phase1_costs[2]+phase1_costs[3]+phase1_costs[4]+phase1_costs[5]+phase1_costs[6]+phase1_costs[7]+phase1_costs[8]+phase1_costs[9]+phase1_costs[10]+phase1_costs[11]+phase1_costs[12]+phase1_costs[13]
        #Subtotal_country_adj_p1 = int(Subtotal_for_one_site*country_names[country_name][pi_rank])
        Overhead_p1 = int(Subtotal_for_one_site_p1*0.10)
        Subtotal_with_overhead_p1 = Subtotal_for_one_site_p1 + Overhead_p1
        #Total_for_all_sites_p1 = Subtotal_with_overhead_p1*no_of_sites


        phase2_c = get_cost(2,t_area)
        #after country adjustment
        phase2_costs = [int(x*country_names[country_name][pi_rank]) for x in phase2_c]
        #Additional costs for non-healthy volunteer
        if healthy_volunteer == False:
            phase2_costs = [int(x*1.05) for x in phase2_costs]
        #Additional costs for younger and older age group
        if age_group == [65,90] or [8,14] :
            phase2_costs = [int(x*1.05) for x in phase2_costs]
        #Added cost based on Number of volunteers
        #phase2_costs = [x+(enrollments*800) for x in phase2_c]

        Subtotal_for_one_site_p2 = phase2_costs[0]+phase2_costs[1]+phase2_costs[2]+phase2_costs[3]+phase2_costs[4]+phase2_costs[5]+phase2_costs[6]+phase2_costs[7]+phase2_costs[8]+phase2_costs[9]+phase2_costs[10]+phase2_costs[11]+phase2_costs[12]+phase2_costs[13]
        #Subtotal_country_adj_p2 = int(Subtotal_for_one_site*country_names[country_name][pi_rank])
        Overhead_p2 = int(Subtotal_for_one_site_p2*0.10)
        Subtotal_with_overhead_p2 = Subtotal_for_one_site_p2 + Overhead_p2
        #Total_for_all_sites_p2 = Subtotal_with_overhead_p2*no_of_sites


        phase3_c = get_cost(3,t_area)
        #after country adjustment
        phase3_costs = [int(x*country_names[country_name][pi_rank]) for x in phase3_c]
        #Additional costs for non-healthy volunteer
        if healthy_volunteer == False:
            phase3_costs = [int(x*1.05) for x in phase3_costs]
        #Additional costs for younger and older age group
        if age_group == [65,90] or [8,14] :
            phase3_costs = [int(x*1.05) for x in phase3_costs]
        #Added cost based on Number of volunteers
        #phase3_costs = [x+(enrollments*500) for x in phase3_c]

        Subtotal_for_one_site_p3 = phase3_costs[0]+phase3_costs[1]+phase3_costs[2]+phase3_costs[3]+phase3_costs[4]+phase3_costs[5]+phase3_costs[6]+phase3_costs[7]+phase3_costs[8]+phase3_costs[9]+phase3_costs[10]+phase3_costs[11]+phase3_costs[12]+phase3_costs[13]
        #Subtotal_country_adj_p3 = int(Subtotal_for_one_site*country_names[country_name][pi_rank])
        Overhead_p3 = int(Subtotal_for_one_site_p3*0.10)
        Subtotal_with_overhead_p3 = Subtotal_for_one_site_p3 + Overhead_p3

        #Total_for_all_sites_p3 = Subtotal_with_overhead_p3*no_of_sites

        #Total_cost_of_study = Total_for_all_sites_p1 + Total_for_all_sites_p2 + Total_for_all_sites_p3

        #ID,Rank of PI,Study Type,Country Name,Therapeutic Area, Sponsor , No. of sites, Req. Healthy Volunteer,Gender,Min Age, Max Age, Study Start Date, Study End Date, Duration of study, Phase 1 length, No.of volunteers, Patient Rec, Patient Retention, RN/CRA, Physician, Procedure, Central lab, Site rec, Site ret, Admin staff, Site Monitoring,Data mgmt, IRB Approval, IRB Amendment, Source data verf, Subtotal, Site overhead, Total for all sites, Phase 2 length, No.of volunteers, Patient Rec, Patient Retention, RN/CRA, Physician, Procedure, Central lab, Site rec, Site ret, Admin staff, Site Monitoring,Data mgmt, IRB Approval, IRB Amendment, Source data verf, Phase 3 length, No.of volunteers, Patient Rec, Patient Retention, RN/CRA, Physician, Procedure, Central lab, Site rec, Site ret, Admin staff, Site Monitoring,Data mgmt, IRB Approval, IRB Amendment, Source data verf, Total costs
        details_row = [id,j,pi_rank,study_type,country_name,t_area,p_company,no_of_sites,
                       healthy_volunteer,gender,age_group[0],age_group[1], start_date,end_date, study_length,
                       phase1_length,enrollments[0],phase1_costs[0],phase1_costs[1],phase1_costs[2],phase1_costs[3],phase1_costs[4],
                       phase1_costs[5],phase1_costs[6],phase1_costs[7],phase1_costs[8],phase1_costs[9],phase1_costs[10],
                       phase1_costs[11],phase1_costs[12],phase1_costs[13],Subtotal_for_one_site_p1,Overhead_p1,Subtotal_with_overhead_p1,
                       #Total_for_all_sites_p1,
                       phase2_length,enrollments[1],phase2_costs[0],phase2_costs[1],phase2_costs[2],phase2_costs[3],phase2_costs[4],
                       phase2_costs[5],phase2_costs[6],phase2_costs[7],phase2_costs[8],phase2_costs[9],phase2_costs[10],
                       phase2_costs[11],phase2_costs[12],phase2_costs[13],Subtotal_for_one_site_p2,Overhead_p2,Subtotal_with_overhead_p2,
                       #Total_for_all_sites_p2,
                       phase3_length,enrollments[2],phase3_costs[0],phase3_costs[1],phase3_costs[2],phase3_costs[3],phase3_costs[4],
                       phase3_costs[5],phase3_costs[6],phase3_costs[7],phase3_costs[8],phase3_costs[9],phase3_costs[10],
                       phase3_costs[11],phase3_costs[12],phase3_costs[13],Subtotal_for_one_site_p3,Overhead_p3,Subtotal_with_overhead_p3,
                       #Total_for_all_sites_p3,
                       #Total_cost_of_study
                       ]


        phase_1_site_total.append(Subtotal_with_overhead_p1)
        phase_2_site_total.append(Subtotal_with_overhead_p2)
        phase_3_site_total.append(Subtotal_with_overhead_p3)

        myfile = open('Generated3.csv','a')
        wr = csv.writer(myfile,quoting = csv.QUOTE_ALL)
        wr.writerow(details_row)

    for p in range(1,site_counter):
        print(sum(phase_1_site_total)+sum(phase_2_site_total)+sum(phase_3_site_total))
