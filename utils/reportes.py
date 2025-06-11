import pandas as pd
import datetime
"""
def generar_reporte(df, path_output="outputs"):
    
    hoy = df['date'].max().date()
    diario = df[df['date'] == pd.Timestamp(hoy)]
    
    path = f"{path_output}/covid_report_{hoy}.xlsx"
    with pd.ExcelWriter(path) as writer:
        diario.to_excel(writer, sheet_name="Hoy", index=False)
        df.to_excel(writer, sheet_name="Histórico", index=False)
    return path, diario, df
    """
import os

def generar_reporte(df, path_output="outputs"):
    hoy = df['date'].max().date()
    
    # ✅ Crear la carpeta si no existe
    if not os.path.exists(path_output):
        os.makedirs(path_output)

    path = f"{path_output}/covid_report_{hoy}.xlsx"

    with pd.ExcelWriter(path) as writer:
        df[df["date"] == pd.Timestamp(hoy)].to_excel(writer, sheet_name="Hoy", index=False)
        df.to_excel(writer, sheet_name="Histórico", index=False)

    return path, df[df["date"] == pd.Timestamp(hoy)], df
