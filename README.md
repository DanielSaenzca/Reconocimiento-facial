# Reconocimiento-facial




Proceso de entrenamiento y realización de la red neuronal y sus problemas


Al instalar tensorflow  como queria usar el entorno queras con visual studio code hubo problemas porque para hacer eso tenia que usar anaconda y resulta que da problemas instalar tensor flow si el nombre de tu carpeta tiene espacios y como mi nombre de usuario en la computadora es Daniel Saenz tiene espacio, despues de un buen rato encontré la solución en stackoverflow y era modificar la carpeta activation.bat para que no ocurriera este error, primero no sabia como modificar un archivo .bat, luego ya descubrí que era clic derecho editar, y luego no tenía permisos de directamente modificar ese archivo lo que hice fue copiarlo en escritorio, modificarlo ahi y despues remplazarlo en la carpeta del sistema.
Para cargar los datos me daba error porque al parecer tenia que poner una r antes del directorio y con eso funcionó, aunque igual fue un error entrenar con una cantidad desproporcionada de imagenes de entrenamiento y prueba.

Hubo demasiados errores durante las pruebas, que me falto alguna coma, que cargue mal la base de datos, entre otras.
A continuación describiré algunos de ellos:
Para la carga de datos, los problemas iniciaron al intalar tensorflow, como yo estoy acostumbrado a trabajar con visual studio code busque como utilizar tensorflow con dicho editor de código el error que me encontré fue que debido a que mi nombre de usuario "Daniel Saenz" tiene un espacio pues anaconda no funcionaba correctamente por lo que busque el error que me daba, y encontré que la solución era modificando un archivo .bat en la instalación de anaconda, aprendí como editar un archivo .bat, y luego no me permitía guardar los cambios directamente en la carpeta de instalación por lo que tuve que hacer una copia de ese archivo .bat modificarlo en el escritorio, y copiar y remplazarlo en la carpeta de instalación.


Luego me dio el error OMP:Error #15 desconozco por que se haya dado, será una cosa de visual studio, pero se resolvió agregando import os  os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
Para la carga de datos instente usar el archivo .csv pero tuve muchos errores hasta que finalmente segui paso a paso la modificación del archivo list_attr_celeba.txt y por fin funcionó.


Igualmente tuve problemas para que encontrara los path de los archivos asi que finalmente puse todo en una sola carpeta y el path fue el mismo que en el ejemplo img_align_celeba/img_align_celeba/ en este caso intenté ponerlo como D:\Tensor-flow\img_align_celeba\img_align_celeba o formas parecidas pero siempre daba algun tipo de error.


Otro problema fue configurar la computadora para que usara la GPU en vez del CPU, esto debido a que mientras hacía el entrenamiento con la base de Datos CelebA observé que avanzaba muy lento, entré al administrador de Tareas y vi que el uso del CPU estaba al 100% y la GPU dedicada, que es una GTX 1650, no se estaba usando, por lo que seguí los pasos del pdf del grupo de Teams para usar la GPU con visual Studio, sin embargo tuve un problema que no encontraba un archivo .dll entonces busqué la solución y era algo relacionado al path y lo unico que debia de hacerse era copiar ese archivo .dll en las carpetas de System32 y SysWOW64.


Luego de esto se aprovechó la GPU y el entrenamiento fue mas rapido, sin embargo se tardó aproximadamente 2 hora por epoca, en este caso entrené solo 2 épocas al principio, y me dio un error al entrenar la primera ya que no había creado la carpeta "Generated" después de esto todo funcionó bien y pude guardar el entrenamiento y las imágenes generadas.


Posteriormente entrené con 10 épocas y las imagenes generadas estan en la carpeta "Generated10epochs"
Finalmente para hacer la red neuronal que reconociera mi rostro cargue el modelo que se entrenó con la base de datos de CelebA, y me dio un accuracy del 66% con 50 epcohs y un batch_size de 16.
