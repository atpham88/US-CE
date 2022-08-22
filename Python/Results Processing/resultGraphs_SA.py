
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from capacityInvestments_SA import *
from costs_SA import *
import altair as alt
from textwrap import wrap

# %% Reference:
def main():
    ref_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results\\"
    # Capacity Expansion:
    (CoalCCS_NE2020_ref_EI, CCCCS_NE2020_ref_EI, CC_NE2020_ref_EI, Nuclear_NE2020_ref_EI, Hydrogen_NE2020_ref_EI,Battery_NE2020_ref_EI,
     DAC_NE2020_ref_EI, Wind_NE2020_ref_EI, Solar_NE2020_ref_EI, CoalCCS_NE2020_ref_EI_2, CCCCS_NE2020_ref_EI_2, CC_NE2020_ref_EI_2,
     Nuclear_NE2020_ref_EI_2, Hydrogen_NE2020_ref_EI_2,Battery_NE2020_ref_EI_2, DAC_NE2020_ref_EI_2, Wind_NE2020_ref_EI_2,
     Solar_NE2020_ref_EI_2) = capInvestments(ref_dir, techCase='Reference', planningScr='NE2020', interConn = 'EI', elec=True)
    (CoalCCS_NE2050_ref_EI, CCCCS_NE2050_ref_EI, CC_NE2050_ref_EI, Nuclear_NE2050_ref_EI, Hydrogen_NE2050_ref_EI,Battery_NE2050_ref_EI,
     DAC_NE2050_ref_EI, Wind_NE2050_ref_EI, Solar_NE2050_ref_EI, CoalCCS_NE2050_ref_EI_2, CCCCS_NE2050_ref_EI_2, CC_NE2050_ref_EI_2,
     Nuclear_NE2050_ref_EI_2, Hydrogen_NE2050_ref_EI_2,Battery_NE2050_ref_EI_2, DAC_NE2050_ref_EI_2, Wind_NE2050_ref_EI_2,
     Solar_NE2050_ref_EI_2) = capInvestments(ref_dir, techCase='Reference', planningScr='NE2050', interConn = 'EI', elec=True)

    (CoalCCS_NE2020_ref_ERCOT, CCCCS_NE2020_ref_ERCOT, CC_NE2020_ref_ERCOT, Nuclear_NE2020_ref_ERCOT, Hydrogen_NE2020_ref_ERCOT,Battery_NE2020_ref_ERCOT,
     DAC_NE2020_ref_ERCOT, Wind_NE2020_ref_ERCOT, Solar_NE2020_ref_ERCOT, CoalCCS_NE2020_ref_ERCOT_2, CCCCS_NE2020_ref_ERCOT_2,
     CC_NE2020_ref_ERCOT_2, Nuclear_NE2020_ref_ERCOT_2, Hydrogen_NE2020_ref_ERCOT_2,Battery_NE2020_ref_ERCOT_2,
     DAC_NE2020_ref_ERCOT_2, Wind_NE2020_ref_ERCOT_2, Solar_NE2020_ref_ERCOT_2) = capInvestments(ref_dir, techCase='Reference', planningScr='NE2020', interConn = 'ERCOT', elec=True)
    (CoalCCS_NE2050_ref_ERCOT, CCCCS_NE2050_ref_ERCOT, CC_NE2050_ref_ERCOT, Nuclear_NE2050_ref_ERCOT, Hydrogen_NE2050_ref_ERCOT,Battery_NE2050_ref_ERCOT,
     DAC_NE2050_ref_ERCOT, Wind_NE2050_ref_ERCOT, Solar_NE2050_ref_ERCOT, CoalCCS_NE2050_ref_ERCOT_2, CCCCS_NE2050_ref_ERCOT_2, CC_NE2050_ref_ERCOT_2, Nuclear_NE2050_ref_ERCOT_2, Hydrogen_NE2050_ref_ERCOT_2,Battery_NE2050_ref_ERCOT_2,
     DAC_NE2050_ref_ERCOT_2, Wind_NE2050_ref_ERCOT_2, Solar_NE2050_ref_ERCOT_2) = capInvestments(ref_dir, techCase='Reference', planningScr='NE2050', interConn = 'ERCOT', elec=True)

    (CoalCCS_NE2020_lh2_EI, CCCCS_NE2020_lh2_EI, CC_NE2020_lh2_EI, Nuclear_NE2020_lh2_EI, Hydrogen_NE2020_lh2_EI, Battery_NE2020_lh2_EI,
     DAC_NE2020_lh2_EI, Wind_NE2020_lh2_EI, Solar_NE2020_lh2_EI, CoalCCS_NE2020_lh2_EI_2, CCCCS_NE2020_lh2_EI_2, CC_NE2020_lh2_EI_2,
     Nuclear_NE2020_lh2_EI_2, Hydrogen_NE2020_lh2_EI_2, Battery_NE2020_lh2_EI_2, DAC_NE2020_lh2_EI_2, Wind_NE2020_lh2_EI_2,
     Solar_NE2020_lh2_EI_2) = capInvestments(ref_dir, techCase='No H2', planningScr='NE2020', interConn='EI', elec=True)
    (CoalCCS_NE2050_lh2_EI, CCCCS_NE2050_lh2_EI, CC_NE2050_lh2_EI, Nuclear_NE2050_lh2_EI, Hydrogen_NE2050_lh2_EI, Battery_NE2050_lh2_EI,
     DAC_NE2050_lh2_EI, Wind_NE2050_lh2_EI, Solar_NE2050_lh2_EI, CoalCCS_NE2050_lh2_EI_2, CCCCS_NE2050_lh2_EI_2, CC_NE2050_lh2_EI_2,
     Nuclear_NE2050_lh2_EI_2, Hydrogen_NE2050_lh2_EI_2, Battery_NE2050_lh2_EI_2, DAC_NE2050_lh2_EI_2, Wind_NE2050_lh2_EI_2,
     Solar_NE2050_lh2_EI_2) = capInvestments(ref_dir, techCase='No H2', planningScr='NE2050', interConn='EI', elec=True)

    (CoalCCS_NE2020_lh2_ERCOT, CCCCS_NE2020_lh2_ERCOT, CC_NE2020_lh2_ERCOT, Nuclear_NE2020_lh2_ERCOT, Hydrogen_NE2020_lh2_ERCOT, Battery_NE2020_lh2_ERCOT,
     DAC_NE2020_lh2_ERCOT, Wind_NE2020_lh2_ERCOT, Solar_NE2020_lh2_ERCOT, CoalCCS_NE2020_lh2_ERCOT_2, CCCCS_NE2020_lh2_ERCOT_2, CC_NE2020_lh2_ERCOT_2,
     Nuclear_NE2020_lh2_ERCOT_2, Hydrogen_NE2020_lh2_ERCOT_2, Battery_NE2020_lh2_ERCOT_2, DAC_NE2020_lh2_ERCOT_2, Wind_NE2020_lh2_ERCOT_2,
     Solar_NE2020_lh2_ERCOT_2) = capInvestments(ref_dir, techCase='No H2', planningScr='NE2020', interConn='ERCOT', elec=True)
    (CoalCCS_NE2050_lh2_ERCOT, CCCCS_NE2050_lh2_ERCOT, CC_NE2050_lh2_ERCOT, Nuclear_NE2050_lh2_ERCOT, Hydrogen_NE2050_lh2_ERCOT, Battery_NE2050_lh2_ERCOT,
     DAC_NE2050_lh2_ERCOT, Wind_NE2050_lh2_ERCOT, Solar_NE2050_lh2_ERCOT, CoalCCS_NE2050_lh2_ERCOT_2, CCCCS_NE2050_lh2_ERCOT_2, CC_NE2050_lh2_ERCOT_2,
     Nuclear_NE2050_lh2_ERCOT_2, Hydrogen_NE2050_lh2_ERCOT_2, Battery_NE2050_lh2_ERCOT_2, DAC_NE2050_lh2_ERCOT_2, Wind_NE2050_lh2_ERCOT_2,
     Solar_NE2050_lh2_ERCOT_2) = capInvestments(ref_dir, techCase='No H2', planningScr='NE2050', interConn='ERCOT', elec=True)

    (CoalCCS_NE2020_he_EI, CCCCS_NE2020_he_EI, CC_NE2020_he_EI, Nuclear_NE2020_he_EI, Hydrogen_NE2020_he_EI, Battery_NE2020_he_EI,
     DAC_NE2020_he_EI, Wind_NE2020_he_EI, Solar_NE2020_he_EI, CoalCCS_NE2020_he_EI_2, CCCCS_NE2020_he_EI_2, CC_NE2020_he_EI_2,
     Nuclear_NE2020_he_EI_2, Hydrogen_NE2020_he_EI_2, Battery_NE2020_he_EI_2, DAC_NE2020_he_EI_2, Wind_NE2020_he_EI_2,
     Solar_NE2020_he_EI_2) = capInvestments(ref_dir, techCase='Reference', planningScr='NE2020', interConn='EI', elec=False)
    (CoalCCS_NE2050_he_EI, CCCCS_NE2050_he_EI, CC_NE2050_he_EI, Nuclear_NE2050_he_EI, Hydrogen_NE2050_he_EI, Battery_NE2050_he_EI,
     DAC_NE2050_he_EI, Wind_NE2050_he_EI, Solar_NE2050_he_EI, CoalCCS_NE2050_he_EI_2, CCCCS_NE2050_he_EI_2, CC_NE2050_he_EI_2,
     Nuclear_NE2050_he_EI_2, Hydrogen_NE2050_he_EI_2, Battery_NE2050_he_EI_2, DAC_NE2050_he_EI_2, Wind_NE2050_he_EI_2,
     Solar_NE2050_he_EI_2) = capInvestments(ref_dir, techCase='Reference', planningScr='NE2050', interConn='EI', elec=False)

    (CoalCCS_NE2020_he_ERCOT, CCCCS_NE2020_he_ERCOT, CC_NE2020_he_ERCOT, Nuclear_NE2020_he_ERCOT, Hydrogen_NE2020_he_ERCOT, Battery_NE2020_he_ERCOT,
     DAC_NE2020_he_ERCOT, Wind_NE2020_he_ERCOT, Solar_NE2020_he_ERCOT, CoalCCS_NE2020_he_ERCOT_2, CCCCS_NE2020_he_ERCOT_2,
     CC_NE2020_he_ERCOT_2, Nuclear_NE2020_he_ERCOT_2, Hydrogen_NE2020_he_ERCOT_2, Battery_NE2020_he_ERCOT_2,
     DAC_NE2020_he_ERCOT_2, Wind_NE2020_he_ERCOT_2, Solar_NE2020_he_ERCOT_2) = capInvestments(ref_dir, techCase='Reference', planningScr='NE2020', interConn='ERCOT', elec=False)
    (CoalCCS_NE2050_he_ERCOT, CCCCS_NE2050_he_ERCOT, CC_NE2050_he_ERCOT, Nuclear_NE2050_he_ERCOT, Hydrogen_NE2050_he_ERCOT, Battery_NE2050_he_ERCOT,
     DAC_NE2050_he_ERCOT, Wind_NE2050_he_ERCOT, Solar_NE2050_he_ERCOT, CoalCCS_NE2050_he_ERCOT_2, CCCCS_NE2050_he_ERCOT_2, CC_NE2050_he_ERCOT_2, Nuclear_NE2050_he_ERCOT_2,
     Hydrogen_NE2050_he_ERCOT_2, Battery_NE2050_he_ERCOT_2, DAC_NE2050_he_ERCOT_2, Wind_NE2050_he_ERCOT_2,
     Solar_NE2050_he_ERCOT_2) = capInvestments(ref_dir, techCase='Reference', planningScr='NE2050', interConn='ERCOT', elec=False)

    (CoalCCS_NE2020_lccs_EI, CCCCS_NE2020_lccs_EI, CC_NE2020_lccs_EI, Nuclear_NE2020_lccs_EI, Hydrogen_NE2020_lccs_EI, Battery_NE2020_lccs_EI,
     DAC_NE2020_lccs_EI, Wind_NE2020_lccs_EI, Solar_NE2020_lccs_EI, CoalCCS_NE2020_lccs_EI_2, CCCCS_NE2020_lccs_EI_2, CC_NE2020_lccs_EI_2,
     Nuclear_NE2020_lccs_EI_2, Hydrogen_NE2020_lccs_EI_2, Battery_NE2020_lccs_EI_2, DAC_NE2020_lccs_EI_2, Wind_NE2020_lccs_EI_2,
     Solar_NE2020_lccs_EI_2) = capInvestments(ref_dir, techCase='No CCS', planningScr='NE2020', interConn='EI', elec=True)
    (CoalCCS_NE2050_lccs_EI, CCCCS_NE2050_lccs_EI, CC_NE2050_lccs_EI, Nuclear_NE2050_lccs_EI, Hydrogen_NE2050_lccs_EI, Battery_NE2050_lccs_EI,
     DAC_NE2050_lccs_EI, Wind_NE2050_lccs_EI, Solar_NE2050_lccs_EI, CoalCCS_NE2050_lccs_EI_2, CCCCS_NE2050_lccs_EI_2, CC_NE2050_lccs_EI_2,
     Nuclear_NE2050_lccs_EI_2, Hydrogen_NE2050_lccs_EI_2, Battery_NE2050_lccs_EI_2, DAC_NE2050_lccs_EI_2, Wind_NE2050_lccs_EI_2,
     Solar_NE2050_lccs_EI_2) = capInvestments(ref_dir, techCase='No CCS', planningScr='NE2050', interConn='EI', elec=True)

    (CoalCCS_NE2020_lccs_ERCOT, CCCCS_NE2020_lccs_ERCOT, CC_NE2020_lccs_ERCOT, Nuclear_NE2020_lccs_ERCOT, Hydrogen_NE2020_lccs_ERCOT, Battery_NE2020_lccs_ERCOT,
     DAC_NE2020_lccs_ERCOT, Wind_NE2020_lccs_ERCOT, Solar_NE2020_lccs_ERCOT, CoalCCS_NE2020_lccs_ERCOT_2, CCCCS_NE2020_lccs_ERCOT_2,
     CC_NE2020_lccs_ERCOT_2, Nuclear_NE2020_lccs_ERCOT_2, Hydrogen_NE2020_lccs_ERCOT_2, Battery_NE2020_lccs_ERCOT_2,
     DAC_NE2020_lccs_ERCOT_2, Wind_NE2020_lccs_ERCOT_2, Solar_NE2020_lccs_ERCOT_2) = capInvestments(ref_dir, techCase='No CCS', planningScr='NE2020', interConn='ERCOT', elec=True)
    (CoalCCS_NE2050_lccs_ERCOT, CCCCS_NE2050_lccs_ERCOT, CC_NE2050_lccs_ERCOT, Nuclear_NE2050_lccs_ERCOT, Hydrogen_NE2050_lccs_ERCOT, Battery_NE2050_lccs_ERCOT,
     DAC_NE2050_lccs_ERCOT, Wind_NE2050_lccs_ERCOT, Solar_NE2050_lccs_ERCOT, CoalCCS_NE2050_lccs_ERCOT_2, CCCCS_NE2050_lccs_ERCOT_2, CC_NE2050_lccs_ERCOT_2, Nuclear_NE2050_lccs_ERCOT_2,
     Hydrogen_NE2050_lccs_ERCOT_2, Battery_NE2050_lccs_ERCOT_2, DAC_NE2050_lccs_ERCOT_2, Wind_NE2050_lccs_ERCOT_2,
     Solar_NE2050_lccs_ERCOT_2) = capInvestments(ref_dir, techCase='No CCS', planningScr='NE2050', interConn='ERCOT', elec=True)

    (CoalCCS_NE2020_ltrans_EI, CCCCS_NE2020_ltrans_EI, CC_NE2020_ltrans_EI, Nuclear_NE2020_ltrans_EI, Hydrogen_NE2020_ltrans_EI, Battery_NE2020_ltrans_EI,
     DAC_NE2020_ltrans_EI, Wind_NE2020_ltrans_EI, Solar_NE2020_ltrans_EI, CoalCCS_NE2020_ltrans_EI_2, CCCCS_NE2020_ltrans_EI_2, CC_NE2020_ltrans_EI_2,
     Nuclear_NE2020_ltrans_EI_2, Hydrogen_NE2020_ltrans_EI_2, Battery_NE2020_ltrans_EI_2, DAC_NE2020_ltrans_EI_2, Wind_NE2020_ltrans_EI_2,
     Solar_NE2020_ltrans_EI_2) = capInvestments(ref_dir, techCase='L Trans', planningScr='NE2020', interConn='EI', elec=True)
    (CoalCCS_NE2050_ltrans_EI, CCCCS_NE2050_ltrans_EI, CC_NE2050_ltrans_EI, Nuclear_NE2050_ltrans_EI, Hydrogen_NE2050_ltrans_EI, Battery_NE2050_ltrans_EI,
     DAC_NE2050_ltrans_EI, Wind_NE2050_ltrans_EI, Solar_NE2050_ltrans_EI, CoalCCS_NE2050_ltrans_EI_2, CCCCS_NE2050_ltrans_EI_2, CC_NE2050_ltrans_EI_2,
     Nuclear_NE2050_ltrans_EI_2, Hydrogen_NE2050_ltrans_EI_2, Battery_NE2050_ltrans_EI_2, DAC_NE2050_ltrans_EI_2, Wind_NE2050_ltrans_EI_2,
     Solar_NE2050_ltrans_EI_2) = capInvestments(ref_dir, techCase='L Trans', planningScr='NE2050', interConn='EI', elec=True)

    (CoalCCS_NE2020_ltrans_ERCOT, CCCCS_NE2020_ltrans_ERCOT, CC_NE2020_ltrans_ERCOT, Nuclear_NE2020_ltrans_ERCOT, Hydrogen_NE2020_ltrans_ERCOT, Battery_NE2020_ltrans_ERCOT,
     DAC_NE2020_ltrans_ERCOT, Wind_NE2020_ltrans_ERCOT, Solar_NE2020_ltrans_ERCOT, CoalCCS_NE2020_ltrans_ERCOT_2, CCCCS_NE2020_ltrans_ERCOT_2,
     CC_NE2020_ltrans_ERCOT_2, Nuclear_NE2020_ltrans_ERCOT_2, Hydrogen_NE2020_ltrans_ERCOT_2, Battery_NE2020_ltrans_ERCOT_2,
     DAC_NE2020_ltrans_ERCOT_2, Wind_NE2020_ltrans_ERCOT_2, Solar_NE2020_ltrans_ERCOT_2) = capInvestments(ref_dir, techCase='L Trans', planningScr='NE2020', interConn='ERCOT', elec=True)
    (CoalCCS_NE2050_ltrans_ERCOT, CCCCS_NE2050_ltrans_ERCOT, CC_NE2050_ltrans_ERCOT, Nuclear_NE2050_ltrans_ERCOT, Hydrogen_NE2050_ltrans_ERCOT, Battery_NE2050_ltrans_ERCOT,
     DAC_NE2050_ltrans_ERCOT, Wind_NE2050_ltrans_ERCOT, Solar_NE2050_ltrans_ERCOT, CoalCCS_NE2050_ltrans_ERCOT_2, CCCCS_NE2050_ltrans_ERCOT_2, CC_NE2050_ltrans_ERCOT_2, Nuclear_NE2050_ltrans_ERCOT_2,
     Hydrogen_NE2050_ltrans_ERCOT_2, Battery_NE2050_ltrans_ERCOT_2, DAC_NE2050_ltrans_ERCOT_2,
     Wind_NE2050_ltrans_ERCOT_2, Solar_NE2050_ltrans_ERCOT_2) = capInvestments(ref_dir, techCase='L Trans', planningScr='NE2050', interConn='ERCOT', elec=True)

    (CoalCCS_NE2020_sCap_EI, CCCCS_NE2020_sCap_EI, CC_NE2020_sCap_EI, Nuclear_NE2020_sCap_EI, Hydrogen_NE2020_sCap_EI, Battery_NE2020_sCap_EI,
     DAC_NE2020_sCap_EI, Wind_NE2020_sCap_EI, Solar_NE2020_sCap_EI, CoalCCS_NE2020_sCap_EI_2, CCCCS_NE2020_sCap_EI_2, CC_NE2020_sCap_EI_2,
     Nuclear_NE2020_sCap_EI_2, Hydrogen_NE2020_sCap_EI_2, Battery_NE2020_sCap_EI_2, DAC_NE2020_sCap_EI_2, Wind_NE2020_sCap_EI_2,
     Solar_NE2020_sCap_EI_2) = capInvestments(ref_dir, techCase='Stringent Cap', planningScr='NE2020', interConn='EI', elec=True)
    (CoalCCS_NE2050_sCap_EI, CCCCS_NE2050_sCap_EI, CC_NE2050_sCap_EI, Nuclear_NE2050_sCap_EI, Hydrogen_NE2050_sCap_EI, Battery_NE2050_sCap_EI,
     DAC_NE2050_sCap_EI, Wind_NE2050_sCap_EI, Solar_NE2050_sCap_EI, CoalCCS_NE2050_sCap_EI_2, CCCCS_NE2050_sCap_EI_2, CC_NE2050_sCap_EI_2,
     Nuclear_NE2050_sCap_EI_2, Hydrogen_NE2050_sCap_EI_2, Battery_NE2050_sCap_EI_2, DAC_NE2050_sCap_EI_2, Wind_NE2050_sCap_EI_2,
     Solar_NE2050_sCap_EI_2) = capInvestments(ref_dir, techCase='Stringent Cap', planningScr='NE2050', interConn='EI', elec=True)

    (CoalCCS_NE2020_sCap_ERCOT, CCCCS_NE2020_sCap_ERCOT, CC_NE2020_sCap_ERCOT, Nuclear_NE2020_sCap_ERCOT, Hydrogen_NE2020_sCap_ERCOT, Battery_NE2020_sCap_ERCOT,
     DAC_NE2020_sCap_ERCOT, Wind_NE2020_sCap_ERCOT, Solar_NE2020_sCap_ERCOT, CoalCCS_NE2020_sCap_ERCOT_2, CCCCS_NE2020_sCap_ERCOT_2,
     CC_NE2020_sCap_ERCOT_2, Nuclear_NE2020_sCap_ERCOT_2, Hydrogen_NE2020_sCap_ERCOT_2, Battery_NE2020_sCap_ERCOT_2,
     DAC_NE2020_sCap_ERCOT_2, Wind_NE2020_sCap_ERCOT_2, Solar_NE2020_sCap_ERCOT_2) = capInvestments(ref_dir, techCase='Stringent Cap', planningScr='NE2020', interConn='ERCOT', elec=True)
    (CoalCCS_NE2050_sCap_ERCOT, CCCCS_NE2050_sCap_ERCOT, CC_NE2050_sCap_ERCOT, Nuclear_NE2050_sCap_ERCOT, Hydrogen_NE2050_sCap_ERCOT, Battery_NE2050_sCap_ERCOT,
     DAC_NE2050_sCap_ERCOT, Wind_NE2050_sCap_ERCOT, Solar_NE2050_sCap_ERCOT, CoalCCS_NE2050_sCap_ERCOT_2, CCCCS_NE2050_sCap_ERCOT_2, CC_NE2050_sCap_ERCOT_2, Nuclear_NE2050_sCap_ERCOT_2,
     Hydrogen_NE2050_sCap_ERCOT_2, Battery_NE2050_sCap_ERCOT_2, DAC_NE2050_sCap_ERCOT_2,
     Wind_NE2050_sCap_ERCOT_2, Solar_NE2050_sCap_ERCOT_2) = capInvestments(ref_dir, techCase='Stringent Cap', planningScr='NE2050', interConn='ERCOT', elec=True)

    df_capEXP_ref, df_capEXP_ref_ERCOT = graphCE(CoalCCS_NE2020_ref_EI, CCCCS_NE2020_ref_EI, CC_NE2020_ref_EI, Nuclear_NE2020_ref_EI, Hydrogen_NE2020_ref_EI,Battery_NE2020_ref_EI,
                                                 DAC_NE2020_ref_EI, Wind_NE2020_ref_EI, Solar_NE2020_ref_EI, CoalCCS_NE2020_ref_EI_2, CCCCS_NE2020_ref_EI_2, CC_NE2020_ref_EI_2,
                                                 Nuclear_NE2020_ref_EI_2, Hydrogen_NE2020_ref_EI_2,Battery_NE2020_ref_EI_2, DAC_NE2020_ref_EI_2, Wind_NE2020_ref_EI_2,
                                                 Solar_NE2020_ref_EI_2, CoalCCS_NE2050_ref_EI, CCCCS_NE2050_ref_EI, CC_NE2050_ref_EI, Nuclear_NE2050_ref_EI, Hydrogen_NE2050_ref_EI,Battery_NE2050_ref_EI,
                                                 DAC_NE2050_ref_EI, Wind_NE2050_ref_EI, Solar_NE2050_ref_EI, CoalCCS_NE2050_ref_EI_2, CCCCS_NE2050_ref_EI_2, CC_NE2050_ref_EI_2,
                                                 Nuclear_NE2050_ref_EI_2, Hydrogen_NE2050_ref_EI_2,Battery_NE2050_ref_EI_2, DAC_NE2050_ref_EI_2, Wind_NE2050_ref_EI_2,
                                                 Solar_NE2050_ref_EI_2, CoalCCS_NE2020_ref_ERCOT, CCCCS_NE2020_ref_ERCOT, CC_NE2020_ref_ERCOT, Nuclear_NE2020_ref_ERCOT, Hydrogen_NE2020_ref_ERCOT,Battery_NE2020_ref_ERCOT,
                                                 DAC_NE2020_ref_ERCOT, Wind_NE2020_ref_ERCOT, Solar_NE2020_ref_ERCOT, CoalCCS_NE2020_ref_ERCOT_2, CCCCS_NE2020_ref_ERCOT_2,
                                                 CC_NE2020_ref_ERCOT_2, Nuclear_NE2020_ref_ERCOT_2, Hydrogen_NE2020_ref_ERCOT_2,Battery_NE2020_ref_ERCOT_2,
                                                 DAC_NE2020_ref_ERCOT_2, Wind_NE2020_ref_ERCOT_2, Solar_NE2020_ref_ERCOT_2, CoalCCS_NE2050_ref_ERCOT, CCCCS_NE2050_ref_ERCOT, CC_NE2050_ref_ERCOT, Nuclear_NE2050_ref_ERCOT, Hydrogen_NE2050_ref_ERCOT,Battery_NE2050_ref_ERCOT,
                                                 DAC_NE2050_ref_ERCOT, Wind_NE2050_ref_ERCOT, Solar_NE2050_ref_ERCOT, CoalCCS_NE2050_ref_ERCOT_2, CCCCS_NE2050_ref_ERCOT_2, CC_NE2050_ref_ERCOT_2, Nuclear_NE2050_ref_ERCOT_2, Hydrogen_NE2050_ref_ERCOT_2,Battery_NE2050_ref_ERCOT_2,
                                                 DAC_NE2050_ref_ERCOT_2, Wind_NE2050_ref_ERCOT_2, Solar_NE2050_ref_ERCOT_2, CoalCCS_NE2020_lh2_EI, CCCCS_NE2020_lh2_EI, CC_NE2020_lh2_EI, Nuclear_NE2020_lh2_EI, Hydrogen_NE2020_lh2_EI, Battery_NE2020_lh2_EI,
                                                 DAC_NE2020_lh2_EI, Wind_NE2020_lh2_EI, Solar_NE2020_lh2_EI, CoalCCS_NE2020_lh2_EI_2, CCCCS_NE2020_lh2_EI_2, CC_NE2020_lh2_EI_2,
                                                 Nuclear_NE2020_lh2_EI_2, Hydrogen_NE2020_lh2_EI_2, Battery_NE2020_lh2_EI_2, DAC_NE2020_lh2_EI_2, Wind_NE2020_lh2_EI_2,
                                                 Solar_NE2020_lh2_EI_2, CoalCCS_NE2050_lh2_EI, CCCCS_NE2050_lh2_EI, CC_NE2050_lh2_EI, Nuclear_NE2050_lh2_EI, Hydrogen_NE2050_lh2_EI, Battery_NE2050_lh2_EI,
                                                 DAC_NE2050_lh2_EI, Wind_NE2050_lh2_EI, Solar_NE2050_lh2_EI, CoalCCS_NE2050_lh2_EI_2, CCCCS_NE2050_lh2_EI_2, CC_NE2050_lh2_EI_2,
                                                 Nuclear_NE2050_lh2_EI_2, Hydrogen_NE2050_lh2_EI_2, Battery_NE2050_lh2_EI_2, DAC_NE2050_lh2_EI_2, Wind_NE2050_lh2_EI_2,
                                                 Solar_NE2050_lh2_EI_2, CoalCCS_NE2020_lh2_ERCOT, CCCCS_NE2020_lh2_ERCOT, CC_NE2020_lh2_ERCOT, Nuclear_NE2020_lh2_ERCOT, Hydrogen_NE2020_lh2_ERCOT, Battery_NE2020_lh2_ERCOT,
                                                 DAC_NE2020_lh2_ERCOT, Wind_NE2020_lh2_ERCOT, Solar_NE2020_lh2_ERCOT, CoalCCS_NE2020_lh2_ERCOT_2, CCCCS_NE2020_lh2_ERCOT_2,
                                                 CC_NE2020_lh2_ERCOT_2, Nuclear_NE2020_lh2_ERCOT_2, Hydrogen_NE2020_lh2_ERCOT_2, Battery_NE2020_lh2_ERCOT_2,
                                                 CoalCCS_NE2050_lh2_ERCOT, CCCCS_NE2050_lh2_ERCOT, CC_NE2050_lh2_ERCOT, Nuclear_NE2050_lh2_ERCOT, Hydrogen_NE2050_lh2_ERCOT, Battery_NE2050_lh2_ERCOT,
                                                 DAC_NE2050_lh2_ERCOT, Wind_NE2050_lh2_ERCOT, Solar_NE2050_lh2_ERCOT, CoalCCS_NE2050_lh2_ERCOT_2, CCCCS_NE2050_lh2_ERCOT_2, CC_NE2050_lh2_ERCOT_2, Nuclear_NE2050_lh2_ERCOT_2,
                                                 Hydrogen_NE2050_lh2_ERCOT_2, Battery_NE2050_lh2_ERCOT_2, DAC_NE2050_lh2_ERCOT_2, Wind_NE2050_lh2_ERCOT_2, Solar_NE2050_lh2_ERCOT_2,
                                                 CoalCCS_NE2020_he_EI, CCCCS_NE2020_he_EI, CC_NE2020_he_EI, Nuclear_NE2020_he_EI, Hydrogen_NE2020_he_EI, Battery_NE2020_he_EI,
                                                 DAC_NE2020_he_EI, Wind_NE2020_he_EI, Solar_NE2020_he_EI, CoalCCS_NE2020_he_EI_2, CCCCS_NE2020_he_EI_2, CC_NE2020_he_EI_2,
                                                 Nuclear_NE2020_he_EI_2, Hydrogen_NE2020_he_EI_2, Battery_NE2020_he_EI_2, DAC_NE2020_he_EI_2, Wind_NE2020_he_EI_2,
                                                 Solar_NE2020_he_EI_2, CoalCCS_NE2050_he_EI, CCCCS_NE2050_he_EI, CC_NE2050_he_EI, Nuclear_NE2050_he_EI, Hydrogen_NE2050_he_EI, Battery_NE2050_he_EI,
                                                 DAC_NE2050_he_EI, Wind_NE2050_he_EI, Solar_NE2050_he_EI, CoalCCS_NE2050_he_EI_2, CCCCS_NE2050_he_EI_2, CC_NE2050_he_EI_2,
                                                 Nuclear_NE2050_he_EI_2, Hydrogen_NE2050_he_EI_2, Battery_NE2050_he_EI_2, DAC_NE2050_he_EI_2, Wind_NE2050_he_EI_2,
                                                 Solar_NE2050_he_EI_2, CoalCCS_NE2020_he_ERCOT, CCCCS_NE2020_he_ERCOT, CC_NE2020_he_ERCOT, Nuclear_NE2020_he_ERCOT, Hydrogen_NE2020_he_ERCOT, Battery_NE2020_he_ERCOT,
                                                 DAC_NE2020_he_ERCOT, Wind_NE2020_he_ERCOT, Solar_NE2020_he_ERCOT, CoalCCS_NE2020_he_ERCOT_2, CCCCS_NE2020_he_ERCOT_2,
                                                 CC_NE2020_he_ERCOT_2, Nuclear_NE2020_he_ERCOT_2, Hydrogen_NE2020_he_ERCOT_2, Battery_NE2020_he_ERCOT_2,
                                                 DAC_NE2020_he_ERCOT_2, Wind_NE2020_he_ERCOT_2, Solar_NE2020_he_ERCOT_2,
                                                 CoalCCS_NE2050_he_ERCOT, CCCCS_NE2050_he_ERCOT, CC_NE2050_he_ERCOT, Nuclear_NE2050_he_ERCOT, Hydrogen_NE2050_he_ERCOT, Battery_NE2050_he_ERCOT,
                                                 DAC_NE2050_he_ERCOT, Wind_NE2050_he_ERCOT, Solar_NE2050_he_ERCOT, CoalCCS_NE2050_he_ERCOT_2, CCCCS_NE2050_he_ERCOT_2, CC_NE2050_he_ERCOT_2, Nuclear_NE2050_he_ERCOT_2, Hydrogen_NE2050_he_ERCOT_2,
                                                 Battery_NE2050_he_ERCOT_2, DAC_NE2050_he_ERCOT_2, Wind_NE2050_he_ERCOT_2, Solar_NE2050_he_ERCOT_2,
                                                 CoalCCS_NE2020_lccs_EI, CCCCS_NE2020_lccs_EI, CC_NE2020_lccs_EI, Nuclear_NE2020_lccs_EI, Hydrogen_NE2020_lccs_EI, Battery_NE2020_lccs_EI,
                                                 DAC_NE2020_lccs_EI, Wind_NE2020_lccs_EI, Solar_NE2020_lccs_EI, CoalCCS_NE2020_lccs_EI_2, CCCCS_NE2020_lccs_EI_2, CC_NE2020_lccs_EI_2,
                                                 Nuclear_NE2020_lccs_EI_2, Hydrogen_NE2020_lccs_EI_2, Battery_NE2020_lccs_EI_2, DAC_NE2020_lccs_EI_2, Wind_NE2020_lccs_EI_2,
                                                 Solar_NE2020_lccs_EI_2, CoalCCS_NE2050_lccs_EI, CCCCS_NE2050_lccs_EI, CC_NE2050_lccs_EI, Nuclear_NE2050_lccs_EI, Hydrogen_NE2050_lccs_EI, Battery_NE2050_lccs_EI,
                                                 DAC_NE2050_lccs_EI, Wind_NE2050_lccs_EI, Solar_NE2050_lccs_EI, CoalCCS_NE2050_lccs_EI_2, CCCCS_NE2050_lccs_EI_2, CC_NE2050_lccs_EI_2,
                                                 Nuclear_NE2050_lccs_EI_2, Hydrogen_NE2050_lccs_EI_2, Battery_NE2050_lccs_EI_2, DAC_NE2050_lccs_EI_2, Wind_NE2050_lccs_EI_2,
                                                 Solar_NE2050_lccs_EI_2, CoalCCS_NE2020_lccs_ERCOT, CCCCS_NE2020_lccs_ERCOT, CC_NE2020_lccs_ERCOT, Nuclear_NE2020_lccs_ERCOT, Hydrogen_NE2020_lccs_ERCOT, Battery_NE2020_lccs_ERCOT,
                                                 DAC_NE2020_lccs_ERCOT, Wind_NE2020_lccs_ERCOT, Solar_NE2020_lccs_ERCOT, CoalCCS_NE2020_lccs_ERCOT_2, CCCCS_NE2020_lccs_ERCOT_2,
                                                 CC_NE2020_lccs_ERCOT_2, Nuclear_NE2020_lccs_ERCOT_2, Hydrogen_NE2020_lccs_ERCOT_2, Battery_NE2020_lccs_ERCOT_2,
                                                 DAC_NE2020_lccs_ERCOT_2, Wind_NE2020_lccs_ERCOT_2, Solar_NE2020_lccs_ERCOT_2,
                                                 CoalCCS_NE2050_lccs_ERCOT, CCCCS_NE2050_lccs_ERCOT, CC_NE2050_lccs_ERCOT, Nuclear_NE2050_lccs_ERCOT, Hydrogen_NE2050_lccs_ERCOT, Battery_NE2050_lccs_ERCOT,
                                                 DAC_NE2050_lccs_ERCOT, Wind_NE2050_lccs_ERCOT, Solar_NE2050_lccs_ERCOT, CoalCCS_NE2050_lccs_ERCOT_2, CCCCS_NE2050_lccs_ERCOT_2, CC_NE2050_lccs_ERCOT_2, Nuclear_NE2050_lccs_ERCOT_2,
                                                 Hydrogen_NE2050_lccs_ERCOT_2, Battery_NE2050_lccs_ERCOT_2, DAC_NE2050_lccs_ERCOT_2, Wind_NE2050_lccs_ERCOT_2, Solar_NE2050_lccs_ERCOT_2,
                                                 CoalCCS_NE2020_ltrans_EI, CCCCS_NE2020_ltrans_EI, CC_NE2020_ltrans_EI, Nuclear_NE2020_ltrans_EI, Hydrogen_NE2020_ltrans_EI, Battery_NE2020_ltrans_EI,
                                                 DAC_NE2020_ltrans_EI, Wind_NE2020_ltrans_EI, Solar_NE2020_ltrans_EI, CoalCCS_NE2020_ltrans_EI_2, CCCCS_NE2020_ltrans_EI_2, CC_NE2020_ltrans_EI_2,
                                                 Nuclear_NE2020_ltrans_EI_2, Hydrogen_NE2020_ltrans_EI_2, Battery_NE2020_ltrans_EI_2, DAC_NE2020_ltrans_EI_2, Wind_NE2020_ltrans_EI_2,
                                                 Solar_NE2020_ltrans_EI_2, CoalCCS_NE2050_ltrans_EI, CCCCS_NE2050_ltrans_EI, CC_NE2050_ltrans_EI, Nuclear_NE2050_ltrans_EI, Hydrogen_NE2050_ltrans_EI, Battery_NE2050_ltrans_EI,
                                                 DAC_NE2050_ltrans_EI, Wind_NE2050_ltrans_EI, Solar_NE2050_ltrans_EI, CoalCCS_NE2050_ltrans_EI_2, CCCCS_NE2050_ltrans_EI_2, CC_NE2050_ltrans_EI_2,
                                                 Nuclear_NE2050_ltrans_EI_2, Hydrogen_NE2050_ltrans_EI_2, Battery_NE2050_ltrans_EI_2, DAC_NE2050_ltrans_EI_2, Wind_NE2050_ltrans_EI_2,
                                                 Solar_NE2050_ltrans_EI_2, CoalCCS_NE2020_ltrans_ERCOT, CCCCS_NE2020_ltrans_ERCOT, CC_NE2020_ltrans_ERCOT, Nuclear_NE2020_ltrans_ERCOT, Hydrogen_NE2020_ltrans_ERCOT, Battery_NE2020_ltrans_ERCOT,
                                                 DAC_NE2020_ltrans_ERCOT, Wind_NE2020_ltrans_ERCOT, Solar_NE2020_ltrans_ERCOT, CoalCCS_NE2020_ltrans_ERCOT_2, CCCCS_NE2020_ltrans_ERCOT_2,
                                                 CC_NE2020_ltrans_ERCOT_2, Nuclear_NE2020_ltrans_ERCOT_2, Hydrogen_NE2020_ltrans_ERCOT_2, Battery_NE2020_ltrans_ERCOT_2,
                                                 DAC_NE2020_ltrans_ERCOT_2, Wind_NE2020_ltrans_ERCOT_2, Solar_NE2020_ltrans_ERCOT_2, CoalCCS_NE2050_ltrans_ERCOT, CCCCS_NE2050_ltrans_ERCOT, CC_NE2050_ltrans_ERCOT, Nuclear_NE2050_ltrans_ERCOT, Hydrogen_NE2050_ltrans_ERCOT, Battery_NE2050_ltrans_ERCOT,
                                                 DAC_NE2050_ltrans_ERCOT, Wind_NE2050_ltrans_ERCOT, Solar_NE2050_ltrans_ERCOT, CoalCCS_NE2050_ltrans_ERCOT_2, CCCCS_NE2050_ltrans_ERCOT_2, CC_NE2050_ltrans_ERCOT_2, Nuclear_NE2050_ltrans_ERCOT_2,
                                                 Hydrogen_NE2050_ltrans_ERCOT_2, Battery_NE2050_ltrans_ERCOT_2, DAC_NE2050_ltrans_ERCOT_2,
                                                 Wind_NE2050_ltrans_ERCOT_2, Solar_NE2050_ltrans_ERCOT_2, CoalCCS_NE2020_sCap_EI, CCCCS_NE2020_sCap_EI, CC_NE2020_sCap_EI, Nuclear_NE2020_sCap_EI, Hydrogen_NE2020_sCap_EI, Battery_NE2020_sCap_EI,
                                                 DAC_NE2020_sCap_EI, Wind_NE2020_sCap_EI, Solar_NE2020_sCap_EI, CoalCCS_NE2020_sCap_EI_2, CCCCS_NE2020_sCap_EI_2, CC_NE2020_sCap_EI_2,
                                                 Nuclear_NE2020_sCap_EI_2, Hydrogen_NE2020_sCap_EI_2, Battery_NE2020_sCap_EI_2, DAC_NE2020_sCap_EI_2, Wind_NE2020_sCap_EI_2,
                                                 Solar_NE2020_sCap_EI_2, CoalCCS_NE2050_sCap_EI, CCCCS_NE2050_sCap_EI, CC_NE2050_sCap_EI, Nuclear_NE2050_sCap_EI, Hydrogen_NE2050_sCap_EI, Battery_NE2050_sCap_EI,
                                                 DAC_NE2050_sCap_EI, Wind_NE2050_sCap_EI, Solar_NE2050_sCap_EI, CoalCCS_NE2050_sCap_EI_2, CCCCS_NE2050_sCap_EI_2, CC_NE2050_sCap_EI_2,
                                                 Nuclear_NE2050_sCap_EI_2, Hydrogen_NE2050_sCap_EI_2, Battery_NE2050_sCap_EI_2, DAC_NE2050_sCap_EI_2, Wind_NE2050_sCap_EI_2,
                                                 Solar_NE2050_sCap_EI_2, CoalCCS_NE2020_sCap_ERCOT, CCCCS_NE2020_sCap_ERCOT, CC_NE2020_sCap_ERCOT, Nuclear_NE2020_sCap_ERCOT, Hydrogen_NE2020_sCap_ERCOT, Battery_NE2020_sCap_ERCOT,
                                                 DAC_NE2020_sCap_ERCOT, Wind_NE2020_sCap_ERCOT, Solar_NE2020_sCap_ERCOT, CoalCCS_NE2020_sCap_ERCOT_2, CCCCS_NE2020_sCap_ERCOT_2,
                                                 CC_NE2020_sCap_ERCOT_2, Nuclear_NE2020_sCap_ERCOT_2, Hydrogen_NE2020_sCap_ERCOT_2, Battery_NE2020_sCap_ERCOT_2,
                                                 DAC_NE2020_sCap_ERCOT_2, Wind_NE2020_sCap_ERCOT_2, Solar_NE2020_sCap_ERCOT_2, CoalCCS_NE2050_sCap_ERCOT, CCCCS_NE2050_sCap_ERCOT, CC_NE2050_sCap_ERCOT, Nuclear_NE2050_sCap_ERCOT, Hydrogen_NE2050_sCap_ERCOT, Battery_NE2050_sCap_ERCOT,
                                                 DAC_NE2050_sCap_ERCOT, Wind_NE2050_sCap_ERCOT, Solar_NE2050_sCap_ERCOT, CoalCCS_NE2050_sCap_ERCOT_2, CCCCS_NE2050_sCap_ERCOT_2, CC_NE2050_sCap_ERCOT_2, Nuclear_NE2050_sCap_ERCOT_2,
                                                 Hydrogen_NE2050_sCap_ERCOT_2, Battery_NE2050_sCap_ERCOT_2, DAC_NE2050_sCap_ERCOT_2,
                                                 Wind_NE2050_sCap_ERCOT_2, Solar_NE2050_sCap_ERCOT_2)

    df_capEXP_ref['PlanningScr'] = df_capEXP_ref['PlanningScr'].apply(wrap, args=[20])
    chart = alt.Chart(df_capEXP_ref).mark_bar(size=20).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Capacity):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Capacity Investments (GW)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Scenario:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Technology',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        # tell Altair which field to use for color segmentation
        color=alt.Color('Technology:N',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ffffff','#ff6f69', '#96ceb4', 'darkolivegreen', 'black', 'saddlebrown', 'lightpink','#ffcc5c','skyblue'],
                        ),
                        )).resolve_scale(y='shared').configure_view(
        # remove grid lines around column clusters
        #strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15,titleFontSize=15
                     ).properties(width=130, height=400).show()

    df_capEXP_ref_ERCOT['PlanningScr'] = df_capEXP_ref_ERCOT['PlanningScr'].apply(wrap, args=[20])
    chart = alt.Chart(df_capEXP_ref_ERCOT).mark_bar(size=20).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Capacity):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Capacity Investments (GW)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Scenario:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Technology',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        # tell Altair which field to use for color segmentation
        color=alt.Color('Technology:N',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ffffff', '#ff6f69', '#96ceb4', 'darkolivegreen', 'black', 'saddlebrown', 'lightpink', '#ffcc5c', 'skyblue'],
                        ),
                        )).resolve_scale(y='shared').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15, titleFontSize=15
                                                                          ).properties(width=130, height=400).show()

    # Costs:
    (totCost_NE2020_ref_EI, opCost_data_NE2020_ref_EI, fixedCost_data_NE2020_ref_EI,
     totCost_NE2020_ref_EI_2, opCost_data_NE2020_ref_EI_2, fixedCost_data_NE2020_ref_EI_2) = costCal(ref_dir, techCase='Reference', planningScr='NE2020', interConn = 'EI', elec=True)
    (totCost_NE2050_ref_EI, opCost_data_NE2050_ref_EI, fixedCost_data_NE2050_ref_EI,
     totCost_NE2050_ref_EI_2, opCost_data_NE2050_ref_EI_2, fixedCost_data_NE2050_ref_EI_2) = costCal(ref_dir, techCase='Reference', planningScr='NE2050', interConn = 'EI', elec=True)

    (totCost_NE2020_ref_ERCOT, opCost_data_NE2020_ref_ERCOT, fixedCost_data_NE2020_ref_ERCOT,
     totCost_NE2020_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT_2) = costCal(ref_dir, techCase='Reference', planningScr='NE2020', interConn='ERCOT', elec=True)
    (totCost_NE2050_ref_ERCOT, opCost_data_NE2050_ref_ERCOT, fixedCost_data_NE2050_ref_ERCOT,
     totCost_NE2050_ref_ERCOT_2, opCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2050_ref_ERCOT_2) = costCal(ref_dir, techCase='Reference', planningScr='NE2050', interConn='ERCOT', elec=True)

    (totCost_NE2020_lh2_EI, opCost_data_NE2020_lh2_EI, fixedCost_data_NE2020_lh2_EI,
     totCost_NE2020_lh2_EI_2, opCost_data_NE2020_lh2_EI_2, fixedCost_data_NE2020_lh2_EI_2) = costCal(ref_dir, techCase='No H2', planningScr='NE2020', interConn='EI', elec=True)
    (totCost_NE2050_lh2_EI, opCost_data_NE2050_lh2_EI, fixedCost_data_NE2050_lh2_EI,
     totCost_NE2050_lh2_EI_2, opCost_data_NE2050_lh2_EI_2, fixedCost_data_NE2050_lh2_EI_2) = costCal(ref_dir, techCase='No H2', planningScr='NE2050', interConn='EI', elec=True)

    (totCost_NE2020_lh2_ERCOT, opCost_data_NE2020_lh2_ERCOT, fixedCost_data_NE2020_lh2_ERCOT,
     totCost_NE2020_lh2_ERCOT_2, opCost_data_NE2020_lh2_ERCOT_2, fixedCost_data_NE2020_lh2_ERCOT_2) = costCal(ref_dir, techCase='No H2', planningScr='NE2020', interConn='ERCOT', elec=True)
    (totCost_NE2050_lh2_ERCOT, opCost_data_NE2050_lh2_ERCOT, fixedCost_data_NE2050_lh2_ERCOT,
     totCost_NE2050_lh2_ERCOT_2, opCost_data_NE2050_lh2_ERCOT_2, fixedCost_data_NE2050_lh2_ERCOT_2) = costCal(ref_dir, techCase='No H2', planningScr='NE2050', interConn='ERCOT', elec=True)

    (totCost_NE2020_lccs_EI, opCost_data_NE2020_lccs_EI, fixedCost_data_NE2020_lccs_EI,
     totCost_NE2020_lccs_EI_2, opCost_data_NE2020_lccs_EI_2, fixedCost_data_NE2020_lccs_EI_2) = costCal(ref_dir, techCase='No CCS', planningScr='NE2020', interConn='EI', elec=True)
    (totCost_NE2050_lccs_EI, opCost_data_NE2050_lccs_EI, fixedCost_data_NE2050_lccs_EI,
     totCost_NE2050_lccs_EI_2, opCost_data_NE2050_lccs_EI_2, fixedCost_data_NE2050_lccs_EI_2) = costCal(ref_dir, techCase='No CCS', planningScr='NE2050', interConn='EI', elec=True)

    (totCost_NE2020_lccs_ERCOT, opCost_data_NE2020_lccs_ERCOT, fixedCost_data_NE2020_lccs_ERCOT,
     totCost_NE2020_lccs_ERCOT_2, opCost_data_NE2020_lccs_ERCOT_2, fixedCost_data_NE2020_lccs_ERCOT_2) = costCal(ref_dir, techCase='No CCS', planningScr='NE2020', interConn='ERCOT', elec=True)
    (totCost_NE2050_lccs_ERCOT, opCost_data_NE2050_lccs_ERCOT, fixedCost_data_NE2050_lccs_ERCOT,
     totCost_NE2050_lccs_ERCOT_2, opCost_data_NE2050_lccs_ERCOT_2, fixedCost_data_NE2050_lccs_ERCOT_2) = costCal(ref_dir, techCase='No CCS', planningScr='NE2050', interConn='ERCOT', elec=True)

    (totCost_NE2020_he_EI, opCost_data_NE2020_he_EI, fixedCost_data_NE2020_he_EI,
     totCost_NE2020_he_EI_2, opCost_data_NE2020_he_EI_2, fixedCost_data_NE2020_he_EI_2) = costCal(ref_dir, techCase='Reference', planningScr='NE2020', interConn='EI', elec=False)
    (totCost_NE2050_he_EI, opCost_data_NE2050_he_EI, fixedCost_data_NE2050_he_EI,
     totCost_NE2050_he_EI_2, opCost_data_NE2050_he_EI_2, fixedCost_data_NE2050_he_EI_2) = costCal(ref_dir, techCase='Reference', planningScr='NE2050', interConn='EI', elec=False)

    (totCost_NE2020_he_ERCOT, opCost_data_NE2020_he_ERCOT, fixedCost_data_NE2020_he_ERCOT,
     totCost_NE2020_he_ERCOT_2, opCost_data_NE2020_he_ERCOT_2, fixedCost_data_NE2020_he_ERCOT_2) = costCal(ref_dir, techCase='Reference', planningScr='NE2020', interConn='ERCOT', elec=False)
    (totCost_NE2050_he_ERCOT, opCost_data_NE2050_he_ERCOT, fixedCost_data_NE2050_he_ERCOT,
     totCost_NE2050_he_ERCOT_2, opCost_data_NE2050_he_ERCOT_2, fixedCost_data_NE2050_he_ERCOT_2) = costCal(ref_dir, techCase='Reference', planningScr='NE2050', interConn='ERCOT', elec=False)

    (totCost_NE2020_ltrans_EI, opCost_data_NE2020_ltrans_EI, fixedCost_data_NE2020_ltrans_EI,
     totCost_NE2020_ltrans_EI_2, opCost_data_NE2020_ltrans_EI_2, fixedCost_data_NE2020_ltrans_EI_2) = costCal(ref_dir, techCase='L Trans', planningScr='NE2020', interConn='EI', elec=True)
    (totCost_NE2050_ltrans_EI, opCost_data_NE2050_ltrans_EI, fixedCost_data_NE2050_ltrans_EI,
     totCost_NE2050_ltrans_EI_2, opCost_data_NE2050_ltrans_EI_2, fixedCost_data_NE2050_ltrans_EI_2) = costCal(ref_dir, techCase='L Trans', planningScr='NE2050', interConn='EI', elec=True)

    (totCost_NE2020_ltrans_ERCOT, opCost_data_NE2020_ltrans_ERCOT, fixedCost_data_NE2020_ltrans_ERCOT,
     totCost_NE2020_ltrans_ERCOT_2, opCost_data_NE2020_ltrans_ERCOT_2, fixedCost_data_NE2020_ltrans_ERCOT_2) = costCal(ref_dir, techCase='L Trans', planningScr='NE2020', interConn='ERCOT', elec=True)
    (totCost_NE2050_ltrans_ERCOT, opCost_data_NE2050_ltrans_ERCOT, fixedCost_data_NE2050_ltrans_ERCOT,
     totCost_NE2050_ltrans_ERCOT_2, opCost_data_NE2050_ltrans_ERCOT_2, fixedCost_data_NE2050_ltrans_ERCOT_2) = costCal(ref_dir, techCase='L Trans', planningScr='NE2050', interConn='ERCOT', elec=True)

    (totCost_NE2020_sCap_EI, opCost_data_NE2020_sCap_EI, fixedCost_data_NE2020_sCap_EI,
     totCost_NE2020_sCap_EI_2, opCost_data_NE2020_sCap_EI_2, fixedCost_data_NE2020_sCap_EI_2) = costCal(ref_dir, techCase='Stringent Cap', planningScr='NE2020', interConn='EI', elec=True)
    (totCost_NE2050_sCap_EI, opCost_data_NE2050_sCap_EI, fixedCost_data_NE2050_sCap_EI,
     totCost_NE2050_sCap_EI_2, opCost_data_NE2050_sCap_EI_2, fixedCost_data_NE2050_sCap_EI_2) = costCal(ref_dir, techCase='Stringent Cap', planningScr='NE2050', interConn='EI', elec=True)

    (totCost_NE2020_sCap_ERCOT, opCost_data_NE2020_sCap_ERCOT, fixedCost_data_NE2020_sCap_ERCOT,
     totCost_NE2020_sCap_ERCOT_2, opCost_data_NE2020_sCap_ERCOT_2, fixedCost_data_NE2020_sCap_ERCOT_2) = costCal(ref_dir, techCase='Stringent Cap', planningScr='NE2020', interConn='ERCOT', elec=True)
    (totCost_NE2050_sCap_ERCOT, opCost_data_NE2050_sCap_ERCOT, fixedCost_data_NE2050_sCap_ERCOT,
     totCost_NE2050_sCap_ERCOT_2, opCost_data_NE2050_sCap_ERCOT_2, fixedCost_data_NE2050_sCap_ERCOT_2) = costCal(ref_dir, techCase='Stringent Cap', planningScr='NE2050', interConn='ERCOT', elec=True)

    df_costs_ref, df_costs_ERCOT_ref = graphCosts(totCost_NE2020_ref_EI, opCost_data_NE2020_ref_EI, fixedCost_data_NE2020_ref_EI,
                                totCost_NE2020_ref_EI_2, opCost_data_NE2020_ref_EI_2, fixedCost_data_NE2020_ref_EI_2,
                                totCost_NE2050_ref_EI, opCost_data_NE2050_ref_EI, fixedCost_data_NE2050_ref_EI,
                                totCost_NE2050_ref_EI_2, opCost_data_NE2050_ref_EI_2, fixedCost_data_NE2050_ref_EI_2,
                                totCost_NE2020_ref_ERCOT, opCost_data_NE2020_ref_ERCOT, fixedCost_data_NE2020_ref_ERCOT,
                                totCost_NE2020_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT_2,
                                totCost_NE2050_ref_ERCOT, opCost_data_NE2050_ref_ERCOT, fixedCost_data_NE2050_ref_ERCOT,
                                totCost_NE2050_ref_ERCOT_2, opCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2050_ref_ERCOT_2,
                                totCost_NE2020_lh2_EI, opCost_data_NE2020_lh2_EI, fixedCost_data_NE2020_lh2_EI,
                                totCost_NE2020_lh2_EI_2, opCost_data_NE2020_lh2_EI_2, fixedCost_data_NE2020_lh2_EI_2,
                                totCost_NE2050_lh2_EI, opCost_data_NE2050_lh2_EI, fixedCost_data_NE2050_lh2_EI,
                                totCost_NE2050_lh2_EI_2, opCost_data_NE2050_lh2_EI_2, fixedCost_data_NE2050_lh2_EI_2,
                                totCost_NE2020_lh2_ERCOT, opCost_data_NE2020_lh2_ERCOT, fixedCost_data_NE2020_lh2_ERCOT,
                                totCost_NE2020_lh2_ERCOT_2, opCost_data_NE2020_lh2_ERCOT_2, fixedCost_data_NE2020_lh2_ERCOT_2,
                                totCost_NE2050_lh2_ERCOT, opCost_data_NE2050_lh2_ERCOT, fixedCost_data_NE2050_lh2_ERCOT,
                                totCost_NE2050_lh2_ERCOT_2, opCost_data_NE2050_lh2_ERCOT_2, fixedCost_data_NE2050_lh2_ERCOT_2,
                                totCost_NE2020_lccs_EI, opCost_data_NE2020_lccs_EI, fixedCost_data_NE2020_lccs_EI,
                                totCost_NE2020_lccs_EI_2, opCost_data_NE2020_lccs_EI_2, fixedCost_data_NE2020_lccs_EI_2,
                                totCost_NE2050_lccs_EI, opCost_data_NE2050_lccs_EI, fixedCost_data_NE2050_lccs_EI,
                                totCost_NE2050_lccs_EI_2, opCost_data_NE2050_lccs_EI_2, fixedCost_data_NE2050_lccs_EI_2,
                                totCost_NE2020_lccs_ERCOT, opCost_data_NE2020_lccs_ERCOT, fixedCost_data_NE2020_lccs_ERCOT,
                                totCost_NE2020_lccs_ERCOT_2, opCost_data_NE2020_lccs_ERCOT_2, fixedCost_data_NE2020_lccs_ERCOT_2,
                                totCost_NE2050_lccs_ERCOT, opCost_data_NE2050_lccs_ERCOT, fixedCost_data_NE2050_lccs_ERCOT,
                                totCost_NE2050_lccs_ERCOT_2, opCost_data_NE2050_lccs_ERCOT_2, fixedCost_data_NE2050_lccs_ERCOT_2,
                                totCost_NE2020_he_EI, opCost_data_NE2020_he_EI, fixedCost_data_NE2020_he_EI,
                                totCost_NE2020_he_EI_2, opCost_data_NE2020_he_EI_2, fixedCost_data_NE2020_he_EI_2,
                                totCost_NE2050_he_EI, opCost_data_NE2050_he_EI, fixedCost_data_NE2050_he_EI,
                                totCost_NE2050_he_EI_2, opCost_data_NE2050_he_EI_2, fixedCost_data_NE2050_he_EI_2,
                                totCost_NE2020_he_ERCOT, opCost_data_NE2020_he_ERCOT, fixedCost_data_NE2020_he_ERCOT,
                                totCost_NE2020_he_ERCOT_2, opCost_data_NE2020_he_ERCOT_2, fixedCost_data_NE2020_he_ERCOT_2,
                                totCost_NE2050_he_ERCOT, opCost_data_NE2050_he_ERCOT, fixedCost_data_NE2050_he_ERCOT,
                                totCost_NE2050_he_ERCOT_2, opCost_data_NE2050_he_ERCOT_2, fixedCost_data_NE2050_he_ERCOT_2,
                                totCost_NE2020_ltrans_EI, opCost_data_NE2020_ltrans_EI, fixedCost_data_NE2020_ltrans_EI,
                                totCost_NE2020_ltrans_EI_2, opCost_data_NE2020_ltrans_EI_2, fixedCost_data_NE2020_ltrans_EI_2,
                                totCost_NE2050_ltrans_EI, opCost_data_NE2050_ltrans_EI, fixedCost_data_NE2050_ltrans_EI,
                                totCost_NE2050_ltrans_EI_2, opCost_data_NE2050_ltrans_EI_2, fixedCost_data_NE2050_ltrans_EI_2,
                                totCost_NE2020_ltrans_ERCOT, opCost_data_NE2020_ltrans_ERCOT, fixedCost_data_NE2020_ltrans_ERCOT,
                                totCost_NE2020_ltrans_ERCOT_2, opCost_data_NE2020_ltrans_ERCOT_2, fixedCost_data_NE2020_ltrans_ERCOT_2,
                                totCost_NE2050_ltrans_ERCOT, opCost_data_NE2050_ltrans_ERCOT, fixedCost_data_NE2050_ltrans_ERCOT,
                                totCost_NE2050_ltrans_ERCOT_2, opCost_data_NE2050_ltrans_ERCOT_2, fixedCost_data_NE2050_ltrans_ERCOT_2,
                                totCost_NE2020_sCap_EI, opCost_data_NE2020_sCap_EI, fixedCost_data_NE2020_sCap_EI,
                                totCost_NE2020_sCap_EI_2, opCost_data_NE2020_sCap_EI_2, fixedCost_data_NE2020_sCap_EI_2,
                                totCost_NE2050_sCap_EI, opCost_data_NE2050_sCap_EI, fixedCost_data_NE2050_sCap_EI,
                                totCost_NE2050_sCap_EI_2, opCost_data_NE2050_sCap_EI_2, fixedCost_data_NE2050_sCap_EI_2,
                                totCost_NE2020_sCap_ERCOT, opCost_data_NE2020_sCap_ERCOT, fixedCost_data_NE2020_sCap_ERCOT,
                                totCost_NE2020_sCap_ERCOT_2, opCost_data_NE2020_sCap_ERCOT_2, fixedCost_data_NE2020_sCap_ERCOT_2,
                                totCost_NE2050_sCap_ERCOT, opCost_data_NE2050_sCap_ERCOT, fixedCost_data_NE2050_sCap_ERCOT,
                                totCost_NE2050_sCap_ERCOT_2, opCost_data_NE2050_sCap_ERCOT_2, fixedCost_data_NE2050_sCap_ERCOT_2)

    df_costs_ref['PlanningScr'] = df_costs_ref['PlanningScr'].apply(wrap, args=[20])
    chart = alt.Chart(df_costs_ref).mark_bar(size=20).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Amount):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Annual Costs (Billion $)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Scenario:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Cost Types',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Cost Types:N',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ffffff','#96ceb4','#ff6f69'],
                        ),
                        )).resolve_scale(y='shared').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15, titleFontSize=15
                                                                          ).properties(width=120, height=400).show()

    df_costs_ERCOT_ref['PlanningScr'] = df_costs_ERCOT_ref['PlanningScr'].apply(wrap, args=[20])
    chart = alt.Chart(df_costs_ERCOT_ref).mark_bar(size=20).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Amount):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Annual Costs (Billion $)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Scenario:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Cost Types',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Cost Types:N',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ffffff', '#96ceb4', '#ff6f69'],
                        ),
                        )).resolve_scale(y='shared').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15, titleFontSize=15
                                                                          ).properties(width=120, height=400).show()


