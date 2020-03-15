# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:42:49 2020

@author: Sam
"""

startScript = "Welcome to the tool selection helper! The goal of this tool is to help users pick an appropriate tool from the variety of options at SNF.\n\nThere are a series of tool options listed in textboxes below. Click the button corresponding to your needs. If you do not care about the tool option or it does not describe your process (i.e. asking about ALD when you are doing CVD), leave it blank. If you do not understand the question, click the 'Help' button in blue.\n\nThe bottom textbox lists all tools which fit the requirements specified. To get the SNF wiki links and staff for each viable tool, click the green 'Get Tool Info' button."

TitM = ["Metal or Dielectric?", "Contamination Status", "Personal or SNF Source", "Conformal", "Wafer Size", "Process Gas", "Temperature", "Batch Size", "Result"]
TitD = ["Metal or Dielectric?", "Contamination Status", "Highest Temperature Allowed", "Thickness", "Si-based Dielectric Type", "ALD-Based Dielectric Type", "Wafer Size", "Substrate Type", "Batch Size", "Result"]
QsM = [["Metal", "Dielectric"], ["Clean", "Semiclean", "Gold Cont", "Clear Answer"], ["Personal/Nonstandard", "SNF/Standard", "Clear Answer"], ["Conformal/Sputter", "Vertical/Evaporated", "Angled", "Clear Answer"], ["4'' Wafer", "6'' Wafer", "Piece/Chip", "Clear Answer"], ["Need Reactive Gas", "No Reactive Gas Contamination", "Clear Answer"], ["Want Substrate Heating", "Clear Answer"], ["<5 Wafers", "<10 Wafers", "Large Batch", "Clear Answer"], [""]]
QsD = [["Metal", "Dielectric"], ["Clean", "Semiclean", "Gold Cont", "Clear Answer"], ["60-80C", "100-200C", "300-450C", "Clear Answer"], ["<5nm/very thin", ">50nm", ">2 micron", "Clear Answer"], ["Deposited SiO2", "Grown SiO2", "SiNx", "Si3N4", "Oxynitride", "Clear Answer"], ["Need ALD", "Thermal ALD", "Plasma ALD", "Clear Answer"], ["4'' Wafer", "6'' Wafer", "Piece/Chip", "Clear Answer"], ["Si", "GaAs/III-V", "Clear Answer"], ["<5 Wafers", "<10 Wafers", "Large Batch", "Clear Answer"], [""]]

counter = 0
names = {
  "no match": "",
  "aja": ['Xiaoqing Xu', 'Graham Ewing', 'https://snfexfab.stanford.edu/equipment/aja-evaporator-aja-evap', 'https://snf.stanford.edu/SNF/equipment/metalization-sputtering/evaporation/aja-evaporator/aja-evaporator'],
  "aja-evap": ['aja'],
  "aja evap": ['aja'],
  "aja evaporator":['aja'],
  "lesker": ['lesker-sputter'],
  "lesker-sputter": ['Maurice Stevens', 'Carsen Kline', 'https://snfexfab.stanford.edu/equipment/lesker-sputter-lesker-sputter', 'https://snf.stanford.edu/SNF/equipment/metalization-sputtering/sputtering/lesker-sputter'],
  "lesker sputter": ['lesker-sputter'],
  "innotec":['Maurice Stevens', 'Jim Haydon', 'https://snfexfab.stanford.edu/equipment/innotec-evaporator-innotec', 'https://snf.stanford.edu/SNF/equipment/metalization-sputtering/evaporation/innotec-es26c-e-beam-evaporator-1'],
  "innotec-evap":['innotec'],
  "innotec_evap":['innotec'],
  "innotec evap":['innotec'],
  "innotec evaporator":['innotec'],
  "intlvac_evap":['intlvac evap'],
  "intlvac evap":['Maurice Stevens', 'Jim Haydon', 'https://snfexfab.stanford.edu/equipment/intlvac-evaporation-intlvacevap', 'https://snf.stanford.edu/SNF/equipment/metalization-sputtering/evaporation/equipment-template?searchterm=intl'],
  "intlvac evaporator":['intlvac evap'],
  "intlvac-evap":['intlvac evap'],
  "intlvac_sputter":['intlvac sputter'],
  "intlvac sputter":['Maurice Stevens', 'Jim Haydon', 'https://snfexfab.stanford.edu/equipment/intlvac-sputter-intlvacsputter', 'https://snf.stanford.edu/SNF/equipment/metalization-sputtering/sputtering/intlvac_sputter?searchterm=intlv'],
  "intlvac-sputter":['intlvac sputter'],
  "metalica":['Xiaoqing Xu', 'Jim Haydon', 'https://snfexfab.stanford.edu/equipment/metalica-sputter-metalica', 'https://snf.stanford.edu/SNF/equipment/metalization-sputtering/sputtering/metallica-sputter-system'],
  "metallica":['metalica'],
  "metallica-sputter":['metalica'],
  "ccp-dep":['Usha Raghuram', 'Elmer Enriquez', 'https://snfexfab.stanford.edu/equipment/plasmatherm-shuttlelock-pecvd-system-ccp-dep', 'https://snf.stanford.edu/SNF/equipment/chemical-vapor-deposition/pecvd/plasmatherm-ccp-dep'],
  "ccp dep":['ccp-dep'],
  "ccp":['ccp-dep'],
  "hdpcvd":['Usha Raghuram', 'Elmer Enriquez', 'https://snfexfab.stanford.edu/equipment/plasmatherm-versaline-hdp-cvd-system-hdpcvd', 'https://snf.stanford.edu/SNF/equipment/chemical-vapor-deposition/pecvd/plasmatherm-versaline-hdpcvd?searchterm=hdpcvd'],
  "hdp":['hdpcvd'],
  "sts":['Usha Raghuram', 'Jim Haydon', 'https://snfexfab.stanford.edu/equipment/sts-plasma-enhanced-cvd-sts', 'https://snf.stanford.edu/SNF/equipment/chemical-vapor-deposition/pecvd/sts-pecvd-tool?searchterm=sts'],
  "fiji":['fiji1'],
  "fiji1":['Michelle Rincon', 'Mike Dickey', 'https://snfexfab.stanford.edu/equipment/fiji-1-fiji1', 'https://docs.google.com/document/d/e/2PACX-1vR18yXWnh6r5DEABuISeMmLAIBdB5AXgxeFAw9lGIETTP1KZGuEkuX-OH7CSxoM9I2AjDX6cydg94Jw/pub'],
  "fiji2":['Michelle Rincon', 'Mike Dickey', 'https://snfexfab.stanford.edu/equipment/fiji-2-fiji2', 'https://docs.google.com/document/d/e/2PACX-1vTvYMnl5Pogh2vroWCvoB4_UlZ-sJk1fUp9b17leHPsii6sBcYETSAyvL4XqOku3VXByB0qJot-fn4i/pub'],
  "fiji3":['Michelle Rincon', 'Mike Dickey', 'https://snfexfab.stanford.edu/equipment/fiji-3-fiji3', 'https://docs.google.com/document/d/e/2PACX-1vTtgX7jJZKntj5vfmCHY2_h3lArzzs2pIAO3uFcS579hj24P6WCLS4XGBsmmx0qTV9sJDVgqeFweZYa/pub'],
  "fiji 1":['fiji1'],
  "fiji 2":['fiji2'],
  "fiji 3":['fiji3'],
  "savannah":['Michelle Rincon', 'Jim Haydon', 'https://snfexfab.stanford.edu/equipment/savannah-savannah', 'https://docs.google.com/document/d/e/2PACX-1vTvCFLsnoevcD5Tr1a3QSYGUH48qGJlh7XcBRCdLg7BaQvSMzq7SayDFys_1T9XWjVee0EjilT0NIpU/pub'],
  "mvd":['Michelle Rincon', 'Jim Haydon', 'https://snfexfab.stanford.edu/equipment/training/mvd-training', 'https://docs.google.com/document/d/e/2PACX-1vTdduthyiw9TQMLOHAbBaG8QvCaOtiIaFaExtvkJQ4Vdss1md4AzNwar8DM8NIMQ8s0X_gdVr4V-C7A/pub'],
  "tylanbpsg":['Maurice Stevens', 'Ray Seymour', 'https://snfexfab.stanford.edu/equipment/tylanbpsg-tylanbpsg', 'https://snf.stanford.edu/SNF/equipment/annealing-oxidation-doping/furnaces/furnaces-forming-gas-anneal-fga-tylanfga-and-fga2/tylanfga-semi-clean?searchterm=tylan'],
  "tylan bpsg":['tylanbpsg'],
  "tylan fga":['tylanbpsg'],
  "fylanfga":['tylanbpsg'],
  "tylan9":['Maurice Stevens', 'Ray Seymour', 'https://snfexfab.stanford.edu/equipment/tylan9-tylan9', 'https://docs.google.com/document/u/1/d/e/2PACX-1vTS9ojlrOLMCEDBKe7Q0QYmyG0uUzUZvHjDPKgEwjKJrYPJmgdWnWETl9qvaFt_SfgPXnTCBi5gtodY/pub'],
  "tylan 9":['tylan9'],
  "thermconitride1":['Maurice Stevens', 'Ray Seymour', 'https://snfexfab.stanford.edu/equipment/thermconitride-thermconitride1', 'https://snf.stanford.edu/SNF/equipment/annealing-oxidation-doping/furnaces/thermco-oxidation-and-annealing-furnaces-thermco1?searchterm=thermco', 'https://snf.stanford.edu/SNF/equipment/annealing-oxidation-doping/furnaces/thermco-oxidation-and-annealing-furnaces-thermco1?searchterm=thermco'],
  "thermconitride":['thermconitride1'],
  "thermcopoly":['Maurice Stevens', 'Ray Seymour', 'https://snfexfab.stanford.edu/equipment/training/thermco-poly-deposition-furnace-training', 'https://snf.stanford.edu/SNF/equipment/chemical-vapor-deposition/low-pressure-cvd/thermcopoly-1/thermcopoly?searchterm=thermcopo'],
  "thermcopoly1":['Maurice Stevens', 'Ray Seymour', 'https://snfexfab.stanford.edu/equipment/training/thermco-poly-deposition-furnace-training', 'https://snf.stanford.edu/SNF/equipment/chemical-vapor-deposition/low-pressure-cvd/thermcopoly-1/thermcopoly?searchterm=thermcopo'],
  "thermcopoly2":['Maurice Stevens', 'Ray Seymour', 'https://snfexfab.stanford.edu/equipment/training/thermco-poly-deposition-furnace-training', 'https://docs.google.com/document/d/e/2PACX-1vRi7GJwGjHiUhJuFEOK17HDgf115XYAmJeEtyq-MwL2_Oz5r4bTDgHmKc3VtUKAUUwhgdxbQnExVlis/pub'],
  "thermcolto":['Maurice Stevens', 'Ray Seymour', 'https://snfexfab.stanford.edu/equipment/thermcolto-thermcolto', 'https://snf.stanford.edu/SNF/equipment/annealing-oxidation-doping/furnaces/thermco-oxidation-and-annealing-furnaces-thermco1?searchterm=thermco'],
  "thermco4":['thermcolto']
}

#["Metal", "Dielectric", "Both"], ["Clean", "Semiclean", "Contaminated", "Clear Answer"], 
#["Personal/Nonstandard", "SNF/Standard", "Clear Answer"], ["Conformal", "Vertical", "Angled", "Clear Answer"],
# ["4'' Wafer", "6'' Wafer", "Piece/Chip", "Clear Answer"], ["Need Reactive Gas", "No Reactive Gas Contamination", "Clear Answer"],
# ["Want Substrate Heating", "Clear Answer"], ["<=5 Wafers", "<=10 Wafers", "Large Batch", "Clear Answer"]
metalKey = {"aja":
            [[-1, 0, 2], [-1, 2],
             [-1, 1], [-1, 1], 
             [-1, 0, 1, 2], [-1, 1],
             [-1], [-1, 0, 1]],
        "lesker":
            [[-1, 0, 2], [-1, 2],
             [-1, 0, 1], [-1, 0], 
             [-1, 0, 1, 2], [-1, 0],
             [-1, 0], [-1, 0]],
        "innotec":
            [[-1, 0], [-1, 2],
             [-1, 0, 1], [-1, 1, 2],
             [-1, 0, 2], [-1, 1],
             [-1], [-1, 0, 1, 2]],
        "intlvac evaporator":
            [[-1, 0], [-1, 0, 1],
             [-1, 0], [-1, 1, 2],
             [-1, 0, 1, 2], [-1, 1],
             [-1], [-1, 0, 1, 2]],
        "intlvac sputter":
            [[-1 ,0], [-1, 0, 1],
             [-1, 0, 1], [-1, 0],
             [-1, 0], [-1, 0],
             [-1], [-1, 0, 1, 2]]
        }
#QsD = [["Metal", "Dielectric", "Both"], ["Clean", "Semiclean", "Gold Contaminated", "Clear Answer"],
    #["60-80C", "100-200C", "300-450C", "Clear Answer"], ["<5nm, >50nm", ">2 micron", "Clear Answer"], 
    #["Glovebox", "Oxynitride"], ["4'' Wafer", "6'' Wafer", "Piece/Chip", "Clear Answer"], ["Si", "GaAs/III-V"]
    #["Need Highly Conformal, thermal, plasma"], ["<5 Wafers", "<10 Wafers", "Large Batch", "Clear Answer"], [""]]

DiKey = {
        "ccp-dep":[[-1, 1], [-1, 0, 1, 2], 
                   [-1, 2], [-1, 1, 2],
                   [-1], [-1, 0, 1, 2],
                   [-1] ,[-1, 0, 1]],
        "hdpcvd":[[-1, 1], [-1, 0, 1, 2],
                  [-1, 0, 1, 2], [-1, 1, 2],
                  [-1], [-1, 0],
                  [-1], [-1, 0]],
        "sts":[[-1, 1], [-1, 2], 
               [-1, 2], [-1, 1, 2], 
               [-1, 1], [-1, 0, 1, 2],
               [-1], [-1, 0, 1]],
        "fiji1":[[-1, 1],[-1, 1],
                 [-1, 0, 1, 2], [-1, 0],
                 [-1], [-1, 0, 1, 2],
                 [-1, 0, 1, 2], [-1, 0]],
        "fiji2":[[-1, 1],[-1, 1, 2],
                 [-1, 0, 1, 2], [-1, 0],
                 [-1], [-1, 0, 1, 2],
                 [-1, 0, 1, 2], [-1, 0]],
        "fiji3":[[-1, 1],[-1, 2],
                 [-1, 0, 1, 2], [-1, 0],
                 [-1], [-1, 0, 1, 2],
                 [-1, 0, 1, 2], [-1, 0]],
        "savannah":[[-1, 1],[-1, 2],
                    [-1, 1, 2], [-1, 0],
                    [-1],[-1, 0, 1, 2],
                    [-1, 0, 1], [-1, 0]],
        "mvd":[[-1, 1],[-1, 2],
                    [-1, 1, 2], [-1, 0],
                    [-1, 0, 1],[-1, 0, 1, 2],
                    [-1, 0], [-1, 0]],
#QsD = [["Metal", "Dielectric", "Both"], ["Clean", "Semiclean", "Gold Contaminated", "Clear Answer"],
    #["60-80C", "100-200C", "300-450C", "Clear Answer"], ["<5nm, >50nm", ">2 micron", "Clear Answer"], 
    #["Glovebox", "Oxynitride", "Stoichiometric Nitride"], ["4'' Wafer", "6'' Wafer", "Piece/Chip", "Clear Answer"], 
    #["Need Highly Conformal"], ["<5 Wafers", "<10 Wafers", "Large Batch", "Clear Answer"], [""]]
        "tylanbpsg":[[-1, 1],[-1, 1],
                      [-1, 2], [-1, 1],
                      [-1], [-1, 0],
                      [-1], [-1, 0, 1, 2]],
        "tylan9":[[-1, 1], [-1, 2],
                  [-1], [-1, 1],
                  [-1], [-1, 0],
                  [-1], [-1, 0, 1, 2]],
        "thermconitride1":[[-1, 1], [-1, 0],
                           [-1], [-1, 1],
                           [-1, 2], [-1, 0, 1],
                           [-1], [-1, 0, 1, 2]],
        "thermcopoly":[[-1, 1], [-1, 0],
                       [-1], [-1, 1],
                       [-1], [-1, 0, 1],
                       [-1], [-1, 0, 1, 2]],
        'thermcopoly2':[[-1, 1],[-1, 2],
                        [-1], [-1, 1],
                       [-1], [-1, 0, 1],
                       [-1], [-1, 0, 1, 2]],
        "thermcolto":[[-1, 1],[-1, 1, 2],
                      [-1, 2], [-1, 1],
                      [-1], [-1, 0],
                      [-1], [-1, 0, 1, 2]]
        }

DHelp = [""]*len(TitD)
DHelp[1] = "SNF classifies tools as clean, semi-clean, or gold contaminated. Once a clean wafer is placed in a gold contaminated tool, it is considered gold contaminated and cannot be placed back in a clean tool. Make sure you design your process such that any gold contaminated processing steps happen at the end."
DHelp[2] = "Select the maximum temperature which will not damage other layers on your substrate. If you can take very high temperature, simply leave this prompt blank. 60-80C corresponds to the temperature of plasma-enhanced ALD, barely above room temperature. 100-200C is for high density plasma plasma-enhanced CVD processes. Standard plasma-enhanced CVD occurs from 300-450C. The furnaces for low pressure CVD and oxide growth are largely above this range, approaching 1000C."
DHelp[3] = "If you need a continuous film that is <5nm, you likely need ALD. However, ALD is slow and cannot be done at SNF for layers above 50nm. Oxide cannot be grown for very thick layers, although both LPCVD and PECVD can deposit multiple micron-thick layers."
DHelp[4] = "CVD tools largely deposit silicon oxide or silicon nitride. The plasma enhanced CVD tools (PECVD) tend to deposit slightly lower quality oxide and not stoichiometric nitride. However, it is done at lower temperature and the resulting film can be tuned more without dopants. Furnaces can be used for oxide growth in exisiting silicon and stoichiometric nitride."
DHelp[6] = "Some wafer holders cannot accomodate 6'' wafers, and pieces often must be attached to 4'' wafers for loadlock systems or ALD tools with gas flow."
DHelp[5] = "If you need a highly conformal or non-silicon based dielectric film, you likely need ALD.\n\nPlasma enhanced ALD processes occur at lower temperature and can be used for non-oxides. However, at SNF those are the Fiji tools which also have a finnicky transfer arm, fail more often, and are harder to get time on. If you do not have a preference but know you need ALD, choose the more general first option."
DHelp[7] = "Many tools, in particular ones which go to high temperature and must be concerned with contamination, do not allow non-Si substrates. SiO2 or SiNx coated wafers can be treated as Si for the purpose of this question. GaAs is the most common non-Si or oxide substrate used at SNF."
DHelp[8] = "The ALD tools are slow and can only take 1-2 wafers at a time. Therefore large throughput processes are not good fits for ALD. The high density PECVD tools also only process one wafer at a time. There are PECVD tools which can handle 3-4 wafers at a time and are appropriate for moderate-sized batches. Once a user is processiing 20 or more wafers, only the full-cassette processing furnace-based tools are appropriate."
MHelp = [""]*len(TitM)
MHelp[1] = "SNF classifies tools as clean, semi-clean, or gold-contaminated. Most metal deposition tools are gold contaminated, but some are semi-clean or clean and can be used to deposit non-gold metals. Once a clean wafer is put in a gold-contaminated tool, it is considered gold-contaminated and cannot go in a clean tool again."
MHelp[2] = "Some tools have a small list of materials which can be deposited. These are usually the high use tools with loadlock systems or clean systems. Lower use tools or bell jar systems with deposition chambers that are opened each time a user deposits usually are easier to clean and allow for more experimentation. If you think you will be the only person at SNF depositing this material, it will likely be a personal source."
MHelp[3] = "Sputtering tools coat all surfaces on the top side of the deposited material or are conformal. Sputtering therefore can cover sidewalls or steps in the substrate, connecting layers and making liftoff more difficult.\n\nEvaporation deposits the material vertically on the substrate. The deposited material therefore will only be continuous across flat surfaces. If you need to evaporate and have the material cover a step, the substrate must be placed at an angle. However, the angling tool and the tilted substrate itself makes the susbtrate tall and so angled evaporation cannot generally be done in loadlock systems."
MHelp[4] = "Many tools have wafer holders. On some tools, those wafer holders work for a variety of wafer sizes or wafer holders can be swapped out. For some tools, chips will need to be mounted onto 4'' wafers."
MHelp[5] = "It is often useful to add in a reactive gas like O2 or N2 to deposit a nitride or oxide. Even if the target being deposited begins as an oxide, with the heat of deposition additional reactive gas must often be added. Generally sputtering tools allow for reactive gasses and evaporating tools do not."
MHelp[6] = "The Lesker sputterer allows the substrate to be heated to change adhesion and film properties."
MHelp[7] = "Some loadlock systems (like the Lesker sputterer) can only take one wafer at a time. This makes batches of >5 wafers take a long time on a high demand tool. Other loadlock systems like the AJA allow for 3 wafers at a time, making approximately 10 wafer tasks feasible. The large bell jar-syle systems can generally handle 20-30 wafers at a time and should be used for large batches."