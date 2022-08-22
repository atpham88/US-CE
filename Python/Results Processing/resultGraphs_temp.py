
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.gridspec as gridspec
import matplotlib.patheffects as PathEffects
from palettable.cartocolors.sequential import *
from palettable.colorbrewer.qualitative import *
from mpl_toolkits.axes_grid1 import make_axes_locatable

from capacityInvestments_temp import *
from costs_temp import *
from generationDispatch import *
from transInvestments_temp import *
from flows_temp import *
from capacityInvestmentsRegions_temp import *
from cfigures_resite import resite_figures
from generationDispatchRegions import *

import altair as alt
from textwrap import wrap

# %% Reference:
def main():
    ref_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results\\"
    techCase = 'L Trans'
    shapefile_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\REEDS\\Shapefiles\\"

    # Capacity Expansion:
    (CoalCCS_NE2020_ref_EI, CCCCS_NE2020_ref_EI, CC_NE2020_ref_EI, Nuclear_NE2020_ref_EI, Hydrogen_NE2020_ref_EI,Battery_NE2020_ref_EI,
     DAC_NE2020_ref_EI, Wind_NE2020_ref_EI, Solar_NE2020_ref_EI, CoalCCS_NE2020_2_ref_EI, CCCCS_NE2020_2_ref_EI, CC_NE2020_2_ref_EI,
     Nuclear_NE2020_2_ref_EI, Hydrogen_NE2020_2_ref_EI,Battery_NE2020_2_ref_EI, DAC_NE2020_2_ref_EI,
     Wind_NE2020_2_ref_EI, Solar_NE2020_2_ref_EI) = capInvestments_temp(ref_dir, techCase, planningScr='NE2020', interConn = 'EI')
    (CoalCCS_NE2050_ref_EI, CCCCS_NE2050_ref_EI, CC_NE2050_ref_EI, Nuclear_NE2050_ref_EI, Hydrogen_NE2050_ref_EI,Battery_NE2050_ref_EI,
     DAC_NE2050_ref_EI, Wind_NE2050_ref_EI, Solar_NE2050_ref_EI, CoalCCS_NE2050_2_ref_EI, CCCCS_NE2050_2_ref_EI, CC_NE2050_2_ref_EI,
     Nuclear_NE2050_2_ref_EI, Hydrogen_NE2050_2_ref_EI,Battery_NE2050_2_ref_EI, DAC_NE2050_2_ref_EI, Wind_NE2050_2_ref_EI,
     Solar_NE2050_2_ref_EI) = capInvestments_temp(ref_dir, techCase, planningScr='NE2050', interConn = 'EI')

    (CoalCCS_NE2020_ref_ERCOT, CCCCS_NE2020_ref_ERCOT, CC_NE2020_ref_ERCOT, Nuclear_NE2020_ref_ERCOT, Hydrogen_NE2020_ref_ERCOT,Battery_NE2020_ref_ERCOT,
     DAC_NE2020_ref_ERCOT, Wind_NE2020_ref_ERCOT, Solar_NE2020_ref_ERCOT, CoalCCS_NE2020_2_ref_ERCOT, CCCCS_NE2020_2_ref_ERCOT,
     CC_NE2020_2_ref_ERCOT, Nuclear_NE2020_2_ref_ERCOT, Hydrogen_NE2020_2_ref_ERCOT,Battery_NE2020_2_ref_ERCOT, DAC_NE2020_2_ref_ERCOT,
     Wind_NE2020_2_ref_ERCOT, Solar_NE2020_2_ref_ERCOT) = capInvestments_temp(ref_dir, techCase, planningScr='NE2020', interConn = 'ERCOT')
    (CoalCCS_NE2050_ref_ERCOT, CCCCS_NE2050_ref_ERCOT, CC_NE2050_ref_ERCOT, Nuclear_NE2050_ref_ERCOT, Hydrogen_NE2050_ref_ERCOT,Battery_NE2050_ref_ERCOT,
     DAC_NE2050_ref_ERCOT, Wind_NE2050_ref_ERCOT, Solar_NE2050_ref_ERCOT, CoalCCS_NE2050_2_ref_ERCOT, CCCCS_NE2050_2_ref_ERCOT, CC_NE2050_2_ref_ERCOT,
     Nuclear_NE2050_2_ref_ERCOT, Hydrogen_NE2050_2_ref_ERCOT,Battery_NE2050_2_ref_ERCOT, DAC_NE2050_2_ref_ERCOT,
     Wind_NE2050_2_ref_ERCOT, Solar_NE2050_2_ref_ERCOT) = capInvestments_temp(ref_dir, techCase, planningScr='NE2050', interConn = 'ERCOT')

    df_capEXP_ref = graphCE(CoalCCS_NE2020_ref_EI, CCCCS_NE2020_ref_EI, CC_NE2020_ref_EI, Nuclear_NE2020_ref_EI, Hydrogen_NE2020_ref_EI,Battery_NE2020_ref_EI,
                            DAC_NE2020_ref_EI, Wind_NE2020_ref_EI, Solar_NE2020_ref_EI, CoalCCS_NE2050_ref_EI, CCCCS_NE2050_ref_EI, CC_NE2050_ref_EI, Nuclear_NE2050_ref_EI, Hydrogen_NE2050_ref_EI,Battery_NE2050_ref_EI,
                            DAC_NE2050_ref_EI, Wind_NE2050_ref_EI, Solar_NE2050_ref_EI, CoalCCS_NE2020_ref_ERCOT, CCCCS_NE2020_ref_ERCOT, CC_NE2020_ref_ERCOT,
                            Nuclear_NE2020_ref_ERCOT, Hydrogen_NE2020_ref_ERCOT,Battery_NE2020_ref_ERCOT, DAC_NE2020_ref_ERCOT, Wind_NE2020_ref_ERCOT,
                            Solar_NE2020_ref_ERCOT, CoalCCS_NE2050_ref_ERCOT, CCCCS_NE2050_ref_ERCOT, CC_NE2050_ref_ERCOT, Nuclear_NE2050_ref_ERCOT, Hydrogen_NE2050_ref_ERCOT,
                            Battery_NE2050_ref_ERCOT, DAC_NE2050_ref_ERCOT, Wind_NE2050_ref_ERCOT, Solar_NE2050_ref_ERCOT,
                            CoalCCS_NE2020_2_ref_EI, CCCCS_NE2020_2_ref_EI, CC_NE2020_2_ref_EI, Nuclear_NE2020_2_ref_EI, Hydrogen_NE2020_2_ref_EI, Battery_NE2020_2_ref_EI,
                            DAC_NE2020_2_ref_EI, Wind_NE2020_2_ref_EI, Solar_NE2020_2_ref_EI, CoalCCS_NE2050_2_ref_EI, CCCCS_NE2050_2_ref_EI, CC_NE2050_2_ref_EI, Nuclear_NE2050_2_ref_EI, Hydrogen_NE2050_2_ref_EI, Battery_NE2050_2_ref_EI,
                            DAC_NE2050_2_ref_EI, Wind_NE2050_2_ref_EI, Solar_NE2050_2_ref_EI, CoalCCS_NE2020_2_ref_ERCOT, CCCCS_NE2020_2_ref_ERCOT, CC_NE2020_2_ref_ERCOT,
                            Nuclear_NE2020_2_ref_ERCOT, Hydrogen_NE2020_2_ref_ERCOT, Battery_NE2020_2_ref_ERCOT, DAC_NE2020_2_ref_ERCOT, Wind_NE2020_2_ref_ERCOT,
                            Solar_NE2020_2_ref_ERCOT, CoalCCS_NE2050_2_ref_ERCOT, CCCCS_NE2050_2_ref_ERCOT, CC_NE2050_2_ref_ERCOT, Nuclear_NE2050_2_ref_ERCOT, Hydrogen_NE2050_2_ref_ERCOT,
                            Battery_NE2050_2_ref_ERCOT, DAC_NE2050_2_ref_ERCOT, Wind_NE2050_2_ref_ERCOT, Solar_NE2050_2_ref_ERCOT)

    df_capEXP_ref['PlanningScr'] = df_capEXP_ref['PlanningScr'].apply(wrap, args=[6])
    chart = alt.Chart(df_capEXP_ref).mark_bar(size=50).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', axis=alt.Axis(labelAngle=-0),title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Capacity):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Capacity Investments (GW)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Region:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Technology',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Technology:N',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ffffff', '#ff6f69', '#96ceb4', 'darkolivegreen', 'black', 'saddlebrown', 'lightpink','#ffcc5c','skyblue'],
                        ),
                        )).resolve_scale(y='independent').configure_view(
        # remove grid lines around column clusters
        #strokeOpacity=0
        ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15,titleFontSize=15
                     ).properties(width=250, height=400).show()

    # Transmission capacity investments:
    (miso_serc_ref_NE2020_EI, pjm_serc_ref_NE2020_EI, ne_ny_ref_NE2020_EI,
     pjm_ny_ref_NE2020_EI, pjm_miso_ref_NE2020_EI, spp_miso_ref_NE2020_EI, ercot_tot_ref_NE2020_EI) = transInvestments_temp(ref_dir, techCase, planningScr='NE2020', interConn = 'EI')
    (miso_serc_ref_NE2050_EI, pjm_serc_ref_NE2050_EI, ne_ny_ref_NE2050_EI,
     pjm_ny_ref_NE2050_EI, pjm_miso_ref_NE2050_EI, spp_miso_ref_NE2050_EI, ercot_tot_ref_NE2050_EI) = transInvestments_temp(ref_dir, techCase, planningScr='NE2050', interConn='EI')

    (miso_serc_ref_NE2020_ERCOT, pjm_serc_ref_NE2020_ERCOT, ne_ny_ref_NE2020_ERCOT,
     pjm_ny_ref_NE2020_ERCOT, pjm_miso_ref_NE2020_ERCOT, spp_miso_ref_NE2020_ERCOT, ercot_tot_ref_NE2020_ERCOT) = transInvestments_temp(ref_dir, techCase, planningScr='NE2020', interConn='ERCOT')
    (miso_serc_ref_NE2050_ERCOT, pjm_serc_ref_NE2050_ERCOT, ne_ny_ref_NE2050_ERCOT,
     pjm_ny_ref_NE2050_ERCOT, pjm_miso_ref_NE2050_ERCOT, spp_miso_ref_NE2050_ERCOT, ercot_tot_ref_NE2050_ERCOT) = transInvestments_temp(ref_dir, techCase, planningScr='NE2050', interConn='ERCOT')

    df_transEXP_ref = graphTCE(miso_serc_ref_NE2020_EI, pjm_serc_ref_NE2020_EI, ne_ny_ref_NE2020_EI, pjm_ny_ref_NE2020_EI, pjm_miso_ref_NE2020_EI,
                               spp_miso_ref_NE2020_EI, miso_serc_ref_NE2050_EI, pjm_serc_ref_NE2050_EI, ne_ny_ref_NE2050_EI, pjm_ny_ref_NE2050_EI,
                               pjm_miso_ref_NE2050_EI, spp_miso_ref_NE2050_EI, miso_serc_ref_NE2020_ERCOT, pjm_serc_ref_NE2020_ERCOT,
                               ne_ny_ref_NE2020_ERCOT, pjm_ny_ref_NE2020_ERCOT, pjm_miso_ref_NE2020_ERCOT, spp_miso_ref_NE2020_ERCOT, miso_serc_ref_NE2050_ERCOT,
                               pjm_serc_ref_NE2050_ERCOT, ne_ny_ref_NE2050_ERCOT, pjm_ny_ref_NE2050_ERCOT, pjm_miso_ref_NE2050_ERCOT, spp_miso_ref_NE2050_ERCOT,
                               ercot_tot_ref_NE2020_EI, ercot_tot_ref_NE2050_EI, ercot_tot_ref_NE2020_ERCOT, ercot_tot_ref_NE2050_ERCOT)

    df_transEXP_ref['PlanningScr'] = df_transEXP_ref['PlanningScr'].apply(wrap, args=[10])
    chart = alt.Chart(df_transEXP_ref).mark_bar(size=50).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', axis=alt.Axis(labelAngle=-0), title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Capacity):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Transmission Capacity Investments (GW)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Region:N', title=None, header=alt.Header(labelFontSize=20)),
        # tell Altair which field to use for color segmentation
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Transmission Lines',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Transmission Lines:N',
                        legend=alt.Legend(columns=2),
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ff6f69', '#96ceb4', 'darkolivegreen', 'saddlebrown', 'lightpink', '#ffcc5c', 'skyblue'],
                        ),
                        )).resolve_scale(y='independent').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15, titleFontSize=15,orient='bottom',
                                                                          ).properties(width=120, height=400).show()

    # Flows:
    (netFlow_EI_serc_NE2020_EI, netFlow_EI_ny_NE2020_EI, netFlow_EI_miso_NE2020_EI,
     netFlow_EI_pjm_NE2020_EI, netFlow_EI_ne_NE2020_EI, netFlow_EI_spp_NE2020_EI, netFlow_ERCOT_NW_NE2020_EI,
     netFlow_ERCOT_SW_NE2020_EI, netFlow_ERCOT_NE_NE2020_EI, netFlow_ERCOT_SE_NE2020_EI) = transFlows_temp(ref_dir, techCase, planningScr='NE2020', interConn='EI')
    (netFlow_EI_serc_NE2050_EI, netFlow_EI_ny_NE2050_EI, netFlow_EI_miso_NE2050_EI,
     netFlow_EI_pjm_NE2050_EI, netFlow_EI_ne_NE2050_EI, netFlow_EI_spp_NE2050_EI, netFlow_ERCOT_NW_NE2050_EI,
     netFlow_ERCOT_SW_NE2050_EI, netFlow_ERCOT_NE_NE2050_EI, netFlow_ERCOT_SE_NE2050_EI) = transFlows_temp(ref_dir, techCase, planningScr='NE2050', interConn='EI')

    (netFlow_EI_serc_NE2020_ERCOT, netFlow_EI_ny_NE2020_ERCOT, netFlow_EI_miso_NE2020_ERCOT,
     netFlow_EI_pjm_NE2020_ERCOT, netFlow_EI_ne_NE2020_ERCOT, netFlow_EI_spp_NE2020_ERCOT, netFlow_ERCOT_NW_NE2020_ERCOT,
     netFlow_ERCOT_SW_NE2020_ERCOT, netFlow_ERCOT_NE_NE2020_ERCOT, netFlow_ERCOT_SE_NE2020_ERCOT) = transFlows_temp(ref_dir, techCase, planningScr='NE2020', interConn='ERCOT')
    (netFlow_EI_serc_NE2050_ERCOT, netFlow_EI_ny_NE2050_ERCOT, netFlow_EI_miso_NE2050_ERCOT,
     netFlow_EI_pjm_NE2050_ERCOT, netFlow_EI_ne_NE2050_ERCOT, netFlow_EI_spp_NE2050_ERCOT, netFlow_ERCOT_NW_NE2050_ERCOT,
     netFlow_ERCOT_SW_NE2050_ERCOT, netFlow_ERCOT_NE_NE2050_ERCOT, netFlow_ERCOT_SE_NE2050_ERCOT) = transFlows_temp(ref_dir, techCase, planningScr='NE2050', interConn='ERCOT')

    df_Flows_ref = graphFlows(netFlow_EI_serc_NE2020_EI, netFlow_EI_ny_NE2020_EI, netFlow_EI_miso_NE2020_EI,
                               netFlow_EI_pjm_NE2020_EI, netFlow_EI_ne_NE2020_EI, netFlow_EI_spp_NE2020_EI, netFlow_ERCOT_NW_NE2020_EI,
                               netFlow_ERCOT_SW_NE2020_EI, netFlow_ERCOT_NE_NE2020_EI, netFlow_ERCOT_SE_NE2020_EI, netFlow_EI_serc_NE2050_EI,
                               netFlow_EI_ny_NE2050_EI, netFlow_EI_miso_NE2050_EI, netFlow_EI_pjm_NE2050_EI,
                               netFlow_EI_ne_NE2050_EI, netFlow_EI_spp_NE2050_EI, netFlow_ERCOT_NW_NE2050_EI, netFlow_ERCOT_SW_NE2050_EI,
                               netFlow_ERCOT_NE_NE2050_EI, netFlow_ERCOT_SE_NE2050_EI, netFlow_EI_serc_NE2020_ERCOT, netFlow_EI_ny_NE2020_ERCOT,
                               netFlow_EI_miso_NE2020_ERCOT, netFlow_EI_pjm_NE2020_ERCOT, netFlow_EI_ne_NE2020_ERCOT, netFlow_EI_spp_NE2020_ERCOT,
                               netFlow_ERCOT_NW_NE2020_ERCOT, netFlow_ERCOT_SW_NE2020_ERCOT, netFlow_ERCOT_NE_NE2020_ERCOT,
                               netFlow_ERCOT_SE_NE2020_ERCOT, netFlow_EI_serc_NE2050_ERCOT,
                               netFlow_EI_ny_NE2050_ERCOT, netFlow_EI_miso_NE2050_ERCOT, netFlow_EI_pjm_NE2050_ERCOT, netFlow_EI_ne_NE2050_ERCOT,
                               netFlow_EI_spp_NE2050_ERCOT, netFlow_ERCOT_NW_NE2050_ERCOT, netFlow_ERCOT_SW_NE2050_ERCOT,
                               netFlow_ERCOT_NE_NE2050_ERCOT, netFlow_ERCOT_SE_NE2050_ERCOT)

    df_Flows_ref['PlanningScr'] = df_Flows_ref['PlanningScr'].apply(wrap, args=[10])
    chart = alt.Chart(df_Flows_ref).mark_bar(size=50).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', axis=alt.Axis(labelAngle=-0),title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Flows):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Generation Flows (TWh)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Region:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Load Region',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Load Region:N',
                        legend=alt.Legend(columns=3),
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ff6f69', '#96ceb4', 'darkolivegreen', 'saddlebrown', 'lightpink',
                                   '#ffcc5c', 'skyblue', '#cdb3e6', '#e6c2b3', '#888da6'],
                        ),
                        )).resolve_scale(y='independent').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15, titleFontSize=15, orient='bottom',
                                                                          ).properties(width=150, height=400).show()

    # Costs:
    (totCost_NE2020_ref_EI, opCost_data_NE2020_ref_EI, fixedCost_data_NE2020_ref_EI,
     totCost_NE2020_ref_EI_2, opCost_data_NE2020_ref_EI_2, fixedCost_data_NE2020_ref_EI_2) = costCal_temp(ref_dir, techCase, planningScr='NE2020', interConn = 'EI')
    (totCost_NE2050_ref_EI, opCost_data_NE2050_ref_EI, fixedCost_data_NE2050_ref_EI,
     totCost_NE2050_ref_EI_2, opCost_data_NE2050_ref_EI_2, fixedCost_data_NE2050_ref_EI_2) = costCal_temp(ref_dir, techCase, planningScr='NE2050', interConn = 'EI')

    (totCost_NE2020_ref_ERCOT, opCost_data_NE2020_ref_ERCOT, fixedCost_data_NE2020_ref_ERCOT,
     totCost_NE2020_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT_2) = costCal_temp(ref_dir, techCase, planningScr='NE2020', interConn='ERCOT')
    (totCost_NE2050_ref_ERCOT, opCost_data_NE2050_ref_ERCOT, fixedCost_data_NE2050_ref_ERCOT,
     totCost_NE2050_ref_ERCOT_2, opCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2050_ref_ERCOT_2) = costCal_temp(ref_dir, techCase, planningScr='NE2050', interConn='ERCOT')

    df_costs_ref = graphCosts(totCost_NE2020_ref_EI, opCost_data_NE2020_ref_EI, fixedCost_data_NE2020_ref_EI,
                              totCost_NE2050_ref_EI, opCost_data_NE2050_ref_EI, fixedCost_data_NE2050_ref_EI,
                              totCost_NE2020_ref_ERCOT, opCost_data_NE2020_ref_ERCOT, fixedCost_data_NE2020_ref_ERCOT,
                              totCost_NE2050_ref_ERCOT, opCost_data_NE2050_ref_ERCOT, fixedCost_data_NE2050_ref_ERCOT,
                              totCost_NE2020_ref_EI_2, opCost_data_NE2020_ref_EI_2, fixedCost_data_NE2020_ref_EI_2,
                              totCost_NE2050_ref_EI_2, opCost_data_NE2050_ref_EI_2, fixedCost_data_NE2050_ref_EI_2,
                              totCost_NE2020_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT_2,
                              totCost_NE2050_ref_ERCOT_2, opCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2050_ref_ERCOT_2)

    df_costs_ref['PlanningScr'] = df_costs_ref['PlanningScr'].apply(wrap, args=[6])
    chart = alt.Chart(df_costs_ref).mark_bar(size=50).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', axis=alt.Axis(labelAngle=-0), title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Amount):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Annual Costs (Billion $)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Region:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Cost Types',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Cost Types:N',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ffffff', '#96ceb4','#ff6f69'] #ffcc5c', 'skyblue'],
                        ),
                        )).resolve_scale(y='independent').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15, titleFontSize=15
                                                                          ).properties(width=250, height=400).show()

    # Capacity investments by Region - EI:
    (CoalCCS_SERC_NE2020_EI, CoalCCS_NE_NE2020_EI, CoalCCS_NY_NE2020_EI, CoalCCS_MISO_NE2020_EI, CoalCCS_PJM_NE2020_EI, CoalCCS_SPP_NE2020_EI,
     CCCCS_SERC_NE2020_EI, CCCCS_NE_NE2020_EI, CCCCS_NY_NE2020_EI, CCCCS_MISO_NE2020_EI, CCCCS_PJM_NE2020_EI, CCCCS_SPP_NE2020_EI,
     CC_SERC_NE2020_EI, CC_NE_NE2020_EI, CC_NY_NE2020_EI, CC_MISO_NE2020_EI, CC_PJM_NE2020_EI, CC_SPP_NE2020_EI,
     Nuclear_SERC_NE2020_EI, Nuclear_NE_NE2020_EI, Nuclear_NY_NE2020_EI, Nuclear_MISO_NE2020_EI, Nuclear_PJM_NE2020_EI, Nuclear_SPP_NE2020_EI,
     Hydrogen_SERC_NE2020_EI, Hydrogen_NE_NE2020_EI, Hydrogen_NY_NE2020_EI, Hydrogen_MISO_NE2020_EI, Hydrogen_PJM_NE2020_EI, Hydrogen_SPP_NE2020_EI,
     Battery_SERC_NE2020_EI, Battery_NE_NE2020_EI, Battery_NY_NE2020_EI, Battery_MISO_NE2020_EI, Battery_PJM_NE2020_EI, Battery_SPP_NE2020_EI,
     Wind_SERC_NE2020_EI, Wind_NE_NE2020_EI, Wind_NY_NE2020_EI, Wind_MISO_NE2020_EI, Wind_PJM_NE2020_EI, Wind_SPP_NE2020_EI,
     Solar_SERC_NE2020_EI, Solar_NE_NE2020_EI, Solar_NY_NE2020_EI, Solar_MISO_NE2020_EI, Solar_PJM_NE2020_EI, Solar_SPP_NE2020_EI,
     DAC_SERC_NE2020_EI, DAC_NE_NE2020_EI, DAC_NY_NE2020_EI, DAC_MISO_NE2020_EI, DAC_PJM_NE2020_EI, DAC_SPP_NE2020_EI,
     CoalCCS_NW_NE2020_EI, CoalCCS_SW_NE2020_EI, CoalCCS_NOE_NE2020_EI, CoalCCS_SE_NE2020_EI,
     CCCCS_NW_NE2020_EI, CCCCS_SW_NE2020_EI, CCCCS_NOE_NE2020_EI, CCCCS_SE_NE2020_EI,
     CC_NW_NE2020_EI, CC_SW_NE2020_EI, CC_NOE_NE2020_EI, CC_SE_NE2020_EI,
     Nuclear_NW_NE2020_EI, Nuclear_SW_NE2020_EI, Nuclear_NOE_NE2020_EI, Nuclear_SE_NE2020_EI,
     Hydrogen_NW_NE2020_EI, Hydrogen_SW_NE2020_EI, Hydrogen_NOE_NE2020_EI, Hydrogen_SE_NE2020_EI,
     Battery_NW_NE2020_EI, Battery_SW_NE2020_EI, Battery_NOE_NE2020_EI, Battery_SE_NE2020_EI,
     DAC_NW_NE2020_EI, DAC_SW_NE2020_EI, DAC_NOE_NE2020_EI, DAC_SE_NE2020_EI,
     Wind_NW_NE2020_EI, Wind_SW_NE2020_EI, Wind_NOE_NE2020_EI, Wind_SE_NE2020_EI,
     Solar_NW_NE2020_EI, Solar_SW_NE2020_EI, Solar_NOE_NE2020_EI, Solar_SE_NE2020_EI,
     CoalCCS_SERC_NE2020_EI_2, CoalCCS_NE_NE2020_EI_2, CoalCCS_NY_NE2020_EI_2, CoalCCS_MISO_NE2020_EI_2, CoalCCS_PJM_NE2020_EI_2, CoalCCS_SPP_NE2020_EI_2,
     CCCCS_SERC_NE2020_EI_2, CCCCS_NE_NE2020_EI_2, CCCCS_NY_NE2020_EI_2, CCCCS_MISO_NE2020_EI_2, CCCCS_PJM_NE2020_EI_2, CCCCS_SPP_NE2020_EI_2,
     CC_SERC_NE2020_EI_2, CC_NE_NE2020_EI_2, CC_NY_NE2020_EI_2, CC_MISO_NE2020_EI_2, CC_PJM_NE2020_EI_2, CC_SPP_NE2020_EI_2,
     Nuclear_SERC_NE2020_EI_2, Nuclear_NE_NE2020_EI_2, Nuclear_NY_NE2020_EI_2, Nuclear_MISO_NE2020_EI_2, Nuclear_PJM_NE2020_EI_2, Nuclear_SPP_NE2020_EI_2,
     Hydrogen_SERC_NE2020_EI_2, Hydrogen_NE_NE2020_EI_2, Hydrogen_NY_NE2020_EI_2, Hydrogen_MISO_NE2020_EI_2, Hydrogen_PJM_NE2020_EI_2, Hydrogen_SPP_NE2020_EI_2,
     Battery_SERC_NE2020_EI_2, Battery_NE_NE2020_EI_2, Battery_NY_NE2020_EI_2, Battery_MISO_NE2020_EI_2, Battery_PJM_NE2020_EI_2, Battery_SPP_NE2020_EI_2,
     Wind_SERC_NE2020_EI_2, Wind_NE_NE2020_EI_2, Wind_NY_NE2020_EI_2, Wind_MISO_NE2020_EI_2, Wind_PJM_NE2020_EI_2, Wind_SPP_NE2020_EI_2,
     Solar_SERC_NE2020_EI_2, Solar_NE_NE2020_EI_2, Solar_NY_NE2020_EI_2, Solar_MISO_NE2020_EI_2, Solar_PJM_NE2020_EI_2, Solar_SPP_NE2020_EI_2,
     DAC_SERC_NE2020_EI_2, DAC_NE_NE2020_EI_2, DAC_NY_NE2020_EI_2, DAC_MISO_NE2020_EI_2, DAC_PJM_NE2020_EI_2, DAC_SPP_NE2020_EI_2,
     CoalCCS_NW_NE2020_EI_2, CoalCCS_SW_NE2020_EI_2, CoalCCS_NOE_NE2020_EI_2, CoalCCS_SE_NE2020_EI_2,
     CCCCS_NW_NE2020_EI_2, CCCCS_SW_NE2020_EI_2, CCCCS_NOE_NE2020_EI_2, CCCCS_SE_NE2020_EI_2,
     CC_NW_NE2020_EI_2, CC_SW_NE2020_EI_2, CC_NOE_NE2020_EI_2, CC_SE_NE2020_EI_2,
     Nuclear_NW_NE2020_EI_2, Nuclear_SW_NE2020_EI_2, Nuclear_NOE_NE2020_EI_2, Nuclear_SE_NE2020_EI_2,
     Hydrogen_NW_NE2020_EI_2, Hydrogen_SW_NE2020_EI_2, Hydrogen_NOE_NE2020_EI_2, Hydrogen_SE_NE2020_EI_2,
     Battery_NW_NE2020_EI_2, Battery_SW_NE2020_EI_2, Battery_NOE_NE2020_EI_2, Battery_SE_NE2020_EI_2,
     DAC_NW_NE2020_EI_2, DAC_SW_NE2020_EI_2, DAC_NOE_NE2020_EI_2, DAC_SE_NE2020_EI_2,
     Wind_NW_NE2020_EI_2, Wind_SW_NE2020_EI_2, Wind_NOE_NE2020_EI_2, Wind_SE_NE2020_EI_2,
     Solar_NW_NE2020_EI_2, Solar_SW_NE2020_EI_2, Solar_NOE_NE2020_EI_2, Solar_SE_NE2020_EI_2) = capRegions_temp(ref_dir, techCase, planningScr='NE2020', interConn='EI')

    (CoalCCS_SERC_NE2050_EI, CoalCCS_NE_NE2050_EI, CoalCCS_NY_NE2050_EI, CoalCCS_MISO_NE2050_EI, CoalCCS_PJM_NE2050_EI, CoalCCS_SPP_NE2050_EI,
     CCCCS_SERC_NE2050_EI, CCCCS_NE_NE2050_EI, CCCCS_NY_NE2050_EI, CCCCS_MISO_NE2050_EI, CCCCS_PJM_NE2050_EI, CCCCS_SPP_NE2050_EI,
     CC_SERC_NE2050_EI, CC_NE_NE2050_EI, CC_NY_NE2050_EI, CC_MISO_NE2050_EI, CC_PJM_NE2050_EI, CC_SPP_NE2050_EI,
     Nuclear_SERC_NE2050_EI, Nuclear_NE_NE2050_EI, Nuclear_NY_NE2050_EI, Nuclear_MISO_NE2050_EI, Nuclear_PJM_NE2050_EI, Nuclear_SPP_NE2050_EI,
     Hydrogen_SERC_NE2050_EI, Hydrogen_NE_NE2050_EI, Hydrogen_NY_NE2050_EI, Hydrogen_MISO_NE2050_EI, Hydrogen_PJM_NE2050_EI, Hydrogen_SPP_NE2050_EI,
     Battery_SERC_NE2050_EI, Battery_NE_NE2050_EI, Battery_NY_NE2050_EI, Battery_MISO_NE2050_EI, Battery_PJM_NE2050_EI, Battery_SPP_NE2050_EI,
     Wind_SERC_NE2050_EI, Wind_NE_NE2050_EI, Wind_NY_NE2050_EI, Wind_MISO_NE2050_EI, Wind_PJM_NE2050_EI, Wind_SPP_NE2050_EI,
     Solar_SERC_NE2050_EI, Solar_NE_NE2050_EI, Solar_NY_NE2050_EI, Solar_MISO_NE2050_EI, Solar_PJM_NE2050_EI, Solar_SPP_NE2050_EI,
     DAC_SERC_NE2050_EI, DAC_NE_NE2050_EI, DAC_NY_NE2050_EI, DAC_MISO_NE2050_EI, DAC_PJM_NE2050_EI, DAC_SPP_NE2050_EI,
     CoalCCS_NW_NE2050_EI, CoalCCS_SW_NE2050_EI, CoalCCS_NOE_NE2050_EI, CoalCCS_SE_NE2050_EI,
     CCCCS_NW_NE2050_EI, CCCCS_SW_NE2050_EI, CCCCS_NOE_NE2050_EI, CCCCS_SE_NE2050_EI,
     CC_NW_NE2050_EI, CC_SW_NE2050_EI, CC_NOE_NE2050_EI, CC_SE_NE2050_EI,
     Nuclear_NW_NE2050_EI, Nuclear_SW_NE2050_EI, Nuclear_NOE_NE2050_EI, Nuclear_SE_NE2050_EI,
     Hydrogen_NW_NE2050_EI, Hydrogen_SW_NE2050_EI, Hydrogen_NOE_NE2050_EI, Hydrogen_SE_NE2050_EI,
     Battery_NW_NE2050_EI, Battery_SW_NE2050_EI, Battery_NOE_NE2050_EI, Battery_SE_NE2050_EI,
     DAC_NW_NE2050_EI, DAC_SW_NE2050_EI, DAC_NOE_NE2050_EI, DAC_SE_NE2050_EI,
     Wind_NW_NE2050_EI, Wind_SW_NE2050_EI, Wind_NOE_NE2050_EI, Wind_SE_NE2050_EI,
     Solar_NW_NE2050_EI, Solar_SW_NE2050_EI, Solar_NOE_NE2050_EI, Solar_SE_NE2050_EI,
     CoalCCS_SERC_NE2050_EI_2, CoalCCS_NE_NE2050_EI_2, CoalCCS_NY_NE2050_EI_2, CoalCCS_MISO_NE2050_EI_2, CoalCCS_PJM_NE2050_EI_2, CoalCCS_SPP_NE2050_EI_2,
     CCCCS_SERC_NE2050_EI_2, CCCCS_NE_NE2050_EI_2, CCCCS_NY_NE2050_EI_2, CCCCS_MISO_NE2050_EI_2, CCCCS_PJM_NE2050_EI_2, CCCCS_SPP_NE2050_EI_2,
     CC_SERC_NE2050_EI_2, CC_NE_NE2050_EI_2, CC_NY_NE2050_EI_2, CC_MISO_NE2050_EI_2, CC_PJM_NE2050_EI_2, CC_SPP_NE2050_EI_2,
     Nuclear_SERC_NE2050_EI_2, Nuclear_NE_NE2050_EI_2, Nuclear_NY_NE2050_EI_2, Nuclear_MISO_NE2050_EI_2, Nuclear_PJM_NE2050_EI_2, Nuclear_SPP_NE2050_EI_2,
     Hydrogen_SERC_NE2050_EI_2, Hydrogen_NE_NE2050_EI_2, Hydrogen_NY_NE2050_EI_2, Hydrogen_MISO_NE2050_EI_2, Hydrogen_PJM_NE2050_EI_2, Hydrogen_SPP_NE2050_EI_2,
     Battery_SERC_NE2050_EI_2, Battery_NE_NE2050_EI_2, Battery_NY_NE2050_EI_2, Battery_MISO_NE2050_EI_2, Battery_PJM_NE2050_EI_2, Battery_SPP_NE2050_EI_2,
     Wind_SERC_NE2050_EI_2, Wind_NE_NE2050_EI_2, Wind_NY_NE2050_EI_2, Wind_MISO_NE2050_EI_2, Wind_PJM_NE2050_EI_2, Wind_SPP_NE2050_EI_2,
     Solar_SERC_NE2050_EI_2, Solar_NE_NE2050_EI_2, Solar_NY_NE2050_EI_2, Solar_MISO_NE2050_EI_2, Solar_PJM_NE2050_EI_2, Solar_SPP_NE2050_EI_2,
     DAC_SERC_NE2050_EI_2, DAC_NE_NE2050_EI_2, DAC_NY_NE2050_EI_2, DAC_MISO_NE2050_EI_2, DAC_PJM_NE2050_EI_2, DAC_SPP_NE2050_EI_2,
     CoalCCS_NW_NE2050_EI_2, CoalCCS_SW_NE2050_EI_2, CoalCCS_NOE_NE2050_EI_2, CoalCCS_SE_NE2050_EI_2,
     CCCCS_NW_NE2050_EI_2, CCCCS_SW_NE2050_EI_2, CCCCS_NOE_NE2050_EI_2, CCCCS_SE_NE2050_EI_2,
     CC_NW_NE2050_EI_2, CC_SW_NE2050_EI_2, CC_NOE_NE2050_EI_2, CC_SE_NE2050_EI_2,
     Nuclear_NW_NE2050_EI_2, Nuclear_SW_NE2050_EI_2, Nuclear_NOE_NE2050_EI_2, Nuclear_SE_NE2050_EI_2,
     Hydrogen_NW_NE2050_EI_2, Hydrogen_SW_NE2050_EI_2, Hydrogen_NOE_NE2050_EI_2, Hydrogen_SE_NE2050_EI_2,
     Battery_NW_NE2050_EI_2, Battery_SW_NE2050_EI_2, Battery_NOE_NE2050_EI_2, Battery_SE_NE2050_EI_2,
     DAC_NW_NE2050_EI_2, DAC_SW_NE2050_EI_2, DAC_NOE_NE2050_EI_2, DAC_SE_NE2050_EI_2,
     Wind_NW_NE2050_EI_2, Wind_SW_NE2050_EI_2, Wind_NOE_NE2050_EI_2, Wind_SE_NE2050_EI_2,
     Solar_NW_NE2050_EI_2, Solar_SW_NE2050_EI_2, Solar_NOE_NE2050_EI_2, Solar_SE_NE2050_EI_2) = capRegions_temp(ref_dir, techCase, planningScr='NE2050', interConn='EI')

    df_capEXP_EI = graphEICap(CoalCCS_SERC_NE2020_EI, CoalCCS_NE_NE2020_EI, CoalCCS_NY_NE2020_EI, CoalCCS_MISO_NE2020_EI, CoalCCS_PJM_NE2020_EI, CoalCCS_SPP_NE2020_EI,
                               CCCCS_SERC_NE2020_EI, CCCCS_NE_NE2020_EI, CCCCS_NY_NE2020_EI, CCCCS_MISO_NE2020_EI, CCCCS_PJM_NE2020_EI, CCCCS_SPP_NE2020_EI,
                               CC_SERC_NE2020_EI, CC_NE_NE2020_EI, CC_NY_NE2020_EI, CC_MISO_NE2020_EI, CC_PJM_NE2020_EI, CC_SPP_NE2020_EI,
                               Nuclear_SERC_NE2020_EI, Nuclear_NE_NE2020_EI, Nuclear_NY_NE2020_EI, Nuclear_MISO_NE2020_EI, Nuclear_PJM_NE2020_EI, Nuclear_SPP_NE2020_EI,
                               Hydrogen_SERC_NE2020_EI, Hydrogen_NE_NE2020_EI, Hydrogen_NY_NE2020_EI, Hydrogen_MISO_NE2020_EI, Hydrogen_PJM_NE2020_EI, Hydrogen_SPP_NE2020_EI,
                               Battery_SERC_NE2020_EI, Battery_NE_NE2020_EI, Battery_NY_NE2020_EI, Battery_MISO_NE2020_EI, Battery_PJM_NE2020_EI, Battery_SPP_NE2020_EI,
                               Wind_SERC_NE2020_EI, Wind_NE_NE2020_EI, Wind_NY_NE2020_EI, Wind_MISO_NE2020_EI, Wind_PJM_NE2020_EI, Wind_SPP_NE2020_EI,
                               Solar_SERC_NE2020_EI, Solar_NE_NE2020_EI, Solar_NY_NE2020_EI, Solar_MISO_NE2020_EI, Solar_PJM_NE2020_EI, Solar_SPP_NE2020_EI,
                               DAC_SERC_NE2020_EI, DAC_NE_NE2020_EI, DAC_NY_NE2020_EI, DAC_MISO_NE2020_EI, DAC_PJM_NE2020_EI, DAC_SPP_NE2020_EI,
                               CoalCCS_NW_NE2020_EI, CoalCCS_SW_NE2020_EI, CoalCCS_NOE_NE2020_EI, CoalCCS_SE_NE2020_EI,
                               CCCCS_NW_NE2020_EI, CCCCS_SW_NE2020_EI, CCCCS_NOE_NE2020_EI, CCCCS_SE_NE2020_EI,
                               CC_NW_NE2020_EI, CC_SW_NE2020_EI, CC_NOE_NE2020_EI, CC_SE_NE2020_EI,
                               Nuclear_NW_NE2020_EI, Nuclear_SW_NE2020_EI, Nuclear_NOE_NE2020_EI, Nuclear_SE_NE2020_EI,
                               Hydrogen_NW_NE2020_EI, Hydrogen_SW_NE2020_EI, Hydrogen_NOE_NE2020_EI, Hydrogen_SE_NE2020_EI,
                               Battery_NW_NE2020_EI, Battery_SW_NE2020_EI, Battery_NOE_NE2020_EI, Battery_SE_NE2020_EI,
                               DAC_NW_NE2020_EI, DAC_SW_NE2020_EI, DAC_NOE_NE2020_EI, DAC_SE_NE2020_EI,
                               Wind_NW_NE2020_EI, Wind_SW_NE2020_EI, Wind_NOE_NE2020_EI, Wind_SE_NE2020_EI,
                               Solar_NW_NE2020_EI, Solar_SW_NE2020_EI, Solar_NOE_NE2020_EI, Solar_SE_NE2020_EI,
                               CoalCCS_SERC_NE2050_EI, CoalCCS_NE_NE2050_EI, CoalCCS_NY_NE2050_EI, CoalCCS_MISO_NE2050_EI, CoalCCS_PJM_NE2050_EI, CoalCCS_SPP_NE2050_EI,
                               CCCCS_SERC_NE2050_EI, CCCCS_NE_NE2050_EI, CCCCS_NY_NE2050_EI, CCCCS_MISO_NE2050_EI, CCCCS_PJM_NE2050_EI, CCCCS_SPP_NE2050_EI,
                               CC_SERC_NE2050_EI, CC_NE_NE2050_EI, CC_NY_NE2050_EI, CC_MISO_NE2050_EI, CC_PJM_NE2050_EI, CC_SPP_NE2050_EI,
                               Nuclear_SERC_NE2050_EI, Nuclear_NE_NE2050_EI, Nuclear_NY_NE2050_EI, Nuclear_MISO_NE2050_EI, Nuclear_PJM_NE2050_EI, Nuclear_SPP_NE2050_EI,
                               Hydrogen_SERC_NE2050_EI, Hydrogen_NE_NE2050_EI, Hydrogen_NY_NE2050_EI, Hydrogen_MISO_NE2050_EI, Hydrogen_PJM_NE2050_EI, Hydrogen_SPP_NE2050_EI,
                               Battery_SERC_NE2050_EI, Battery_NE_NE2050_EI, Battery_NY_NE2050_EI, Battery_MISO_NE2050_EI, Battery_PJM_NE2050_EI, Battery_SPP_NE2050_EI,
                               Wind_SERC_NE2050_EI, Wind_NE_NE2050_EI, Wind_NY_NE2050_EI, Wind_MISO_NE2050_EI, Wind_PJM_NE2050_EI, Wind_SPP_NE2050_EI,
                               Solar_SERC_NE2050_EI, Solar_NE_NE2050_EI, Solar_NY_NE2050_EI, Solar_MISO_NE2050_EI, Solar_PJM_NE2050_EI, Solar_SPP_NE2050_EI,
                               DAC_SERC_NE2050_EI, DAC_NE_NE2050_EI, DAC_NY_NE2050_EI, DAC_MISO_NE2050_EI, DAC_PJM_NE2050_EI, DAC_SPP_NE2050_EI,
                               CoalCCS_NW_NE2050_EI, CoalCCS_SW_NE2050_EI, CoalCCS_NOE_NE2050_EI, CoalCCS_SE_NE2050_EI,
                               CCCCS_NW_NE2050_EI, CCCCS_SW_NE2050_EI, CCCCS_NOE_NE2050_EI, CCCCS_SE_NE2050_EI,
                               CC_NW_NE2050_EI, CC_SW_NE2050_EI, CC_NOE_NE2050_EI, CC_SE_NE2050_EI,
                               Nuclear_NW_NE2050_EI, Nuclear_SW_NE2050_EI, Nuclear_NOE_NE2050_EI, Nuclear_SE_NE2050_EI,
                               Hydrogen_NW_NE2050_EI, Hydrogen_SW_NE2050_EI, Hydrogen_NOE_NE2050_EI, Hydrogen_SE_NE2050_EI,
                               Battery_NW_NE2050_EI, Battery_SW_NE2050_EI, Battery_NOE_NE2050_EI, Battery_SE_NE2050_EI,
                               DAC_NW_NE2050_EI, DAC_SW_NE2050_EI, DAC_NOE_NE2050_EI, DAC_SE_NE2050_EI,
                               Wind_NW_NE2050_EI, Wind_SW_NE2050_EI, Wind_NOE_NE2050_EI, Wind_SE_NE2050_EI,
                               Solar_NW_NE2050_EI, Solar_SW_NE2050_EI, Solar_NOE_NE2050_EI, Solar_SE_NE2050_EI,
                              CoalCCS_SERC_NE2020_EI_2, CoalCCS_NE_NE2020_EI_2, CoalCCS_NY_NE2020_EI_2, CoalCCS_MISO_NE2020_EI_2, CoalCCS_PJM_NE2020_EI_2, CoalCCS_SPP_NE2020_EI_2,
                              CCCCS_SERC_NE2020_EI_2, CCCCS_NE_NE2020_EI_2, CCCCS_NY_NE2020_EI_2, CCCCS_MISO_NE2020_EI_2, CCCCS_PJM_NE2020_EI_2, CCCCS_SPP_NE2020_EI_2,
                              CC_SERC_NE2020_EI_2, CC_NE_NE2020_EI_2, CC_NY_NE2020_EI_2, CC_MISO_NE2020_EI_2, CC_PJM_NE2020_EI_2, CC_SPP_NE2020_EI_2,
                              Nuclear_SERC_NE2020_EI_2, Nuclear_NE_NE2020_EI_2, Nuclear_NY_NE2020_EI_2, Nuclear_MISO_NE2020_EI_2, Nuclear_PJM_NE2020_EI_2, Nuclear_SPP_NE2020_EI_2,
                              Hydrogen_SERC_NE2020_EI_2, Hydrogen_NE_NE2020_EI_2, Hydrogen_NY_NE2020_EI_2, Hydrogen_MISO_NE2020_EI_2, Hydrogen_PJM_NE2020_EI_2, Hydrogen_SPP_NE2020_EI_2,
                              Battery_SERC_NE2020_EI_2, Battery_NE_NE2020_EI_2, Battery_NY_NE2020_EI_2, Battery_MISO_NE2020_EI_2, Battery_PJM_NE2020_EI_2, Battery_SPP_NE2020_EI_2,
                              Wind_SERC_NE2020_EI_2, Wind_NE_NE2020_EI_2, Wind_NY_NE2020_EI_2, Wind_MISO_NE2020_EI_2, Wind_PJM_NE2020_EI_2, Wind_SPP_NE2020_EI_2,
                              Solar_SERC_NE2020_EI_2, Solar_NE_NE2020_EI_2, Solar_NY_NE2020_EI_2, Solar_MISO_NE2020_EI_2, Solar_PJM_NE2020_EI_2, Solar_SPP_NE2020_EI_2,
                              DAC_SERC_NE2020_EI_2, DAC_NE_NE2020_EI_2, DAC_NY_NE2020_EI_2, DAC_MISO_NE2020_EI_2, DAC_PJM_NE2020_EI_2, DAC_SPP_NE2020_EI_2,
                              CoalCCS_NW_NE2020_EI_2, CoalCCS_SW_NE2020_EI_2, CoalCCS_NOE_NE2020_EI_2, CoalCCS_SE_NE2020_EI_2,
                              CCCCS_NW_NE2020_EI_2, CCCCS_SW_NE2020_EI_2, CCCCS_NOE_NE2020_EI_2, CCCCS_SE_NE2020_EI_2,
                              CC_NW_NE2020_EI_2, CC_SW_NE2020_EI_2, CC_NOE_NE2020_EI_2, CC_SE_NE2020_EI_2,
                              Nuclear_NW_NE2020_EI_2, Nuclear_SW_NE2020_EI_2, Nuclear_NOE_NE2020_EI_2, Nuclear_SE_NE2020_EI_2,
                              Hydrogen_NW_NE2020_EI_2, Hydrogen_SW_NE2020_EI_2, Hydrogen_NOE_NE2020_EI_2, Hydrogen_SE_NE2020_EI_2,
                              Battery_NW_NE2020_EI_2, Battery_SW_NE2020_EI_2, Battery_NOE_NE2020_EI_2, Battery_SE_NE2020_EI_2,
                              DAC_NW_NE2020_EI_2, DAC_SW_NE2020_EI_2, DAC_NOE_NE2020_EI_2, DAC_SE_NE2020_EI_2,
                              Wind_NW_NE2020_EI_2, Wind_SW_NE2020_EI_2, Wind_NOE_NE2020_EI_2, Wind_SE_NE2020_EI_2,
                              Solar_NW_NE2020_EI_2, Solar_SW_NE2020_EI_2, Solar_NOE_NE2020_EI_2, Solar_SE_NE2020_EI_2,
                              CoalCCS_SERC_NE2050_EI_2, CoalCCS_NE_NE2050_EI_2, CoalCCS_NY_NE2050_EI_2, CoalCCS_MISO_NE2050_EI_2, CoalCCS_PJM_NE2050_EI_2, CoalCCS_SPP_NE2050_EI_2,
                              CCCCS_SERC_NE2050_EI_2, CCCCS_NE_NE2050_EI_2, CCCCS_NY_NE2050_EI_2, CCCCS_MISO_NE2050_EI_2, CCCCS_PJM_NE2050_EI_2, CCCCS_SPP_NE2050_EI_2,
                              CC_SERC_NE2050_EI_2, CC_NE_NE2050_EI_2, CC_NY_NE2050_EI_2, CC_MISO_NE2050_EI_2, CC_PJM_NE2050_EI_2, CC_SPP_NE2050_EI_2,
                              Nuclear_SERC_NE2050_EI_2, Nuclear_NE_NE2050_EI_2, Nuclear_NY_NE2050_EI_2, Nuclear_MISO_NE2050_EI_2, Nuclear_PJM_NE2050_EI_2, Nuclear_SPP_NE2050_EI_2,
                              Hydrogen_SERC_NE2050_EI_2, Hydrogen_NE_NE2050_EI_2, Hydrogen_NY_NE2050_EI_2, Hydrogen_MISO_NE2050_EI_2, Hydrogen_PJM_NE2050_EI_2, Hydrogen_SPP_NE2050_EI_2,
                              Battery_SERC_NE2050_EI_2, Battery_NE_NE2050_EI_2, Battery_NY_NE2050_EI_2, Battery_MISO_NE2050_EI_2, Battery_PJM_NE2050_EI_2, Battery_SPP_NE2050_EI_2,
                              Wind_SERC_NE2050_EI_2, Wind_NE_NE2050_EI_2, Wind_NY_NE2050_EI_2, Wind_MISO_NE2050_EI_2, Wind_PJM_NE2050_EI_2, Wind_SPP_NE2050_EI_2,
                              Solar_SERC_NE2050_EI_2, Solar_NE_NE2050_EI_2, Solar_NY_NE2050_EI_2, Solar_MISO_NE2050_EI_2, Solar_PJM_NE2050_EI_2, Solar_SPP_NE2050_EI_2,
                              DAC_SERC_NE2050_EI_2, DAC_NE_NE2050_EI_2, DAC_NY_NE2050_EI_2, DAC_MISO_NE2050_EI_2, DAC_PJM_NE2050_EI_2, DAC_SPP_NE2050_EI_2,
                              CoalCCS_NW_NE2050_EI_2, CoalCCS_SW_NE2050_EI_2, CoalCCS_NOE_NE2050_EI_2, CoalCCS_SE_NE2050_EI_2,
                              CCCCS_NW_NE2050_EI_2, CCCCS_SW_NE2050_EI_2, CCCCS_NOE_NE2050_EI_2, CCCCS_SE_NE2050_EI_2,
                              CC_NW_NE2050_EI_2, CC_SW_NE2050_EI_2, CC_NOE_NE2050_EI_2, CC_SE_NE2050_EI_2,
                              Nuclear_NW_NE2050_EI_2, Nuclear_SW_NE2050_EI_2, Nuclear_NOE_NE2050_EI_2, Nuclear_SE_NE2050_EI_2,
                              Hydrogen_NW_NE2050_EI_2, Hydrogen_SW_NE2050_EI_2, Hydrogen_NOE_NE2050_EI_2, Hydrogen_SE_NE2050_EI_2,
                              Battery_NW_NE2050_EI_2, Battery_SW_NE2050_EI_2, Battery_NOE_NE2050_EI_2, Battery_SE_NE2050_EI_2,
                              DAC_NW_NE2050_EI_2, DAC_SW_NE2050_EI_2, DAC_NOE_NE2050_EI_2, DAC_SE_NE2050_EI_2,
                              Wind_NW_NE2050_EI_2, Wind_SW_NE2050_EI_2, Wind_NOE_NE2050_EI_2, Wind_SE_NE2050_EI_2,
                              Solar_NW_NE2050_EI_2, Solar_SW_NE2050_EI_2, Solar_NOE_NE2050_EI_2, Solar_SE_NE2050_EI_2)

    chart = alt.Chart(df_capEXP_EI).mark_bar(size=17).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Capacity):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Capacity Investments (GW)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Region:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Technology',
            sort='ascending'),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Technology:N',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['#ffffff','#ff6f69', '#96ceb4', 'darkolivegreen', 'black', 'saddlebrown', 'lightpink', '#ffcc5c', 'skyblue'],
                        ),
                        )).resolve_scale(y='shared').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=15, titleFontSize=15
                                                                          ).properties(width=85, height=400).show()

    # Capacity investments by Region - ERCOT:
    (CoalCCS_SERC_NE2020_ERCOT, CoalCCS_NE_NE2020_ERCOT, CoalCCS_NY_NE2020_ERCOT, CoalCCS_MISO_NE2020_ERCOT, CoalCCS_PJM_NE2020_ERCOT, CoalCCS_SPP_NE2020_ERCOT,
     CCCCS_SERC_NE2020_ERCOT, CCCCS_NE_NE2020_ERCOT, CCCCS_NY_NE2020_ERCOT, CCCCS_MISO_NE2020_ERCOT, CCCCS_PJM_NE2020_ERCOT, CCCCS_SPP_NE2020_ERCOT,
     CC_SERC_NE2020_ERCOT, CC_NE_NE2020_ERCOT, CC_NY_NE2020_ERCOT, CC_MISO_NE2020_ERCOT, CC_PJM_NE2020_ERCOT, CC_SPP_NE2020_ERCOT,
     Nuclear_SERC_NE2020_ERCOT, Nuclear_NE_NE2020_ERCOT, Nuclear_NY_NE2020_ERCOT, Nuclear_MISO_NE2020_ERCOT, Nuclear_PJM_NE2020_ERCOT, Nuclear_SPP_NE2020_ERCOT,
     Hydrogen_SERC_NE2020_ERCOT, Hydrogen_NE_NE2020_ERCOT, Hydrogen_NY_NE2020_ERCOT, Hydrogen_MISO_NE2020_ERCOT, Hydrogen_PJM_NE2020_ERCOT, Hydrogen_SPP_NE2020_ERCOT,
     Battery_SERC_NE2020_ERCOT, Battery_NE_NE2020_ERCOT, Battery_NY_NE2020_ERCOT, Battery_MISO_NE2020_ERCOT, Battery_PJM_NE2020_ERCOT, Battery_SPP_NE2020_ERCOT,
     Wind_SERC_NE2020_ERCOT, Wind_NE_NE2020_ERCOT, Wind_NY_NE2020_ERCOT, Wind_MISO_NE2020_ERCOT, Wind_PJM_NE2020_ERCOT, Wind_SPP_NE2020_ERCOT,
     Solar_SERC_NE2020_ERCOT, Solar_NE_NE2020_ERCOT, Solar_NY_NE2020_ERCOT, Solar_MISO_NE2020_ERCOT, Solar_PJM_NE2020_ERCOT, Solar_SPP_NE2020_ERCOT,
     DAC_SERC_NE2020_ERCOT, DAC_NE_NE2020_ERCOT, DAC_NY_NE2020_ERCOT, DAC_MISO_NE2020_ERCOT, DAC_PJM_NE2020_ERCOT, DAC_SPP_NE2020_ERCOT,
     CoalCCS_NW_NE2020_ERCOT, CoalCCS_SW_NE2020_ERCOT, CoalCCS_NOE_NE2020_ERCOT, CoalCCS_SE_NE2020_ERCOT,
     CCCCS_NW_NE2020_ERCOT, CCCCS_SW_NE2020_ERCOT, CCCCS_NOE_NE2020_ERCOT, CCCCS_SE_NE2020_ERCOT,
     CC_NW_NE2020_ERCOT, CC_SW_NE2020_ERCOT, CC_NOE_NE2020_ERCOT, CC_SE_NE2020_ERCOT,
     Nuclear_NW_NE2020_ERCOT, Nuclear_SW_NE2020_ERCOT, Nuclear_NOE_NE2020_ERCOT, Nuclear_SE_NE2020_ERCOT,
     Hydrogen_NW_NE2020_ERCOT, Hydrogen_SW_NE2020_ERCOT, Hydrogen_NOE_NE2020_ERCOT, Hydrogen_SE_NE2020_ERCOT,
     Battery_NW_NE2020_ERCOT, Battery_SW_NE2020_ERCOT, Battery_NOE_NE2020_ERCOT, Battery_SE_NE2020_ERCOT,
     DAC_NW_NE2020_ERCOT, DAC_SW_NE2020_ERCOT, DAC_NOE_NE2020_ERCOT, DAC_SE_NE2020_ERCOT,
     Wind_NW_NE2020_ERCOT, Wind_SW_NE2020_ERCOT, Wind_NOE_NE2020_ERCOT, Wind_SE_NE2020_ERCOT,
     Solar_NW_NE2020_ERCOT, Solar_SW_NE2020_ERCOT, Solar_NOE_NE2020_ERCOT, Solar_SE_NE2020_ERCOT,
     CoalCCS_SERC_NE2020_ERCOT_2, CoalCCS_NE_NE2020_ERCOT_2, CoalCCS_NY_NE2020_ERCOT_2, CoalCCS_MISO_NE2020_ERCOT_2, CoalCCS_PJM_NE2020_ERCOT_2, CoalCCS_SPP_NE2020_ERCOT_2,
     CCCCS_SERC_NE2020_ERCOT_2, CCCCS_NE_NE2020_ERCOT_2, CCCCS_NY_NE2020_ERCOT_2, CCCCS_MISO_NE2020_ERCOT_2, CCCCS_PJM_NE2020_ERCOT_2, CCCCS_SPP_NE2020_ERCOT_2,
     CC_SERC_NE2020_ERCOT_2, CC_NE_NE2020_ERCOT_2, CC_NY_NE2020_ERCOT_2, CC_MISO_NE2020_ERCOT_2, CC_PJM_NE2020_ERCOT_2, CC_SPP_NE2020_ERCOT_2,
     Nuclear_SERC_NE2020_ERCOT_2, Nuclear_NE_NE2020_ERCOT_2, Nuclear_NY_NE2020_ERCOT_2, Nuclear_MISO_NE2020_ERCOT_2, Nuclear_PJM_NE2020_ERCOT_2, Nuclear_SPP_NE2020_ERCOT_2,
     Hydrogen_SERC_NE2020_ERCOT_2, Hydrogen_NE_NE2020_ERCOT_2, Hydrogen_NY_NE2020_ERCOT_2, Hydrogen_MISO_NE2020_ERCOT_2, Hydrogen_PJM_NE2020_ERCOT_2, Hydrogen_SPP_NE2020_ERCOT_2,
     Battery_SERC_NE2020_ERCOT_2, Battery_NE_NE2020_ERCOT_2, Battery_NY_NE2020_ERCOT_2, Battery_MISO_NE2020_ERCOT_2, Battery_PJM_NE2020_ERCOT_2, Battery_SPP_NE2020_ERCOT_2,
     Wind_SERC_NE2020_ERCOT_2, Wind_NE_NE2020_ERCOT_2, Wind_NY_NE2020_ERCOT_2, Wind_MISO_NE2020_ERCOT_2, Wind_PJM_NE2020_ERCOT_2, Wind_SPP_NE2020_ERCOT_2,
     Solar_SERC_NE2020_ERCOT_2, Solar_NE_NE2020_ERCOT_2, Solar_NY_NE2020_ERCOT_2, Solar_MISO_NE2020_ERCOT_2, Solar_PJM_NE2020_ERCOT_2, Solar_SPP_NE2020_ERCOT_2,
     DAC_SERC_NE2020_ERCOT_2, DAC_NE_NE2020_ERCOT_2, DAC_NY_NE2020_ERCOT_2, DAC_MISO_NE2020_ERCOT_2, DAC_PJM_NE2020_ERCOT_2, DAC_SPP_NE2020_ERCOT_2,
     CoalCCS_NW_NE2020_ERCOT_2, CoalCCS_SW_NE2020_ERCOT_2, CoalCCS_NOE_NE2020_ERCOT_2, CoalCCS_SE_NE2020_ERCOT_2,
     CCCCS_NW_NE2020_ERCOT_2, CCCCS_SW_NE2020_ERCOT_2, CCCCS_NOE_NE2020_ERCOT_2, CCCCS_SE_NE2020_ERCOT_2,
     CC_NW_NE2020_ERCOT_2, CC_SW_NE2020_ERCOT_2, CC_NOE_NE2020_ERCOT_2, CC_SE_NE2020_ERCOT_2,
     Nuclear_NW_NE2020_ERCOT_2, Nuclear_SW_NE2020_ERCOT_2, Nuclear_NOE_NE2020_ERCOT_2, Nuclear_SE_NE2020_ERCOT_2,
     Hydrogen_NW_NE2020_ERCOT_2, Hydrogen_SW_NE2020_ERCOT_2, Hydrogen_NOE_NE2020_ERCOT_2, Hydrogen_SE_NE2020_ERCOT_2,
     Battery_NW_NE2020_ERCOT_2, Battery_SW_NE2020_ERCOT_2, Battery_NOE_NE2020_ERCOT_2, Battery_SE_NE2020_ERCOT_2,
     DAC_NW_NE2020_ERCOT_2, DAC_SW_NE2020_ERCOT_2, DAC_NOE_NE2020_ERCOT_2, DAC_SE_NE2020_ERCOT_2,
     Wind_NW_NE2020_ERCOT_2, Wind_SW_NE2020_ERCOT_2, Wind_NOE_NE2020_ERCOT_2, Wind_SE_NE2020_ERCOT_2,
     Solar_NW_NE2020_ERCOT_2, Solar_SW_NE2020_ERCOT_2, Solar_NOE_NE2020_ERCOT_2, Solar_SE_NE2020_ERCOT_2) = capRegions_temp(ref_dir, techCase, planningScr='NE2020', interConn='ERCOT')

    (CoalCCS_SERC_NE2050_ERCOT, CoalCCS_NE_NE2050_ERCOT, CoalCCS_NY_NE2050_ERCOT, CoalCCS_MISO_NE2050_ERCOT, CoalCCS_PJM_NE2050_ERCOT, CoalCCS_SPP_NE2050_ERCOT,
     CCCCS_SERC_NE2050_ERCOT, CCCCS_NE_NE2050_ERCOT, CCCCS_NY_NE2050_ERCOT, CCCCS_MISO_NE2050_ERCOT, CCCCS_PJM_NE2050_ERCOT, CCCCS_SPP_NE2050_ERCOT,
     CC_SERC_NE2050_ERCOT, CC_NE_NE2050_ERCOT, CC_NY_NE2050_ERCOT, CC_MISO_NE2050_ERCOT, CC_PJM_NE2050_ERCOT, CC_SPP_NE2050_ERCOT,
     Nuclear_SERC_NE2050_ERCOT, Nuclear_NE_NE2050_ERCOT, Nuclear_NY_NE2050_ERCOT, Nuclear_MISO_NE2050_ERCOT, Nuclear_PJM_NE2050_ERCOT, Nuclear_SPP_NE2050_ERCOT,
     Hydrogen_SERC_NE2050_ERCOT, Hydrogen_NE_NE2050_ERCOT, Hydrogen_NY_NE2050_ERCOT, Hydrogen_MISO_NE2050_ERCOT, Hydrogen_PJM_NE2050_ERCOT, Hydrogen_SPP_NE2050_ERCOT,
     Battery_SERC_NE2050_ERCOT, Battery_NE_NE2050_ERCOT, Battery_NY_NE2050_ERCOT, Battery_MISO_NE2050_ERCOT, Battery_PJM_NE2050_ERCOT, Battery_SPP_NE2050_ERCOT,
     Wind_SERC_NE2050_ERCOT, Wind_NE_NE2050_ERCOT, Wind_NY_NE2050_ERCOT, Wind_MISO_NE2050_ERCOT, Wind_PJM_NE2050_ERCOT, Wind_SPP_NE2050_ERCOT,
     Solar_SERC_NE2050_ERCOT, Solar_NE_NE2050_ERCOT, Solar_NY_NE2050_ERCOT, Solar_MISO_NE2050_ERCOT, Solar_PJM_NE2050_ERCOT, Solar_SPP_NE2050_ERCOT,
     DAC_SERC_NE2050_ERCOT, DAC_NE_NE2050_ERCOT, DAC_NY_NE2050_ERCOT, DAC_MISO_NE2050_ERCOT, DAC_PJM_NE2050_ERCOT, DAC_SPP_NE2050_ERCOT,
     CoalCCS_NW_NE2050_ERCOT, CoalCCS_SW_NE2050_ERCOT, CoalCCS_NOE_NE2050_ERCOT, CoalCCS_SE_NE2050_ERCOT,
     CCCCS_NW_NE2050_ERCOT, CCCCS_SW_NE2050_ERCOT, CCCCS_NOE_NE2050_ERCOT, CCCCS_SE_NE2050_ERCOT,
     CC_NW_NE2050_ERCOT, CC_SW_NE2050_ERCOT, CC_NOE_NE2050_ERCOT, CC_SE_NE2050_ERCOT,
     Nuclear_NW_NE2050_ERCOT, Nuclear_SW_NE2050_ERCOT, Nuclear_NOE_NE2050_ERCOT, Nuclear_SE_NE2050_ERCOT,
     Hydrogen_NW_NE2050_ERCOT, Hydrogen_SW_NE2050_ERCOT, Hydrogen_NOE_NE2050_ERCOT, Hydrogen_SE_NE2050_ERCOT,
     Battery_NW_NE2050_ERCOT, Battery_SW_NE2050_ERCOT, Battery_NOE_NE2050_ERCOT, Battery_SE_NE2050_ERCOT,
     DAC_NW_NE2050_ERCOT, DAC_SW_NE2050_ERCOT, DAC_NOE_NE2050_ERCOT, DAC_SE_NE2050_ERCOT,
     Wind_NW_NE2050_ERCOT, Wind_SW_NE2050_ERCOT, Wind_NOE_NE2050_ERCOT, Wind_SE_NE2050_ERCOT,
     Solar_NW_NE2050_ERCOT, Solar_SW_NE2050_ERCOT, Solar_NOE_NE2050_ERCOT, Solar_SE_NE2050_ERCOT,
     CoalCCS_SERC_NE2050_ERCOT_2, CoalCCS_NE_NE2050_ERCOT_2, CoalCCS_NY_NE2050_ERCOT_2, CoalCCS_MISO_NE2050_ERCOT_2, CoalCCS_PJM_NE2050_ERCOT_2, CoalCCS_SPP_NE2050_ERCOT_2,
     CCCCS_SERC_NE2050_ERCOT_2, CCCCS_NE_NE2050_ERCOT_2, CCCCS_NY_NE2050_ERCOT_2, CCCCS_MISO_NE2050_ERCOT_2, CCCCS_PJM_NE2050_ERCOT_2, CCCCS_SPP_NE2050_ERCOT_2,
     CC_SERC_NE2050_ERCOT_2, CC_NE_NE2050_ERCOT_2, CC_NY_NE2050_ERCOT_2, CC_MISO_NE2050_ERCOT_2, CC_PJM_NE2050_ERCOT_2, CC_SPP_NE2050_ERCOT_2,
     Nuclear_SERC_NE2050_ERCOT_2, Nuclear_NE_NE2050_ERCOT_2, Nuclear_NY_NE2050_ERCOT_2, Nuclear_MISO_NE2050_ERCOT_2, Nuclear_PJM_NE2050_ERCOT_2, Nuclear_SPP_NE2050_ERCOT_2,
     Hydrogen_SERC_NE2050_ERCOT_2, Hydrogen_NE_NE2050_ERCOT_2, Hydrogen_NY_NE2050_ERCOT_2, Hydrogen_MISO_NE2050_ERCOT_2, Hydrogen_PJM_NE2050_ERCOT_2, Hydrogen_SPP_NE2050_ERCOT_2,
     Battery_SERC_NE2050_ERCOT_2, Battery_NE_NE2050_ERCOT_2, Battery_NY_NE2050_ERCOT_2, Battery_MISO_NE2050_ERCOT_2, Battery_PJM_NE2050_ERCOT_2, Battery_SPP_NE2050_ERCOT_2,
     Wind_SERC_NE2050_ERCOT_2, Wind_NE_NE2050_ERCOT_2, Wind_NY_NE2050_ERCOT_2, Wind_MISO_NE2050_ERCOT_2, Wind_PJM_NE2050_ERCOT_2, Wind_SPP_NE2050_ERCOT_2,
     Solar_SERC_NE2050_ERCOT_2, Solar_NE_NE2050_ERCOT_2, Solar_NY_NE2050_ERCOT_2, Solar_MISO_NE2050_ERCOT_2, Solar_PJM_NE2050_ERCOT_2, Solar_SPP_NE2050_ERCOT_2,
     DAC_SERC_NE2050_ERCOT_2, DAC_NE_NE2050_ERCOT_2, DAC_NY_NE2050_ERCOT_2, DAC_MISO_NE2050_ERCOT_2, DAC_PJM_NE2050_ERCOT_2, DAC_SPP_NE2050_ERCOT_2,
     CoalCCS_NW_NE2050_ERCOT_2, CoalCCS_SW_NE2050_ERCOT_2, CoalCCS_NOE_NE2050_ERCOT_2, CoalCCS_SE_NE2050_ERCOT_2,
     CCCCS_NW_NE2050_ERCOT_2, CCCCS_SW_NE2050_ERCOT_2, CCCCS_NOE_NE2050_ERCOT_2, CCCCS_SE_NE2050_ERCOT_2,
     CC_NW_NE2050_ERCOT_2, CC_SW_NE2050_ERCOT_2, CC_NOE_NE2050_ERCOT_2, CC_SE_NE2050_ERCOT_2,
     Nuclear_NW_NE2050_ERCOT_2, Nuclear_SW_NE2050_ERCOT_2, Nuclear_NOE_NE2050_ERCOT_2, Nuclear_SE_NE2050_ERCOT_2,
     Hydrogen_NW_NE2050_ERCOT_2, Hydrogen_SW_NE2050_ERCOT_2, Hydrogen_NOE_NE2050_ERCOT_2, Hydrogen_SE_NE2050_ERCOT_2,
     Battery_NW_NE2050_ERCOT_2, Battery_SW_NE2050_ERCOT_2, Battery_NOE_NE2050_ERCOT_2, Battery_SE_NE2050_ERCOT_2,
     DAC_NW_NE2050_ERCOT_2, DAC_SW_NE2050_ERCOT_2, DAC_NOE_NE2050_ERCOT_2, DAC_SE_NE2050_ERCOT_2,
     Wind_NW_NE2050_ERCOT_2, Wind_SW_NE2050_ERCOT_2, Wind_NOE_NE2050_ERCOT_2, Wind_SE_NE2050_ERCOT_2,
     Solar_NW_NE2050_ERCOT_2, Solar_SW_NE2050_ERCOT_2, Solar_NOE_NE2050_ERCOT_2, Solar_SE_NE2050_ERCOT_2) = capRegions_temp(ref_dir, techCase, planningScr='NE2050', interConn='ERCOT')

    df_capEXP_ERCOT = graphERCOTCap(CoalCCS_SERC_NE2020_ERCOT, CoalCCS_NE_NE2020_ERCOT, CoalCCS_NY_NE2020_ERCOT, CoalCCS_MISO_NE2020_ERCOT, CoalCCS_PJM_NE2020_ERCOT, CoalCCS_SPP_NE2020_ERCOT,
                                     CCCCS_SERC_NE2020_ERCOT, CCCCS_NE_NE2020_ERCOT, CCCCS_NY_NE2020_ERCOT, CCCCS_MISO_NE2020_ERCOT, CCCCS_PJM_NE2020_ERCOT, CCCCS_SPP_NE2020_ERCOT,
                                     CC_SERC_NE2020_ERCOT, CC_NE_NE2020_ERCOT, CC_NY_NE2020_ERCOT, CC_MISO_NE2020_ERCOT, CC_PJM_NE2020_ERCOT, CC_SPP_NE2020_ERCOT,
                                     Nuclear_SERC_NE2020_ERCOT, Nuclear_NE_NE2020_ERCOT, Nuclear_NY_NE2020_ERCOT, Nuclear_MISO_NE2020_ERCOT, Nuclear_PJM_NE2020_ERCOT, Nuclear_SPP_NE2020_ERCOT,
                                     Hydrogen_SERC_NE2020_ERCOT, Hydrogen_NE_NE2020_ERCOT, Hydrogen_NY_NE2020_ERCOT, Hydrogen_MISO_NE2020_ERCOT, Hydrogen_PJM_NE2020_ERCOT, Hydrogen_SPP_NE2020_ERCOT,
                                     Battery_SERC_NE2020_ERCOT, Battery_NE_NE2020_ERCOT, Battery_NY_NE2020_ERCOT, Battery_MISO_NE2020_ERCOT, Battery_PJM_NE2020_ERCOT, Battery_SPP_NE2020_ERCOT,
                                     Wind_SERC_NE2020_ERCOT, Wind_NE_NE2020_ERCOT, Wind_NY_NE2020_ERCOT, Wind_MISO_NE2020_ERCOT, Wind_PJM_NE2020_ERCOT, Wind_SPP_NE2020_ERCOT,
                                     Solar_SERC_NE2020_ERCOT, Solar_NE_NE2020_ERCOT, Solar_NY_NE2020_ERCOT, Solar_MISO_NE2020_ERCOT, Solar_PJM_NE2020_ERCOT, Solar_SPP_NE2020_ERCOT,
                                     DAC_SERC_NE2020_ERCOT, DAC_NE_NE2020_ERCOT, DAC_NY_NE2020_ERCOT, DAC_MISO_NE2020_ERCOT, DAC_PJM_NE2020_ERCOT, DAC_SPP_NE2020_ERCOT,
                                     CoalCCS_NW_NE2020_ERCOT, CoalCCS_SW_NE2020_ERCOT, CoalCCS_NOE_NE2020_ERCOT, CoalCCS_SE_NE2020_ERCOT,
                                     CCCCS_NW_NE2020_ERCOT, CCCCS_SW_NE2020_ERCOT, CCCCS_NOE_NE2020_ERCOT, CCCCS_SE_NE2020_ERCOT,
                                     CC_NW_NE2020_ERCOT, CC_SW_NE2020_ERCOT, CC_NOE_NE2020_ERCOT, CC_SE_NE2020_ERCOT,
                                     Nuclear_NW_NE2020_ERCOT, Nuclear_SW_NE2020_ERCOT, Nuclear_NOE_NE2020_ERCOT, Nuclear_SE_NE2020_ERCOT,
                                     Hydrogen_NW_NE2020_ERCOT, Hydrogen_SW_NE2020_ERCOT, Hydrogen_NOE_NE2020_ERCOT, Hydrogen_SE_NE2020_ERCOT,
                                     Battery_NW_NE2020_ERCOT, Battery_SW_NE2020_ERCOT, Battery_NOE_NE2020_ERCOT, Battery_SE_NE2020_ERCOT,
                                     DAC_NW_NE2020_ERCOT, DAC_SW_NE2020_ERCOT, DAC_NOE_NE2020_ERCOT, DAC_SE_NE2020_ERCOT,
                                     Wind_NW_NE2020_ERCOT, Wind_SW_NE2020_ERCOT, Wind_NOE_NE2020_ERCOT, Wind_SE_NE2020_ERCOT,
                                     Solar_NW_NE2020_ERCOT, Solar_SW_NE2020_ERCOT, Solar_NOE_NE2020_ERCOT, Solar_SE_NE2020_ERCOT,
                                     CoalCCS_SERC_NE2050_ERCOT, CoalCCS_NE_NE2050_ERCOT, CoalCCS_NY_NE2050_ERCOT, CoalCCS_MISO_NE2050_ERCOT, CoalCCS_PJM_NE2050_ERCOT, CoalCCS_SPP_NE2050_ERCOT,
                                     CCCCS_SERC_NE2050_ERCOT, CCCCS_NE_NE2050_ERCOT, CCCCS_NY_NE2050_ERCOT, CCCCS_MISO_NE2050_ERCOT, CCCCS_PJM_NE2050_ERCOT, CCCCS_SPP_NE2050_ERCOT,
                                     CC_SERC_NE2050_ERCOT, CC_NE_NE2050_ERCOT, CC_NY_NE2050_ERCOT, CC_MISO_NE2050_ERCOT, CC_PJM_NE2050_ERCOT, CC_SPP_NE2050_ERCOT,
                                     Nuclear_SERC_NE2050_ERCOT, Nuclear_NE_NE2050_ERCOT, Nuclear_NY_NE2050_ERCOT, Nuclear_MISO_NE2050_ERCOT, Nuclear_PJM_NE2050_ERCOT, Nuclear_SPP_NE2050_ERCOT,
                                     Hydrogen_SERC_NE2050_ERCOT, Hydrogen_NE_NE2050_ERCOT, Hydrogen_NY_NE2050_ERCOT, Hydrogen_MISO_NE2050_ERCOT, Hydrogen_PJM_NE2050_ERCOT, Hydrogen_SPP_NE2050_ERCOT,
                                     Battery_SERC_NE2050_ERCOT, Battery_NE_NE2050_ERCOT, Battery_NY_NE2050_ERCOT, Battery_MISO_NE2050_ERCOT, Battery_PJM_NE2050_ERCOT, Battery_SPP_NE2050_ERCOT,
                                     Wind_SERC_NE2050_ERCOT, Wind_NE_NE2050_ERCOT, Wind_NY_NE2050_ERCOT, Wind_MISO_NE2050_ERCOT, Wind_PJM_NE2050_ERCOT, Wind_SPP_NE2050_ERCOT,
                                     Solar_SERC_NE2050_ERCOT, Solar_NE_NE2050_ERCOT, Solar_NY_NE2050_ERCOT, Solar_MISO_NE2050_ERCOT, Solar_PJM_NE2050_ERCOT, Solar_SPP_NE2050_ERCOT,
                                     DAC_SERC_NE2050_ERCOT, DAC_NE_NE2050_ERCOT, DAC_NY_NE2050_ERCOT, DAC_MISO_NE2050_ERCOT, DAC_PJM_NE2050_ERCOT, DAC_SPP_NE2050_ERCOT,
                                     CoalCCS_NW_NE2050_ERCOT, CoalCCS_SW_NE2050_ERCOT, CoalCCS_NOE_NE2050_ERCOT, CoalCCS_SE_NE2050_ERCOT,
                                     CCCCS_NW_NE2050_ERCOT, CCCCS_SW_NE2050_ERCOT, CCCCS_NOE_NE2050_ERCOT, CCCCS_SE_NE2050_ERCOT,
                                     CC_NW_NE2050_ERCOT, CC_SW_NE2050_ERCOT, CC_NOE_NE2050_ERCOT, CC_SE_NE2050_ERCOT,
                                     Nuclear_NW_NE2050_ERCOT, Nuclear_SW_NE2050_ERCOT, Nuclear_NOE_NE2050_ERCOT, Nuclear_SE_NE2050_ERCOT,
                                     Hydrogen_NW_NE2050_ERCOT, Hydrogen_SW_NE2050_ERCOT, Hydrogen_NOE_NE2050_ERCOT, Hydrogen_SE_NE2050_ERCOT,
                                     Battery_NW_NE2050_ERCOT, Battery_SW_NE2050_ERCOT, Battery_NOE_NE2050_ERCOT, Battery_SE_NE2050_ERCOT,
                                     DAC_NW_NE2050_ERCOT, DAC_SW_NE2050_ERCOT, DAC_NOE_NE2050_ERCOT, DAC_SE_NE2050_ERCOT,
                                     Wind_NW_NE2050_ERCOT, Wind_SW_NE2050_ERCOT, Wind_NOE_NE2050_ERCOT, Wind_SE_NE2050_ERCOT,
                                     Solar_NW_NE2050_ERCOT, Solar_SW_NE2050_ERCOT, Solar_NOE_NE2050_ERCOT, Solar_SE_NE2050_ERCOT,
                                    CoalCCS_SERC_NE2020_ERCOT_2, CoalCCS_NE_NE2020_ERCOT_2, CoalCCS_NY_NE2020_ERCOT_2, CoalCCS_MISO_NE2020_ERCOT_2, CoalCCS_PJM_NE2020_ERCOT_2,
                                    CoalCCS_SPP_NE2020_ERCOT_2, CCCCS_SERC_NE2020_ERCOT_2, CCCCS_NE_NE2020_ERCOT_2, CCCCS_NY_NE2020_ERCOT_2, CCCCS_MISO_NE2020_ERCOT_2, CCCCS_PJM_NE2020_ERCOT_2, CCCCS_SPP_NE2020_ERCOT_2,
                                    CC_SERC_NE2020_ERCOT_2, CC_NE_NE2020_ERCOT_2, CC_NY_NE2020_ERCOT_2, CC_MISO_NE2020_ERCOT_2, CC_PJM_NE2020_ERCOT_2, CC_SPP_NE2020_ERCOT_2,
                                    Nuclear_SERC_NE2020_ERCOT_2, Nuclear_NE_NE2020_ERCOT_2, Nuclear_NY_NE2020_ERCOT_2, Nuclear_MISO_NE2020_ERCOT_2, Nuclear_PJM_NE2020_ERCOT_2,
                                    Nuclear_SPP_NE2020_ERCOT_2, Hydrogen_SERC_NE2020_ERCOT_2, Hydrogen_NE_NE2020_ERCOT_2, Hydrogen_NY_NE2020_ERCOT_2, Hydrogen_MISO_NE2020_ERCOT_2, Hydrogen_PJM_NE2020_ERCOT_2,
                                    Hydrogen_SPP_NE2020_ERCOT_2, Battery_SERC_NE2020_ERCOT_2, Battery_NE_NE2020_ERCOT_2, Battery_NY_NE2020_ERCOT_2, Battery_MISO_NE2020_ERCOT_2, Battery_PJM_NE2020_ERCOT_2,
                                    Battery_SPP_NE2020_ERCOT_2, Wind_SERC_NE2020_ERCOT_2, Wind_NE_NE2020_ERCOT_2, Wind_NY_NE2020_ERCOT_2, Wind_MISO_NE2020_ERCOT_2, Wind_PJM_NE2020_ERCOT_2, Wind_SPP_NE2020_ERCOT_2,
                                    Solar_SERC_NE2020_ERCOT_2, Solar_NE_NE2020_ERCOT_2, Solar_NY_NE2020_ERCOT_2, Solar_MISO_NE2020_ERCOT_2, Solar_PJM_NE2020_ERCOT_2, Solar_SPP_NE2020_ERCOT_2,
                                    DAC_SERC_NE2020_ERCOT_2, DAC_NE_NE2020_ERCOT_2, DAC_NY_NE2020_ERCOT_2, DAC_MISO_NE2020_ERCOT_2, DAC_PJM_NE2020_ERCOT_2, DAC_SPP_NE2020_ERCOT_2,
                                    CoalCCS_NW_NE2020_ERCOT_2, CoalCCS_SW_NE2020_ERCOT_2, CoalCCS_NOE_NE2020_ERCOT_2, CoalCCS_SE_NE2020_ERCOT_2,
                                    CCCCS_NW_NE2020_ERCOT_2, CCCCS_SW_NE2020_ERCOT_2, CCCCS_NOE_NE2020_ERCOT_2, CCCCS_SE_NE2020_ERCOT_2,
                                    CC_NW_NE2020_ERCOT_2, CC_SW_NE2020_ERCOT_2, CC_NOE_NE2020_ERCOT_2, CC_SE_NE2020_ERCOT_2,
                                    Nuclear_NW_NE2020_ERCOT_2, Nuclear_SW_NE2020_ERCOT_2, Nuclear_NOE_NE2020_ERCOT_2, Nuclear_SE_NE2020_ERCOT_2,
                                    Hydrogen_NW_NE2020_ERCOT_2, Hydrogen_SW_NE2020_ERCOT_2, Hydrogen_NOE_NE2020_ERCOT_2, Hydrogen_SE_NE2020_ERCOT_2,
                                    Battery_NW_NE2020_ERCOT_2, Battery_SW_NE2020_ERCOT_2, Battery_NOE_NE2020_ERCOT_2, Battery_SE_NE2020_ERCOT_2,
                                    DAC_NW_NE2020_ERCOT_2, DAC_SW_NE2020_ERCOT_2, DAC_NOE_NE2020_ERCOT_2, DAC_SE_NE2020_ERCOT_2,
                                    Wind_NW_NE2020_ERCOT_2, Wind_SW_NE2020_ERCOT_2, Wind_NOE_NE2020_ERCOT_2, Wind_SE_NE2020_ERCOT_2,
                                    Solar_NW_NE2020_ERCOT_2, Solar_SW_NE2020_ERCOT_2, Solar_NOE_NE2020_ERCOT_2, Solar_SE_NE2020_ERCOT_2,
                                    CoalCCS_SERC_NE2050_ERCOT_2, CoalCCS_NE_NE2050_ERCOT_2, CoalCCS_NY_NE2050_ERCOT_2, CoalCCS_MISO_NE2050_ERCOT_2, CoalCCS_PJM_NE2050_ERCOT_2,
                                    CoalCCS_SPP_NE2050_ERCOT_2, CCCCS_SERC_NE2050_ERCOT_2, CCCCS_NE_NE2050_ERCOT_2, CCCCS_NY_NE2050_ERCOT_2, CCCCS_MISO_NE2050_ERCOT_2, CCCCS_PJM_NE2050_ERCOT_2, CCCCS_SPP_NE2050_ERCOT_2,
                                    CC_SERC_NE2050_ERCOT_2, CC_NE_NE2050_ERCOT_2, CC_NY_NE2050_ERCOT_2, CC_MISO_NE2050_ERCOT_2, CC_PJM_NE2050_ERCOT_2, CC_SPP_NE2050_ERCOT_2,
                                    Nuclear_SERC_NE2050_ERCOT_2, Nuclear_NE_NE2050_ERCOT_2, Nuclear_NY_NE2050_ERCOT_2, Nuclear_MISO_NE2050_ERCOT_2, Nuclear_PJM_NE2050_ERCOT_2,
                                    Nuclear_SPP_NE2050_ERCOT_2, Hydrogen_SERC_NE2050_ERCOT_2, Hydrogen_NE_NE2050_ERCOT_2, Hydrogen_NY_NE2050_ERCOT_2, Hydrogen_MISO_NE2050_ERCOT_2, Hydrogen_PJM_NE2050_ERCOT_2,
                                    Hydrogen_SPP_NE2050_ERCOT_2, Battery_SERC_NE2050_ERCOT_2, Battery_NE_NE2050_ERCOT_2, Battery_NY_NE2050_ERCOT_2, Battery_MISO_NE2050_ERCOT_2, Battery_PJM_NE2050_ERCOT_2,
                                    Battery_SPP_NE2050_ERCOT_2, Wind_SERC_NE2050_ERCOT_2, Wind_NE_NE2050_ERCOT_2, Wind_NY_NE2050_ERCOT_2, Wind_MISO_NE2050_ERCOT_2, Wind_PJM_NE2050_ERCOT_2, Wind_SPP_NE2050_ERCOT_2,
                                    Solar_SERC_NE2050_ERCOT_2, Solar_NE_NE2050_ERCOT_2, Solar_NY_NE2050_ERCOT_2, Solar_MISO_NE2050_ERCOT_2, Solar_PJM_NE2050_ERCOT_2, Solar_SPP_NE2050_ERCOT_2,
                                    DAC_SERC_NE2050_ERCOT_2, DAC_NE_NE2050_ERCOT_2, DAC_NY_NE2050_ERCOT_2, DAC_MISO_NE2050_ERCOT_2, DAC_PJM_NE2050_ERCOT_2, DAC_SPP_NE2050_ERCOT_2,
                                    CoalCCS_NW_NE2050_ERCOT_2, CoalCCS_SW_NE2050_ERCOT_2, CoalCCS_NOE_NE2050_ERCOT_2, CoalCCS_SE_NE2050_ERCOT_2,
                                    CCCCS_NW_NE2050_ERCOT_2, CCCCS_SW_NE2050_ERCOT_2, CCCCS_NOE_NE2050_ERCOT_2, CCCCS_SE_NE2050_ERCOT_2,
                                    CC_NW_NE2050_ERCOT_2, CC_SW_NE2050_ERCOT_2, CC_NOE_NE2050_ERCOT_2, CC_SE_NE2050_ERCOT_2,
                                    Nuclear_NW_NE2050_ERCOT_2, Nuclear_SW_NE2050_ERCOT_2, Nuclear_NOE_NE2050_ERCOT_2, Nuclear_SE_NE2050_ERCOT_2,
                                    Hydrogen_NW_NE2050_ERCOT_2, Hydrogen_SW_NE2050_ERCOT_2, Hydrogen_NOE_NE2050_ERCOT_2, Hydrogen_SE_NE2050_ERCOT_2,
                                    Battery_NW_NE2050_ERCOT_2, Battery_SW_NE2050_ERCOT_2, Battery_NOE_NE2050_ERCOT_2, Battery_SE_NE2050_ERCOT_2,
                                    DAC_NW_NE2050_ERCOT_2, DAC_SW_NE2050_ERCOT_2, DAC_NOE_NE2050_ERCOT_2, DAC_SE_NE2050_ERCOT_2,
                                    Wind_NW_NE2050_ERCOT_2, Wind_SW_NE2050_ERCOT_2, Wind_NOE_NE2050_ERCOT_2, Wind_SE_NE2050_ERCOT_2,
                                    Solar_NW_NE2050_ERCOT_2, Solar_SW_NE2050_ERCOT_2, Solar_NOE_NE2050_ERCOT_2, Solar_SE_NE2050_ERCOT_2)

    chart = alt.Chart(df_capEXP_ERCOT).mark_bar(size=25).encode(
        # tell Altair which field to group columns on
        x=alt.X('PlanningScr:N', title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('sum(Capacity):Q',
                axis=alt.Axis(
                    grid=False,
                    title='Capacity Investments (GW)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Region:N', title=None, header=alt.Header(labelFontSize=20)),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Technology',
            sort='ascending'),
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
                                                                          ).properties(width=125, height=400).show()

    # Capacity all regions:
    df_capEXP_all = df_capEXP_EI.append(df_capEXP_ERCOT, ignore_index=True)
    df_capEXP_all['PlanningScr'] = df_capEXP_all['PlanningScr'].apply(wrap, args=[20])
    p = alt.Chart(df_capEXP_all).mark_bar(size=25).encode(
        y = alt.Y('sum(Capacity):Q', axis=alt.Axis(grid=False,title='Capacity Investments (GW)')),
        x = alt.X('PlanningScr:N', title=None, sort=alt.EncodingSortField(field="PlanningScr", op="count", order='ascending')),
        order=alt.Order('Technology',sort='ascending'),
        color = alt.Color('Technology:N',scale=alt.Scale(range=['#ffffff', '#ff6f69', '#96ceb4', 'darkolivegreen', 'black', 'saddlebrown', 'lightpink', '#ffcc5c', 'skyblue'],),),
        facet=alt.Facet('Region',columns=6,title=None,header=alt.Header(labelFontSize=18),
                        sort=alt.EncodingSortField('Region', op='count', order='ascending'))
        ).configure_axis(titleFontSize=20, labelFontSize=18).configure_legend(labelFontSize=18, titleFontSize=18
                                                                          ).properties(width=150, height=400).show()


    # Wind and solar resources:
    (wind_cf, solar_cf, pRegionShapes, loadregions) = resite_figures(shapefile_dir)

    geometry = [Point(xy) for xy in zip(wind_cf.lon, wind_cf.lat)]
    wind_cf = gpd.GeoDataFrame(wind_cf, crs="EPSG:4326", geometry=geometry)
    solar_cf = gpd.GeoDataFrame(solar_cf, crs="EPSG:4326", geometry=geometry)

    windinPoly = gpd.sjoin(wind_cf, loadregions, how='left', op='within')
    solarinPoly = gpd.sjoin(solar_cf, loadregions, how='left', op='within')
    windinPoly = windinPoly.dropna()
    solarinPoly = solarinPoly.dropna()

    # Map of renewable sites:
    fig, ax = plt.subplots(figsize=(8, 4.5))
    cln = 'region'
    # ax.set_aspect('equal')
    windinPoly.plot(ax=ax, column='wind_cf', cmap='viridis_r', markersize=16, legend='True', label="Wind capacity factor")
    loadregions.plot(ax=ax, facecolor="none", edgecolors='black', linewidth=0.7)
    loadregions.plot(ax=ax, column='region', facecolor="none", cmap=BluGrn_6.mpl_colormap, linewidth=2)
    plt.axis('off')
    f = plt.gcf()
    cax = f.get_axes()[1]
    cax.set_ylabel("Wind Capacity Factor", fontweight='bold')
    for idx, row in loadregions.iterrows():
        fnt = 10
        txt = plt.annotate(text=row[cln], xy=(loadregions.geometry.centroid.x[idx], loadregions.geometry.centroid.y[idx]),
                           horizontalalignment='center', fontsize=fnt, fontweight='bold', wrap=True, color='k')
        txt.set_path_effects([PathEffects.withStroke(linewidth=4, foreground='w')])
    ax.autoscale()
    # sm = plt.cm.ScalarMappable(cmap='rainbow', norm=plt.Normalize(vmin=latlonGpd_join['wind_cf'].min(), vmax=latlonGpd_join['wind_cf'].max()))
    # cbar_axis = inset_axes(latlonGpd_join, width='10%', height='5%',loc='lower right')
    # plt.colorbar(sm, cax=cbar_axis, orientation='horizontal', pad=0.02)
    minx, miny, maxx, maxy = pRegionShapes.total_bounds
    plt.xlim(minx, maxx)
    plt.ylim(miny, maxy)
    fig.tight_layout()
    plt.show()
    fig.savefig("C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results\\Figures\\" + 'WindMap', dpi=300)

    # Solar
    fig, ax = plt.subplots(figsize=(8, 4.5))
    cln = 'region'
    # ax.set_aspect('equal')
    solarinPoly.plot(ax=ax, column='solar_cf', cmap='viridis_r', markersize=15, legend='True', label="Solar capacity factor")
    loadregions.plot(ax=ax, facecolor="none", edgecolors='black', linewidth=0.7)
    loadregions.plot(ax=ax, column='region', facecolor="none", cmap=BluGrn_6.mpl_colormap, linewidth=1.5)
    plt.axis('off')
    f = plt.gcf()
    cax = f.get_axes()[1]
    cax.set_ylabel("Solar Capacity Factor", fontweight='bold')
    for idx, row in loadregions.iterrows():
        fnt = 10
        txt = plt.annotate(text=row[cln], xy=(loadregions.geometry.centroid.x[idx], loadregions.geometry.centroid.y[idx]),
                           horizontalalignment='center', fontsize=fnt, fontweight='bold', wrap=True, color='k')
        txt.set_path_effects([PathEffects.withStroke(linewidth=4, foreground='w')])
    ax.autoscale()
    # sm = plt.cm.ScalarMappable(cmap='rainbow', norm=plt.Normalize(vmin=latlonGpd_join['wind_cf'].min(), vmax=latlonGpd_join['wind_cf'].max()))
    # cbar_axis = inset_axes(latlonGpd_join, width='10%', height='5%',loc='lower right')
    # plt.colorbar(sm, cax=cbar_axis, orientation='horizontal', pad=0.02)
    minx, miny, maxx, maxy = pRegionShapes.total_bounds
    plt.xlim(minx, maxx)
    plt.ylim(miny, maxy)
    fig.tight_layout()
    plt.show()
    fig.savefig("C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results\\Figures\\" + 'SolarMap', dpi=300)


def graphCE(CoalCCS_NE2020_ref_EI, CCCCS_NE2020_ref_EI, CC_NE2020_ref_EI, Nuclear_NE2020_ref_EI, Hydrogen_NE2020_ref_EI,Battery_NE2020_ref_EI,
            DAC_NE2020_ref_EI, Wind_NE2020_ref_EI, Solar_NE2020_ref_EI, CoalCCS_NE2050_ref_EI, CCCCS_NE2050_ref_EI, CC_NE2050_ref_EI, Nuclear_NE2050_ref_EI, Hydrogen_NE2050_ref_EI,Battery_NE2050_ref_EI,
            DAC_NE2050_ref_EI, Wind_NE2050_ref_EI, Solar_NE2050_ref_EI, CoalCCS_NE2020_ref_ERCOT, CCCCS_NE2020_ref_ERCOT, CC_NE2020_ref_ERCOT,
            Nuclear_NE2020_ref_ERCOT, Hydrogen_NE2020_ref_ERCOT,Battery_NE2020_ref_ERCOT, DAC_NE2020_ref_ERCOT, Wind_NE2020_ref_ERCOT,
            Solar_NE2020_ref_ERCOT, CoalCCS_NE2050_ref_ERCOT, CCCCS_NE2050_ref_ERCOT, CC_NE2050_ref_ERCOT, Nuclear_NE2050_ref_ERCOT, Hydrogen_NE2050_ref_ERCOT,
            Battery_NE2050_ref_ERCOT, DAC_NE2050_ref_ERCOT, Wind_NE2050_ref_ERCOT, Solar_NE2050_ref_ERCOT,
            CoalCCS_NE2020_2_ref_EI, CCCCS_NE2020_2_ref_EI, CC_NE2020_2_ref_EI, Nuclear_NE2020_2_ref_EI, Hydrogen_NE2020_2_ref_EI, Battery_NE2020_2_ref_EI,
            DAC_NE2020_2_ref_EI, Wind_NE2020_2_ref_EI, Solar_NE2020_2_ref_EI, CoalCCS_NE2050_2_ref_EI, CCCCS_NE2050_2_ref_EI, CC_NE2050_2_ref_EI, Nuclear_NE2050_2_ref_EI, Hydrogen_NE2050_2_ref_EI, Battery_NE2050_2_ref_EI,
            DAC_NE2050_2_ref_EI, Wind_NE2050_2_ref_EI, Solar_NE2050_2_ref_EI, CoalCCS_NE2020_2_ref_ERCOT, CCCCS_NE2020_2_ref_ERCOT, CC_NE2020_2_ref_ERCOT,
            Nuclear_NE2020_2_ref_ERCOT, Hydrogen_NE2020_2_ref_ERCOT, Battery_NE2020_2_ref_ERCOT, DAC_NE2020_2_ref_ERCOT, Wind_NE2020_2_ref_ERCOT,
            Solar_NE2020_2_ref_ERCOT, CoalCCS_NE2050_2_ref_ERCOT, CCCCS_NE2050_2_ref_ERCOT, CC_NE2050_2_ref_ERCOT, Nuclear_NE2050_2_ref_ERCOT, Hydrogen_NE2050_2_ref_ERCOT,
            Battery_NE2050_2_ref_ERCOT, DAC_NE2050_2_ref_ERCOT, Wind_NE2050_2_ref_ERCOT, Solar_NE2050_2_ref_ERCOT):

  CoalCCS_ref = [CoalCCS_NE2050_ref_EI-CoalCCS_NE2050_2_ref_EI, CoalCCS_NE2050_2_ref_EI, CoalCCS_NE2020_ref_EI, CoalCCS_NE2050_ref_ERCOT-CoalCCS_NE2050_2_ref_ERCOT, CoalCCS_NE2050_2_ref_ERCOT, CoalCCS_NE2020_ref_ERCOT]
  planType_coalCCS = ['Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS']
  region_Col = ['EI', 'EI', 'EI', 'ERCOT', 'ERCOT', 'ERCOT']
  planning_Col = ['NE2050NZS', 'NE2050NES', 'NE2020', 'NE2050NZS', 'NE2050NES', 'NE2020']

  CC_ref = [CC_NE2050_ref_EI-CC_NE2050_2_ref_EI, CC_NE2050_2_ref_EI, CC_NE2020_ref_EI, CC_NE2050_ref_ERCOT-CC_NE2050_2_ref_ERCOT, CC_NE2050_2_ref_ERCOT, CC_NE2020_ref_ERCOT]
  planType_CC = ['NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC']

  CCCCS_ref = [CCCCS_NE2050_ref_EI-CCCCS_NE2050_2_ref_EI, CCCCS_NE2050_2_ref_EI, CCCCS_NE2020_ref_EI, CCCCS_NE2050_ref_ERCOT-CCCCS_NE2050_2_ref_ERCOT, CCCCS_NE2050_2_ref_ERCOT, CCCCS_NE2020_ref_ERCOT]
  planType_CCCCS = ['NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS']

  Nuclear_ref = [Nuclear_NE2050_ref_EI-Nuclear_NE2050_2_ref_EI, Nuclear_NE2050_2_ref_EI, Nuclear_NE2020_ref_EI, Nuclear_NE2050_ref_ERCOT-Nuclear_NE2050_2_ref_ERCOT, Nuclear_NE2050_2_ref_ERCOT, Nuclear_NE2020_ref_ERCOT]
  planType_Nuclear = ['Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear']

  H2_ref = [Hydrogen_NE2050_ref_EI-Hydrogen_NE2050_2_ref_EI, Hydrogen_NE2050_2_ref_EI, Hydrogen_NE2020_ref_EI, Hydrogen_NE2050_ref_ERCOT-Hydrogen_NE2050_2_ref_ERCOT, Hydrogen_NE2050_2_ref_ERCOT, Hydrogen_NE2020_ref_ERCOT]
  planType_H2 = ['Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen']

  Bat_ref = [Battery_NE2050_ref_EI-Battery_NE2050_2_ref_EI, Battery_NE2050_2_ref_EI, Battery_NE2020_ref_EI, Battery_NE2050_ref_ERCOT-Battery_NE2050_2_ref_ERCOT, Battery_NE2050_2_ref_ERCOT, Battery_NE2020_ref_ERCOT]
  planType_Bat = ['Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery']

  DAC_ref = [(DAC_NE2050_ref_EI-DAC_NE2050_2_ref_EI), DAC_NE2050_2_ref_EI, DAC_NE2020_ref_EI, (DAC_NE2050_ref_ERCOT-DAC_NE2050_2_ref_ERCOT), DAC_NE2050_2_ref_ERCOT, DAC_NE2020_ref_ERCOT]
  planType_DAC = ['DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS']

  Wind_ref = [Wind_NE2050_ref_EI-Wind_NE2050_2_ref_EI, Wind_NE2050_2_ref_EI, Wind_NE2020_ref_EI, Wind_NE2050_ref_ERCOT-Wind_NE2050_2_ref_ERCOT, Wind_NE2050_2_ref_ERCOT, Wind_NE2020_ref_ERCOT]
  planType_Wind = ['Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind']

  Solar_ref = [Solar_NE2050_ref_EI-Solar_NE2050_2_ref_EI, Solar_NE2050_2_ref_EI, Solar_NE2020_ref_EI, Solar_NE2050_ref_ERCOT-Solar_NE2050_2_ref_ERCOT, Solar_NE2050_2_ref_ERCOT, Solar_NE2020_ref_ERCOT]
  planType_Solar = ['Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV']

  filler_NE2050_ref_EI = (CoalCCS_NE2050_ref_EI + CC_NE2050_ref_EI + CCCCS_NE2050_ref_EI + Nuclear_NE2050_ref_EI + Hydrogen_NE2050_ref_EI + Battery_NE2050_ref_EI -DAC_NE2050_ref_EI + Wind_NE2050_ref_EI + Solar_NE2050_ref_EI) \
                         - (CoalCCS_NE2050_2_ref_EI + CC_NE2050_2_ref_EI + CCCCS_NE2050_2_ref_EI + Nuclear_NE2050_2_ref_EI + Hydrogen_NE2050_2_ref_EI + Battery_NE2050_2_ref_EI -DAC_NE2050_2_ref_EI + Wind_NE2050_2_ref_EI + Solar_NE2050_2_ref_EI)

  filler_NE2050_ref_ERCOT = (CoalCCS_NE2050_ref_ERCOT + CC_NE2050_ref_ERCOT + CCCCS_NE2050_ref_ERCOT + Nuclear_NE2050_ref_ERCOT + Hydrogen_NE2050_ref_ERCOT + Battery_NE2050_ref_ERCOT - DAC_NE2050_ref_ERCOT + Wind_NE2050_ref_ERCOT + Solar_NE2050_ref_ERCOT) \
                            - (CoalCCS_NE2050_2_ref_ERCOT + CC_NE2050_2_ref_ERCOT + CCCCS_NE2050_2_ref_ERCOT + Nuclear_NE2050_2_ref_ERCOT + Hydrogen_NE2050_2_ref_ERCOT + Battery_NE2050_2_ref_ERCOT - DAC_NE2050_2_ref_ERCOT + Wind_NE2050_2_ref_ERCOT + Solar_NE2050_2_ref_ERCOT)
  filler_ref = [0, filler_NE2050_ref_EI, 0, 0, filler_NE2050_ref_ERCOT, 0]
  planType_filler = ['', '', '', '', '', '']

  capEXP_ref = np.hstack((CC_ref, CCCCS_ref, Nuclear_ref, H2_ref, Bat_ref, DAC_ref, Wind_ref, Solar_ref, filler_ref))
  planType_ref = np.hstack((planType_CC, planType_CCCCS, planType_Nuclear, planType_H2, planType_Bat, planType_DAC, planType_Wind, planType_Solar, planType_filler))
  region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col,  planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col))

  cap_ref = np.vstack((region_ref, planning_ref, planType_ref, capEXP_ref))
  df_capEXP_ref = pd.DataFrame(cap_ref)
  df_capEXP_ref = df_capEXP_ref.transpose()
  df_capEXP_ref.rename({0: 'Region', 1: 'PlanningScr', 2: 'Technology', 3: 'Capacity'},axis=1, inplace=True)
  df_capEXP_ref = df_capEXP_ref.astype({'Capacity': float})

  return df_capEXP_ref

