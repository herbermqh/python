import os
import shutil
import fileinput

directorio="/home/userh/Documents/LaTeX/matematica/problemas-examenes"
os.chdir(directorio)
dir_exam=os.getcwd()

# print("Escriba el nombre del examen")
# nombre_examen_input=input()

nombre_examen_input=[
    "UMSA_MAT__2021_II__psa",
]


for item in nombre_examen_input:

    # nombre_examen_list=nombre_examen_input.split()
    nombre_examen_list=item.split("_")

    materia="MATEMATICA"
    universidad = nombre_examen_list[0]
    exam = nombre_examen_list[1]
    parcial = nombre_examen_list[2]
    ano_examen = nombre_examen_list[3]
    semestre_examen = nombre_examen_list[4]
    fila_examen = nombre_examen_list[5]
    exam_perteneciente = nombre_examen_list[6]

    #nombre del archibo examen
    if fila_examen=="":
        if parcial=="":
            nombre_examen = universidad+"_"+exam+"_"+ano_examen+semestre_examen+"_"+exam_perteneciente
        else:
            nombre_examen = universidad+"_"+exam+"_"+parcial+"_"+ano_examen+semestre_examen+"_"+exam_perteneciente
    else:
        nombre_examen = universidad+"_"+exam+"_"+parcial+"_"+ano_examen+semestre_examen+"_"+fila_examen+"_"+exam_perteneciente

    #funcion para crear directorios, archivos y capetas del examen

    def examen(name_exam):
        #nombres de carpetas

        #directorios
        if parcial=="":
            dir_parent_exam=universidad+"_"+exam+"_"+semestre_examen+"_"+exam_perteneciente
        else:
            dir_parent_exam=universidad+"_"+exam+"_"+parcial+"_"+semestre_examen+"_"+exam_perteneciente
        
        dir_images_ejercicios=dir_parent_exam+"/"+name_exam+"/IMAGES-EJERCICIOS"
        dir_readme_images_ejecicios=dir_exam+"/"+dir_parent_exam+"/"+name_exam+"/IMAGES-EJERCICIOS/README.md"
        dir_ejercicios_plantilla=dir_exam+"/universidad-examen#parcial-añoSemestre/EJERCICIOS.tex"
        dir_ejercicios_crear=dir_exam+"/"+dir_parent_exam+"/"+name_exam
        dir_ejercicios_latexmain=dir_exam+"/"+dir_parent_exam+"/"+name_exam+"/EJERCICIOS.latexmain"
        dir_examen_main_plantilla=dir_exam+"/universidad-examen#parcial-añoSemestre/universidad-examen#parcial-añoSemestre.tex"
        dir_examen_main=dir_exam+"/"+dir_parent_exam+"/"+name_exam+"/"+name_exam+".tex"
        dir_examen_main_latexmain=dir_exam+"/"+dir_parent_exam+"/"+name_exam+"/"+name_exam+".latexmain"
        #crear directorio UNIVERSIDAD-MATERIA-PARCIAL-SEMESTRE-EXAMEN_DISTINTIVO si no exite
        if os.path.exists(dir_parent_exam):
            pass
        else:
            os.makedirs(dir_parent_exam)
        # crea directorio "IMAGES-EJERCICIOS"
        os.makedirs(dir_images_ejercicios)
        # crea archivo README.md en IMAGES-EJERCICIOS 
        readme_md=open(dir_readme_images_ejecicios, "w")
        readme_md.close()
        # crea archivo EJERCICIOS
        shutil.copy(dir_ejercicios_plantilla,dir_ejercicios_crear)
        # crea archivo EJERCICIOS.latexmain
        ejercicios_latexmain=open(dir_ejercicios_latexmain,"w")
        ejercicios_latexmain.close()
        # crea archivo main o EXAMEN
        shutil.copy(dir_examen_main_plantilla,dir_examen_main)
        # crea archivo main.latexmain
        main_latexmain=open(dir_examen_main_latexmain, "w")
        main_latexmain.close()
        #detalles de main
        with fileinput.FileInput(dir_examen_main, inplace=True) as file:
            for line in file:
                print(line.replace("MATERIA",materia), end="") 
        with fileinput.FileInput(dir_examen_main, inplace=True) as file:
            for line in file:
                print(line.replace("SEMESTRE",semestre_examen), end="")
        with fileinput.FileInput(dir_examen_main, inplace=True) as file:
            for line in file:
                print(line.replace("ANO",ano_examen), end="")
        with fileinput.FileInput(dir_examen_main, inplace=True) as file:
            for line in file:
                print(line.replace("FILA",fila_examen), end="")

    examen(nombre_examen)


