#La Universidad del Valle requiere un programa que le permita conocer cómo califican los
#estudiantes la comida de la cafetería central. Para ello definió una escala de 1 a 10 (1 denota
#horrible y 10 denota excelente). El programa debe ser capaz capturar la calificación de
# cualquier número de estudiantes (no se sabe cuántos estudiantes se encuestarán, así que
# cuando el encuestador ingrese la calificación de 0, se sabrá que la encuesta habrá concluido).
# El programa deberá mostrar en su salida cuántos estudiantes fueron encuestados, así como el
# resumen de la encuesta como el promedio y cuál es la nota más alta dada y la nota más baja

#
calificaciones = []
#
for i in range (0, 10):
    nota= int(input("Ingrese la calificación del estudiante: "))
    if nota <= 0 and nota >= 10:
        break
    calificaciones.append(nota)


NotaA=max(calificaciones)
NotaM=min(calificaciones)
Promedio=sum(calificaciones)/len(calificaciones)
print("La nota más alta dada es: ", NotaA)
print("La nota más baja dada es: ", NotaM)
print("El promedio de las calificaciones es: ", Promedio)
print("El total de estudiantes encuestados es: ", len(calificaciones))