def graphTCE(miso_serc_ref_NE2020_EI, pjm_serc_ref_NE2020_EI, ne_ny_ref_NE2020_EI, pjm_ny_ref_NE2020_EI, pjm_miso_ref_NE2020_EI,
               spp_miso_ref_NE2020_EI, miso_serc_ref_NE2050_EI, pjm_serc_ref_NE2050_EI, ne_ny_ref_NE2050_EI, pjm_ny_ref_NE2050_EI,
               pjm_miso_ref_NE2050_EI, spp_miso_ref_NE2050_EI, miso_serc_ref_NE2020_ERCOT, pjm_serc_ref_NE2020_ERCOT,
               ne_ny_ref_NE2020_ERCOT, pjm_ny_ref_NE2020_ERCOT, pjm_miso_ref_NE2020_ERCOT, spp_miso_ref_NE2020_ERCOT, miso_serc_ref_NE2050_ERCOT,
               pjm_serc_ref_NE2050_ERCOT, ne_ny_ref_NE2050_ERCOT, pjm_ny_ref_NE2050_ERCOT, pjm_miso_ref_NE2050_ERCOT, spp_miso_ref_NE2050_ERCOT,
               ercot_tot_ref_NE2020_EI, ercot_tot_ref_NE2050_EI, ercot_tot_ref_NE2020_ERCOT, ercot_tot_ref_NE2050_ERCOT):

  MISO_SERC_ref = [miso_serc_ref_NE2050_EI, miso_serc_ref_NE2020_EI, miso_serc_ref_NE2050_ERCOT, miso_serc_ref_NE2020_ERCOT]
  planType_MISO_SERC = ['MISO-SERC', 'MISO-SERC', 'MISO-SERC', 'MISO-SERC']
  region_Col = ['EI', 'EI','ERCOT', 'ERCOT']
  planning_Col = ['Plan After Net-Zero',  'Plan Now', 'Plan After Net-Zero', 'Plan Now']

  PJM_SERC_ref = [pjm_serc_ref_NE2050_EI, pjm_serc_ref_NE2020_EI, pjm_serc_ref_NE2050_ERCOT, pjm_serc_ref_NE2020_ERCOT]
  planType_PJM_SERC = ['PJM-SERC', 'PJM-SERC', 'PJM-SERC', 'PJM-SERC']

  NE_NY_ref = [ne_ny_ref_NE2050_EI, ne_ny_ref_NE2020_EI, ne_ny_ref_NE2050_ERCOT, ne_ny_ref_NE2020_ERCOT]
  planType_NE_NY = ['NE-NY', 'NE-NY', 'NE-NY', 'NE-NY']

  PJM_NY_ref = [pjm_ny_ref_NE2050_EI, pjm_ny_ref_NE2020_EI, pjm_ny_ref_NE2050_ERCOT, pjm_ny_ref_NE2020_ERCOT]
  planType_PJM_NY = ['PJM-NY', 'PJM-NY', 'PJM-NY', 'PJM-NY']

  PJM_MISO_ref = [ pjm_miso_ref_NE2050_EI, pjm_miso_ref_NE2020_EI, pjm_miso_ref_NE2050_ERCOT, pjm_miso_ref_NE2020_ERCOT]
  planType_PJM_MISO = ['PJM-MISO', 'PJM-MISO', 'PJM-MISO', 'PJM-MISO']

  SPP_MISO_ref = [spp_miso_ref_NE2050_EI, spp_miso_ref_NE2020_EI, spp_miso_ref_NE2050_ERCOT, spp_miso_ref_NE2020_ERCOT]
  planType_SPP_MISO = ['SPP-MISO', 'SPP-MISO', 'SPP-MISO', 'SPP-MISO']

  ERCOT_ref = [ercot_tot_ref_NE2050_EI, ercot_tot_ref_NE2020_EI, ercot_tot_ref_NE2050_ERCOT, ercot_tot_ref_NE2020_ERCOT]
  planType_ERCOT = ['ERCOT Total', 'ERCOT Total', 'ERCOT Total', 'ERCOT Total']

  transEXP_ref = np.hstack((MISO_SERC_ref, PJM_SERC_ref, NE_NY_ref, PJM_NY_ref, PJM_MISO_ref, SPP_MISO_ref, ERCOT_ref))
  planType_ref = np.hstack((planType_MISO_SERC, planType_PJM_SERC, planType_NE_NY, planType_PJM_NY, planType_PJM_MISO, planType_SPP_MISO, planType_ERCOT))
  region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col,  planning_Col, planning_Col, planning_Col, planning_Col, planning_Col))

  trans_ref = np.vstack((region_ref, planning_ref, planType_ref, transEXP_ref))
  df_transEXP_ref = pd.DataFrame(trans_ref)
  df_transEXP_ref = df_transEXP_ref.transpose()
  df_transEXP_ref.rename({0: 'Region', 1: 'PlanningScr', 2: 'Transmission Lines', 3: 'Capacity'},axis=1, inplace=True)
  df_transEXP_ref = df_transEXP_ref.astype({'Capacity': float})

  return df_transEXP_ref