def graphCE(CoalCCS_NE2020_ref_EI, CCCCS_NE2020_ref_EI, CC_NE2020_ref_EI, Nuclear_NE2020_ref_EI, Hydrogen_NE2020_ref_EI,Battery_NE2020_ref_EI,
             DAC_NE2020_ref_EI, Wind_NE2020_ref_EI, Solar_NE2020_ref_EI, CoalCCS_NE2020_ref_EI_2, CCCCS_NE2020_ref_EI_2, CC_NE2020_ref_EI_2,
             Nuclear_NE2020_ref_EI_2, Hydrogen_NE2020_ref_EI_2,Battery_NE2020_ref_EI_2, DAC_NE2020_ref_EI_2, Wind_NE2020_ref_EI_2,
             Solar_NE2020_ref_EI_2, CoalCCS_NE2050_ref_EI, CCCCS_NE2050_ref_EI, CC_NE2050_ref_EI, Nuclear_NE2050_ref_EI, Hydrogen_NE2050_ref_EI,Battery_NE2050_ref_EI,
             DAC_NE2050_ref_EI, Wind_NE2050_ref_EI, Solar_NE2050_ref_EI, CoalCCS_NE2050_ref_EI_2, CCCCS_NE2050_ref_EI_2, CC_NE2050_ref_EI_2,
             Nuclear_NE2050_ref_EI_2, Hydrogen_NE2050_ref_EI_2,Battery_NE2050_ref_EI_2, DAC_NE2050_ref_EI_2, Wind_NE2050_ref_EI_2,
             Solar_NE2050_ref_EI_2, CoalCCS_NE2020_ref_ERCOT, CCCCS_NE2020_ref_ERCOT, CC_NE2020_ref_ERCOT, Nuclear_NE2020_ref_ERCOT, Hydrogen_NE2020_ref_ERCOT,Battery_NE2020_ref_ERCOT,
             DAC_NE2020_ref_ERCOT, Wind_NE2020_ref_ERCOT, Solar_NE2020_ref_ERCOT, CoalCCS_NE2020_ref_ERCOT_2, CCCCS_NE2020_ref_ERCOT_2,
             CC_NE2020_ref_ERCOT_2, Nuclear_NE2020_ref_ERCOT_2, Hydrogen_NE2020_ref_ERCOT_2,Battery_NE2020_ref_ERCOT_2,
             DAC_NE2020_ref_ERCOT_2, Wind_NE2020_ref_ERCOT_2, Solar_NE2020_ref_ERCOT_2, CoalCCS_NE2050_ref_ERCOT, CCCCS_NE2050_ref_ERCOT, CC_NE2050_ref_ERCOT, Nuclear_NE2050_ref_ERCOT, Hydrogen_NE2050_ref_ERCOT,Battery_NE2050_ref_ERCOT,
             DAC_NE2050_ref_ERCOT, Wind_NE2050_ref_ERCOT, Solar_NE2050_ref_ERCOT, CoalCCS_NE2050_ref_ERCOT_2, CCCCS_NE2050_ref_ERCOT_2, CC_NE2050_ref_ERCOT_2, Nuclear_NE2050_ref_ERCOT_2, Hydrogen_NE2050_ref_ERCOT_2,Battery_NE2050_ref_ERCOT_2,
             DAC_NE2050_ref_ERCOT_2, Wind_NE2050_ref_ERCOT_2, Solar_NE2050_ref_ERCOT_2, CoalCCS_NE2020_lh2_EI, CCCCS_NE2020_lh2_EI, CC_NE2020_lh2_EI, Nuclear_NE2020_lh2_EI, Hydrogen_NE2020_lh2_EI, Battery_NE2020_lh2_EI,
             DAC_NE2020_lh2_EI, Wind_NE2020_lh2_EI, Solar_NE2020_lh2_EI, CoalCCS_NE2020_lh2_EI_2, CCCCS_NE2020_lh2_EI_2, CC_NE2020_lh2_EI_2,
             Nuclear_NE2020_lh2_EI_2, Hydrogen_NE2020_lh2_EI_2, Battery_NE2020_lh2_EI_2, DAC_NE2020_lh2_EI_2, Wind_NE2020_lh2_EI_2,
             Solar_NE2020_lh2_EI_2, CoalCCS_NE2050_lh2_EI, CCCCS_NE2050_lh2_EI, CC_NE2050_lh2_EI, Nuclear_NE2050_lh2_EI, Hydrogen_NE2050_lh2_EI, Battery_NE2050_lh2_EI,
             DAC_NE2050_lh2_EI, Wind_NE2050_lh2_EI, Solar_NE2050_lh2_EI, CoalCCS_NE2050_lh2_EI_2, CCCCS_NE2050_lh2_EI_2, CC_NE2050_lh2_EI_2,
             Nuclear_NE2050_lh2_EI_2, Hydrogen_NE2050_lh2_EI_2, Battery_NE2050_lh2_EI_2, DAC_NE2050_lh2_EI_2, Wind_NE2050_lh2_EI_2,
             Solar_NE2050_lh2_EI_2, CoalCCS_NE2020_lh2_ERCOT, CCCCS_NE2020_lh2_ERCOT, CC_NE2020_lh2_ERCOT, Nuclear_NE2020_lh2_ERCOT, Hydrogen_NE2020_lh2_ERCOT, Battery_NE2020_lh2_ERCOT,
             DAC_NE2020_lh2_ERCOT, Wind_NE2020_lh2_ERCOT, Solar_NE2020_lh2_ERCOT, CoalCCS_NE2020_lh2_ERCOT_2, CCCCS_NE2020_lh2_ERCOT_2,
             CC_NE2020_lh2_ERCOT_2, Nuclear_NE2020_lh2_ERCOT_2, Hydrogen_NE2020_lh2_ERCOT_2, Battery_NE2020_lh2_ERCOT_2,
             CoalCCS_NE2050_lh2_ERCOT, CCCCS_NE2050_lh2_ERCOT, CC_NE2050_lh2_ERCOT, Nuclear_NE2050_lh2_ERCOT, Hydrogen_NE2050_lh2_ERCOT, Battery_NE2050_lh2_ERCOT,
             DAC_NE2050_lh2_ERCOT, Wind_NE2050_lh2_ERCOT, Solar_NE2050_lh2_ERCOT, CoalCCS_NE2050_lh2_ERCOT_2, CCCCS_NE2050_lh2_ERCOT_2, CC_NE2050_lh2_ERCOT_2, Nuclear_NE2050_lh2_ERCOT_2,
             Hydrogen_NE2050_lh2_ERCOT_2, Battery_NE2050_lh2_ERCOT_2, DAC_NE2050_lh2_ERCOT_2, Wind_NE2050_lh2_ERCOT_2, Solar_NE2050_lh2_ERCOT_2,
             CoalCCS_NE2020_he_EI, CCCCS_NE2020_he_EI, CC_NE2020_he_EI, Nuclear_NE2020_he_EI, Hydrogen_NE2020_he_EI, Battery_NE2020_he_EI,
             DAC_NE2020_he_EI, Wind_NE2020_he_EI, Solar_NE2020_he_EI, CoalCCS_NE2020_he_EI_2, CCCCS_NE2020_he_EI_2, CC_NE2020_he_EI_2,
             Nuclear_NE2020_he_EI_2, Hydrogen_NE2020_he_EI_2, Battery_NE2020_he_EI_2, DAC_NE2020_he_EI_2, Wind_NE2020_he_EI_2,
             Solar_NE2020_he_EI_2, CoalCCS_NE2050_he_EI, CCCCS_NE2050_he_EI, CC_NE2050_he_EI, Nuclear_NE2050_he_EI, Hydrogen_NE2050_he_EI, Battery_NE2050_he_EI,
             DAC_NE2050_he_EI, Wind_NE2050_he_EI, Solar_NE2050_he_EI, CoalCCS_NE2050_he_EI_2, CCCCS_NE2050_he_EI_2, CC_NE2050_he_EI_2,
             Nuclear_NE2050_he_EI_2, Hydrogen_NE2050_he_EI_2, Battery_NE2050_he_EI_2, DAC_NE2050_he_EI_2, Wind_NE2050_he_EI_2,
             Solar_NE2050_he_EI_2, CoalCCS_NE2020_he_ERCOT, CCCCS_NE2020_he_ERCOT, CC_NE2020_he_ERCOT, Nuclear_NE2020_he_ERCOT, Hydrogen_NE2020_he_ERCOT, Battery_NE2020_he_ERCOT,
             DAC_NE2020_he_ERCOT, Wind_NE2020_he_ERCOT, Solar_NE2020_he_ERCOT, CoalCCS_NE2020_he_ERCOT_2, CCCCS_NE2020_he_ERCOT_2,
             CC_NE2020_he_ERCOT_2, Nuclear_NE2020_he_ERCOT_2, Hydrogen_NE2020_he_ERCOT_2, Battery_NE2020_he_ERCOT_2,
             DAC_NE2020_he_ERCOT_2, Wind_NE2020_he_ERCOT_2, Solar_NE2020_he_ERCOT_2,
             CoalCCS_NE2050_he_ERCOT, CCCCS_NE2050_he_ERCOT, CC_NE2050_he_ERCOT, Nuclear_NE2050_he_ERCOT, Hydrogen_NE2050_he_ERCOT, Battery_NE2050_he_ERCOT,
             DAC_NE2050_he_ERCOT, Wind_NE2050_he_ERCOT, Solar_NE2050_he_ERCOT, CoalCCS_NE2050_he_ERCOT_2, CCCCS_NE2050_he_ERCOT_2, CC_NE2050_he_ERCOT_2, Nuclear_NE2050_he_ERCOT_2, Hydrogen_NE2050_he_ERCOT_2,
             Battery_NE2050_he_ERCOT_2, DAC_NE2050_he_ERCOT_2, Wind_NE2050_he_ERCOT_2, Solar_NE2050_he_ERCOT_2,
             CoalCCS_NE2020_lccs_EI, CCCCS_NE2020_lccs_EI, CC_NE2020_lccs_EI, Nuclear_NE2020_lccs_EI, Hydrogen_NE2020_lccs_EI, Battery_NE2020_lccs_EI,
             DAC_NE2020_lccs_EI, Wind_NE2020_lccs_EI, Solar_NE2020_lccs_EI, CoalCCS_NE2020_lccs_EI_2, CCCCS_NE2020_lccs_EI_2, CC_NE2020_lccs_EI_2,
             Nuclear_NE2020_lccs_EI_2, Hydrogen_NE2020_lccs_EI_2, Battery_NE2020_lccs_EI_2, DAC_NE2020_lccs_EI_2, Wind_NE2020_lccs_EI_2,
             Solar_NE2020_lccs_EI_2, CoalCCS_NE2050_lccs_EI, CCCCS_NE2050_lccs_EI, CC_NE2050_lccs_EI, Nuclear_NE2050_lccs_EI, Hydrogen_NE2050_lccs_EI, Battery_NE2050_lccs_EI,
             DAC_NE2050_lccs_EI, Wind_NE2050_lccs_EI, Solar_NE2050_lccs_EI, CoalCCS_NE2050_lccs_EI_2, CCCCS_NE2050_lccs_EI_2, CC_NE2050_lccs_EI_2,
             Nuclear_NE2050_lccs_EI_2, Hydrogen_NE2050_lccs_EI_2, Battery_NE2050_lccs_EI_2, DAC_NE2050_lccs_EI_2, Wind_NE2050_lccs_EI_2,
             Solar_NE2050_lccs_EI_2, CoalCCS_NE2020_lccs_ERCOT, CCCCS_NE2020_lccs_ERCOT, CC_NE2020_lccs_ERCOT, Nuclear_NE2020_lccs_ERCOT, Hydrogen_NE2020_lccs_ERCOT, Battery_NE2020_lccs_ERCOT,
             DAC_NE2020_lccs_ERCOT, Wind_NE2020_lccs_ERCOT, Solar_NE2020_lccs_ERCOT, CoalCCS_NE2020_lccs_ERCOT_2, CCCCS_NE2020_lccs_ERCOT_2,
             CC_NE2020_lccs_ERCOT_2, Nuclear_NE2020_lccs_ERCOT_2, Hydrogen_NE2020_lccs_ERCOT_2, Battery_NE2020_lccs_ERCOT_2,
             DAC_NE2020_lccs_ERCOT_2, Wind_NE2020_lccs_ERCOT_2, Solar_NE2020_lccs_ERCOT_2,
             CoalCCS_NE2050_lccs_ERCOT, CCCCS_NE2050_lccs_ERCOT, CC_NE2050_lccs_ERCOT, Nuclear_NE2050_lccs_ERCOT, Hydrogen_NE2050_lccs_ERCOT, Battery_NE2050_lccs_ERCOT,
             DAC_NE2050_lccs_ERCOT, Wind_NE2050_lccs_ERCOT, Solar_NE2050_lccs_ERCOT, CoalCCS_NE2050_lccs_ERCOT_2, CCCCS_NE2050_lccs_ERCOT_2, CC_NE2050_lccs_ERCOT_2, Nuclear_NE2050_lccs_ERCOT_2,
             Hydrogen_NE2050_lccs_ERCOT_2, Battery_NE2050_lccs_ERCOT_2, DAC_NE2050_lccs_ERCOT_2, Wind_NE2050_lccs_ERCOT_2, Solar_NE2050_lccs_ERCOT_2,
             CoalCCS_NE2020_ltrans_EI, CCCCS_NE2020_ltrans_EI, CC_NE2020_ltrans_EI, Nuclear_NE2020_ltrans_EI, Hydrogen_NE2020_ltrans_EI, Battery_NE2020_ltrans_EI,
             DAC_NE2020_ltrans_EI, Wind_NE2020_ltrans_EI, Solar_NE2020_ltrans_EI, CoalCCS_NE2020_ltrans_EI_2, CCCCS_NE2020_ltrans_EI_2, CC_NE2020_ltrans_EI_2,
             Nuclear_NE2020_ltrans_EI_2, Hydrogen_NE2020_ltrans_EI_2, Battery_NE2020_ltrans_EI_2, DAC_NE2020_ltrans_EI_2, Wind_NE2020_ltrans_EI_2,
             Solar_NE2020_ltrans_EI_2, CoalCCS_NE2050_ltrans_EI, CCCCS_NE2050_ltrans_EI, CC_NE2050_ltrans_EI, Nuclear_NE2050_ltrans_EI, Hydrogen_NE2050_ltrans_EI, Battery_NE2050_ltrans_EI,
             DAC_NE2050_ltrans_EI, Wind_NE2050_ltrans_EI, Solar_NE2050_ltrans_EI, CoalCCS_NE2050_ltrans_EI_2, CCCCS_NE2050_ltrans_EI_2, CC_NE2050_ltrans_EI_2,
             Nuclear_NE2050_ltrans_EI_2, Hydrogen_NE2050_ltrans_EI_2, Battery_NE2050_ltrans_EI_2, DAC_NE2050_ltrans_EI_2, Wind_NE2050_ltrans_EI_2,
             Solar_NE2050_ltrans_EI_2, CoalCCS_NE2020_ltrans_ERCOT, CCCCS_NE2020_ltrans_ERCOT, CC_NE2020_ltrans_ERCOT, Nuclear_NE2020_ltrans_ERCOT, Hydrogen_NE2020_ltrans_ERCOT, Battery_NE2020_ltrans_ERCOT,
             DAC_NE2020_ltrans_ERCOT, Wind_NE2020_ltrans_ERCOT, Solar_NE2020_ltrans_ERCOT, CoalCCS_NE2020_ltrans_ERCOT_2, CCCCS_NE2020_ltrans_ERCOT_2,
             CC_NE2020_ltrans_ERCOT_2, Nuclear_NE2020_ltrans_ERCOT_2, Hydrogen_NE2020_ltrans_ERCOT_2, Battery_NE2020_ltrans_ERCOT_2,
             DAC_NE2020_ltrans_ERCOT_2, Wind_NE2020_ltrans_ERCOT_2, Solar_NE2020_ltrans_ERCOT_2, CoalCCS_NE2050_ltrans_ERCOT, CCCCS_NE2050_ltrans_ERCOT, CC_NE2050_ltrans_ERCOT, Nuclear_NE2050_ltrans_ERCOT, Hydrogen_NE2050_ltrans_ERCOT, Battery_NE2050_ltrans_ERCOT,
             DAC_NE2050_ltrans_ERCOT, Wind_NE2050_ltrans_ERCOT, Solar_NE2050_ltrans_ERCOT, CoalCCS_NE2050_ltrans_ERCOT_2, CCCCS_NE2050_ltrans_ERCOT_2, CC_NE2050_ltrans_ERCOT_2, Nuclear_NE2050_ltrans_ERCOT_2,
             Hydrogen_NE2050_ltrans_ERCOT_2, Battery_NE2050_ltrans_ERCOT_2, DAC_NE2050_ltrans_ERCOT_2,
             Wind_NE2050_ltrans_ERCOT_2, Solar_NE2050_ltrans_ERCOT_2, CoalCCS_NE2020_sCap_EI, CCCCS_NE2020_sCap_EI, CC_NE2020_sCap_EI, Nuclear_NE2020_sCap_EI, Hydrogen_NE2020_sCap_EI, Battery_NE2020_sCap_EI,
             DAC_NE2020_sCap_EI, Wind_NE2020_sCap_EI, Solar_NE2020_sCap_EI, CoalCCS_NE2020_sCap_EI_2, CCCCS_NE2020_sCap_EI_2, CC_NE2020_sCap_EI_2,
             Nuclear_NE2020_sCap_EI_2, Hydrogen_NE2020_sCap_EI_2, Battery_NE2020_sCap_EI_2, DAC_NE2020_sCap_EI_2, Wind_NE2020_sCap_EI_2,
             Solar_NE2020_sCap_EI_2, CoalCCS_NE2050_sCap_EI, CCCCS_NE2050_sCap_EI, CC_NE2050_sCap_EI, Nuclear_NE2050_sCap_EI, Hydrogen_NE2050_sCap_EI, Battery_NE2050_sCap_EI,
             DAC_NE2050_sCap_EI, Wind_NE2050_sCap_EI, Solar_NE2050_sCap_EI, CoalCCS_NE2050_sCap_EI_2, CCCCS_NE2050_sCap_EI_2, CC_NE2050_sCap_EI_2,
             Nuclear_NE2050_sCap_EI_2, Hydrogen_NE2050_sCap_EI_2, Battery_NE2050_sCap_EI_2, DAC_NE2050_sCap_EI_2, Wind_NE2050_sCap_EI_2,
             Solar_NE2050_sCap_EI_2, CoalCCS_NE2020_sCap_ERCOT, CCCCS_NE2020_sCap_ERCOT, CC_NE2020_sCap_ERCOT, Nuclear_NE2020_sCap_ERCOT, Hydrogen_NE2020_sCap_ERCOT, Battery_NE2020_sCap_ERCOT,
             DAC_NE2020_sCap_ERCOT, Wind_NE2020_sCap_ERCOT, Solar_NE2020_sCap_ERCOT, CoalCCS_NE2020_sCap_ERCOT_2, CCCCS_NE2020_sCap_ERCOT_2,
             CC_NE2020_sCap_ERCOT_2, Nuclear_NE2020_sCap_ERCOT_2, Hydrogen_NE2020_sCap_ERCOT_2, Battery_NE2020_sCap_ERCOT_2,
             DAC_NE2020_sCap_ERCOT_2, Wind_NE2020_sCap_ERCOT_2, Solar_NE2020_sCap_ERCOT_2, CoalCCS_NE2050_sCap_ERCOT, CCCCS_NE2050_sCap_ERCOT, CC_NE2050_sCap_ERCOT, Nuclear_NE2050_sCap_ERCOT, Hydrogen_NE2050_sCap_ERCOT, Battery_NE2050_sCap_ERCOT,
             DAC_NE2050_sCap_ERCOT, Wind_NE2050_sCap_ERCOT, Solar_NE2050_sCap_ERCOT, CoalCCS_NE2050_sCap_ERCOT_2, CCCCS_NE2050_sCap_ERCOT_2, CC_NE2050_sCap_ERCOT_2, Nuclear_NE2050_sCap_ERCOT_2,
             Hydrogen_NE2050_sCap_ERCOT_2, Battery_NE2050_sCap_ERCOT_2, DAC_NE2050_sCap_ERCOT_2,
             Wind_NE2050_sCap_ERCOT_2, Solar_NE2050_sCap_ERCOT_2):


  region_Col = ['Reference', 'Reference', 'Reference', 'No H2', 'No H2', 'No H2', 'No CCS', 'No CCS', 'No CCS',
                'High Elec', 'High Elec', 'High Elec', 'Lim Trans', 'Lim Trans', 'Lim Trans', 'Low Cap', 'Low Cap', 'Low Cap']
  planning_Col = ['Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now']

  CC_ref = [CC_NE2050_ref_EI-CC_NE2050_ref_EI_2, CC_NE2050_ref_EI_2, CC_NE2020_ref_EI,
            CC_NE2050_lh2_EI-CC_NE2050_lh2_EI_2, CC_NE2050_lh2_EI_2, CC_NE2020_lh2_EI,
            CC_NE2050_lccs_EI-CC_NE2050_lccs_EI_2, CC_NE2050_lccs_EI_2, CC_NE2020_lccs_EI,
            CC_NE2050_he_EI-CC_NE2050_he_EI_2, CC_NE2050_he_EI_2, CC_NE2020_he_EI,
            CC_NE2050_ltrans_EI-CC_NE2050_ltrans_EI_2, CC_NE2050_ltrans_EI_2, CC_NE2020_ltrans_EI,
            CC_NE2050_sCap_EI - CC_NE2050_sCap_EI_2, CC_NE2050_sCap_EI_2, CC_NE2020_sCap_EI]
  planType_CC = ['NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC',
                 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC',
                 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC']

  CCCCS_ref = [CCCCS_NE2050_ref_EI - CCCCS_NE2050_ref_EI_2, CCCCS_NE2050_ref_EI_2, CCCCS_NE2020_ref_EI,
               CCCCS_NE2050_lh2_EI - CCCCS_NE2050_lh2_EI_2, CCCCS_NE2050_lh2_EI_2, CCCCS_NE2020_lh2_EI,
               CCCCS_NE2050_lccs_EI - CCCCS_NE2050_lccs_EI_2, CCCCS_NE2050_lccs_EI_2, CCCCS_NE2020_lccs_EI,
               CCCCS_NE2050_he_EI - CCCCS_NE2050_he_EI_2, CCCCS_NE2050_he_EI_2, CCCCS_NE2020_he_EI,
               CCCCS_NE2050_ltrans_EI - CCCCS_NE2050_ltrans_EI_2, CCCCS_NE2050_ltrans_EI_2, CCCCS_NE2020_ltrans_EI,
               CCCCS_NE2050_sCap_EI - CCCCS_NE2050_sCap_EI_2, CCCCS_NE2050_sCap_EI_2, CCCCS_NE2020_sCap_EI]
  planType_CCCCS = ['NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS',
                    'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS',
                    'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS']

  Nuclear_ref = [Nuclear_NE2050_ref_EI - Nuclear_NE2050_ref_EI_2, Nuclear_NE2050_ref_EI_2, Nuclear_NE2020_ref_EI,
                Nuclear_NE2050_lh2_EI - Nuclear_NE2050_lh2_EI_2, Nuclear_NE2050_lh2_EI_2, Nuclear_NE2020_lh2_EI,
                Nuclear_NE2050_lccs_EI - Nuclear_NE2050_lccs_EI_2, Nuclear_NE2050_lccs_EI_2, Nuclear_NE2020_lccs_EI,
                Nuclear_NE2050_he_EI - Nuclear_NE2050_he_EI_2, Nuclear_NE2050_he_EI_2, Nuclear_NE2020_he_EI,
                Nuclear_NE2050_ltrans_EI - Nuclear_NE2050_ltrans_EI_2, Nuclear_NE2050_ltrans_EI_2, Nuclear_NE2020_ltrans_EI,
                Nuclear_NE2050_sCap_EI - Nuclear_NE2050_sCap_EI_2, Nuclear_NE2050_sCap_EI_2, Nuclear_NE2020_sCap_EI]
  planType_Nuclear = ['Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear',
                      'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear',
                      'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear']

  H2_ref = [Hydrogen_NE2050_ref_EI - Hydrogen_NE2050_ref_EI_2, Hydrogen_NE2050_ref_EI_2, Hydrogen_NE2020_ref_EI,
                Hydrogen_NE2050_lh2_EI - Hydrogen_NE2050_lh2_EI_2, Hydrogen_NE2050_lh2_EI_2, Hydrogen_NE2020_lh2_EI,
                Hydrogen_NE2050_lccs_EI - Hydrogen_NE2050_lccs_EI_2, Hydrogen_NE2050_lccs_EI_2, Hydrogen_NE2020_lccs_EI,
                Hydrogen_NE2050_he_EI - Hydrogen_NE2050_he_EI_2, Hydrogen_NE2050_he_EI_2, Hydrogen_NE2020_he_EI,
                Hydrogen_NE2050_ltrans_EI - Hydrogen_NE2050_ltrans_EI_2, Hydrogen_NE2050_ltrans_EI_2, Hydrogen_NE2020_ltrans_EI,
                Hydrogen_NE2050_sCap_EI - Hydrogen_NE2050_sCap_EI_2, Hydrogen_NE2050_sCap_EI_2, Hydrogen_NE2020_sCap_EI]
  planType_H2 = ['Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen',
                 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen',
                 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen']

  Bat_ref = [Battery_NE2050_ref_EI - Battery_NE2050_ref_EI_2, Battery_NE2050_ref_EI_2, Battery_NE2020_ref_EI,
                Battery_NE2050_lh2_EI - Battery_NE2050_lh2_EI_2, Battery_NE2050_lh2_EI_2, Battery_NE2020_lh2_EI,
                Battery_NE2050_lccs_EI - Battery_NE2050_lccs_EI_2, Battery_NE2050_lccs_EI_2, Battery_NE2020_lccs_EI,
                Battery_NE2050_he_EI - Battery_NE2050_he_EI_2, Battery_NE2050_he_EI_2, Battery_NE2020_he_EI,
                Battery_NE2050_ltrans_EI - Battery_NE2050_ltrans_EI_2, Battery_NE2050_ltrans_EI_2, Battery_NE2020_ltrans_EI,
                Battery_NE2050_sCap_EI - Battery_NE2050_sCap_EI_2, Battery_NE2050_sCap_EI_2, Battery_NE2020_sCap_EI]
  planType_Bat = ['Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery',
                 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery',
                 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery']

  DAC_ref = [-(DAC_NE2050_ref_EI - DAC_NE2050_ref_EI_2), -DAC_NE2050_ref_EI_2, -DAC_NE2020_ref_EI,
                -(DAC_NE2050_lh2_EI - DAC_NE2050_lh2_EI_2), -DAC_NE2050_lh2_EI_2, -DAC_NE2020_lh2_EI,
                -(DAC_NE2050_lccs_EI - DAC_NE2050_lccs_EI_2), -DAC_NE2050_lccs_EI_2, -DAC_NE2020_lccs_EI,
                -(DAC_NE2050_he_EI - DAC_NE2050_he_EI_2), -DAC_NE2050_he_EI_2, -DAC_NE2020_he_EI,
                -(DAC_NE2050_ltrans_EI - DAC_NE2050_ltrans_EI_2), -DAC_NE2050_ltrans_EI_2, -DAC_NE2020_ltrans_EI,
                -(DAC_NE2050_sCap_EI - DAC_NE2050_sCap_EI_2), -DAC_NE2050_sCap_EI_2, -DAC_NE2020_sCap_EI]
  planType_DAC = ['DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS',
                 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS',
                 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS']

  Wind_ref = [Wind_NE2050_ref_EI - Wind_NE2050_ref_EI_2, Wind_NE2050_ref_EI_2, Wind_NE2020_ref_EI,
                Wind_NE2050_lh2_EI - Wind_NE2050_lh2_EI_2, Wind_NE2050_lh2_EI_2, Wind_NE2020_lh2_EI,
                Wind_NE2050_lccs_EI - Wind_NE2050_lccs_EI_2, Wind_NE2050_lccs_EI_2, Wind_NE2020_lccs_EI,
                Wind_NE2050_he_EI - Wind_NE2050_he_EI_2, Wind_NE2050_he_EI_2, Wind_NE2020_he_EI,
                Wind_NE2050_ltrans_EI - Wind_NE2050_ltrans_EI_2, Wind_NE2050_ltrans_EI_2, Wind_NE2020_ltrans_EI,
                Wind_NE2050_sCap_EI - Wind_NE2050_sCap_EI_2, Wind_NE2050_sCap_EI_2, Wind_NE2020_sCap_EI]
  planType_Wind = ['Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind',
                 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind',
                 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind']

  Solar_ref = [Solar_NE2050_ref_EI - Solar_NE2050_ref_EI_2, Solar_NE2050_ref_EI_2, Solar_NE2020_ref_EI,
                Solar_NE2050_lh2_EI - Solar_NE2050_lh2_EI_2, Solar_NE2050_lh2_EI_2, Solar_NE2020_lh2_EI,
                Solar_NE2050_lccs_EI - Solar_NE2050_lccs_EI_2, Solar_NE2050_lccs_EI_2, Solar_NE2020_lccs_EI,
                Solar_NE2050_he_EI - Solar_NE2050_he_EI_2, Solar_NE2050_he_EI_2, Solar_NE2020_he_EI,
                Solar_NE2050_ltrans_EI - Solar_NE2050_ltrans_EI_2, Solar_NE2050_ltrans_EI_2, Solar_NE2020_ltrans_EI,
                Solar_NE2050_sCap_EI - Solar_NE2050_sCap_EI_2, Solar_NE2050_sCap_EI_2, Solar_NE2020_sCap_EI]
  planType_Solar = ['Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV',
                 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV',
                 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV']

  filler_ref_tot = (CC_NE2050_ref_EI + CCCCS_NE2050_ref_EI + Nuclear_NE2050_ref_EI + Hydrogen_NE2050_ref_EI + Battery_NE2050_ref_EI \
                - DAC_NE2050_ref_EI + Wind_NE2050_ref_EI + Solar_NE2050_ref_EI) - \
               (CC_NE2050_ref_EI_2 + CCCCS_NE2050_ref_EI_2 + Nuclear_NE2050_ref_EI_2 + Hydrogen_NE2050_ref_EI_2 + Battery_NE2050_ref_EI_2 \
                - DAC_NE2050_ref_EI_2 + Wind_NE2050_ref_EI_2 + Solar_NE2050_ref_EI_2)

  filler_lh2_tot = (CC_NE2050_lh2_EI + CCCCS_NE2050_lh2_EI + Nuclear_NE2050_lh2_EI + Hydrogen_NE2050_lh2_EI + Battery_NE2050_lh2_EI \
                    - DAC_NE2050_lh2_EI + Wind_NE2050_lh2_EI + Solar_NE2050_lh2_EI) - \
                   (CC_NE2050_lh2_EI_2 + CCCCS_NE2050_lh2_EI_2 + Nuclear_NE2050_lh2_EI_2 + Hydrogen_NE2050_lh2_EI_2 + Battery_NE2050_lh2_EI_2 \
                    - DAC_NE2050_lh2_EI_2 + Wind_NE2050_lh2_EI_2 + Solar_NE2050_lh2_EI_2)
  filler_lccs_tot = (CC_NE2050_lccs_EI + CCCCS_NE2050_lccs_EI + Nuclear_NE2050_lccs_EI + Hydrogen_NE2050_lccs_EI + Battery_NE2050_lccs_EI \
                     - DAC_NE2050_lccs_EI + Wind_NE2050_lccs_EI + Solar_NE2050_lccs_EI) - \
                    (CC_NE2050_lccs_EI_2 + CCCCS_NE2050_lccs_EI_2 + Nuclear_NE2050_lccs_EI_2 + Hydrogen_NE2050_lccs_EI_2 + Battery_NE2050_lccs_EI_2 \
                     - DAC_NE2050_lccs_EI_2 + Wind_NE2050_lccs_EI_2 + Solar_NE2050_lccs_EI_2)

  filler_he_tot = (CC_NE2050_he_EI + CCCCS_NE2050_he_EI + Nuclear_NE2050_he_EI + Hydrogen_NE2050_he_EI + Battery_NE2050_he_EI \
                   - DAC_NE2050_he_EI + Wind_NE2050_he_EI + Solar_NE2050_he_EI) - \
                  (CC_NE2050_he_EI_2 + CCCCS_NE2050_he_EI_2 + Nuclear_NE2050_he_EI_2 + Hydrogen_NE2050_he_EI_2 + Battery_NE2050_he_EI_2 \
                   - DAC_NE2050_he_EI_2 + Wind_NE2050_he_EI_2 + Solar_NE2050_he_EI_2)

  filler_ltrans_tot = (CC_NE2050_ltrans_EI + CCCCS_NE2050_ltrans_EI + Nuclear_NE2050_ltrans_EI + Hydrogen_NE2050_ltrans_EI + Battery_NE2050_ltrans_EI \
                       - DAC_NE2050_ltrans_EI + Wind_NE2050_ltrans_EI + Solar_NE2050_ltrans_EI) - \
                      (CC_NE2050_ltrans_EI_2 + CCCCS_NE2050_ltrans_EI_2 + Nuclear_NE2050_ltrans_EI_2 + Hydrogen_NE2050_ltrans_EI_2 + Battery_NE2050_ltrans_EI_2 \
                       - DAC_NE2050_ltrans_EI_2 + Wind_NE2050_ltrans_EI_2 + Solar_NE2050_ltrans_EI_2)

  filler_sCap_tot = (CC_NE2050_sCap_EI + CCCCS_NE2050_sCap_EI + Nuclear_NE2050_sCap_EI + Hydrogen_NE2050_sCap_EI + Battery_NE2050_sCap_EI \
                     - DAC_NE2050_sCap_EI + Wind_NE2050_sCap_EI + Solar_NE2050_sCap_EI) - \
                    (CC_NE2050_sCap_EI_2 + CCCCS_NE2050_sCap_EI_2 + Nuclear_NE2050_sCap_EI_2 + Hydrogen_NE2050_sCap_EI_2 + Battery_NE2050_sCap_EI_2 \
                     - DAC_NE2050_sCap_EI_2 + Wind_NE2050_sCap_EI_2 + Solar_NE2050_sCap_EI_2)

  filerer_ref = [0, filler_ref_tot, 0, 0, filler_lh2_tot, 0, 0, filler_lccs_tot, 0,
                 0, filler_he_tot, 0, 0, filler_ltrans_tot, 0, 0, filler_sCap_tot, 0]
  planType_filler = ['', '', '', '', '', '','', '', '', '', '', '','', '', '', '', '', '']

  capEXP_ref = np.hstack((CC_ref, CCCCS_ref, Nuclear_ref, H2_ref, Bat_ref, DAC_ref, Wind_ref, Solar_ref, filerer_ref))
  planType_ref = np.hstack((planType_CC, planType_CCCCS, planType_Nuclear, planType_H2,
                            planType_Bat, planType_DAC, planType_Wind, planType_Solar, planType_filler))
  region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col,  planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col,planning_Col))

  cap_ref = np.vstack((region_ref, planning_ref, planType_ref, capEXP_ref))
  df_capEXP_ref = pd.DataFrame(cap_ref)
  df_capEXP_ref = df_capEXP_ref.transpose()
  df_capEXP_ref.rename({0: 'Scenario', 1: 'PlanningScr', 2: 'Technology', 3: 'Capacity'},axis=1, inplace=True)
  df_capEXP_ref = df_capEXP_ref.astype({'Capacity': float})

  # ERCOT:

  CC_ref = [CC_NE2050_ref_ERCOT - CC_NE2050_ref_ERCOT_2, CC_NE2050_ref_ERCOT_2, CC_NE2020_ref_ERCOT,
            CC_NE2050_lh2_ERCOT - CC_NE2050_lh2_ERCOT_2, CC_NE2050_lh2_ERCOT_2, CC_NE2020_lh2_ERCOT,
            CC_NE2050_lccs_ERCOT - CC_NE2050_lccs_ERCOT_2, CC_NE2050_lccs_ERCOT_2, CC_NE2020_lccs_ERCOT,
            CC_NE2050_he_ERCOT - CC_NE2050_he_ERCOT_2, CC_NE2050_he_ERCOT_2, CC_NE2020_he_ERCOT,
            CC_NE2050_ltrans_ERCOT - CC_NE2050_ltrans_ERCOT_2, CC_NE2050_ltrans_ERCOT_2, CC_NE2020_ltrans_ERCOT,
            CC_NE2050_sCap_ERCOT - CC_NE2050_sCap_ERCOT_2, CC_NE2050_sCap_ERCOT_2, CC_NE2020_sCap_ERCOT]
  planType_CC = ['NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC',
                 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC',
                 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC']

  CCCCS_ref = [CCCCS_NE2050_ref_ERCOT - CCCCS_NE2050_ref_ERCOT_2, CCCCS_NE2050_ref_ERCOT_2, CCCCS_NE2020_ref_ERCOT,
               CCCCS_NE2050_lh2_ERCOT - CCCCS_NE2050_lh2_ERCOT_2, CCCCS_NE2050_lh2_ERCOT_2, CCCCS_NE2020_lh2_ERCOT,
               CCCCS_NE2050_lccs_ERCOT - CCCCS_NE2050_lccs_ERCOT_2, CCCCS_NE2050_lccs_ERCOT_2, CCCCS_NE2020_lccs_ERCOT,
               CCCCS_NE2050_he_ERCOT - CCCCS_NE2050_he_ERCOT_2, CCCCS_NE2050_he_ERCOT_2, CCCCS_NE2020_he_ERCOT,
               CCCCS_NE2050_ltrans_ERCOT - CCCCS_NE2050_ltrans_ERCOT_2, CCCCS_NE2050_ltrans_ERCOT_2, CCCCS_NE2020_ltrans_ERCOT,
               CCCCS_NE2050_sCap_ERCOT - CCCCS_NE2050_sCap_ERCOT_2, CCCCS_NE2050_sCap_ERCOT_2, CCCCS_NE2020_sCap_ERCOT]
  planType_CCCCS = ['NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS',
                    'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS',
                    'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS']

  Nuclear_ref = [Nuclear_NE2050_ref_ERCOT - Nuclear_NE2050_ref_ERCOT_2, Nuclear_NE2050_ref_ERCOT_2, Nuclear_NE2020_ref_ERCOT,
                 Nuclear_NE2050_lh2_ERCOT - Nuclear_NE2050_lh2_ERCOT_2, Nuclear_NE2050_lh2_ERCOT_2, Nuclear_NE2020_lh2_ERCOT,
                 Nuclear_NE2050_lccs_ERCOT - Nuclear_NE2050_lccs_ERCOT_2, Nuclear_NE2050_lccs_ERCOT_2, Nuclear_NE2020_lccs_ERCOT,
                 Nuclear_NE2050_he_ERCOT - Nuclear_NE2050_he_ERCOT_2, Nuclear_NE2050_he_ERCOT_2, Nuclear_NE2020_he_ERCOT,
                 Nuclear_NE2050_ltrans_ERCOT - Nuclear_NE2050_ltrans_ERCOT_2, Nuclear_NE2050_ltrans_ERCOT_2, Nuclear_NE2020_ltrans_ERCOT,
                 Nuclear_NE2050_sCap_ERCOT - Nuclear_NE2050_sCap_ERCOT_2, Nuclear_NE2050_sCap_ERCOT_2, Nuclear_NE2020_sCap_ERCOT]
  planType_Nuclear = ['Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear',
                      'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear',
                      'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear']

  H2_ref = [Hydrogen_NE2050_ref_ERCOT - Hydrogen_NE2050_ref_ERCOT_2, Hydrogen_NE2050_ref_ERCOT_2, Hydrogen_NE2020_ref_ERCOT,
            Hydrogen_NE2050_lh2_ERCOT - Hydrogen_NE2050_lh2_ERCOT_2, Hydrogen_NE2050_lh2_ERCOT_2, Hydrogen_NE2020_lh2_ERCOT,
            Hydrogen_NE2050_lccs_ERCOT - Hydrogen_NE2050_lccs_ERCOT_2, Hydrogen_NE2050_lccs_ERCOT_2, Hydrogen_NE2020_lccs_ERCOT,
            Hydrogen_NE2050_he_ERCOT - Hydrogen_NE2050_he_ERCOT_2, Hydrogen_NE2050_he_ERCOT_2, Hydrogen_NE2020_he_ERCOT,
            Hydrogen_NE2050_ltrans_ERCOT - Hydrogen_NE2050_ltrans_ERCOT_2, Hydrogen_NE2050_ltrans_ERCOT_2, Hydrogen_NE2020_ltrans_ERCOT,
            Hydrogen_NE2050_sCap_ERCOT - Hydrogen_NE2050_sCap_ERCOT_2, Hydrogen_NE2050_sCap_ERCOT_2, Hydrogen_NE2020_sCap_ERCOT]
  planType_H2 = ['Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen',
                 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen',
                 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen']

  Bat_ref = [Battery_NE2050_ref_ERCOT - Battery_NE2050_ref_ERCOT_2, Battery_NE2050_ref_ERCOT_2, Battery_NE2020_ref_ERCOT,
             Battery_NE2050_lh2_ERCOT - Battery_NE2050_lh2_ERCOT_2, Battery_NE2050_lh2_ERCOT_2, Battery_NE2020_lh2_ERCOT,
             Battery_NE2050_lccs_ERCOT - Battery_NE2050_lccs_ERCOT_2, Battery_NE2050_lccs_ERCOT_2, Battery_NE2020_lccs_ERCOT,
             Battery_NE2050_he_ERCOT - Battery_NE2050_he_ERCOT_2, Battery_NE2050_he_ERCOT_2, Battery_NE2020_he_ERCOT,
             Battery_NE2050_ltrans_ERCOT - Battery_NE2050_ltrans_ERCOT_2, Battery_NE2050_ltrans_ERCOT_2, Battery_NE2020_ltrans_ERCOT,
             Battery_NE2050_sCap_ERCOT - Battery_NE2050_sCap_ERCOT_2, Battery_NE2050_sCap_ERCOT_2, Battery_NE2020_sCap_ERCOT]
  planType_Bat = ['Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery',
                  'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery',
                  'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery']

  DAC_ref = [-(DAC_NE2050_ref_ERCOT - DAC_NE2050_ref_ERCOT_2), -DAC_NE2050_ref_ERCOT_2, -DAC_NE2020_ref_ERCOT,
             -(DAC_NE2050_lh2_ERCOT - DAC_NE2050_lh2_ERCOT_2), -DAC_NE2050_lh2_ERCOT_2, -DAC_NE2020_lh2_ERCOT,
             -(DAC_NE2050_lccs_ERCOT - DAC_NE2050_lccs_ERCOT_2), -DAC_NE2050_lccs_ERCOT_2, -DAC_NE2020_lccs_ERCOT,
             -(DAC_NE2050_he_ERCOT - DAC_NE2050_he_ERCOT_2), -DAC_NE2050_he_ERCOT_2, -DAC_NE2020_he_ERCOT,
             -(DAC_NE2050_ltrans_ERCOT - DAC_NE2050_ltrans_ERCOT_2), -DAC_NE2050_ltrans_ERCOT_2, -DAC_NE2020_ltrans_ERCOT,
             -(DAC_NE2050_sCap_ERCOT - DAC_NE2050_sCap_ERCOT_2), -DAC_NE2050_sCap_ERCOT_2, -DAC_NE2020_sCap_ERCOT]
  planType_DAC = ['DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS',
                  'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS',
                  'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS']

  Wind_ref = [Wind_NE2050_ref_ERCOT - Wind_NE2050_ref_ERCOT_2, Wind_NE2050_ref_ERCOT_2, Wind_NE2020_ref_ERCOT,
              Wind_NE2050_lh2_ERCOT - Wind_NE2050_lh2_ERCOT_2, Wind_NE2050_lh2_ERCOT_2, Wind_NE2020_lh2_ERCOT,
              Wind_NE2050_lccs_ERCOT - Wind_NE2050_lccs_ERCOT_2, Wind_NE2050_lccs_ERCOT_2, Wind_NE2020_lccs_ERCOT,
              Wind_NE2050_he_ERCOT - Wind_NE2050_he_ERCOT_2, Wind_NE2050_he_ERCOT_2, Wind_NE2020_he_ERCOT,
              Wind_NE2050_ltrans_ERCOT - Wind_NE2050_ltrans_ERCOT_2, Wind_NE2050_ltrans_ERCOT_2, Wind_NE2020_ltrans_ERCOT,
              Wind_NE2050_sCap_ERCOT - Wind_NE2050_sCap_ERCOT_2, Wind_NE2050_sCap_ERCOT_2, Wind_NE2020_sCap_ERCOT]
  planType_Wind = ['Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind',
                   'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind',
                   'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind']

  Solar_ref = [Solar_NE2050_ref_ERCOT - Solar_NE2050_ref_ERCOT_2, Solar_NE2050_ref_ERCOT_2, Solar_NE2020_ref_ERCOT,
               Solar_NE2050_lh2_ERCOT - Solar_NE2050_lh2_ERCOT_2, Solar_NE2050_lh2_ERCOT_2, Solar_NE2020_lh2_ERCOT,
               Solar_NE2050_lccs_ERCOT - Solar_NE2050_lccs_ERCOT_2, Solar_NE2050_lccs_ERCOT_2, Solar_NE2020_lccs_ERCOT,
               Solar_NE2050_he_ERCOT - Solar_NE2050_he_ERCOT_2, Solar_NE2050_he_ERCOT_2, Solar_NE2020_he_ERCOT,
               Solar_NE2050_ltrans_ERCOT - Solar_NE2050_ltrans_ERCOT_2, Solar_NE2050_ltrans_ERCOT_2, Solar_NE2020_ltrans_ERCOT,
               Solar_NE2050_sCap_ERCOT - Solar_NE2050_sCap_ERCOT_2, Solar_NE2050_sCap_ERCOT_2, Solar_NE2020_sCap_ERCOT]
  planType_Solar = ['Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV',
                    'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV',
                    'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV']

  filler_ref_tot = (CC_NE2050_ref_ERCOT + CCCCS_NE2050_ref_ERCOT + Nuclear_NE2050_ref_ERCOT + Hydrogen_NE2050_ref_ERCOT + Battery_NE2050_ref_ERCOT \
                    - DAC_NE2050_ref_ERCOT + Wind_NE2050_ref_ERCOT + Solar_NE2050_ref_ERCOT) - \
                   (CC_NE2050_ref_ERCOT_2 + CCCCS_NE2050_ref_ERCOT_2 + Nuclear_NE2050_ref_ERCOT_2 + Hydrogen_NE2050_ref_ERCOT_2 + Battery_NE2050_ref_ERCOT_2 \
                    - DAC_NE2050_ref_ERCOT_2 + Wind_NE2050_ref_ERCOT_2 + Solar_NE2050_ref_ERCOT_2)

  filler_lh2_tot = (CC_NE2050_lh2_ERCOT + CCCCS_NE2050_lh2_ERCOT + Nuclear_NE2050_lh2_ERCOT + Hydrogen_NE2050_lh2_ERCOT + Battery_NE2050_lh2_ERCOT \
                    - DAC_NE2050_lh2_ERCOT + Wind_NE2050_lh2_ERCOT + Solar_NE2050_lh2_ERCOT) - \
                   (CC_NE2050_lh2_ERCOT_2 + CCCCS_NE2050_lh2_ERCOT_2 + Nuclear_NE2050_lh2_ERCOT_2 + Hydrogen_NE2050_lh2_ERCOT_2 + Battery_NE2050_lh2_ERCOT_2 \
                    - DAC_NE2050_lh2_ERCOT_2 + Wind_NE2050_lh2_ERCOT_2 + Solar_NE2050_lh2_ERCOT_2)
  filler_lccs_tot = (CC_NE2050_lccs_ERCOT + CCCCS_NE2050_lccs_ERCOT + Nuclear_NE2050_lccs_ERCOT + Hydrogen_NE2050_lccs_ERCOT + Battery_NE2050_lccs_ERCOT \
                     - DAC_NE2050_lccs_ERCOT + Wind_NE2050_lccs_ERCOT + Solar_NE2050_lccs_ERCOT) - \
                    (CC_NE2050_lccs_ERCOT_2 + CCCCS_NE2050_lccs_ERCOT_2 + Nuclear_NE2050_lccs_ERCOT_2 + Hydrogen_NE2050_lccs_ERCOT_2 + Battery_NE2050_lccs_ERCOT_2 \
                     - DAC_NE2050_lccs_ERCOT_2 + Wind_NE2050_lccs_ERCOT_2 + Solar_NE2050_lccs_ERCOT_2)

  filler_he_tot = (CC_NE2050_he_ERCOT + CCCCS_NE2050_he_ERCOT + Nuclear_NE2050_he_ERCOT + Hydrogen_NE2050_he_ERCOT + Battery_NE2050_he_ERCOT \
                   - DAC_NE2050_he_ERCOT + Wind_NE2050_he_ERCOT + Solar_NE2050_he_ERCOT) - \
                  (CC_NE2050_he_ERCOT_2 + CCCCS_NE2050_he_ERCOT_2 + Nuclear_NE2050_he_ERCOT_2 + Hydrogen_NE2050_he_ERCOT_2 + Battery_NE2050_he_ERCOT_2 \
                   - DAC_NE2050_he_ERCOT_2 + Wind_NE2050_he_ERCOT_2 + Solar_NE2050_he_ERCOT_2)

  filler_ltrans_tot = (CC_NE2050_ltrans_ERCOT + CCCCS_NE2050_ltrans_ERCOT + Nuclear_NE2050_ltrans_ERCOT + Hydrogen_NE2050_ltrans_ERCOT + Battery_NE2050_ltrans_ERCOT \
                       - DAC_NE2050_ltrans_ERCOT + Wind_NE2050_ltrans_ERCOT + Solar_NE2050_ltrans_ERCOT) - \
                      (CC_NE2050_ltrans_ERCOT_2 + CCCCS_NE2050_ltrans_ERCOT_2 + Nuclear_NE2050_ltrans_ERCOT_2 + Hydrogen_NE2050_ltrans_ERCOT_2 + Battery_NE2050_ltrans_ERCOT_2 \
                       - DAC_NE2050_ltrans_ERCOT_2 + Wind_NE2050_ltrans_ERCOT_2 + Solar_NE2050_ltrans_ERCOT_2)

  filler_sCap_tot = (CC_NE2050_sCap_ERCOT + CCCCS_NE2050_sCap_ERCOT + Nuclear_NE2050_sCap_ERCOT + Hydrogen_NE2050_sCap_ERCOT + Battery_NE2050_sCap_ERCOT \
                     - DAC_NE2050_sCap_ERCOT + Wind_NE2050_sCap_ERCOT + Solar_NE2050_sCap_ERCOT) - \
                    (CC_NE2050_sCap_ERCOT_2 + CCCCS_NE2050_sCap_ERCOT_2 + Nuclear_NE2050_sCap_ERCOT_2 + Hydrogen_NE2050_sCap_ERCOT_2 + Battery_NE2050_sCap_ERCOT_2 \
                     - DAC_NE2050_sCap_ERCOT_2 + Wind_NE2050_sCap_ERCOT_2 + Solar_NE2050_sCap_ERCOT_2)

  filerer_ref = [0, filler_ref_tot, 0, 0, filler_lh2_tot, 0, 0, filler_lccs_tot, 0,
                 0, filler_he_tot, 0, 0, filler_ltrans_tot, 0, 0, filler_sCap_tot, 0]
  planType_filler = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

  capEXP_ref = np.hstack((CC_ref, CCCCS_ref, Nuclear_ref, H2_ref, Bat_ref, DAC_ref, Wind_ref, Solar_ref, filerer_ref))
  planType_ref = np.hstack((planType_CC, planType_CCCCS, planType_Nuclear, planType_H2, planType_Bat,
                            planType_DAC, planType_Wind, planType_Solar, planType_filler))
  region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col, planning_Col, planning_Col, planning_Col,
                            planning_Col, planning_Col, planning_Col, planning_Col))

  cap_ref_ERCOT = np.vstack((region_ref, planning_ref, planType_ref, capEXP_ref))
  df_capEXP_ref_ERCOT = pd.DataFrame(cap_ref_ERCOT)
  df_capEXP_ref_ERCOT = df_capEXP_ref_ERCOT.transpose()
  df_capEXP_ref_ERCOT.rename({0: 'Scenario', 1: 'PlanningScr', 2: 'Technology', 3: 'Capacity'}, axis=1, inplace=True)
  df_capEXP_ref_ERCOT = df_capEXP_ref_ERCOT.astype({'Capacity': float})

  return df_capEXP_ref, df_capEXP_ref_ERCOT

def graphCosts(totCost_NE2020_ref_EI, opCost_data_NE2020_ref_EI, fixedCost_data_NE2020_ref_EI,
                totCost_NE2020_ref_EI_2, opCost_data_NE2020_ref_EI_2, fixedCost_data_NE2020_ref_EI_2,
                totCost_NE2050_ref_EI, opCost_data_NE2050_ref_EI, fixedCost_data_NE2050_ref_EI,
                totCost_NE2050_ref_EI_2, opCost_data_NE2050_ref_EI_2, fixedCost_data_NE2050_ref_EI_2,
                totCost_NE2020_ref_ERCOT, opCost_data_NE2020_ref_ERCOT, fixedCost_data_NE2020_ref_ERCOT,
                totCost_NE2020_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT_2,
                totCost_NE2050_ref_ERCOT, opCost_data_NE2050_ref_ERCOT, fixedCost_data_NE2050_ref_ERCOT,
                totCost_NE2050_ref_ERCOT_2, opCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2050_ref_ERCOT_2,
                totCost_NE2020_lh2_EI, opCost_data_NE2020_lh2_EI, fixedCost_data_NE2020_lh2_EI,
                totCost_NE2020_lh2_EI_2, opCost_data_NE2020_lh2_EI_2, fixedCost_data_NE2020_lh2_EI_2,
                totCost_NE2050_lh2_EI, opCost_data_NE2050_lh2_EI, fixedCost_data_NE2050_lh2_EI,
                totCost_NE2050_lh2_EI_2, opCost_data_NE2050_lh2_EI_2, fixedCost_data_NE2050_lh2_EI_2,
                totCost_NE2020_lh2_ERCOT, opCost_data_NE2020_lh2_ERCOT, fixedCost_data_NE2020_lh2_ERCOT,
                totCost_NE2020_lh2_ERCOT_2, opCost_data_NE2020_lh2_ERCOT_2, fixedCost_data_NE2020_lh2_ERCOT_2,
                totCost_NE2050_lh2_ERCOT, opCost_data_NE2050_lh2_ERCOT, fixedCost_data_NE2050_lh2_ERCOT,
                totCost_NE2050_lh2_ERCOT_2, opCost_data_NE2050_lh2_ERCOT_2, fixedCost_data_NE2050_lh2_ERCOT_2,
                totCost_NE2020_lccs_EI, opCost_data_NE2020_lccs_EI, fixedCost_data_NE2020_lccs_EI,
                totCost_NE2020_lccs_EI_2, opCost_data_NE2020_lccs_EI_2, fixedCost_data_NE2020_lccs_EI_2,
                totCost_NE2050_lccs_EI, opCost_data_NE2050_lccs_EI, fixedCost_data_NE2050_lccs_EI,
                totCost_NE2050_lccs_EI_2, opCost_data_NE2050_lccs_EI_2, fixedCost_data_NE2050_lccs_EI_2,
                totCost_NE2020_lccs_ERCOT, opCost_data_NE2020_lccs_ERCOT, fixedCost_data_NE2020_lccs_ERCOT,
                totCost_NE2020_lccs_ERCOT_2, opCost_data_NE2020_lccs_ERCOT_2, fixedCost_data_NE2020_lccs_ERCOT_2,
                totCost_NE2050_lccs_ERCOT, opCost_data_NE2050_lccs_ERCOT, fixedCost_data_NE2050_lccs_ERCOT,
                totCost_NE2050_lccs_ERCOT_2, opCost_data_NE2050_lccs_ERCOT_2, fixedCost_data_NE2050_lccs_ERCOT_2,
                totCost_NE2020_he_EI, opCost_data_NE2020_he_EI, fixedCost_data_NE2020_he_EI,
                totCost_NE2020_he_EI_2, opCost_data_NE2020_he_EI_2, fixedCost_data_NE2020_he_EI_2,
                totCost_NE2050_he_EI, opCost_data_NE2050_he_EI, fixedCost_data_NE2050_he_EI,
                totCost_NE2050_he_EI_2, opCost_data_NE2050_he_EI_2, fixedCost_data_NE2050_he_EI_2,
                totCost_NE2020_he_ERCOT, opCost_data_NE2020_he_ERCOT, fixedCost_data_NE2020_he_ERCOT,
                totCost_NE2020_he_ERCOT_2, opCost_data_NE2020_he_ERCOT_2, fixedCost_data_NE2020_he_ERCOT_2,
                totCost_NE2050_he_ERCOT, opCost_data_NE2050_he_ERCOT, fixedCost_data_NE2050_he_ERCOT,
                totCost_NE2050_he_ERCOT_2, opCost_data_NE2050_he_ERCOT_2, fixedCost_data_NE2050_he_ERCOT_2,
                totCost_NE2020_ltrans_EI, opCost_data_NE2020_ltrans_EI, fixedCost_data_NE2020_ltrans_EI,
                totCost_NE2020_ltrans_EI_2, opCost_data_NE2020_ltrans_EI_2, fixedCost_data_NE2020_ltrans_EI_2,
                totCost_NE2050_ltrans_EI, opCost_data_NE2050_ltrans_EI, fixedCost_data_NE2050_ltrans_EI,
                totCost_NE2050_ltrans_EI_2, opCost_data_NE2050_ltrans_EI_2, fixedCost_data_NE2050_ltrans_EI_2,
                totCost_NE2020_ltrans_ERCOT, opCost_data_NE2020_ltrans_ERCOT, fixedCost_data_NE2020_ltrans_ERCOT,
                totCost_NE2020_ltrans_ERCOT_2, opCost_data_NE2020_ltrans_ERCOT_2, fixedCost_data_NE2020_ltrans_ERCOT_2,
                totCost_NE2050_ltrans_ERCOT, opCost_data_NE2050_ltrans_ERCOT, fixedCost_data_NE2050_ltrans_ERCOT,
                totCost_NE2050_ltrans_ERCOT_2, opCost_data_NE2050_ltrans_ERCOT_2, fixedCost_data_NE2050_ltrans_ERCOT_2,
                totCost_NE2020_sCap_EI, opCost_data_NE2020_sCap_EI, fixedCost_data_NE2020_sCap_EI,
                totCost_NE2020_sCap_EI_2, opCost_data_NE2020_sCap_EI_2, fixedCost_data_NE2020_sCap_EI_2,
                totCost_NE2050_sCap_EI, opCost_data_NE2050_sCap_EI, fixedCost_data_NE2050_sCap_EI,
                totCost_NE2050_sCap_EI_2, opCost_data_NE2050_sCap_EI_2, fixedCost_data_NE2050_sCap_EI_2,
                totCost_NE2020_sCap_ERCOT, opCost_data_NE2020_sCap_ERCOT, fixedCost_data_NE2020_sCap_ERCOT,
                totCost_NE2020_sCap_ERCOT_2, opCost_data_NE2020_sCap_ERCOT_2, fixedCost_data_NE2020_sCap_ERCOT_2,
                totCost_NE2050_sCap_ERCOT, opCost_data_NE2050_sCap_ERCOT, fixedCost_data_NE2050_sCap_ERCOT,
                totCost_NE2050_sCap_ERCOT_2, opCost_data_NE2050_sCap_ERCOT_2, fixedCost_data_NE2050_sCap_ERCOT_2):

  fixedCost_ref = [fixedCost_data_NE2050_ref_EI-fixedCost_data_NE2050_ref_EI_2, fixedCost_data_NE2050_ref_EI_2, fixedCost_data_NE2020_ref_EI,
                   fixedCost_data_NE2050_lh2_EI-fixedCost_data_NE2050_lh2_EI_2, fixedCost_data_NE2050_lh2_EI_2, fixedCost_data_NE2020_lh2_EI,
                   fixedCost_data_NE2050_lccs_EI-fixedCost_data_NE2050_lccs_EI_2, fixedCost_data_NE2050_lccs_EI_2, fixedCost_data_NE2020_lccs_EI,
                   fixedCost_data_NE2050_he_EI-fixedCost_data_NE2050_he_EI_2, fixedCost_data_NE2050_he_EI_2, fixedCost_data_NE2020_he_EI,
                   fixedCost_data_NE2050_ltrans_EI-fixedCost_data_NE2050_ltrans_EI_2, fixedCost_data_NE2050_ltrans_EI_2, fixedCost_data_NE2020_ltrans_EI,
                   fixedCost_data_NE2050_sCap_EI-fixedCost_data_NE2050_sCap_EI_2, fixedCost_data_NE2050_sCap_EI_2, fixedCost_data_NE2020_sCap_EI]
  fixedcostType_Col = ['Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost',
                       'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost',
                       'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost']
  region_Col = ['Reference', 'Reference', 'Reference', 'No H2', 'No H2', 'No H2', 'No CCS', 'No CCS', 'No CCS',
                'High Elec', 'High Elec', 'High Elec', 'Lim Trans', 'Lim Trans', 'Lim Trans','Low Cap','Low Cap','Low Cap']
  planning_Col = ['Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now']

  opCost_ref = [opCost_data_NE2050_ref_EI-opCost_data_NE2050_ref_EI_2, opCost_data_NE2050_ref_EI_2, opCost_data_NE2020_ref_EI,
                opCost_data_NE2050_lh2_EI-opCost_data_NE2050_lh2_EI_2, opCost_data_NE2050_lh2_EI_2, opCost_data_NE2020_lh2_EI,
                opCost_data_NE2050_lccs_EI-opCost_data_NE2050_lccs_EI_2, opCost_data_NE2050_lccs_EI_2, opCost_data_NE2020_lccs_EI,
                opCost_data_NE2050_he_EI-opCost_data_NE2050_he_EI_2, opCost_data_NE2050_he_EI_2, opCost_data_NE2020_he_EI,
                opCost_data_NE2050_ltrans_EI-opCost_data_NE2050_ltrans_EI_2, opCost_data_NE2050_ltrans_EI_2, opCost_data_NE2020_ltrans_EI,
                opCost_data_NE2050_sCap_EI-opCost_data_NE2050_sCap_EI_2, opCost_data_NE2050_sCap_EI_2, opCost_data_NE2020_sCap_EI]
  opcostType_Col = ['Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost',
                    'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost',
                    'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost']

  filler_ref = [0, totCost_NE2050_ref_EI- totCost_NE2050_ref_EI_2, 0, 0, totCost_NE2050_lh2_EI- totCost_NE2050_lh2_EI_2, 0,
                0, totCost_NE2050_lccs_EI- totCost_NE2050_lccs_EI_2, 0, 0, totCost_NE2050_he_EI- totCost_NE2050_he_EI_2, 0,
                0, totCost_NE2050_ltrans_EI- totCost_NE2050_ltrans_EI_2, 0, 0, totCost_NE2050_sCap_EI- totCost_NE2050_sCap_EI_2, 0]
  filler_Col = ['', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '']

  costsData_ref = np.hstack((fixedCost_ref, opCost_ref, filler_ref))
  costType_ref = np.hstack((fixedcostType_Col, opcostType_Col, filler_Col))
  region_ref = np.hstack((region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col, planning_Col))

  cost_ref = np.vstack((region_ref, planning_ref, costType_ref, costsData_ref))
  df_costs_ref = pd.DataFrame(cost_ref)
  df_costs_ref = df_costs_ref.transpose()
  df_costs_ref.rename({0: 'Scenario', 1: 'PlanningScr', 2: 'Cost Types', 3: 'Amount'},axis=1, inplace=True)
  df_costs_ref = df_costs_ref.astype({'Amount': float})

  # ERCOT:
  fixedCost_ref = [fixedCost_data_NE2050_ref_ERCOT - fixedCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT,
                   fixedCost_data_NE2050_lh2_ERCOT - fixedCost_data_NE2050_lh2_ERCOT_2, fixedCost_data_NE2050_lh2_ERCOT_2, fixedCost_data_NE2020_lh2_ERCOT,
                   fixedCost_data_NE2050_ref_ERCOT - fixedCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT,
                   fixedCost_data_NE2050_he_ERCOT - fixedCost_data_NE2050_he_ERCOT_2, fixedCost_data_NE2050_he_ERCOT_2, fixedCost_data_NE2020_he_ERCOT,
                   fixedCost_data_NE2050_ltrans_ERCOT - fixedCost_data_NE2050_ltrans_ERCOT_2, fixedCost_data_NE2050_ltrans_ERCOT_2, fixedCost_data_NE2020_ltrans_ERCOT,
                   fixedCost_data_NE2050_sCap_ERCOT - fixedCost_data_NE2050_sCap_ERCOT_2, fixedCost_data_NE2050_sCap_ERCOT_2, fixedCost_data_NE2020_sCap_ERCOT]
  fixedcostType_Col = ['Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost',
                       'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost',
                       'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost']
  region_Col = ['Reference', 'Reference', 'Reference', 'No H2', 'No H2', 'No H2', 'No CCS', 'No CCS', 'No CCS',
                'High Elec', 'High Elec', 'High Elec', 'Lim Trans', 'Lim Trans', 'Lim Trans', 'Low Cap', 'Low Cap', 'Low Cap']
  planning_Col = ['Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                  'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now']

  opCost_ref = [opCost_data_NE2050_ref_ERCOT - opCost_data_NE2050_ref_ERCOT_2, opCost_data_NE2050_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT,
                opCost_data_NE2050_lh2_ERCOT - opCost_data_NE2050_lh2_ERCOT_2, opCost_data_NE2050_lh2_ERCOT_2, opCost_data_NE2020_lh2_ERCOT,
                opCost_data_NE2050_ref_ERCOT - opCost_data_NE2050_ref_ERCOT_2, opCost_data_NE2050_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT,
                opCost_data_NE2050_he_ERCOT - opCost_data_NE2050_he_ERCOT_2, opCost_data_NE2050_he_ERCOT_2, opCost_data_NE2020_he_ERCOT,
                opCost_data_NE2050_ltrans_ERCOT - opCost_data_NE2050_ltrans_ERCOT_2, opCost_data_NE2050_ltrans_ERCOT_2, opCost_data_NE2020_ltrans_ERCOT,
                opCost_data_NE2050_sCap_ERCOT - opCost_data_NE2050_sCap_ERCOT_2, opCost_data_NE2050_sCap_ERCOT_2, opCost_data_NE2020_sCap_ERCOT]
  opcostType_Col = ['Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost',
                    'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost',
                    'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost']

  filler_ref = [0, totCost_NE2050_ref_ERCOT - totCost_NE2050_ref_ERCOT_2, 0, 0, totCost_NE2050_lh2_ERCOT - totCost_NE2050_lh2_ERCOT_2, 0,
                0, totCost_NE2050_ref_ERCOT - totCost_NE2050_ref_ERCOT_2, 0, 0, totCost_NE2050_he_ERCOT - totCost_NE2050_he_ERCOT_2, 0,
                0, totCost_NE2050_ltrans_ERCOT - totCost_NE2050_ltrans_ERCOT_2, 0, 0, totCost_NE2050_sCap_ERCOT - totCost_NE2050_sCap_ERCOT_2, 0]
  filler_Col = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

  costsData_ERCOT_ref = np.hstack((fixedCost_ref, opCost_ref, filler_ref))
  costType_ERCOT_ref = np.hstack((fixedcostType_Col, opcostType_Col, filler_Col))
  region_ERCOT_ref = np.hstack((region_Col, region_Col, region_Col))
  planning_ERCOT_ref = np.hstack((planning_Col, planning_Col, planning_Col))

  cost_ERCOT_ref = np.vstack((region_ERCOT_ref, planning_ERCOT_ref, costType_ERCOT_ref, costsData_ERCOT_ref))
  df_costs_ERCOT_ref = pd.DataFrame(cost_ERCOT_ref)
  df_costs_ERCOT_ref = df_costs_ERCOT_ref.transpose()
  df_costs_ERCOT_ref.rename({0: 'Scenario', 1: 'PlanningScr', 2: 'Cost Types', 3: 'Amount'}, axis=1, inplace=True)
  df_costs_ERCOT_ref = df_costs_ERCOT_ref.astype({'Amount': float})

  return df_costs_ref, df_costs_ERCOT_ref

main()

