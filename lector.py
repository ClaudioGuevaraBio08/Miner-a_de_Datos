import pandas as pd
#Importa de datos. 
fet_2016 = pd.read_csv("~/Documentos/Mineria/FET_2016.csv", sep = ";")
fet_2017 = pd.read_csv("~/Documentos/Mineria/FET_2017.csv", sep = ";")
fet_2015 = pd.read_csv("~/Documentos/Mineria/FET_2015.csv", sep = ";")
nac_2016 = pd.read_csv("~/Documentos/Mineria/NAC_2016.csv", sep = ";", encoding= "latin", low_memory=False)
nac_2017 = pd.read_csv("~/Documentos/Mineria/NAC_2017.csv", sep = ";", encoding = "latin", low_memory=False)
nac_2015 = pd.read_csv("~/Documentos/Mineria/NAC_2015.csv", sep = ";", encoding= "latin", low_memory=False)


fet = pd.concat([fet_2016,fet_2017], ignore_index = True).drop(["DIA_DEF", "MES_DEF", "ANO_DEF", "LOCAL_DEF", "DIAG1", "DIAG2", "AT_MEDICA", "CAL_MEDICO", "COD_MENOR", "NUTRITIVO", "PARTO_ABOR", "FUND_CAUSA", "DIA_PARTO", "MES_PARTO", "ANO_PARTO"], axis = 1) #Concatena y elimina los atributos mencionados
fet["ESTADO"] = 0 #Agrega estado = 0 para muertos
nac = pd.concat([nac_2016,nac_2017], ignore_index = True).drop(["DIA_NAC", "MES_NAC", "ANO_NAC", "TIPO_PARTO", "ATENC_PART", "LOCAL_PART", "TALLA", "ESTAB"], axis = 1)#Concatena y elimina los atributos mencionados
nac["ESTADO"] = 1 #Agrega estado = 1 para vivos. 
total = pd.concat([nac,fet], ignore_index = True).drop(["HIJ_VIVOS","HIJ_FALL", "HIJ_MORT"], axis = 1) #Elimina algunos comunes
total.dropna() #Elimina nulos
total.to_csv("~/Escritorio/Data.csv") #Exporta 