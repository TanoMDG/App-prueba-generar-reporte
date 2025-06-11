from utils.api_covid import get_data_country
from utils.reportes import generar_reporte
from utils.email_utils import enviar_email
import datetime, json

with open("config.json") as f:
    cfg = json.load(f)

pais = cfg["country"]
df = get_data_country(pais)
file_path, _, _ = generar_reporte(df)
enviar_email(file_path)