def graphFlows(netFlow_EI_serc_NE2020_EI, netFlow_EI_ny_NE2020_EI, netFlow_EI_miso_NE2020_EI,
               netFlow_EI_pjm_NE2020_EI, netFlow_EI_ne_NE2020_EI, netFlow_EI_spp_NE2020_EI, netFlow_ERCOT_NW_NE2020_EI,
               netFlow_ERCOT_SW_NE2020_EI, netFlow_ERCOT_NE_NE2020_EI, netFlow_ERCOT_SE_NE2020_EI, netFlow_EI_serc_NE2050_EI,
               netFlow_EI_ny_NE2050_EI, netFlow_EI_miso_NE2050_EI, netFlow_EI_pjm_NE2050_EI,
               netFlow_EI_ne_NE2050_EI, netFlow_EI_spp_NE2050_EI, netFlow_ERCOT_NW_NE2050_EI, netFlow_ERCOT_SW_NE2050_EI,
               netFlow_ERCOT_NE_NE2050_EI, netFlow_ERCOT_SE_NE2050_EI, netFlow_EI_serc_NE2020_ERCOT, netFlow_EI_ny_NE2020_ERCOT,
               netFlow_EI_miso_NE2020_ERCOT, netFlow_EI_pjm_NE2020_ERCOT, netFlow_EI_ne_NE2020_ERCOT, netFlow_EI_spp_NE2020_ERCOT,
               netFlow_ERCOT_NW_NE2020_ERCOT, netFlow_ERCOT_SW_NE2020_ERCOT, netFlow_ERCOT_NE_NE2020_ERCOT,
               netFlow_ERCOT_SE_NE2020_ERCOT, netFlow_EI_serc_NE2050_ERCOT,
               netFlow_EI_ny_NE2050_ERCOT, netFlow_EI_miso_NE2050_ERCOT, netFlow_EI_pjm_NE2050_ERCOT, netFlow_EI_ne_NE2050_ERCOT,
               netFlow_EI_spp_NE2050_ERCOT, netFlow_ERCOT_NW_NE2050_ERCOT, netFlow_ERCOT_SW_NE2050_ERCOT,
               netFlow_ERCOT_NE_NE2050_ERCOT, netFlow_ERCOT_SE_NE2050_ERCOT):

  SERC_ref = [netFlow_EI_serc_NE2050_EI, netFlow_EI_serc_NE2020_EI,
              netFlow_EI_serc_NE2050_ERCOT, netFlow_EI_serc_NE2020_ERCOT]
  planType_SERC = ['SERC', 'SERC', 'SERC', 'SERC']
  region_Col = ['EI', 'EI', 'ERCOT', 'ERCOT']
  planning_Col = ['Plan After Net-Zero', 'Plan Now', 'Plan After Net-Zero', 'Plan Now']

  NY_ref = [netFlow_EI_ny_NE2050_EI, netFlow_EI_ny_NE2020_EI,
            netFlow_EI_ny_NE2050_ERCOT, netFlow_EI_ny_NE2020_ERCOT]
  planType_NY = ['NY', 'NY', 'NY', 'NY']

  NE_ref = [netFlow_EI_ne_NE2050_EI, netFlow_EI_ne_NE2020_EI,
            netFlow_EI_ne_NE2050_ERCOT, netFlow_EI_ne_NE2020_ERCOT]
  planType_NE = ['NE', 'NE', 'NE', 'NE']

  PJM_ref = [netFlow_EI_pjm_NE2050_EI, netFlow_EI_pjm_NE2020_EI,
             netFlow_EI_pjm_NE2050_ERCOT, netFlow_EI_pjm_NE2020_ERCOT]
  planType_PJM = ['PJM', 'PJM', 'PJM', 'PJM']

  MISO_ref = [netFlow_EI_miso_NE2050_EI, netFlow_EI_miso_NE2020_EI,
              netFlow_EI_miso_NE2050_ERCOT, netFlow_EI_miso_NE2020_ERCOT]
  planType_MISO = ['MISO', 'MISO', 'MISO', 'MISO']

  SPP_ref = [netFlow_EI_spp_NE2050_EI, netFlow_EI_spp_NE2020_EI,
             netFlow_EI_spp_NE2050_ERCOT, netFlow_EI_spp_NE2020_ERCOT]
  planType_SPP = ['SPP', 'SPP', 'SPP', 'SPP']

  ERCOT_NW = [netFlow_ERCOT_NW_NE2050_EI, netFlow_ERCOT_NW_NE2020_EI,
              netFlow_ERCOT_NW_NE2050_ERCOT, netFlow_ERCOT_NW_NE2020_ERCOT]
  planType_ERCOT_NW = ['ERCOT NW', 'ERCOT NW', 'ERCOT NW', 'ERCOT NW']

  ERCOT_SW = [netFlow_ERCOT_SW_NE2050_EI, netFlow_ERCOT_SW_NE2020_EI,
              netFlow_ERCOT_SW_NE2050_ERCOT, netFlow_ERCOT_SW_NE2020_ERCOT]
  planType_ERCOT_SW = ['ERCOT SW', 'ERCOT SW', 'ERCOT SW', 'ERCOT SW']

  ERCOT_NE = [netFlow_ERCOT_NE_NE2050_EI, netFlow_ERCOT_NE_NE2020_EI,
              netFlow_ERCOT_NE_NE2050_ERCOT, netFlow_ERCOT_NE_NE2020_ERCOT]
  planType_ERCOT_NE = ['ERCOT NE', 'ERCOT NE', 'ERCOT NE', 'ERCOT NE']

  ERCOT_SE = [netFlow_ERCOT_SE_NE2050_EI, netFlow_ERCOT_SE_NE2020_EI,
              netFlow_ERCOT_SE_NE2050_ERCOT, netFlow_ERCOT_SE_NE2020_ERCOT]
  planType_ERCOT_SE = ['ERCOT SE', 'ERCOT SE', 'ERCOT SE', 'ERCOT SE']

  flowsEXP_ref = np.hstack((SERC_ref, NY_ref, NE_ref, PJM_ref, MISO_ref, SPP_ref, ERCOT_NW, ERCOT_SW, ERCOT_NE, ERCOT_SE))
  planType_ref = np.hstack((planType_SERC, planType_NY, planType_NE, planType_PJM, planType_MISO, planType_SPP,
                            planType_ERCOT_NW, planType_ERCOT_SW, planType_ERCOT_NE, planType_ERCOT_SE))
  region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col,  planning_Col, planning_Col, planning_Col, planning_Col,
                            planning_Col, planning_Col, planning_Col, planning_Col))

  flows_ref = np.vstack((region_ref, planning_ref, planType_ref, flowsEXP_ref))
  df_flows_ref = pd.DataFrame(flows_ref)
  df_flows_ref = df_flows_ref.transpose()
  df_flows_ref.rename({0: 'Region', 1: 'PlanningScr', 2: 'Load Region', 3: 'Flows'},axis=1, inplace=True)
  df_flows_ref = df_flows_ref.astype({'Flows': float})

  return df_flows_ref

