import pandas as pd

#manera en la que se pueden leer ambos archivos si es que cambian de formato
try:
    # Intentar leer como CSV
    df_estudiantes = pd.read_csv("C:/Users/Liliana/OneDrive/Documentos/Proyectos_Python/respuestas_estudiantes.csv")
except:
    # Si falla, intentar como Excel
    df_estudiantes = pd.read_excel("C:/Users/Liliana/OneDrive/Documentos/Proyectos_Python/respuestas_estudiantes.xlsx")

# === Leer archivo de respuestas correctas ===
try:
    #intentar leer como CSV
    df_correctas = pd.read_csv("C:/Users/Liliana/OneDrive/Documentos/Proyectos_Python/respuestas_correctas.csv")
except:
    #Si falla, intentar como Excel
    df_correctas = pd.read_excel("C:/Users/Liliana/OneDrive/Documentos/Proyectos_Python/respuestas_correctas.xlsx")

preguntas = df_correctas['Pregunta'].values

clave_respuestas = {}

for i in range(df_correctas.shape[0]):
    pregunta = df_correctas['Pregunta'].iloc[i]
    respuesta = df_correctas['Respuesta'].iloc[i]

    clave_respuestas[pregunta] = respuesta

df_estudiantes['Puntuación'] = 0
for p in preguntas:
    respuesta_correcta = clave_respuestas[p]
    df_estudiantes['Puntuación'] = df_estudiantes['Puntuación'].add(
        (df_estudiantes[p] == respuesta_correcta).astype(int))
    
##para que nos de una calificacion del 1 al 10, ya que mi archivo tiene 20 preguntas en vez de 10
df_estudiantes['Puntuación'] = (df_estudiantes['Puntuación'] / len(preguntas)) * 10

df_detalle = df_estudiantes.copy()

for p in preguntas:
    df_detalle[p] = df_detalle[p].where(
        df_detalle[p] == clave_respuestas[p],
        df_detalle[p] + 'X'
    )

df_detalle = df_detalle.sort_values('Puntuación', ascending=False)
print("Leyenda: RespuestaX = Incorrecta")
print(df_detalle.to_string(index=False))

print("\n ==== RESULTADOS DE LOS ESTUDIANTES ====")
print(df_estudiantes[['Nombre','Puntuación']].sort_values('Puntuación', ascending=False).to_string(index=False))

df_estudiantes.to_csv("resultados_examen.csv", index=False)
Eliminar archivo Python innecesario


print("\nResultados guardados en 'resultados_examen.csv'")
