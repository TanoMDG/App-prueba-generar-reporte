import pandas as pd
import datetime

def generar_reporte(df, path_output="outputs"):
    hoy = df['date'].max().date()
    diario = df[df['date'] == pd.Timestamp(hoy)]
    
    path = f"{path_output}/covid_report_{hoy}.xlsx"
    with pd.ExcelWriter(path) as writer:
        diario.to_excel(writer, sheet_name="Hoy", index=False)
        df.to_excel(writer, sheet_name="Histórico", index=False)
    return path, diario, df