def graphCosts(totCost_NE2020_ref_EI, opCost_data_NE2020_ref_EI, fixedCost_data_NE2020_ref_EI,
              totCost_NE2050_ref_EI, opCost_data_NE2050_ref_EI, fixedCost_data_NE2050_ref_EI,
              totCost_NE2020_ref_ERCOT, opCost_data_NE2020_ref_ERCOT, fixedCost_data_NE2020_ref_ERCOT,
              totCost_NE2050_ref_ERCOT, opCost_data_NE2050_ref_ERCOT, fixedCost_data_NE2050_ref_ERCOT,
              totCost_NE2020_ref_EI_2, opCost_data_NE2020_ref_EI_2, fixedCost_data_NE2020_ref_EI_2,
              totCost_NE2050_ref_EI_2, opCost_data_NE2050_ref_EI_2, fixedCost_data_NE2050_ref_EI_2,
              totCost_NE2020_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT_2,
              totCost_NE2050_ref_ERCOT_2, opCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2050_ref_ERCOT_2):

  fixedCost_ref = [fixedCost_data_NE2050_ref_EI-fixedCost_data_NE2050_ref_EI_2, fixedCost_data_NE2050_ref_EI_2,
                   fixedCost_data_NE2020_ref_EI, fixedCost_data_NE2050_ref_ERCOT-fixedCost_data_NE2050_ref_ERCOT_2,
                   fixedCost_data_NE2050_ref_ERCOT_2, fixedCost_data_NE2020_ref_ERCOT]
  fixedcostType_Col = ['Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost', 'Capital Cost']
  region_Col = ['EI', 'EI', 'EI', 'ERCOT', 'ERCOT', 'ERCOT']
  planning_Col = ['NE2050NZS', 'NE2050NES', 'NE2020', 'NE2050NZS', 'NE2050NES', 'NE2020']

  opCost_ref = [opCost_data_NE2050_ref_EI-opCost_data_NE2050_ref_EI_2, opCost_data_NE2050_ref_EI_2,
                opCost_data_NE2020_ref_EI, opCost_data_NE2050_ref_ERCOT-opCost_data_NE2050_ref_ERCOT_2,
                opCost_data_NE2050_ref_ERCOT_2, opCost_data_NE2020_ref_ERCOT]
  opcostType_Col = ['Operating Cost', 'Operating Cost', 'Operating Cost', 'Operating Cost','Operating Cost', 'Operating Cost']
  filler_ref = [0, totCost_NE2050_ref_EI-totCost_NE2050_ref_EI_2, 0, 0, totCost_NE2050_ref_ERCOT-totCost_NE2050_ref_ERCOT_2,0]
  filler_Col = ['', '', '', '', '', '']

  costsData_ref = np.hstack((fixedCost_ref, opCost_ref, filler_ref))
  costType_ref = np.hstack((fixedcostType_Col, opcostType_Col, filler_Col))
  region_ref = np.hstack((region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col, planning_Col))

  cost_ref = np.vstack((region_ref, planning_ref, costType_ref, costsData_ref))
  df_costs_ref = pd.DataFrame(cost_ref)
  df_costs_ref = df_costs_ref.transpose()
  df_costs_ref.rename({0: 'Region', 1: 'PlanningScr', 2: 'Cost Types', 3: 'Amount'},axis=1, inplace=True)
  df_costs_ref = df_costs_ref.astype({'Amount': float})

  return df_costs_ref

