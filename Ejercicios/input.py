nota_tarea=float(input("Ingrese nota de la tarea: "))
nota_leccion=float(input("Ingrese nota de la leccion: "))
nota_examen=float(input("Ingrese nota del examen:"))

total_promedio = (nota_tarea + nota_leccion + nota_examen)/3

print(f"Promedio: {total_promedio}")