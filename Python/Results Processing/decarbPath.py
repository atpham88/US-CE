import pandas as pd
import numpy as np
import altair as alt

startYear = 2020
endYear = 2050

def main():
    (NZ_2020_EI, NZ_2020_EI, NEin2020_2020_EI, NEin2020_2050_EI, NEin2050_2020_EI,
     NEin2050_2050_EI) = decarbPath(startYear, endYear, co2Ems2020= 1274, co2EmsCapInFinalYear=-725)
    (NZ_2020_ERCOT, NZ_2020_ERCOT, NEin2020_2020_ERCOT, NEin2020_2050_ERCOT, NEin2050_2020_ERCOT,
     NEin2050_2050_ERCOT) = decarbPath(startYear, endYear, co2Ems2020=131, co2EmsCapInFinalYear=-90)

    NE2020 = [NEin2020_2020_EI, NEin2020_2050_EI, NEin2020_2050_EI,
              NEin2020_2020_ERCOT, NEin2020_2050_ERCOT, NEin2020_2050_ERCOT]
    NE2020_Col = ['Plan Now', 'Plan Now', 'Plan Now', 'Plan Now', 'Plan Now', 'Plan Now']
    region_Col = ['EI', 'EI', 'EI', 'ERCOT', 'ERCOT', 'ERCOT']
    year = ['Now', '2050', '2050', 'Now', '2050', '2050']

    NE2050 = [NEin2050_2020_EI, NEin2050_2050_EI, NEin2020_2050_EI,
              NEin2050_2020_ERCOT, NEin2050_2050_ERCOT, NEin2020_2050_ERCOT]
    NE2050_Col = ['Plan After Net-Zero', 'Plan After Net-Zero', 'Plan After Net-Zero',
                  'Plan After Net-Zero', 'Plan After Net-Zero', 'Plan After Net-Zero']

    decarbData_ref = np.hstack((NE2020, NE2050))
    decarbType_ref = np.hstack((NE2020_Col, NE2050_Col))
    region_ref = np.hstack((region_Col, region_Col))
    planning_ref = np.hstack((year, year))

    decarb_ref = np.vstack((region_ref, planning_ref, decarbType_ref, decarbData_ref))
    df_decarb_ref = pd.DataFrame(decarb_ref)
    df_decarb_ref = df_decarb_ref.transpose()
    df_decarb_ref.rename({0: 'Region', 1: 'Year', 2: 'Pathway', 3: 'Amount'}, axis=1, inplace=True)
    df_decarb_ref = df_decarb_ref.astype({'Amount': float})

    # Plot decarbonization pathway:
    chart = alt.Chart(df_decarb_ref).mark_line(size = 3).encode(
            # tell Altair which field to group columns on
            x=alt.X('Year', axis=alt.Axis(labelAngle=-0), title=None, sort=None),
            # tell Altair which field to use as Y values and how to calculate
            y=alt.Y('Amount',
                    axis=alt.Axis(
                        grid=False,
                        title='CO2 Emission Cap (Million Tons)')),
            # tell Altair which field to use to use as the set of columns to be  represented in each group
            column=alt.Column('Region', title=None, header=alt.Header(labelFontSize=20)),
            # tell Altair which field to use for color segmentation
            color=alt.Color('Pathway',
                            scale=alt.Scale(
                                # make it look pretty with an enjoyable color pallet
                                range=['darkolivegreen', 'lightpink'],
                            ),legend=alt.Legend(columns=1)
                            )).resolve_scale(y='independent').configure_view(
            # remove grid lines around column clusters
            # strokeOpacity=0
        ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=17, titleFontSize=17
                                                                                      ).properties(width=250, height=400).show()


    # Second way:
    NE2020_scr_EI = [NEin2020_2020_EI, NEin2020_2050_EI, NEin2020_2050_EI]
    NE2020_scr_ERCOT = [NEin2020_2020_ERCOT, NEin2020_2050_ERCOT, NEin2020_2050_ERCOT]
    NE2020_Col = ['Plan Now', 'Plan Now', 'Plan Now']
    year = ['Now', '2050', '2050']

    NE2050_scr_EI = [NEin2050_2020_EI, NEin2050_2050_EI, NEin2020_2050_EI]
    NE2050_scr_ERCOT = [NEin2050_2020_ERCOT, NEin2050_2050_ERCOT, NEin2020_2050_ERCOT]
    NE2050_Col = ['Plan After Net-Zero', 'Plan After Net-Zero', 'Plan After Net-Zero']

    NE2050DACS_scr_EI = [NEin2050_2020_EI, NEin2050_2050_EI, NEin2020_2050_EI]
    NE2050DACS_scr_ERCOT = [NEin2050_2020_ERCOT, NEin2050_2050_ERCOT, NEin2020_2050_ERCOT]
    NE2050DACS_Col = ['NE2050+DACS', 'NE2050+DACS', 'NE2050+DACS']

    decarbData_ref_EI = np.hstack((NE2020_scr_EI, NE2050_scr_EI, NE2050DACS_scr_EI))
    decarbType_ref = np.hstack((NE2020_Col, NE2050_Col, NE2050DACS_Col))
    decarbData_ref_ERCOT = np.hstack((NE2020_scr_ERCOT, NE2050_scr_ERCOT, NE2050DACS_scr_ERCOT))
    planning_ref = np.hstack((year, year, year))

    decarb_ref_EI = np.vstack((planning_ref, decarbType_ref, decarbData_ref_EI))
    df_decarb_ref_EI = pd.DataFrame(decarb_ref_EI)
    df_decarb_ref_EI = df_decarb_ref_EI.transpose()
    df_decarb_ref_EI.rename({0: 'Year', 1: 'Scenario', 2: 'Amount'}, axis=1, inplace=True)
    df_decarb_ref_EI = df_decarb_ref_EI.astype({'Amount': float})

    decarb_ref_ERCOT = np.vstack((planning_ref, decarbType_ref, decarbData_ref_ERCOT))
    df_decarb_ref_ERCOT = pd.DataFrame(decarb_ref_ERCOT)
    df_decarb_ref_ERCOT = df_decarb_ref_ERCOT.transpose()
    df_decarb_ref_ERCOT.rename({0: 'Year', 1: 'Scenario', 2: 'Amount'}, axis=1, inplace=True)
    df_decarb_ref_ERCOT = df_decarb_ref_ERCOT.astype({'Amount': float})

    # Plot scenarios - EI:
    chart_ei = alt.Chart(df_decarb_ref_EI).mark_line(size=3).encode(
        # tell Altair which field to group columns on
        x=alt.X('Year', title='Year'),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('Amount',
                axis=alt.Axis(
                    grid=True,
                    title='CO2 Emission Cap (Million Tons)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Scenario', title=None, header=alt.Header(labelFontSize=20)),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Scenario',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['darkolivegreen', 'lightpink', 'skyblue'],
                        ), legend=alt.Legend(columns=1)
                        )).resolve_scale(y='shared').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
        ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=17, titleFontSize=17
                                                                          ).properties(width=300, height=200).show()

    # Plot scenarios - ERCOT:
    chart_ec = alt.Chart(df_decarb_ref_ERCOT).mark_line(size=3).encode(
        # tell Altair which field to group columns on
        x=alt.X('Year', title='Year'),
        # tell Altair which field to use as Y values and how to calculate
        y=alt.Y('Amount',
                axis=alt.Axis(
                    grid=True,
                    title='CO2 Emission Cap (Million Tons)')),
        # tell Altair which field to use to use as the set of columns to be  represented in each group
        column=alt.Column('Scenario', title=None, header=alt.Header(labelFontSize=20)),
        # tell Altair which field to use for color segmentation
        color=alt.Color('Scenario',
                        scale=alt.Scale(
                            # make it look pretty with an enjoyable color pallet
                            range=['darkolivegreen', 'lightpink', 'skyblue'],
                        ), legend=alt.Legend(columns=1)
                        )).resolve_scale(y='shared').configure_view(
        # remove grid lines around column clusters
        # strokeOpacity=0
    ).configure_axis(titleFontSize=16, labelFontSize=14).configure_legend(labelFontSize=17, titleFontSize=17
                                                                          ).properties(width=300, height=200).show()


def decarbPath(startYear, endYear, co2Ems2020, co2EmsCapInFinalYear):

    # Net-Zero System:
    NZ_2020 = co2Ems2020 - (co2Ems2020-0)/3*0
    NZ_2050 = co2Ems2020 - (co2Ems2020-0)/3*3

    NZ = np.array([NZ_2020, NZ_2050])

    # Negative System in 2020:
    NEin2020_2020 = co2Ems2020 - (co2Ems2020-co2EmsCapInFinalYear)/3*0
    NEin2020_2050 = co2Ems2020 - (co2Ems2020-co2EmsCapInFinalYear)/3*3

    NEin2020 = np.array([NEin2020_2020, NEin2020_2050])

    # Negative System in 2050:
    NEin2050_2020 = NZ_2020
    NEin2050_2050 = NZ_2050

    NEin2050 = np.array([NEin2050_2020, NEin2050_2050, co2EmsCapInFinalYear])
    return (NZ_2020, NZ_2020, NEin2020_2020, NEin2020_2050, NEin2050_2020, NEin2050_2050)

main()