def graphGen(Coal_Gen_NE2020_EI, CCCCS_Gen_NE2020_EI, CC_Gen_NE2020_EI, battery_Gen_NE2020_EI, hydrogen_Gen_NE2020_EI,
              nuclear_Gen_NE2020_EI, dac_Gen_NE2020_EI, solar_Gen_NE2020_EI, wind_Gen_NE2020_EI, CT_Gen_NE2020_EI,
              OG_Gen_NE2020_EI, bio_Gen_NE2020_EI, pump_Gen_NE2020_EI, Others_Gen_NE2020_EI, Coal_Gen_NE2050_EI, CCCCS_Gen_NE2050_EI,
              CC_Gen_NE2050_EI, battery_Gen_NE2050_EI, hydrogen_Gen_NE2050_EI, nuclear_Gen_NE2050_EI, dac_Gen_NE2050_EI,
              solar_Gen_NE2050_EI, wind_Gen_NE2050_EI, CT_Gen_NE2050_EI, OG_Gen_NE2050_EI, bio_Gen_NE2050_EI,
              pump_Gen_NE2050_EI, Others_Gen_NE2050_EI, Coal_Gen_NE2020_ERCOT, CCCCS_Gen_NE2020_ERCOT, CC_Gen_NE2020_ERCOT,
              battery_Gen_NE2020_ERCOT, hydrogen_Gen_NE2020_ERCOT, nuclear_Gen_NE2020_ERCOT, dac_Gen_NE2020_ERCOT,
              solar_Gen_NE2020_ERCOT, wind_Gen_NE2020_ERCOT, CT_Gen_NE2020_ERCOT, OG_Gen_NE2020_ERCOT, bio_Gen_NE2020_ERCOT,
              pump_Gen_NE2020_ERCOT, Others_Gen_NE2020_ERCOT, Coal_Gen_NE2050_ERCOT,
              CCCCS_Gen_NE2050_ERCOT, CC_Gen_NE2050_ERCOT, battery_Gen_NE2050_ERCOT, hydrogen_Gen_NE2050_ERCOT,
              nuclear_Gen_NE2050_ERCOT, dac_Gen_NE2050_ERCOT, solar_Gen_NE2050_ERCOT, wind_Gen_NE2050_ERCOT,
              CT_Gen_NE2050_ERCOT, OG_Gen_NE2050_ERCOT, bio_Gen_NE2050_ERCOT, pump_Gen_NE2050_ERCOT, Others_Gen_NE2050_ERCOT):

  CoalCCS_ref = [Coal_Gen_NE2050_EI, Coal_Gen_NE2020_EI, Coal_Gen_NE2050_ERCOT, Coal_Gen_NE2020_ERCOT]
  planType_coal = ['Coal', 'Coal', 'Coal', 'Coal']
  region_Col = ['EI', 'EI', 'ERCOT', 'ERCOT']
  planning_Col = ['NE2050', 'NE2020', 'NE2050', 'NE2020']

  CC_ref = [CC_Gen_NE2050_EI, CC_Gen_NE2020_EI, CC_Gen_NE2050_ERCOT, CC_Gen_NE2020_ERCOT]
  planType_CC = ['NGCC', 'NGCC', 'NGCC', 'NGCC']

  CCCCS_ref = [CCCCS_Gen_NE2050_EI, CCCCS_Gen_NE2020_EI, CCCCS_Gen_NE2050_ERCOT, CCCCS_Gen_NE2020_ERCOT]
  planType_CCCCS = ['NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS']

  Nuclear_ref = [nuclear_Gen_NE2050_EI, nuclear_Gen_NE2020_EI, nuclear_Gen_NE2050_ERCOT, nuclear_Gen_NE2020_ERCOT]
  planType_Nuclear = ['Nuclear', 'Nuclear', 'Nuclear', 'Nuclear']

  H2_ref = [hydrogen_Gen_NE2050_EI, hydrogen_Gen_NE2020_EI, hydrogen_Gen_NE2050_ERCOT, hydrogen_Gen_NE2020_ERCOT]
  planType_H2 = ['Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen']

  Bat_ref = [battery_Gen_NE2050_EI, battery_Gen_NE2020_EI, battery_Gen_NE2050_ERCOT, battery_Gen_NE2020_ERCOT]
  planType_Bat = ['Battery', 'Battery', 'Battery', 'Battery']

  DAC_ref = [dac_Gen_NE2050_EI, dac_Gen_NE2020_EI, dac_Gen_NE2050_ERCOT, dac_Gen_NE2020_ERCOT]
  planType_DAC = ['DACS', 'DACS', 'DACS', 'DACS']

  Wind_ref = [wind_Gen_NE2050_EI, wind_Gen_NE2020_EI, wind_Gen_NE2050_ERCOT, wind_Gen_NE2020_ERCOT]
  planType_Wind = ['Wind', 'Wind', 'Wind', 'Wind']

  Solar_ref = [solar_Gen_NE2050_EI, solar_Gen_NE2020_EI, solar_Gen_NE2050_ERCOT, solar_Gen_NE2020_ERCOT]
  planType_Solar = ['Solar PV', 'Solar PV', 'Solar PV', 'Solar PV']

  gen_ref = np.hstack((CC_ref, CCCCS_ref, Nuclear_ref, H2_ref, Bat_ref, DAC_ref, Wind_ref, Solar_ref))
  planType_ref = np.hstack((planType_CC, planType_CCCCS, planType_Nuclear, planType_H2, planType_Bat, planType_DAC, planType_Wind, planType_Solar))
  region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col))

  genCE_ref = np.vstack((region_ref, planning_ref, planType_ref, gen_ref))
  df_genCE_ref = pd.DataFrame(genCE_ref)
  df_genCE_ref = df_genCE_ref.transpose()
  df_genCE_ref.rename({0: 'Region', 1: 'PlanningScr', 2: 'Technology', 3: 'Gen'},axis=1, inplace=True)
  df_genCE_ref = df_genCE_ref.astype({'Gen': float})

  return df_genCE_ref

