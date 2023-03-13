class Estudiantes:
    
        estudiante1="Hirai Momo"
        estudiante2="Myoi Mina"
        
        
class Materia:

    materia1="Psicologia"
    materia2="Liderazgo"
    
from Estudiantes import Estudiantes
from Materia import Materia


class Notas(Estudiantes,Materia):
        pass
        Estudiante1_LabPsico=10            #Notas del estudiante 1 en el laboratorio de psicologia 
        Estudiante1_LabLiderazgo=8         #y liderazgo
        Estudiante2_LabPsico=10            # Notas del estudiante 2 en laboratorio de psicologia
        Estudiante2_LabLiderazgo=9         #y liderazgo
        Estudiante1_ParcialPsico=9         # Parcial de psicologia, estdudiante 1
        Estudiante1_ParcialLiderazgo=7     #Parcial de LIDERAZGO, estdudiante 1
        Estudiante2_ParcialPsico=9         # Parcial de psicologia, estdudiante 2
        Estudiante2_ParcialLiderazgo=10    # Parcial de Liderazgo, estdudiante 1
         
        def VerNotas():
          return "La estudiante {} presenta las siguientes calificaciones en las materias: \n Materia1: {} \n Nota Laboratorio:{} \n Nota Parcial:{} \n\n Materia2: {} \n Nota Laboratorio: {} \n Nota Parcial: {}".format(Estudiantes.estudiante1,Materia.materia1,Notas.Estudiante1_LabPsico,Notas.Estudiante1_ParcialPsico,Materia.materia2,Notas.Estudiante1_LabLiderazgo,Notas.Estudiante1_ParcialLiderazgo)

MostrarNotas = Notas()
print(Notas.VerNotas())