def graphGenRegions(CCCCS_Gen_SERC_NE2020_EI,CC_Gen_SERC_NE2020_EI,battery_Gen_SERC_NE2020_EI,hydrogen_Gen_SERC_NE2020_EI,
                     nuclear_Gen_SERC_NE2020_EI,dac_Gen_SERC_NE2020_EI,solar_Gen_SERC_NE2020_EI,wind_Gen_SERC_NE2020_EI,
                     CCCCS_Gen_NY_NE2020_EI,CC_Gen_NY_NE2020_EI,battery_Gen_NY_NE2020_EI,hydrogen_Gen_NY_NE2020_EI,
                     nuclear_Gen_NY_NE2020_EI,dac_Gen_NY_NE2020_EI,solar_Gen_NY_NE2020_EI, wind_Gen_NY_NE2020_EI,CCCCS_Gen_NE_NE2020_EI,
                     CC_Gen_NE_NE2020_EI,battery_Gen_NE_NE2020_EI,hydrogen_Gen_NE_NE2020_EI,nuclear_Gen_NE_NE2020_EI,
                     dac_Gen_NE_NE2020_EI,solar_Gen_NE_NE2020_EI,wind_Gen_NE_NE2020_EI,CCCCS_Gen_MISO_NE2020_EI,CC_Gen_MISO_NE2020_EI,
                     battery_Gen_MISO_NE2020_EI,hydrogen_Gen_MISO_NE2020_EI,nuclear_Gen_MISO_NE2020_EI,dac_Gen_MISO_NE2020_EI,
                     solar_Gen_MISO_NE2020_EI,wind_Gen_MISO_NE2020_EI,CCCCS_Gen_PJM_NE2020_EI,CC_Gen_PJM_NE2020_EI,battery_Gen_PJM_NE2020_EI,
                     hydrogen_Gen_PJM_NE2020_EI,nuclear_Gen_PJM_NE2020_EI,dac_Gen_PJM_NE2020_EI,solar_Gen_PJM_NE2020_EI,
                     wind_Gen_PJM_NE2020_EI,CCCCS_Gen_SPP_NE2020_EI,CC_Gen_SPP_NE2020_EI,battery_Gen_SPP_NE2020_EI,hydrogen_Gen_SPP_NE2020_EI,
                     nuclear_Gen_SPP_NE2020_EI,dac_Gen_SPP_NE2020_EI,solar_Gen_SPP_NE2020_EI,wind_Gen_SPP_NE2020_EI,CCCCS_Gen_NW_NE2020_EI,
                     CC_Gen_NW_NE2020_EI,battery_Gen_NW_NE2020_EI,hydrogen_Gen_NW_NE2020_EI,nuclear_Gen_NW_NE2020_EI,dac_Gen_NW_NE2020_EI,
                     solar_Gen_NW_NE2020_EI,wind_Gen_NW_NE2020_EI,CCCCS_Gen_SW_NE2020_EI,CC_Gen_SW_NE2020_EI,battery_Gen_SW_NE2020_EI,
                     hydrogen_Gen_SW_NE2020_EI,nuclear_Gen_SW_NE2020_EI,dac_Gen_SW_NE2020_EI,solar_Gen_SW_NE2020_EI,wind_Gen_SW_NE2020_EI,
                     CCCCS_Gen_NOE_NE2020_EI,CC_Gen_NOE_NE2020_EI,battery_Gen_NOE_NE2020_EI,hydrogen_Gen_NOE_NE2020_EI,nuclear_Gen_NOE_NE2020_EI,
                     dac_Gen_NOE_NE2020_EI,solar_Gen_NOE_NE2020_EI,wind_Gen_NOE_NE2020_EI,CCCCS_Gen_SE_NE2020_EI,CC_Gen_SE_NE2020_EI,
                     battery_Gen_SE_NE2020_EI,hydrogen_Gen_SE_NE2020_EI,nuclear_Gen_SE_NE2020_EI,dac_Gen_SE_NE2020_EI,solar_Gen_SE_NE2020_EI,
                     wind_Gen_SE_NE2020_EI,
                     CCCCS_Gen_SERC_NE2050_EI, CC_Gen_SERC_NE2050_EI, battery_Gen_SERC_NE2050_EI, hydrogen_Gen_SERC_NE2050_EI,
                     nuclear_Gen_SERC_NE2050_EI, dac_Gen_SERC_NE2050_EI, solar_Gen_SERC_NE2050_EI, wind_Gen_SERC_NE2050_EI,
                     CCCCS_Gen_NY_NE2050_EI, CC_Gen_NY_NE2050_EI, battery_Gen_NY_NE2050_EI, hydrogen_Gen_NY_NE2050_EI,
                     nuclear_Gen_NY_NE2050_EI, dac_Gen_NY_NE2050_EI, solar_Gen_NY_NE2050_EI, wind_Gen_NY_NE2050_EI, CCCCS_Gen_NE_NE2050_EI,
                     CC_Gen_NE_NE2050_EI, battery_Gen_NE_NE2050_EI, hydrogen_Gen_NE_NE2050_EI, nuclear_Gen_NE_NE2050_EI,
                     dac_Gen_NE_NE2050_EI, solar_Gen_NE_NE2050_EI, wind_Gen_NE_NE2050_EI, CCCCS_Gen_MISO_NE2050_EI, CC_Gen_MISO_NE2050_EI,
                     battery_Gen_MISO_NE2050_EI, hydrogen_Gen_MISO_NE2050_EI, nuclear_Gen_MISO_NE2050_EI, dac_Gen_MISO_NE2050_EI,
                     solar_Gen_MISO_NE2050_EI, wind_Gen_MISO_NE2050_EI, CCCCS_Gen_PJM_NE2050_EI, CC_Gen_PJM_NE2050_EI, battery_Gen_PJM_NE2050_EI,
                     hydrogen_Gen_PJM_NE2050_EI, nuclear_Gen_PJM_NE2050_EI, dac_Gen_PJM_NE2050_EI, solar_Gen_PJM_NE2050_EI,
                     wind_Gen_PJM_NE2050_EI, CCCCS_Gen_SPP_NE2050_EI, CC_Gen_SPP_NE2050_EI, battery_Gen_SPP_NE2050_EI, hydrogen_Gen_SPP_NE2050_EI,
                     nuclear_Gen_SPP_NE2050_EI, dac_Gen_SPP_NE2050_EI, solar_Gen_SPP_NE2050_EI, wind_Gen_SPP_NE2050_EI, CCCCS_Gen_NW_NE2050_EI,
                     CC_Gen_NW_NE2050_EI, battery_Gen_NW_NE2050_EI, hydrogen_Gen_NW_NE2050_EI, nuclear_Gen_NW_NE2050_EI, dac_Gen_NW_NE2050_EI,
                     solar_Gen_NW_NE2050_EI, wind_Gen_NW_NE2050_EI, CCCCS_Gen_SW_NE2050_EI, CC_Gen_SW_NE2050_EI, battery_Gen_SW_NE2050_EI,
                     hydrogen_Gen_SW_NE2050_EI, nuclear_Gen_SW_NE2050_EI, dac_Gen_SW_NE2050_EI, solar_Gen_SW_NE2050_EI, wind_Gen_SW_NE2050_EI,
                     CCCCS_Gen_NOE_NE2050_EI, CC_Gen_NOE_NE2050_EI, battery_Gen_NOE_NE2050_EI, hydrogen_Gen_NOE_NE2050_EI, nuclear_Gen_NOE_NE2050_EI,
                     dac_Gen_NOE_NE2050_EI, solar_Gen_NOE_NE2050_EI, wind_Gen_NOE_NE2050_EI, CCCCS_Gen_SE_NE2050_EI, CC_Gen_SE_NE2050_EI,
                     battery_Gen_SE_NE2050_EI, hydrogen_Gen_SE_NE2050_EI, nuclear_Gen_SE_NE2050_EI, dac_Gen_SE_NE2050_EI, solar_Gen_SE_NE2050_EI,
                     wind_Gen_SE_NE2050_EI,
                     CCCCS_Gen_SERC_NE2020_ERCOT, CC_Gen_SERC_NE2020_ERCOT, battery_Gen_SERC_NE2020_ERCOT, hydrogen_Gen_SERC_NE2020_ERCOT,
                     nuclear_Gen_SERC_NE2020_ERCOT, dac_Gen_SERC_NE2020_ERCOT, solar_Gen_SERC_NE2020_ERCOT, wind_Gen_SERC_NE2020_ERCOT,
                     CCCCS_Gen_NY_NE2020_ERCOT, CC_Gen_NY_NE2020_ERCOT, battery_Gen_NY_NE2020_ERCOT, hydrogen_Gen_NY_NE2020_ERCOT,
                     nuclear_Gen_NY_NE2020_ERCOT, dac_Gen_NY_NE2020_ERCOT, solar_Gen_NY_NE2020_ERCOT, wind_Gen_NY_NE2020_ERCOT, CCCCS_Gen_NE_NE2020_ERCOT,
                     CC_Gen_NE_NE2020_ERCOT, battery_Gen_NE_NE2020_ERCOT, hydrogen_Gen_NE_NE2020_ERCOT, nuclear_Gen_NE_NE2020_ERCOT,
                     dac_Gen_NE_NE2020_ERCOT, solar_Gen_NE_NE2020_ERCOT, wind_Gen_NE_NE2020_ERCOT, CCCCS_Gen_MISO_NE2020_ERCOT, CC_Gen_MISO_NE2020_ERCOT,
                     battery_Gen_MISO_NE2020_ERCOT, hydrogen_Gen_MISO_NE2020_ERCOT, nuclear_Gen_MISO_NE2020_ERCOT, dac_Gen_MISO_NE2020_ERCOT,
                     solar_Gen_MISO_NE2020_ERCOT, wind_Gen_MISO_NE2020_ERCOT, CCCCS_Gen_PJM_NE2020_ERCOT, CC_Gen_PJM_NE2020_ERCOT, battery_Gen_PJM_NE2020_ERCOT,
                     hydrogen_Gen_PJM_NE2020_ERCOT, nuclear_Gen_PJM_NE2020_ERCOT, dac_Gen_PJM_NE2020_ERCOT, solar_Gen_PJM_NE2020_ERCOT,
                     wind_Gen_PJM_NE2020_ERCOT, CCCCS_Gen_SPP_NE2020_ERCOT, CC_Gen_SPP_NE2020_ERCOT, battery_Gen_SPP_NE2020_ERCOT, hydrogen_Gen_SPP_NE2020_ERCOT,
                     nuclear_Gen_SPP_NE2020_ERCOT, dac_Gen_SPP_NE2020_ERCOT, solar_Gen_SPP_NE2020_ERCOT, wind_Gen_SPP_NE2020_ERCOT, CCCCS_Gen_NW_NE2020_ERCOT,
                     CC_Gen_NW_NE2020_ERCOT, battery_Gen_NW_NE2020_ERCOT, hydrogen_Gen_NW_NE2020_ERCOT, nuclear_Gen_NW_NE2020_ERCOT, dac_Gen_NW_NE2020_ERCOT,
                     solar_Gen_NW_NE2020_ERCOT, wind_Gen_NW_NE2020_ERCOT, CCCCS_Gen_SW_NE2020_ERCOT, CC_Gen_SW_NE2020_ERCOT, battery_Gen_SW_NE2020_ERCOT,
                     hydrogen_Gen_SW_NE2020_ERCOT, nuclear_Gen_SW_NE2020_ERCOT, dac_Gen_SW_NE2020_ERCOT, solar_Gen_SW_NE2020_ERCOT, wind_Gen_SW_NE2020_ERCOT,
                     CCCCS_Gen_NOE_NE2020_ERCOT, CC_Gen_NOE_NE2020_ERCOT, battery_Gen_NOE_NE2020_ERCOT, hydrogen_Gen_NOE_NE2020_ERCOT, nuclear_Gen_NOE_NE2020_ERCOT,
                     dac_Gen_NOE_NE2020_ERCOT, solar_Gen_NOE_NE2020_ERCOT, wind_Gen_NOE_NE2020_ERCOT, CCCCS_Gen_SE_NE2020_ERCOT, CC_Gen_SE_NE2020_ERCOT,
                     battery_Gen_SE_NE2020_ERCOT, hydrogen_Gen_SE_NE2020_ERCOT, nuclear_Gen_SE_NE2020_ERCOT, dac_Gen_SE_NE2020_ERCOT, solar_Gen_SE_NE2020_ERCOT,
                     wind_Gen_SE_NE2020_ERCOT,
                     CCCCS_Gen_SERC_NE2050_ERCOT, CC_Gen_SERC_NE2050_ERCOT, battery_Gen_SERC_NE2050_ERCOT, hydrogen_Gen_SERC_NE2050_ERCOT,
                     nuclear_Gen_SERC_NE2050_ERCOT, dac_Gen_SERC_NE2050_ERCOT, solar_Gen_SERC_NE2050_ERCOT, wind_Gen_SERC_NE2050_ERCOT,
                     CCCCS_Gen_NY_NE2050_ERCOT, CC_Gen_NY_NE2050_ERCOT, battery_Gen_NY_NE2050_ERCOT, hydrogen_Gen_NY_NE2050_ERCOT,
                     nuclear_Gen_NY_NE2050_ERCOT, dac_Gen_NY_NE2050_ERCOT, solar_Gen_NY_NE2050_ERCOT, wind_Gen_NY_NE2050_ERCOT, CCCCS_Gen_NE_NE2050_ERCOT,
                     CC_Gen_NE_NE2050_ERCOT, battery_Gen_NE_NE2050_ERCOT, hydrogen_Gen_NE_NE2050_ERCOT, nuclear_Gen_NE_NE2050_ERCOT,
                     dac_Gen_NE_NE2050_ERCOT, solar_Gen_NE_NE2050_ERCOT, wind_Gen_NE_NE2050_ERCOT, CCCCS_Gen_MISO_NE2050_ERCOT, CC_Gen_MISO_NE2050_ERCOT,
                     battery_Gen_MISO_NE2050_ERCOT, hydrogen_Gen_MISO_NE2050_ERCOT, nuclear_Gen_MISO_NE2050_ERCOT, dac_Gen_MISO_NE2050_ERCOT,
                     solar_Gen_MISO_NE2050_ERCOT, wind_Gen_MISO_NE2050_ERCOT, CCCCS_Gen_PJM_NE2050_ERCOT, CC_Gen_PJM_NE2050_ERCOT, battery_Gen_PJM_NE2050_ERCOT,
                     hydrogen_Gen_PJM_NE2050_ERCOT, nuclear_Gen_PJM_NE2050_ERCOT, dac_Gen_PJM_NE2050_ERCOT, solar_Gen_PJM_NE2050_ERCOT,
                     wind_Gen_PJM_NE2050_ERCOT, CCCCS_Gen_SPP_NE2050_ERCOT, CC_Gen_SPP_NE2050_ERCOT, battery_Gen_SPP_NE2050_ERCOT, hydrogen_Gen_SPP_NE2050_ERCOT,
                     nuclear_Gen_SPP_NE2050_ERCOT, dac_Gen_SPP_NE2050_ERCOT, solar_Gen_SPP_NE2050_ERCOT, wind_Gen_SPP_NE2050_ERCOT, CCCCS_Gen_NW_NE2050_ERCOT,
                     CC_Gen_NW_NE2050_ERCOT, battery_Gen_NW_NE2050_ERCOT, hydrogen_Gen_NW_NE2050_ERCOT, nuclear_Gen_NW_NE2050_ERCOT, dac_Gen_NW_NE2050_ERCOT,
                     solar_Gen_NW_NE2050_ERCOT, wind_Gen_NW_NE2050_ERCOT, CCCCS_Gen_SW_NE2050_ERCOT, CC_Gen_SW_NE2050_ERCOT, battery_Gen_SW_NE2050_ERCOT,
                     hydrogen_Gen_SW_NE2050_ERCOT, nuclear_Gen_SW_NE2050_ERCOT, dac_Gen_SW_NE2050_ERCOT, solar_Gen_SW_NE2050_ERCOT, wind_Gen_SW_NE2050_ERCOT,
                     CCCCS_Gen_NOE_NE2050_ERCOT, CC_Gen_NOE_NE2050_ERCOT, battery_Gen_NOE_NE2050_ERCOT, hydrogen_Gen_NOE_NE2050_ERCOT, nuclear_Gen_NOE_NE2050_ERCOT,
                     dac_Gen_NOE_NE2050_ERCOT, solar_Gen_NOE_NE2050_ERCOT, wind_Gen_NOE_NE2050_ERCOT, CCCCS_Gen_SE_NE2050_ERCOT, CC_Gen_SE_NE2050_ERCOT,
                     battery_Gen_SE_NE2050_ERCOT, hydrogen_Gen_SE_NE2050_ERCOT, nuclear_Gen_SE_NE2050_ERCOT, dac_Gen_SE_NE2050_ERCOT, solar_Gen_SE_NE2050_ERCOT,
                     wind_Gen_SE_NE2050_ERCOT):

  CC_ref = [CC_Gen_SERC_NE2050_EI, CC_Gen_SERC_NE2020_EI, CC_Gen_NY_NE2050_EI, CC_Gen_NY_NE2020_EI,
            CC_Gen_NE_NE2050_EI, CC_Gen_NE_NE2020_EI, CC_Gen_MISO_NE2050_EI, CC_Gen_MISO_NE2020_EI,
            CC_Gen_PJM_NE2050_EI, CC_Gen_PJM_NE2020_EI, CC_Gen_SPP_NE2050_EI, CC_Gen_SPP_NE2020_EI,
            CC_Gen_SW_NE2050_ERCOT,CC_Gen_SW_NE2020_ERCOT,CC_Gen_NW_NE2050_ERCOT,CC_Gen_NW_NE2020_ERCOT,
            CC_Gen_NOE_NE2050_ERCOT,CC_Gen_NOE_NE2020_ERCOT,CC_Gen_SE_NE2050_ERCOT,CC_Gen_SE_NE2020_ERCOT]

  planning_Col = ['NE2050', 'NE2020', 'NE2050', 'NE2020', 'NE2050', 'NE2020', 'NE2050', 'NE2020',
                  'NE2050', 'NE2020', 'NE2050', 'NE2020', 'NE2050', 'NE2020', 'NE2050', 'NE2020',
                  'NE2050', 'NE2020', 'NE2050', 'NE2020']

  planType_CC = ['NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC','NGCC','NGCC',
                 'NGCC','NGCC','NGCC', 'NGCC','NGCC','NGCC', 'NGCC', 'NGCC','NGCC','NGCC','NGCC']
  region_Col = ['SERC', 'SERC', 'NY', 'NY', 'NE', 'NE', 'MISO', 'MISO', 'PJM', 'PJM', 'SPP', 'SPP',
                 'ERCOT-SW', 'ERCOT-SW', 'ERCOT-NW', 'ERCOT-NW', 'ERCOT-NE', 'ERCOT-NE', 'ERCOT-SE', 'ERCOT-SE']

  CCCCS_ref = [CCCCS_Gen_SERC_NE2050_EI, CCCCS_Gen_SERC_NE2020_EI, CCCCS_Gen_NY_NE2050_EI, CCCCS_Gen_NY_NE2020_EI,
               CCCCS_Gen_NE_NE2050_EI, CCCCS_Gen_NE_NE2020_EI, CCCCS_Gen_MISO_NE2050_EI, CCCCS_Gen_MISO_NE2020_EI,
               CCCCS_Gen_PJM_NE2050_EI, CCCCS_Gen_PJM_NE2020_EI, CCCCS_Gen_SPP_NE2050_EI, CCCCS_Gen_SPP_NE2020_EI,
               CCCCS_Gen_SW_NE2050_ERCOT, CCCCS_Gen_SW_NE2020_ERCOT, CCCCS_Gen_NW_NE2050_ERCOT, CCCCS_Gen_NW_NE2020_ERCOT,
               CCCCS_Gen_NOE_NE2050_ERCOT, CCCCS_Gen_NOE_NE2020_ERCOT, CCCCS_Gen_SE_NE2050_ERCOT, CCCCS_Gen_SE_NE2020_ERCOT]
  planType_CCCCS = ['NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS',
                    'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS']

  Nuclear_ref = [nuclear_Gen_SERC_NE2050_EI, nuclear_Gen_SERC_NE2020_EI, nuclear_Gen_NY_NE2050_EI, nuclear_Gen_NY_NE2020_EI,
                 nuclear_Gen_NE_NE2050_EI, nuclear_Gen_NE_NE2020_EI, nuclear_Gen_MISO_NE2050_EI, nuclear_Gen_MISO_NE2020_EI,
                 nuclear_Gen_PJM_NE2050_EI, nuclear_Gen_PJM_NE2020_EI, nuclear_Gen_SPP_NE2050_EI, nuclear_Gen_SPP_NE2020_EI,
                 nuclear_Gen_SW_NE2050_ERCOT, nuclear_Gen_SW_NE2020_ERCOT, nuclear_Gen_NW_NE2050_ERCOT, nuclear_Gen_NW_NE2020_ERCOT,
                 nuclear_Gen_NOE_NE2050_ERCOT, nuclear_Gen_NOE_NE2020_ERCOT, nuclear_Gen_SE_NE2050_ERCOT, nuclear_Gen_SE_NE2020_ERCOT]
  planType_Nuclear = ['Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear',
                      'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear']

  H2_ref = [hydrogen_Gen_SERC_NE2050_EI, hydrogen_Gen_SERC_NE2020_EI, hydrogen_Gen_NY_NE2050_EI, hydrogen_Gen_NY_NE2020_EI,
              hydrogen_Gen_NE_NE2050_EI, hydrogen_Gen_NE_NE2020_EI, hydrogen_Gen_MISO_NE2050_EI, hydrogen_Gen_MISO_NE2020_EI,
              hydrogen_Gen_PJM_NE2050_EI, hydrogen_Gen_PJM_NE2020_EI, hydrogen_Gen_SPP_NE2050_EI, hydrogen_Gen_SPP_NE2020_EI,
              hydrogen_Gen_SW_NE2050_ERCOT, hydrogen_Gen_SW_NE2020_ERCOT, hydrogen_Gen_NW_NE2050_ERCOT, hydrogen_Gen_NW_NE2020_ERCOT,
              hydrogen_Gen_NOE_NE2050_ERCOT, hydrogen_Gen_NOE_NE2020_ERCOT, hydrogen_Gen_SE_NE2050_ERCOT, hydrogen_Gen_SE_NE2020_ERCOT]
  planType_H2 = ['Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen',
                       'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen']

  Bat_ref = [battery_Gen_SERC_NE2050_EI, battery_Gen_SERC_NE2020_EI, battery_Gen_NY_NE2050_EI, battery_Gen_NY_NE2020_EI,
             battery_Gen_NE_NE2050_EI, battery_Gen_NE_NE2020_EI, battery_Gen_MISO_NE2050_EI, battery_Gen_MISO_NE2020_EI,
             battery_Gen_PJM_NE2050_EI, battery_Gen_PJM_NE2020_EI, battery_Gen_SPP_NE2050_EI, battery_Gen_SPP_NE2020_EI,
             battery_Gen_SW_NE2050_ERCOT, battery_Gen_SW_NE2020_ERCOT, battery_Gen_NW_NE2050_ERCOT, battery_Gen_NW_NE2020_ERCOT,
             battery_Gen_NOE_NE2050_ERCOT, battery_Gen_NOE_NE2020_ERCOT, battery_Gen_SE_NE2050_ERCOT, battery_Gen_SE_NE2020_ERCOT]
  planType_Bat = ['Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery',
                      'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery']

  DAC_ref = [dac_Gen_SERC_NE2050_EI, dac_Gen_SERC_NE2020_EI, dac_Gen_NY_NE2050_EI, dac_Gen_NY_NE2020_EI,
              dac_Gen_NE_NE2050_EI, dac_Gen_NE_NE2020_EI, dac_Gen_MISO_NE2050_EI, dac_Gen_MISO_NE2020_EI,
              dac_Gen_PJM_NE2050_EI, dac_Gen_PJM_NE2020_EI, dac_Gen_SPP_NE2050_EI, dac_Gen_SPP_NE2020_EI,
              dac_Gen_SW_NE2050_ERCOT, dac_Gen_SW_NE2020_ERCOT, dac_Gen_NW_NE2050_ERCOT, dac_Gen_NW_NE2020_ERCOT,
              dac_Gen_NOE_NE2050_ERCOT, dac_Gen_NOE_NE2020_ERCOT, dac_Gen_SE_NE2050_ERCOT, dac_Gen_SE_NE2020_ERCOT]
  planType_DAC = ['DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS',
                   'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS']

  Wind_ref = [wind_Gen_SERC_NE2050_EI, wind_Gen_SERC_NE2020_EI, wind_Gen_NY_NE2050_EI, wind_Gen_NY_NE2020_EI,
              wind_Gen_NE_NE2050_EI, wind_Gen_NE_NE2020_EI, wind_Gen_MISO_NE2050_EI, wind_Gen_MISO_NE2020_EI,
              wind_Gen_PJM_NE2050_EI, wind_Gen_PJM_NE2020_EI, wind_Gen_SPP_NE2050_EI, wind_Gen_SPP_NE2020_EI,
              wind_Gen_SW_NE2050_ERCOT, wind_Gen_SW_NE2020_ERCOT, wind_Gen_NW_NE2050_ERCOT, wind_Gen_NW_NE2020_ERCOT,
              wind_Gen_NOE_NE2050_ERCOT, wind_Gen_NOE_NE2020_ERCOT, wind_Gen_SE_NE2050_ERCOT, wind_Gen_SE_NE2020_ERCOT]
  planType_Wind = ['Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind',
                   'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind']

  Solar_ref = [solar_Gen_SERC_NE2050_EI, solar_Gen_SERC_NE2020_EI, solar_Gen_NY_NE2050_EI, solar_Gen_NY_NE2020_EI,
               solar_Gen_NE_NE2050_EI, solar_Gen_NE_NE2020_EI, solar_Gen_MISO_NE2050_EI, solar_Gen_MISO_NE2020_EI,
               solar_Gen_PJM_NE2050_EI, solar_Gen_PJM_NE2020_EI, solar_Gen_SPP_NE2050_EI, solar_Gen_SPP_NE2020_EI,
               solar_Gen_SW_NE2050_ERCOT, solar_Gen_SW_NE2020_ERCOT, solar_Gen_NW_NE2050_ERCOT, solar_Gen_NW_NE2020_ERCOT,
               solar_Gen_NOE_NE2050_ERCOT, solar_Gen_NOE_NE2020_ERCOT, solar_Gen_SE_NE2050_ERCOT, solar_Gen_SE_NE2020_ERCOT]
  planType_Solar = ['Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV',
                    'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV']


  gen_ref = np.hstack((CC_ref, CCCCS_ref, Nuclear_ref, H2_ref, Bat_ref, DAC_ref, Wind_ref, Solar_ref))
  planType_ref = np.hstack((planType_CC, planType_CCCCS, planType_Nuclear, planType_H2, planType_Bat, planType_DAC, planType_Wind, planType_Solar))
  region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
  planning_ref = np.hstack((planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col))

  genCE_ref = np.vstack((region_ref, planning_ref, planType_ref, gen_ref))
  df_genCE_ref = pd.DataFrame(genCE_ref)
  df_genCE_ref = df_genCE_ref.transpose()
  df_genCE_ref.rename({0: 'Region', 1: 'PlanningScr', 2: 'Technology', 3: 'Gen'},axis=1, inplace=True)
  df_genCERegion_ref = df_genCE_ref.astype({'Gen': float})

  return df_genCERegion_ref

def genCF(cf_CCCCS_NE2050_EI, cf_dac_NE2050_EI, cf_bat_NE2050_EI, cf_h2_NE2050_EI,
          cf_CCCCS_NE2020_EI, cf_dac_NE2020_EI, cf_bat_NE2020_EI, cf_h2_NE2020_EI,
          cf_CCCCS_NE2050_ERCOT, cf_dac_NE2050_ERCOT, cf_bat_NE2050_ERCOT, cf_h2_NE2050_ERCOT,
          cf_CCCCS_NE2020_ERCOT, cf_dac_NE2020_ERCOT, cf_bat_NE2020_ERCOT, cf_h2_NE2020_ERCOT):

    CCCCS_ref = [cf_CCCCS_NE2050_EI, cf_CCCCS_NE2020_EI, cf_CCCCS_NE2050_ERCOT, cf_CCCCS_NE2020_ERCOT]
    planType_CCCCS = ['NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS']
    region_Col = ['EI', 'EI', 'ERCOT', 'ERCOT']
    planning_Col = ['NE2050', 'NE2020', 'NE2050', 'NE2020']

    H2_ref = [cf_h2_NE2050_EI, cf_h2_NE2020_EI, cf_h2_NE2050_ERCOT, cf_h2_NE2020_ERCOT]
    planType_H2 = ['Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen']

    Bat_ref = [cf_bat_NE2050_EI, cf_bat_NE2020_EI, cf_bat_NE2050_ERCOT, cf_bat_NE2020_ERCOT]
    planType_Bat = ['Battery', 'Battery', 'Battery', 'Battery']

    DAC_ref = [cf_dac_NE2050_EI, cf_dac_NE2020_EI, cf_dac_NE2050_ERCOT, cf_dac_NE2020_ERCOT]
    planType_DAC = ['DACS', 'DACS', 'DACS', 'DACS']

    cf_ref = np.hstack((CCCCS_ref, H2_ref, Bat_ref, DAC_ref))
    planType_ref = np.hstack((planType_CCCCS, planType_H2, planType_Bat, planType_DAC))
    region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col))
    planning_ref = np.hstack((planning_Col, planning_Col, planning_Col, planning_Col))

    cfCE_ref = np.vstack((region_ref, planning_ref, planType_ref, cf_ref))
    df_CF = pd.DataFrame(cfCE_ref)
    df_CF = df_CF.transpose()
    df_CF.rename({0: 'Region', 1: 'PlanningScr', 2: 'Technology', 3: 'Capacity Factor'}, axis=1, inplace=True)
    df_CF = df_CF.astype({'Capacity Factor': float})

    return df_CF

def graphEICap(CoalCCS_SERC_NE2020_EI, CoalCCS_NE_NE2020_EI, CoalCCS_NY_NE2020_EI, CoalCCS_MISO_NE2020_EI, CoalCCS_PJM_NE2020_EI, CoalCCS_SPP_NE2020_EI,
               CCCCS_SERC_NE2020_EI, CCCCS_NE_NE2020_EI, CCCCS_NY_NE2020_EI, CCCCS_MISO_NE2020_EI, CCCCS_PJM_NE2020_EI, CCCCS_SPP_NE2020_EI,
               CC_SERC_NE2020_EI, CC_NE_NE2020_EI, CC_NY_NE2020_EI, CC_MISO_NE2020_EI, CC_PJM_NE2020_EI, CC_SPP_NE2020_EI,
               Nuclear_SERC_NE2020_EI, Nuclear_NE_NE2020_EI, Nuclear_NY_NE2020_EI, Nuclear_MISO_NE2020_EI, Nuclear_PJM_NE2020_EI, Nuclear_SPP_NE2020_EI,
               Hydrogen_SERC_NE2020_EI, Hydrogen_NE_NE2020_EI, Hydrogen_NY_NE2020_EI, Hydrogen_MISO_NE2020_EI, Hydrogen_PJM_NE2020_EI, Hydrogen_SPP_NE2020_EI,
               Battery_SERC_NE2020_EI, Battery_NE_NE2020_EI, Battery_NY_NE2020_EI, Battery_MISO_NE2020_EI, Battery_PJM_NE2020_EI, Battery_SPP_NE2020_EI,
               Wind_SERC_NE2020_EI, Wind_NE_NE2020_EI, Wind_NY_NE2020_EI, Wind_MISO_NE2020_EI, Wind_PJM_NE2020_EI, Wind_SPP_NE2020_EI,
               Solar_SERC_NE2020_EI, Solar_NE_NE2020_EI, Solar_NY_NE2020_EI, Solar_MISO_NE2020_EI, Solar_PJM_NE2020_EI, Solar_SPP_NE2020_EI,
               DAC_SERC_NE2020_EI, DAC_NE_NE2020_EI, DAC_NY_NE2020_EI, DAC_MISO_NE2020_EI, DAC_PJM_NE2020_EI, DAC_SPP_NE2020_EI,
               CoalCCS_NW_NE2020_EI, CoalCCS_SW_NE2020_EI, CoalCCS_NOE_NE2020_EI, CoalCCS_SE_NE2020_EI,
               CCCCS_NW_NE2020_EI, CCCCS_SW_NE2020_EI, CCCCS_NOE_NE2020_EI, CCCCS_SE_NE2020_EI,
               CC_NW_NE2020_EI, CC_SW_NE2020_EI, CC_NOE_NE2020_EI, CC_SE_NE2020_EI,
               Nuclear_NW_NE2020_EI, Nuclear_SW_NE2020_EI, Nuclear_NOE_NE2020_EI, Nuclear_SE_NE2020_EI,
               Hydrogen_NW_NE2020_EI, Hydrogen_SW_NE2020_EI, Hydrogen_NOE_NE2020_EI, Hydrogen_SE_NE2020_EI,
               Battery_NW_NE2020_EI, Battery_SW_NE2020_EI, Battery_NOE_NE2020_EI, Battery_SE_NE2020_EI,
               DAC_NW_NE2020_EI, DAC_SW_NE2020_EI, DAC_NOE_NE2020_EI, DAC_SE_NE2020_EI,
               Wind_NW_NE2020_EI, Wind_SW_NE2020_EI, Wind_NOE_NE2020_EI, Wind_SE_NE2020_EI,
               Solar_NW_NE2020_EI, Solar_SW_NE2020_EI, Solar_NOE_NE2020_EI, Solar_SE_NE2020_EI,
               CoalCCS_SERC_NE2050_EI, CoalCCS_NE_NE2050_EI, CoalCCS_NY_NE2050_EI, CoalCCS_MISO_NE2050_EI, CoalCCS_PJM_NE2050_EI, CoalCCS_SPP_NE2050_EI,
               CCCCS_SERC_NE2050_EI, CCCCS_NE_NE2050_EI, CCCCS_NY_NE2050_EI, CCCCS_MISO_NE2050_EI, CCCCS_PJM_NE2050_EI, CCCCS_SPP_NE2050_EI,
               CC_SERC_NE2050_EI, CC_NE_NE2050_EI, CC_NY_NE2050_EI, CC_MISO_NE2050_EI, CC_PJM_NE2050_EI, CC_SPP_NE2050_EI,
               Nuclear_SERC_NE2050_EI, Nuclear_NE_NE2050_EI, Nuclear_NY_NE2050_EI, Nuclear_MISO_NE2050_EI, Nuclear_PJM_NE2050_EI, Nuclear_SPP_NE2050_EI,
               Hydrogen_SERC_NE2050_EI, Hydrogen_NE_NE2050_EI, Hydrogen_NY_NE2050_EI, Hydrogen_MISO_NE2050_EI, Hydrogen_PJM_NE2050_EI, Hydrogen_SPP_NE2050_EI,
               Battery_SERC_NE2050_EI, Battery_NE_NE2050_EI, Battery_NY_NE2050_EI, Battery_MISO_NE2050_EI, Battery_PJM_NE2050_EI, Battery_SPP_NE2050_EI,
               Wind_SERC_NE2050_EI, Wind_NE_NE2050_EI, Wind_NY_NE2050_EI, Wind_MISO_NE2050_EI, Wind_PJM_NE2050_EI, Wind_SPP_NE2050_EI,
               Solar_SERC_NE2050_EI, Solar_NE_NE2050_EI, Solar_NY_NE2050_EI, Solar_MISO_NE2050_EI, Solar_PJM_NE2050_EI, Solar_SPP_NE2050_EI,
               DAC_SERC_NE2050_EI, DAC_NE_NE2050_EI, DAC_NY_NE2050_EI, DAC_MISO_NE2050_EI, DAC_PJM_NE2050_EI, DAC_SPP_NE2050_EI,
               CoalCCS_NW_NE2050_EI, CoalCCS_SW_NE2050_EI, CoalCCS_NOE_NE2050_EI, CoalCCS_SE_NE2050_EI,
               CCCCS_NW_NE2050_EI, CCCCS_SW_NE2050_EI, CCCCS_NOE_NE2050_EI, CCCCS_SE_NE2050_EI,
               CC_NW_NE2050_EI, CC_SW_NE2050_EI, CC_NOE_NE2050_EI, CC_SE_NE2050_EI,
               Nuclear_NW_NE2050_EI, Nuclear_SW_NE2050_EI, Nuclear_NOE_NE2050_EI, Nuclear_SE_NE2050_EI,
               Hydrogen_NW_NE2050_EI, Hydrogen_SW_NE2050_EI, Hydrogen_NOE_NE2050_EI, Hydrogen_SE_NE2050_EI,
               Battery_NW_NE2050_EI, Battery_SW_NE2050_EI, Battery_NOE_NE2050_EI, Battery_SE_NE2050_EI,
               DAC_NW_NE2050_EI, DAC_SW_NE2050_EI, DAC_NOE_NE2050_EI, DAC_SE_NE2050_EI,
               Wind_NW_NE2050_EI, Wind_SW_NE2050_EI, Wind_NOE_NE2050_EI, Wind_SE_NE2050_EI,
               Solar_NW_NE2050_EI, Solar_SW_NE2050_EI, Solar_NOE_NE2050_EI, Solar_SE_NE2050_EI,
              CoalCCS_SERC_NE2020_EI_2, CoalCCS_NE_NE2020_EI_2, CoalCCS_NY_NE2020_EI_2, CoalCCS_MISO_NE2020_EI_2, CoalCCS_PJM_NE2020_EI_2, CoalCCS_SPP_NE2020_EI_2,
              CCCCS_SERC_NE2020_EI_2, CCCCS_NE_NE2020_EI_2, CCCCS_NY_NE2020_EI_2, CCCCS_MISO_NE2020_EI_2, CCCCS_PJM_NE2020_EI_2, CCCCS_SPP_NE2020_EI_2,
              CC_SERC_NE2020_EI_2, CC_NE_NE2020_EI_2, CC_NY_NE2020_EI_2, CC_MISO_NE2020_EI_2, CC_PJM_NE2020_EI_2, CC_SPP_NE2020_EI_2,
              Nuclear_SERC_NE2020_EI_2, Nuclear_NE_NE2020_EI_2, Nuclear_NY_NE2020_EI_2, Nuclear_MISO_NE2020_EI_2, Nuclear_PJM_NE2020_EI_2, Nuclear_SPP_NE2020_EI_2,
              Hydrogen_SERC_NE2020_EI_2, Hydrogen_NE_NE2020_EI_2, Hydrogen_NY_NE2020_EI_2, Hydrogen_MISO_NE2020_EI_2, Hydrogen_PJM_NE2020_EI_2, Hydrogen_SPP_NE2020_EI_2,
              Battery_SERC_NE2020_EI_2, Battery_NE_NE2020_EI_2, Battery_NY_NE2020_EI_2, Battery_MISO_NE2020_EI_2, Battery_PJM_NE2020_EI_2, Battery_SPP_NE2020_EI_2,
              Wind_SERC_NE2020_EI_2, Wind_NE_NE2020_EI_2, Wind_NY_NE2020_EI_2, Wind_MISO_NE2020_EI_2, Wind_PJM_NE2020_EI_2, Wind_SPP_NE2020_EI_2,
              Solar_SERC_NE2020_EI_2, Solar_NE_NE2020_EI_2, Solar_NY_NE2020_EI_2, Solar_MISO_NE2020_EI_2, Solar_PJM_NE2020_EI_2, Solar_SPP_NE2020_EI_2,
              DAC_SERC_NE2020_EI_2, DAC_NE_NE2020_EI_2, DAC_NY_NE2020_EI_2, DAC_MISO_NE2020_EI_2, DAC_PJM_NE2020_EI_2, DAC_SPP_NE2020_EI_2,
              CoalCCS_NW_NE2020_EI_2, CoalCCS_SW_NE2020_EI_2, CoalCCS_NOE_NE2020_EI_2, CoalCCS_SE_NE2020_EI_2,
              CCCCS_NW_NE2020_EI_2, CCCCS_SW_NE2020_EI_2, CCCCS_NOE_NE2020_EI_2, CCCCS_SE_NE2020_EI_2,
              CC_NW_NE2020_EI_2, CC_SW_NE2020_EI_2, CC_NOE_NE2020_EI_2, CC_SE_NE2020_EI_2,
              Nuclear_NW_NE2020_EI_2, Nuclear_SW_NE2020_EI_2, Nuclear_NOE_NE2020_EI_2, Nuclear_SE_NE2020_EI_2,
              Hydrogen_NW_NE2020_EI_2, Hydrogen_SW_NE2020_EI_2, Hydrogen_NOE_NE2020_EI_2, Hydrogen_SE_NE2020_EI_2,
              Battery_NW_NE2020_EI_2, Battery_SW_NE2020_EI_2, Battery_NOE_NE2020_EI_2, Battery_SE_NE2020_EI_2,
              DAC_NW_NE2020_EI_2, DAC_SW_NE2020_EI_2, DAC_NOE_NE2020_EI_2, DAC_SE_NE2020_EI_2,
              Wind_NW_NE2020_EI_2, Wind_SW_NE2020_EI_2, Wind_NOE_NE2020_EI_2, Wind_SE_NE2020_EI_2,
              Solar_NW_NE2020_EI_2, Solar_SW_NE2020_EI_2, Solar_NOE_NE2020_EI_2, Solar_SE_NE2020_EI_2,
              CoalCCS_SERC_NE2050_EI_2, CoalCCS_NE_NE2050_EI_2, CoalCCS_NY_NE2050_EI_2, CoalCCS_MISO_NE2050_EI_2, CoalCCS_PJM_NE2050_EI_2, CoalCCS_SPP_NE2050_EI_2,
              CCCCS_SERC_NE2050_EI_2, CCCCS_NE_NE2050_EI_2, CCCCS_NY_NE2050_EI_2, CCCCS_MISO_NE2050_EI_2, CCCCS_PJM_NE2050_EI_2, CCCCS_SPP_NE2050_EI_2,
              CC_SERC_NE2050_EI_2, CC_NE_NE2050_EI_2, CC_NY_NE2050_EI_2, CC_MISO_NE2050_EI_2, CC_PJM_NE2050_EI_2, CC_SPP_NE2050_EI_2,
              Nuclear_SERC_NE2050_EI_2, Nuclear_NE_NE2050_EI_2, Nuclear_NY_NE2050_EI_2, Nuclear_MISO_NE2050_EI_2, Nuclear_PJM_NE2050_EI_2, Nuclear_SPP_NE2050_EI_2,
              Hydrogen_SERC_NE2050_EI_2, Hydrogen_NE_NE2050_EI_2, Hydrogen_NY_NE2050_EI_2, Hydrogen_MISO_NE2050_EI_2, Hydrogen_PJM_NE2050_EI_2, Hydrogen_SPP_NE2050_EI_2,
              Battery_SERC_NE2050_EI_2, Battery_NE_NE2050_EI_2, Battery_NY_NE2050_EI_2, Battery_MISO_NE2050_EI_2, Battery_PJM_NE2050_EI_2, Battery_SPP_NE2050_EI_2,
              Wind_SERC_NE2050_EI_2, Wind_NE_NE2050_EI_2, Wind_NY_NE2050_EI_2, Wind_MISO_NE2050_EI_2, Wind_PJM_NE2050_EI_2, Wind_SPP_NE2050_EI_2,
              Solar_SERC_NE2050_EI_2, Solar_NE_NE2050_EI_2, Solar_NY_NE2050_EI_2, Solar_MISO_NE2050_EI_2, Solar_PJM_NE2050_EI_2, Solar_SPP_NE2050_EI_2,
              DAC_SERC_NE2050_EI_2, DAC_NE_NE2050_EI_2, DAC_NY_NE2050_EI_2, DAC_MISO_NE2050_EI_2, DAC_PJM_NE2050_EI_2, DAC_SPP_NE2050_EI_2,
              CoalCCS_NW_NE2050_EI_2, CoalCCS_SW_NE2050_EI_2, CoalCCS_NOE_NE2050_EI_2, CoalCCS_SE_NE2050_EI_2,
              CCCCS_NW_NE2050_EI_2, CCCCS_SW_NE2050_EI_2, CCCCS_NOE_NE2050_EI_2, CCCCS_SE_NE2050_EI_2,
              CC_NW_NE2050_EI_2, CC_SW_NE2050_EI_2, CC_NOE_NE2050_EI_2, CC_SE_NE2050_EI_2,
              Nuclear_NW_NE2050_EI_2, Nuclear_SW_NE2050_EI_2, Nuclear_NOE_NE2050_EI_2, Nuclear_SE_NE2050_EI_2,
              Hydrogen_NW_NE2050_EI_2, Hydrogen_SW_NE2050_EI_2, Hydrogen_NOE_NE2050_EI_2, Hydrogen_SE_NE2050_EI_2,
              Battery_NW_NE2050_EI_2, Battery_SW_NE2050_EI_2, Battery_NOE_NE2050_EI_2, Battery_SE_NE2050_EI_2,
              DAC_NW_NE2050_EI_2, DAC_SW_NE2050_EI_2, DAC_NOE_NE2050_EI_2, DAC_SE_NE2050_EI_2,
              Wind_NW_NE2050_EI_2, Wind_SW_NE2050_EI_2, Wind_NOE_NE2050_EI_2, Wind_SE_NE2050_EI_2,
              Solar_NW_NE2050_EI_2, Solar_SW_NE2050_EI_2, Solar_NOE_NE2050_EI_2, Solar_SE_NE2050_EI_2):

    CoalCCS_ref = [CoalCCS_SERC_NE2050_EI-CoalCCS_SERC_NE2050_EI_2, CoalCCS_SERC_NE2050_EI_2, CoalCCS_SERC_NE2020_EI,
                   CoalCCS_NY_NE2050_EI-CoalCCS_NY_NE2050_EI_2, CoalCCS_NY_NE2050_EI_2, CoalCCS_NY_NE2020_EI,
                   CoalCCS_NE_NE2050_EI-CoalCCS_NE_NE2050_EI_2, CoalCCS_NE_NE2050_EI_2, CoalCCS_NE_NE2020_EI,
                   CoalCCS_PJM_NE2050_EI-CoalCCS_PJM_NE2050_EI_2, CoalCCS_PJM_NE2050_EI_2, CoalCCS_PJM_NE2020_EI,
                   CoalCCS_MISO_NE2050_EI-CoalCCS_MISO_NE2050_EI_2, CoalCCS_MISO_NE2050_EI_2, CoalCCS_MISO_NE2020_EI,
                   CoalCCS_SPP_NE2050_EI-CoalCCS_SPP_NE2050_EI_2, CoalCCS_SPP_NE2050_EI_2, CoalCCS_SPP_NE2020_EI]

    planType_coalCCS = ['Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS',
                        'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS',
                        'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS']
    region_Col = ['SERC', 'SERC', 'SERC', 'NY', 'NY', 'NY','NE', 'NE', 'NE', 'PJM', 'PJM', 'PJM','MISO', 'MISO', 'MISO', 'SPP', 'SPP', 'SPP']
    planning_Col = ['Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                    'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                    'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                    'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                    'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                    'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now']

    CC_ref = [CC_SERC_NE2050_EI-CC_SERC_NE2050_EI_2, CC_SERC_NE2050_EI_2, CC_SERC_NE2020_EI,
                   CC_NY_NE2050_EI-CC_NY_NE2050_EI_2, CC_NY_NE2050_EI_2, CC_NY_NE2020_EI,
                   CC_NE_NE2050_EI-CC_NE_NE2050_EI_2, CC_NE_NE2050_EI_2, CC_NE_NE2020_EI,
                   CC_PJM_NE2050_EI-CC_PJM_NE2050_EI_2, CC_PJM_NE2050_EI_2, CC_PJM_NE2020_EI,
                   CC_MISO_NE2050_EI-CC_MISO_NE2050_EI_2, CC_MISO_NE2050_EI_2, CC_MISO_NE2020_EI,
                   CC_SPP_NE2050_EI-CC_SPP_NE2050_EI_2, CC_SPP_NE2050_EI_2, CC_SPP_NE2020_EI]
    planType_CC = ['NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC','NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC','NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC']

    CCCCS_ref = [CCCCS_SERC_NE2050_EI-CCCCS_SERC_NE2050_EI_2, CCCCS_SERC_NE2050_EI_2, CCCCS_SERC_NE2020_EI,
                   CCCCS_NY_NE2050_EI-CCCCS_NY_NE2050_EI_2, CCCCS_NY_NE2050_EI_2, CCCCS_NY_NE2020_EI,
                   CCCCS_NE_NE2050_EI-CCCCS_NE_NE2050_EI_2, CCCCS_NE_NE2050_EI_2, CCCCS_NE_NE2020_EI,
                   CCCCS_PJM_NE2050_EI-CCCCS_PJM_NE2050_EI_2, CCCCS_PJM_NE2050_EI_2, CCCCS_PJM_NE2020_EI,
                   CCCCS_MISO_NE2050_EI-CCCCS_MISO_NE2050_EI_2, CCCCS_MISO_NE2050_EI_2, CCCCS_MISO_NE2020_EI,
                   CCCCS_SPP_NE2050_EI-CCCCS_SPP_NE2050_EI_2, CCCCS_SPP_NE2050_EI_2, CCCCS_SPP_NE2020_EI]
    planType_CCCCS = ['NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS',
                      'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS',
                      'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS']

    Nuclear_ref = [Nuclear_SERC_NE2050_EI-Nuclear_SERC_NE2050_EI_2, Nuclear_SERC_NE2050_EI_2, Nuclear_SERC_NE2020_EI,
                   Nuclear_NY_NE2050_EI-Nuclear_NY_NE2050_EI_2, Nuclear_NY_NE2050_EI_2, Nuclear_NY_NE2020_EI,
                   Nuclear_NE_NE2050_EI-Nuclear_NE_NE2050_EI_2, Nuclear_NE_NE2050_EI_2, Nuclear_NE_NE2020_EI,
                   Nuclear_PJM_NE2050_EI-Nuclear_PJM_NE2050_EI_2, Nuclear_PJM_NE2050_EI_2, Nuclear_PJM_NE2020_EI,
                   Nuclear_MISO_NE2050_EI-Nuclear_MISO_NE2050_EI_2, Nuclear_MISO_NE2050_EI_2, Nuclear_MISO_NE2020_EI,
                   Nuclear_SPP_NE2050_EI-Nuclear_SPP_NE2050_EI_2, Nuclear_SPP_NE2050_EI_2, Nuclear_SPP_NE2020_EI]
    planType_Nuclear = ['Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear',
                        'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear',
                        'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear']

    H2_ref = [Hydrogen_SERC_NE2050_EI-Hydrogen_SERC_NE2050_EI_2, Hydrogen_SERC_NE2050_EI_2, Hydrogen_SERC_NE2020_EI,
                   Hydrogen_NY_NE2050_EI-Hydrogen_NY_NE2050_EI_2, Hydrogen_NY_NE2050_EI_2, Hydrogen_NY_NE2020_EI,
                   Hydrogen_NE_NE2050_EI-Hydrogen_NE_NE2050_EI_2, Hydrogen_NE_NE2050_EI_2, Hydrogen_NE_NE2020_EI,
                   Hydrogen_PJM_NE2050_EI-Hydrogen_PJM_NE2050_EI_2, Hydrogen_PJM_NE2050_EI_2, Hydrogen_PJM_NE2020_EI,
                   Hydrogen_MISO_NE2050_EI-Hydrogen_MISO_NE2050_EI_2, Hydrogen_MISO_NE2050_EI_2, Hydrogen_MISO_NE2020_EI,
                   Hydrogen_SPP_NE2050_EI-Hydrogen_SPP_NE2050_EI_2, Hydrogen_SPP_NE2050_EI_2, Hydrogen_SPP_NE2020_EI]
    planType_H2 = ['Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen',
                   'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen',
                   'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen']

    Bat_ref = [Battery_SERC_NE2050_EI-Battery_SERC_NE2050_EI_2, Battery_SERC_NE2050_EI_2, Battery_SERC_NE2020_EI,
                   Battery_NY_NE2050_EI-Battery_NY_NE2050_EI_2, Battery_NY_NE2050_EI_2, Battery_NY_NE2020_EI,
                   Battery_NE_NE2050_EI-Battery_NE_NE2050_EI_2, Battery_NE_NE2050_EI_2, Battery_NE_NE2020_EI,
                   Battery_PJM_NE2050_EI-Battery_PJM_NE2050_EI_2, Battery_PJM_NE2050_EI_2, Battery_PJM_NE2020_EI,
                   Battery_MISO_NE2050_EI-Battery_MISO_NE2050_EI_2, Battery_MISO_NE2050_EI_2, Battery_MISO_NE2020_EI,
                   Battery_SPP_NE2050_EI-Battery_SPP_NE2050_EI_2, Battery_SPP_NE2050_EI_2, Battery_SPP_NE2020_EI]
    planType_Bat = ['Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery',
                    'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery',
                    'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery']

    DAC_ref = [(DAC_SERC_NE2050_EI-DAC_SERC_NE2050_EI_2), DAC_SERC_NE2050_EI_2, DAC_SERC_NE2020_EI,
                   (DAC_NY_NE2050_EI-DAC_NY_NE2050_EI_2),DAC_NY_NE2050_EI_2, DAC_NY_NE2020_EI,
                   (DAC_NE_NE2050_EI-DAC_NE_NE2050_EI_2), DAC_NE_NE2050_EI_2, DAC_NE_NE2020_EI,
                   (DAC_PJM_NE2050_EI-DAC_PJM_NE2050_EI_2), DAC_PJM_NE2050_EI_2, DAC_PJM_NE2020_EI,
                   (DAC_MISO_NE2050_EI-DAC_MISO_NE2050_EI_2), DAC_MISO_NE2050_EI_2, DAC_MISO_NE2020_EI,
                   (DAC_SPP_NE2050_EI-DAC_SPP_NE2050_EI_2), DAC_SPP_NE2050_EI_2, DAC_SPP_NE2020_EI]
    planType_DAC = ['DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS']

    Wind_ref = [Wind_SERC_NE2050_EI-Wind_SERC_NE2050_EI_2, Wind_SERC_NE2050_EI_2, Wind_SERC_NE2020_EI,
                   Wind_NY_NE2050_EI-Wind_NY_NE2050_EI_2, Wind_NY_NE2050_EI_2, Wind_NY_NE2020_EI,
                   Wind_NE_NE2050_EI-Wind_NE_NE2050_EI_2, Wind_NE_NE2050_EI_2, Wind_NE_NE2020_EI,
                   Wind_PJM_NE2050_EI-Wind_PJM_NE2050_EI_2, Wind_PJM_NE2050_EI_2, Wind_PJM_NE2020_EI,
                   Wind_MISO_NE2050_EI-Wind_MISO_NE2050_EI_2, Wind_MISO_NE2050_EI_2, Wind_MISO_NE2020_EI,
                   Wind_SPP_NE2050_EI-Wind_SPP_NE2050_EI_2, Wind_SPP_NE2050_EI_2, Wind_SPP_NE2020_EI]
    planType_Wind = ['Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind','Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind','Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind']

    Solar_ref = [Solar_SERC_NE2050_EI-Solar_SERC_NE2050_EI_2, Solar_SERC_NE2050_EI_2, Solar_SERC_NE2020_EI,
                   Solar_NY_NE2050_EI-Solar_NY_NE2050_EI_2, Solar_NY_NE2050_EI_2, Solar_NY_NE2020_EI,
                   Solar_NE_NE2050_EI-Solar_NE_NE2050_EI_2, Solar_NE_NE2050_EI_2, Solar_NE_NE2020_EI,
                   Solar_PJM_NE2050_EI-Solar_PJM_NE2050_EI_2, Solar_PJM_NE2050_EI_2, Solar_PJM_NE2020_EI,
                   Solar_MISO_NE2050_EI-Solar_MISO_NE2050_EI_2, Solar_MISO_NE2050_EI_2, Solar_MISO_NE2020_EI,
                   Solar_SPP_NE2050_EI-Solar_SPP_NE2050_EI_2, Solar_SPP_NE2050_EI_2, Solar_SPP_NE2020_EI]
    planType_Solar = ['Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV',
                      'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV',
                      'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV']

    filler_SERC_NE2050_EI_2 = (CoalCCS_SERC_NE2050_EI + CC_SERC_NE2050_EI + CCCCS_SERC_NE2050_EI + Nuclear_SERC_NE2050_EI + Hydrogen_SERC_NE2050_EI + Battery_SERC_NE2050_EI - DAC_SERC_NE2050_EI + Wind_SERC_NE2050_EI + Solar_SERC_NE2050_EI) \
                           - (CoalCCS_SERC_NE2050_EI_2 + CC_SERC_NE2050_EI_2 + CCCCS_SERC_NE2050_EI_2 + Nuclear_SERC_NE2050_EI_2 + Hydrogen_SERC_NE2050_EI_2 + Battery_SERC_NE2050_EI_2 - DAC_SERC_NE2050_EI_2 + Wind_SERC_NE2050_EI_2 + Solar_SERC_NE2050_EI_2)

    filler_NY_NE2050_EI_2 = (CoalCCS_NY_NE2050_EI + CC_NY_NE2050_EI + CCCCS_NY_NE2050_EI + Nuclear_NY_NE2050_EI + Hydrogen_NY_NE2050_EI + Battery_NY_NE2050_EI - DAC_NY_NE2050_EI + Wind_NY_NE2050_EI + Solar_NY_NE2050_EI) \
                            - (CoalCCS_NY_NE2050_EI_2 + CC_NY_NE2050_EI_2 + CCCCS_NY_NE2050_EI_2 + Nuclear_NY_NE2050_EI_2 + Hydrogen_NY_NE2050_EI_2 + Battery_NY_NE2050_EI_2 - DAC_NY_NE2050_EI_2 + Wind_NY_NE2050_EI_2 + Solar_NY_NE2050_EI_2)

    filler_NE_NE2050_EI_2 = (CoalCCS_NE_NE2050_EI + CC_NE_NE2050_EI + CCCCS_NE_NE2050_EI + Nuclear_NE_NE2050_EI + Hydrogen_NE_NE2050_EI + Battery_NE_NE2050_EI - DAC_NE_NE2050_EI + Wind_NE_NE2050_EI + Solar_NE_NE2050_EI) \
                            - (CoalCCS_NE_NE2050_EI_2 + CC_NE_NE2050_EI_2 + CCCCS_NE_NE2050_EI_2 + Nuclear_NE_NE2050_EI_2 + Hydrogen_NE_NE2050_EI_2 + Battery_NE_NE2050_EI_2 - DAC_NE_NE2050_EI_2 + Wind_NE_NE2050_EI_2 + Solar_NE_NE2050_EI_2)

    filler_PJM_NE2050_EI_2 = (CoalCCS_PJM_NE2050_EI + CC_PJM_NE2050_EI + CCCCS_PJM_NE2050_EI + Nuclear_PJM_NE2050_EI + Hydrogen_PJM_NE2050_EI + Battery_PJM_NE2050_EI - DAC_PJM_NE2050_EI + Wind_PJM_NE2050_EI + Solar_PJM_NE2050_EI) \
                             - ( CoalCCS_PJM_NE2050_EI_2 + CC_PJM_NE2050_EI_2 + CCCCS_PJM_NE2050_EI_2 + Nuclear_PJM_NE2050_EI_2 + Hydrogen_PJM_NE2050_EI_2 + Battery_PJM_NE2050_EI_2 - DAC_PJM_NE2050_EI_2 + Wind_PJM_NE2050_EI_2 + Solar_PJM_NE2050_EI_2)

    filler_MISO_NE2050_EI_2 = (CoalCCS_MISO_NE2050_EI + CC_MISO_NE2050_EI + CCCCS_MISO_NE2050_EI + Nuclear_MISO_NE2050_EI + Hydrogen_MISO_NE2050_EI + Battery_MISO_NE2050_EI - DAC_MISO_NE2050_EI + Wind_MISO_NE2050_EI + Solar_MISO_NE2050_EI) \
                              - (CoalCCS_MISO_NE2050_EI_2 + CC_MISO_NE2050_EI_2 + CCCCS_MISO_NE2050_EI_2 + Nuclear_MISO_NE2050_EI_2 + Hydrogen_MISO_NE2050_EI_2 + Battery_MISO_NE2050_EI_2 - DAC_MISO_NE2050_EI_2 + Wind_MISO_NE2050_EI_2 + Solar_MISO_NE2050_EI_2)

    filler_SPP_NE2050_EI_2 = (CoalCCS_SPP_NE2050_EI + CC_SPP_NE2050_EI + CCCCS_SPP_NE2050_EI + Nuclear_SPP_NE2050_EI + Hydrogen_SPP_NE2050_EI + Battery_SPP_NE2050_EI - DAC_SPP_NE2050_EI + Wind_SPP_NE2050_EI + Solar_SPP_NE2050_EI) \
                             - (CoalCCS_SPP_NE2050_EI_2 + CC_SPP_NE2050_EI_2 + CCCCS_SPP_NE2050_EI_2 + Nuclear_SPP_NE2050_EI_2 + Hydrogen_SPP_NE2050_EI_2 + Battery_SPP_NE2050_EI_2 - DAC_SPP_NE2050_EI_2 + Wind_SPP_NE2050_EI_2 + Solar_SPP_NE2050_EI_2)

    filler_ref = [0, filler_SERC_NE2050_EI_2, 0, 0, filler_NY_NE2050_EI_2, 0,0, filler_NE_NE2050_EI_2, 0,
                  0, filler_PJM_NE2050_EI_2, 0, 0, filler_MISO_NE2050_EI_2, 0, 0, filler_SPP_NE2050_EI_2, 0]
    planType_filler = ['', '', '', '', '', '','', '', '', '', '', '','', '', '', '', '', '']

    capEXP_EI_ref = np.hstack((CC_ref, CCCCS_ref, Nuclear_ref, H2_ref, Bat_ref, DAC_ref, Wind_ref, Solar_ref, filler_ref))
    planType_ref = np.hstack((planType_CC, planType_CCCCS, planType_Nuclear, planType_H2, planType_Bat, planType_DAC, planType_Wind, planType_Solar, planType_filler))
    region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
    planning_ref = np.hstack((planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col))

    capEI_ref = np.vstack((region_ref, planning_ref, planType_ref, capEXP_EI_ref))
    df_capEXP_EI = pd.DataFrame(capEI_ref)
    df_capEXP_EI = df_capEXP_EI.transpose()
    df_capEXP_EI.rename({0: 'Region', 1: 'PlanningScr', 2: 'Technology', 3: 'Capacity'}, axis=1, inplace=True)
    df_capEXP_EI = df_capEXP_EI.astype({'Capacity': float})

    return df_capEXP_EI


def graphERCOTCap(CoalCCS_SERC_NE2020_ERCOT, CoalCCS_NE_NE2020_ERCOT, CoalCCS_NY_NE2020_ERCOT, CoalCCS_MISO_NE2020_ERCOT, CoalCCS_PJM_NE2020_ERCOT, CoalCCS_SPP_NE2020_ERCOT,
                 CCCCS_SERC_NE2020_ERCOT, CCCCS_NE_NE2020_ERCOT, CCCCS_NY_NE2020_ERCOT, CCCCS_MISO_NE2020_ERCOT, CCCCS_PJM_NE2020_ERCOT, CCCCS_SPP_NE2020_ERCOT,
                 CC_SERC_NE2020_ERCOT, CC_NE_NE2020_ERCOT, CC_NY_NE2020_ERCOT, CC_MISO_NE2020_ERCOT, CC_PJM_NE2020_ERCOT, CC_SPP_NE2020_ERCOT,
                 Nuclear_SERC_NE2020_ERCOT, Nuclear_NE_NE2020_ERCOT, Nuclear_NY_NE2020_ERCOT, Nuclear_MISO_NE2020_ERCOT, Nuclear_PJM_NE2020_ERCOT, Nuclear_SPP_NE2020_ERCOT,
                 Hydrogen_SERC_NE2020_ERCOT, Hydrogen_NE_NE2020_ERCOT, Hydrogen_NY_NE2020_ERCOT, Hydrogen_MISO_NE2020_ERCOT, Hydrogen_PJM_NE2020_ERCOT, Hydrogen_SPP_NE2020_ERCOT,
                 Battery_SERC_NE2020_ERCOT, Battery_NE_NE2020_ERCOT, Battery_NY_NE2020_ERCOT, Battery_MISO_NE2020_ERCOT, Battery_PJM_NE2020_ERCOT, Battery_SPP_NE2020_ERCOT,
                 Wind_SERC_NE2020_ERCOT, Wind_NE_NE2020_ERCOT, Wind_NY_NE2020_ERCOT, Wind_MISO_NE2020_ERCOT, Wind_PJM_NE2020_ERCOT, Wind_SPP_NE2020_ERCOT,
                 Solar_SERC_NE2020_ERCOT, Solar_NE_NE2020_ERCOT, Solar_NY_NE2020_ERCOT, Solar_MISO_NE2020_ERCOT, Solar_PJM_NE2020_ERCOT, Solar_SPP_NE2020_ERCOT,
                 DAC_SERC_NE2020_ERCOT, DAC_NE_NE2020_ERCOT, DAC_NY_NE2020_ERCOT, DAC_MISO_NE2020_ERCOT, DAC_PJM_NE2020_ERCOT, DAC_SPP_NE2020_ERCOT,
                 CoalCCS_NW_NE2020_ERCOT, CoalCCS_SW_NE2020_ERCOT, CoalCCS_NOE_NE2020_ERCOT, CoalCCS_SE_NE2020_ERCOT,
                 CCCCS_NW_NE2020_ERCOT, CCCCS_SW_NE2020_ERCOT, CCCCS_NOE_NE2020_ERCOT, CCCCS_SE_NE2020_ERCOT,
                 CC_NW_NE2020_ERCOT, CC_SW_NE2020_ERCOT, CC_NOE_NE2020_ERCOT, CC_SE_NE2020_ERCOT,
                 Nuclear_NW_NE2020_ERCOT, Nuclear_SW_NE2020_ERCOT, Nuclear_NOE_NE2020_ERCOT, Nuclear_SE_NE2020_ERCOT,
                 Hydrogen_NW_NE2020_ERCOT, Hydrogen_SW_NE2020_ERCOT, Hydrogen_NOE_NE2020_ERCOT, Hydrogen_SE_NE2020_ERCOT,
                 Battery_NW_NE2020_ERCOT, Battery_SW_NE2020_ERCOT, Battery_NOE_NE2020_ERCOT, Battery_SE_NE2020_ERCOT,
                 DAC_NW_NE2020_ERCOT, DAC_SW_NE2020_ERCOT, DAC_NOE_NE2020_ERCOT, DAC_SE_NE2020_ERCOT,
                 Wind_NW_NE2020_ERCOT, Wind_SW_NE2020_ERCOT, Wind_NOE_NE2020_ERCOT, Wind_SE_NE2020_ERCOT,
                 Solar_NW_NE2020_ERCOT, Solar_SW_NE2020_ERCOT, Solar_NOE_NE2020_ERCOT, Solar_SE_NE2020_ERCOT,
                 CoalCCS_SERC_NE2050_ERCOT, CoalCCS_NE_NE2050_ERCOT, CoalCCS_NY_NE2050_ERCOT, CoalCCS_MISO_NE2050_ERCOT, CoalCCS_PJM_NE2050_ERCOT, CoalCCS_SPP_NE2050_ERCOT,
                 CCCCS_SERC_NE2050_ERCOT, CCCCS_NE_NE2050_ERCOT, CCCCS_NY_NE2050_ERCOT, CCCCS_MISO_NE2050_ERCOT, CCCCS_PJM_NE2050_ERCOT, CCCCS_SPP_NE2050_ERCOT,
                 CC_SERC_NE2050_ERCOT, CC_NE_NE2050_ERCOT, CC_NY_NE2050_ERCOT, CC_MISO_NE2050_ERCOT, CC_PJM_NE2050_ERCOT, CC_SPP_NE2050_ERCOT,
                 Nuclear_SERC_NE2050_ERCOT, Nuclear_NE_NE2050_ERCOT, Nuclear_NY_NE2050_ERCOT, Nuclear_MISO_NE2050_ERCOT, Nuclear_PJM_NE2050_ERCOT, Nuclear_SPP_NE2050_ERCOT,
                 Hydrogen_SERC_NE2050_ERCOT, Hydrogen_NE_NE2050_ERCOT, Hydrogen_NY_NE2050_ERCOT, Hydrogen_MISO_NE2050_ERCOT, Hydrogen_PJM_NE2050_ERCOT, Hydrogen_SPP_NE2050_ERCOT,
                 Battery_SERC_NE2050_ERCOT, Battery_NE_NE2050_ERCOT, Battery_NY_NE2050_ERCOT, Battery_MISO_NE2050_ERCOT, Battery_PJM_NE2050_ERCOT, Battery_SPP_NE2050_ERCOT,
                 Wind_SERC_NE2050_ERCOT, Wind_NE_NE2050_ERCOT, Wind_NY_NE2050_ERCOT, Wind_MISO_NE2050_ERCOT, Wind_PJM_NE2050_ERCOT, Wind_SPP_NE2050_ERCOT,
                 Solar_SERC_NE2050_ERCOT, Solar_NE_NE2050_ERCOT, Solar_NY_NE2050_ERCOT, Solar_MISO_NE2050_ERCOT, Solar_PJM_NE2050_ERCOT, Solar_SPP_NE2050_ERCOT,
                 DAC_SERC_NE2050_ERCOT, DAC_NE_NE2050_ERCOT, DAC_NY_NE2050_ERCOT, DAC_MISO_NE2050_ERCOT, DAC_PJM_NE2050_ERCOT, DAC_SPP_NE2050_ERCOT,
                 CoalCCS_NW_NE2050_ERCOT, CoalCCS_SW_NE2050_ERCOT, CoalCCS_NOE_NE2050_ERCOT, CoalCCS_SE_NE2050_ERCOT,
                 CCCCS_NW_NE2050_ERCOT, CCCCS_SW_NE2050_ERCOT, CCCCS_NOE_NE2050_ERCOT, CCCCS_SE_NE2050_ERCOT,
                 CC_NW_NE2050_ERCOT, CC_SW_NE2050_ERCOT, CC_NOE_NE2050_ERCOT, CC_SE_NE2050_ERCOT,
                 Nuclear_NW_NE2050_ERCOT, Nuclear_SW_NE2050_ERCOT, Nuclear_NOE_NE2050_ERCOT, Nuclear_SE_NE2050_ERCOT,
                 Hydrogen_NW_NE2050_ERCOT, Hydrogen_SW_NE2050_ERCOT, Hydrogen_NOE_NE2050_ERCOT, Hydrogen_SE_NE2050_ERCOT,
                 Battery_NW_NE2050_ERCOT, Battery_SW_NE2050_ERCOT, Battery_NOE_NE2050_ERCOT, Battery_SE_NE2050_ERCOT,
                 DAC_NW_NE2050_ERCOT, DAC_SW_NE2050_ERCOT, DAC_NOE_NE2050_ERCOT, DAC_SE_NE2050_ERCOT,
                 Wind_NW_NE2050_ERCOT, Wind_SW_NE2050_ERCOT, Wind_NOE_NE2050_ERCOT, Wind_SE_NE2050_ERCOT,
                 Solar_NW_NE2050_ERCOT, Solar_SW_NE2050_ERCOT, Solar_NOE_NE2050_ERCOT, Solar_SE_NE2050_ERCOT,
                CoalCCS_SERC_NE2020_ERCOT_2, CoalCCS_NE_NE2020_ERCOT_2, CoalCCS_NY_NE2020_ERCOT_2, CoalCCS_MISO_NE2020_ERCOT_2, CoalCCS_PJM_NE2020_ERCOT_2,
                CoalCCS_SPP_NE2020_ERCOT_2, CCCCS_SERC_NE2020_ERCOT_2, CCCCS_NE_NE2020_ERCOT_2, CCCCS_NY_NE2020_ERCOT_2, CCCCS_MISO_NE2020_ERCOT_2, CCCCS_PJM_NE2020_ERCOT_2, CCCCS_SPP_NE2020_ERCOT_2,
                CC_SERC_NE2020_ERCOT_2, CC_NE_NE2020_ERCOT_2, CC_NY_NE2020_ERCOT_2, CC_MISO_NE2020_ERCOT_2, CC_PJM_NE2020_ERCOT_2, CC_SPP_NE2020_ERCOT_2,
                Nuclear_SERC_NE2020_ERCOT_2, Nuclear_NE_NE2020_ERCOT_2, Nuclear_NY_NE2020_ERCOT_2, Nuclear_MISO_NE2020_ERCOT_2, Nuclear_PJM_NE2020_ERCOT_2,
                Nuclear_SPP_NE2020_ERCOT_2, Hydrogen_SERC_NE2020_ERCOT_2, Hydrogen_NE_NE2020_ERCOT_2, Hydrogen_NY_NE2020_ERCOT_2, Hydrogen_MISO_NE2020_ERCOT_2, Hydrogen_PJM_NE2020_ERCOT_2,
                Hydrogen_SPP_NE2020_ERCOT_2, Battery_SERC_NE2020_ERCOT_2, Battery_NE_NE2020_ERCOT_2, Battery_NY_NE2020_ERCOT_2, Battery_MISO_NE2020_ERCOT_2, Battery_PJM_NE2020_ERCOT_2,
                Battery_SPP_NE2020_ERCOT_2, Wind_SERC_NE2020_ERCOT_2, Wind_NE_NE2020_ERCOT_2, Wind_NY_NE2020_ERCOT_2, Wind_MISO_NE2020_ERCOT_2, Wind_PJM_NE2020_ERCOT_2, Wind_SPP_NE2020_ERCOT_2,
                Solar_SERC_NE2020_ERCOT_2, Solar_NE_NE2020_ERCOT_2, Solar_NY_NE2020_ERCOT_2, Solar_MISO_NE2020_ERCOT_2, Solar_PJM_NE2020_ERCOT_2, Solar_SPP_NE2020_ERCOT_2,
                DAC_SERC_NE2020_ERCOT_2, DAC_NE_NE2020_ERCOT_2, DAC_NY_NE2020_ERCOT_2, DAC_MISO_NE2020_ERCOT_2, DAC_PJM_NE2020_ERCOT_2, DAC_SPP_NE2020_ERCOT_2,
                CoalCCS_NW_NE2020_ERCOT_2, CoalCCS_SW_NE2020_ERCOT_2, CoalCCS_NOE_NE2020_ERCOT_2, CoalCCS_SE_NE2020_ERCOT_2,
                CCCCS_NW_NE2020_ERCOT_2, CCCCS_SW_NE2020_ERCOT_2, CCCCS_NOE_NE2020_ERCOT_2, CCCCS_SE_NE2020_ERCOT_2,
                CC_NW_NE2020_ERCOT_2, CC_SW_NE2020_ERCOT_2, CC_NOE_NE2020_ERCOT_2, CC_SE_NE2020_ERCOT_2,
                Nuclear_NW_NE2020_ERCOT_2, Nuclear_SW_NE2020_ERCOT_2, Nuclear_NOE_NE2020_ERCOT_2, Nuclear_SE_NE2020_ERCOT_2,
                Hydrogen_NW_NE2020_ERCOT_2, Hydrogen_SW_NE2020_ERCOT_2, Hydrogen_NOE_NE2020_ERCOT_2, Hydrogen_SE_NE2020_ERCOT_2,
                Battery_NW_NE2020_ERCOT_2, Battery_SW_NE2020_ERCOT_2, Battery_NOE_NE2020_ERCOT_2, Battery_SE_NE2020_ERCOT_2,
                DAC_NW_NE2020_ERCOT_2, DAC_SW_NE2020_ERCOT_2, DAC_NOE_NE2020_ERCOT_2, DAC_SE_NE2020_ERCOT_2,
                Wind_NW_NE2020_ERCOT_2, Wind_SW_NE2020_ERCOT_2, Wind_NOE_NE2020_ERCOT_2, Wind_SE_NE2020_ERCOT_2,
                Solar_NW_NE2020_ERCOT_2, Solar_SW_NE2020_ERCOT_2, Solar_NOE_NE2020_ERCOT_2, Solar_SE_NE2020_ERCOT_2,
                CoalCCS_SERC_NE2050_ERCOT_2, CoalCCS_NE_NE2050_ERCOT_2, CoalCCS_NY_NE2050_ERCOT_2, CoalCCS_MISO_NE2050_ERCOT_2, CoalCCS_PJM_NE2050_ERCOT_2,
                CoalCCS_SPP_NE2050_ERCOT_2, CCCCS_SERC_NE2050_ERCOT_2, CCCCS_NE_NE2050_ERCOT_2, CCCCS_NY_NE2050_ERCOT_2, CCCCS_MISO_NE2050_ERCOT_2, CCCCS_PJM_NE2050_ERCOT_2, CCCCS_SPP_NE2050_ERCOT_2,
                CC_SERC_NE2050_ERCOT_2, CC_NE_NE2050_ERCOT_2, CC_NY_NE2050_ERCOT_2, CC_MISO_NE2050_ERCOT_2, CC_PJM_NE2050_ERCOT_2, CC_SPP_NE2050_ERCOT_2,
                Nuclear_SERC_NE2050_ERCOT_2, Nuclear_NE_NE2050_ERCOT_2, Nuclear_NY_NE2050_ERCOT_2, Nuclear_MISO_NE2050_ERCOT_2, Nuclear_PJM_NE2050_ERCOT_2,
                Nuclear_SPP_NE2050_ERCOT_2, Hydrogen_SERC_NE2050_ERCOT_2, Hydrogen_NE_NE2050_ERCOT_2, Hydrogen_NY_NE2050_ERCOT_2, Hydrogen_MISO_NE2050_ERCOT_2, Hydrogen_PJM_NE2050_ERCOT_2,
                Hydrogen_SPP_NE2050_ERCOT_2, Battery_SERC_NE2050_ERCOT_2, Battery_NE_NE2050_ERCOT_2, Battery_NY_NE2050_ERCOT_2, Battery_MISO_NE2050_ERCOT_2, Battery_PJM_NE2050_ERCOT_2,
                Battery_SPP_NE2050_ERCOT_2, Wind_SERC_NE2050_ERCOT_2, Wind_NE_NE2050_ERCOT_2, Wind_NY_NE2050_ERCOT_2, Wind_MISO_NE2050_ERCOT_2, Wind_PJM_NE2050_ERCOT_2, Wind_SPP_NE2050_ERCOT_2,
                Solar_SERC_NE2050_ERCOT_2, Solar_NE_NE2050_ERCOT_2, Solar_NY_NE2050_ERCOT_2, Solar_MISO_NE2050_ERCOT_2, Solar_PJM_NE2050_ERCOT_2, Solar_SPP_NE2050_ERCOT_2,
                DAC_SERC_NE2050_ERCOT_2, DAC_NE_NE2050_ERCOT_2, DAC_NY_NE2050_ERCOT_2, DAC_MISO_NE2050_ERCOT_2, DAC_PJM_NE2050_ERCOT_2, DAC_SPP_NE2050_ERCOT_2,
                CoalCCS_NW_NE2050_ERCOT_2, CoalCCS_SW_NE2050_ERCOT_2, CoalCCS_NOE_NE2050_ERCOT_2, CoalCCS_SE_NE2050_ERCOT_2,
                CCCCS_NW_NE2050_ERCOT_2, CCCCS_SW_NE2050_ERCOT_2, CCCCS_NOE_NE2050_ERCOT_2, CCCCS_SE_NE2050_ERCOT_2,
                CC_NW_NE2050_ERCOT_2, CC_SW_NE2050_ERCOT_2, CC_NOE_NE2050_ERCOT_2, CC_SE_NE2050_ERCOT_2,
                Nuclear_NW_NE2050_ERCOT_2, Nuclear_SW_NE2050_ERCOT_2, Nuclear_NOE_NE2050_ERCOT_2, Nuclear_SE_NE2050_ERCOT_2,
                Hydrogen_NW_NE2050_ERCOT_2, Hydrogen_SW_NE2050_ERCOT_2, Hydrogen_NOE_NE2050_ERCOT_2, Hydrogen_SE_NE2050_ERCOT_2,
                Battery_NW_NE2050_ERCOT_2, Battery_SW_NE2050_ERCOT_2, Battery_NOE_NE2050_ERCOT_2, Battery_SE_NE2050_ERCOT_2,
                DAC_NW_NE2050_ERCOT_2, DAC_SW_NE2050_ERCOT_2, DAC_NOE_NE2050_ERCOT_2, DAC_SE_NE2050_ERCOT_2,
                Wind_NW_NE2050_ERCOT_2, Wind_SW_NE2050_ERCOT_2, Wind_NOE_NE2050_ERCOT_2, Wind_SE_NE2050_ERCOT_2,
                Solar_NW_NE2050_ERCOT_2, Solar_SW_NE2050_ERCOT_2, Solar_NOE_NE2050_ERCOT_2, Solar_SE_NE2050_ERCOT_2):

    CoalCCS_ref = [CoalCCS_NW_NE2050_ERCOT-CoalCCS_NW_NE2050_ERCOT_2, CoalCCS_NW_NE2050_ERCOT_2, CoalCCS_NW_NE2020_ERCOT,
                   CoalCCS_SW_NE2050_ERCOT-CoalCCS_SW_NE2050_ERCOT_2, CoalCCS_SW_NE2050_ERCOT_2, CoalCCS_SW_NE2020_ERCOT,
                   CoalCCS_NOE_NE2050_ERCOT-CoalCCS_NOE_NE2050_ERCOT_2, CoalCCS_NOE_NE2050_ERCOT_2, CoalCCS_NOE_NE2020_ERCOT,
                   CoalCCS_SE_NE2050_ERCOT-CoalCCS_SE_NE2050_ERCOT_2, CoalCCS_SE_NE2050_ERCOT_2, CoalCCS_SE_NE2020_ERCOT]

    planType_coalCCS = ['Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS',
                        'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS', 'Coal CCS']
    region_Col = ['ERCOT-NW', 'ERCOT-NW', 'ERCOT-NW', 'ERCOT-SW', 'ERCOT-SW', 'ERCOT-SW',
                  'ERCOT-NE', 'ERCOT-NE', 'ERCOT-NE', 'ERCOT-SE', 'ERCOT-SE', 'ERCOT-SE']
    planning_Col = ['Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                    'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                    'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now',
                    'Plan After Net-Zero NZS', 'Plan After Net-Zero NES', 'Plan Now']

    CC_ref = [CC_NW_NE2050_ERCOT-CC_NW_NE2050_ERCOT_2, CC_NW_NE2050_ERCOT_2, CC_NW_NE2020_ERCOT,
                   CC_SW_NE2050_ERCOT-CC_SW_NE2050_ERCOT_2, CC_SW_NE2050_ERCOT_2, CC_SW_NE2020_ERCOT,
                   CC_NOE_NE2050_ERCOT-CC_NOE_NE2050_ERCOT_2, CC_NOE_NE2050_ERCOT_2, CC_NOE_NE2020_ERCOT,
                   CC_SE_NE2050_ERCOT-CC_SE_NE2050_ERCOT_2, CC_SE_NE2050_ERCOT_2, CC_SE_NE2020_ERCOT]
    planType_CC = ['NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC', 'NGCC']

    CCCCS_ref = [CCCCS_NW_NE2050_ERCOT-CCCCS_NW_NE2050_ERCOT_2, CCCCS_NW_NE2050_ERCOT_2, CCCCS_NW_NE2020_ERCOT,
                   CCCCS_SW_NE2050_ERCOT-CCCCS_SW_NE2050_ERCOT_2, CCCCS_SW_NE2050_ERCOT_2, CCCCS_SW_NE2020_ERCOT,
                   CCCCS_NOE_NE2050_ERCOT-CCCCS_NOE_NE2050_ERCOT_2, CCCCS_NOE_NE2050_ERCOT_2, CCCCS_NOE_NE2020_ERCOT,
                   CCCCS_SE_NE2050_ERCOT-CCCCS_SE_NE2050_ERCOT_2, CCCCS_SE_NE2050_ERCOT_2, CCCCS_SE_NE2020_ERCOT]
    planType_CCCCS = ['NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS',
                      'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS', 'NGCC CCS']

    Nuclear_ref = [Nuclear_NW_NE2050_ERCOT-Nuclear_NW_NE2050_ERCOT_2, Nuclear_NW_NE2050_ERCOT_2, Nuclear_NW_NE2020_ERCOT,
                   Nuclear_SW_NE2050_ERCOT-Nuclear_SW_NE2050_ERCOT_2, Nuclear_SW_NE2050_ERCOT_2, Nuclear_SW_NE2020_ERCOT,
                   Nuclear_NOE_NE2050_ERCOT-Nuclear_NOE_NE2050_ERCOT_2, Nuclear_NOE_NE2050_ERCOT_2, Nuclear_NOE_NE2020_ERCOT,
                   Nuclear_SE_NE2050_ERCOT-Nuclear_SE_NE2050_ERCOT_2, Nuclear_SE_NE2050_ERCOT_2, Nuclear_SE_NE2020_ERCOT]
    planType_Nuclear = ['Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear',
                        'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear', 'Nuclear']

    H2_ref = [Hydrogen_NW_NE2050_ERCOT-Hydrogen_NW_NE2050_ERCOT_2, Hydrogen_NW_NE2050_ERCOT_2, Hydrogen_NW_NE2020_ERCOT,
                   Hydrogen_SW_NE2050_ERCOT-Hydrogen_SW_NE2050_ERCOT_2, Hydrogen_SW_NE2050_ERCOT_2, Hydrogen_SW_NE2020_ERCOT,
                   Hydrogen_NOE_NE2050_ERCOT-Hydrogen_NOE_NE2050_ERCOT_2, Hydrogen_NOE_NE2050_ERCOT_2, Hydrogen_NOE_NE2020_ERCOT,
                   Hydrogen_SE_NE2050_ERCOT-Hydrogen_SE_NE2050_ERCOT_2, Hydrogen_SE_NE2050_ERCOT_2, Hydrogen_SE_NE2020_ERCOT]
    planType_H2 = ['Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen',
                   'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen']

    Bat_ref = [Battery_NW_NE2050_ERCOT-Battery_NW_NE2050_ERCOT_2, Battery_NW_NE2050_ERCOT_2, Battery_NW_NE2020_ERCOT,
                   Battery_SW_NE2050_ERCOT-Battery_SW_NE2050_ERCOT_2, Battery_SW_NE2050_ERCOT_2, Battery_SW_NE2020_ERCOT,
                   Battery_NOE_NE2050_ERCOT-Battery_NOE_NE2050_ERCOT_2, Battery_NOE_NE2050_ERCOT_2, Battery_NOE_NE2020_ERCOT,
                   Battery_SE_NE2050_ERCOT-Battery_SE_NE2050_ERCOT_2, Battery_SE_NE2050_ERCOT_2, Battery_SE_NE2020_ERCOT]
    planType_Bat = ['Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery',
                    'Battery', 'Battery', 'Battery', 'Battery', 'Battery', 'Battery']

    DAC_ref = [(DAC_NW_NE2050_ERCOT-DAC_NW_NE2050_ERCOT_2), DAC_NW_NE2050_ERCOT_2, DAC_NW_NE2020_ERCOT,
                   (DAC_SW_NE2050_ERCOT-DAC_SW_NE2050_ERCOT_2), DAC_SW_NE2050_ERCOT_2, DAC_SW_NE2020_ERCOT,
                   (DAC_NOE_NE2050_ERCOT-DAC_NOE_NE2050_ERCOT_2), DAC_NOE_NE2050_ERCOT_2, DAC_NOE_NE2020_ERCOT,
                   (DAC_SE_NE2050_ERCOT-DAC_SE_NE2050_ERCOT_2), DAC_SE_NE2050_ERCOT_2, DAC_SE_NE2020_ERCOT]
    planType_DAC = ['DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS', 'DACS']

    Wind_ref = [Wind_NW_NE2050_ERCOT-Wind_NW_NE2050_ERCOT_2, Wind_NW_NE2050_ERCOT_2, Wind_NW_NE2020_ERCOT,
                   Wind_SW_NE2050_ERCOT-Wind_SW_NE2050_ERCOT_2, Wind_SW_NE2050_ERCOT_2, Wind_SW_NE2020_ERCOT,
                   Wind_NOE_NE2050_ERCOT-Wind_NOE_NE2050_ERCOT_2, Wind_NOE_NE2050_ERCOT_2, Wind_NOE_NE2020_ERCOT,
                   Wind_SE_NE2050_ERCOT-Wind_SE_NE2050_ERCOT_2, Wind_SE_NE2050_ERCOT_2, Wind_SE_NE2020_ERCOT]
    planType_Wind = ['Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind', 'Wind']

    Solar_ref = [Solar_NW_NE2050_ERCOT-Solar_NW_NE2050_ERCOT_2, Solar_NW_NE2050_ERCOT_2, Solar_NW_NE2020_ERCOT,
                   Solar_SW_NE2050_ERCOT-Solar_SW_NE2050_ERCOT_2, Solar_SW_NE2050_ERCOT_2, Solar_SW_NE2020_ERCOT,
                   Solar_NOE_NE2050_ERCOT-Solar_NOE_NE2050_ERCOT_2, Solar_NOE_NE2050_ERCOT_2, Solar_NOE_NE2020_ERCOT,
                   Solar_SE_NE2050_ERCOT-Solar_SE_NE2050_ERCOT_2, Solar_SE_NE2050_ERCOT_2, Solar_SE_NE2020_ERCOT]
    planType_Solar = ['Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV',
                      'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV', 'Solar PV']

    filler_NW_NE2050_ERCOT_2 = (CoalCCS_NW_NE2050_ERCOT + CC_NW_NE2050_ERCOT + CCCCS_NW_NE2050_ERCOT + Nuclear_NW_NE2050_ERCOT + Hydrogen_NW_NE2050_ERCOT + Battery_NW_NE2050_ERCOT - DAC_NW_NE2050_ERCOT + Wind_NW_NE2050_ERCOT + Solar_NW_NE2050_ERCOT) \
                              - (CoalCCS_NW_NE2050_ERCOT_2 + CC_NW_NE2050_ERCOT_2 + CCCCS_NW_NE2050_ERCOT_2 + Nuclear_NW_NE2050_ERCOT_2 + Hydrogen_NW_NE2050_ERCOT_2 + Battery_NW_NE2050_ERCOT_2 - DAC_NW_NE2050_ERCOT_2 + Wind_NW_NE2050_ERCOT_2 + Solar_NW_NE2050_ERCOT_2)
    filler_SW_NE2050_ERCOT_2 = (CoalCCS_SW_NE2050_ERCOT + CC_SW_NE2050_ERCOT + CCCCS_SW_NE2050_ERCOT + Nuclear_SW_NE2050_ERCOT + Hydrogen_SW_NE2050_ERCOT + Battery_SW_NE2050_ERCOT - DAC_SW_NE2050_ERCOT + Wind_SW_NE2050_ERCOT + Solar_SW_NE2050_ERCOT) \
                               - (CoalCCS_SW_NE2050_ERCOT_2 + CC_SW_NE2050_ERCOT_2 + CCCCS_SW_NE2050_ERCOT_2 + Nuclear_SW_NE2050_ERCOT_2 + Hydrogen_SW_NE2050_ERCOT_2 + Battery_SW_NE2050_ERCOT_2 - DAC_SW_NE2050_ERCOT_2 + Wind_SW_NE2050_ERCOT_2 + Solar_SW_NE2050_ERCOT_2)
    filler_NOE_NE2050_ERCOT_2 = (CoalCCS_NOE_NE2050_ERCOT + CC_NOE_NE2050_ERCOT + CCCCS_NOE_NE2050_ERCOT + Nuclear_NOE_NE2050_ERCOT + Hydrogen_NOE_NE2050_ERCOT + Battery_NOE_NE2050_ERCOT - DAC_NOE_NE2050_ERCOT + Wind_NOE_NE2050_ERCOT + Solar_NOE_NE2050_ERCOT) \
                                - (CoalCCS_NOE_NE2050_ERCOT_2 + CC_NOE_NE2050_ERCOT_2 + CCCCS_NOE_NE2050_ERCOT_2 + Nuclear_NOE_NE2050_ERCOT_2 + Hydrogen_NOE_NE2050_ERCOT_2 + Battery_NOE_NE2050_ERCOT_2 - DAC_NOE_NE2050_ERCOT_2 + Wind_NOE_NE2050_ERCOT_2 + Solar_NOE_NE2050_ERCOT_2)
    filler_SE_NE2050_ERCOT_2 = (CoalCCS_SE_NE2050_ERCOT + CC_SE_NE2050_ERCOT + CCCCS_SE_NE2050_ERCOT + Nuclear_SE_NE2050_ERCOT + Hydrogen_SE_NE2050_ERCOT + Battery_SE_NE2050_ERCOT - DAC_SE_NE2050_ERCOT + Wind_SE_NE2050_ERCOT + Solar_SE_NE2050_ERCOT) \
                               - (CoalCCS_SE_NE2050_ERCOT_2 + CC_SE_NE2050_ERCOT_2 + CCCCS_SE_NE2050_ERCOT_2 + Nuclear_SE_NE2050_ERCOT_2 + Hydrogen_SE_NE2050_ERCOT_2 + Battery_SE_NE2050_ERCOT_2 - DAC_SE_NE2050_ERCOT_2 + Wind_SE_NE2050_ERCOT_2 + Solar_SE_NE2050_ERCOT_2)

    filler_ref = [0, filler_NW_NE2050_ERCOT_2, 0, 0, filler_SW_NE2050_ERCOT_2, 0, 0, filler_NOE_NE2050_ERCOT_2, 0,0, filler_SE_NE2050_ERCOT_2, 0]
    planType_filler = ['', '', '', '', '', '', '', '', '', '', '', '']

    capEXP_ERCOT_ref = np.hstack((CC_ref, CCCCS_ref, Nuclear_ref, H2_ref, Bat_ref, DAC_ref, Wind_ref, Solar_ref, filler_ref))
    planType_ref = np.hstack((planType_CC, planType_CCCCS, planType_Nuclear, planType_H2, planType_Bat, planType_DAC, planType_Wind, planType_Solar, planType_filler))
    region_ref = np.hstack((region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col, region_Col))
    planning_ref = np.hstack((planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col, planning_Col))

    capERCOT_ref = np.vstack((region_ref, planning_ref, planType_ref, capEXP_ERCOT_ref))
    df_capEXP_ERCOT = pd.DataFrame(capERCOT_ref)
    df_capEXP_ERCOT = df_capEXP_ERCOT.transpose()
    df_capEXP_ERCOT.rename({0: 'Region', 1: 'PlanningScr', 2: 'Technology', 3: 'Capacity'}, axis=1, inplace=True)
    df_capEXP_ERCOT = df_capEXP_ERCOT.astype({'Capacity': float})

    return df_capEXP_ERCOT



main()

