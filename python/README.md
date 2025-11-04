<h1>Python un buen comienzo</h1>
<h3>Como es bien conocido python es un gran lenguaje para empezar es practico, sencillo y con muchisimo contenido que esta constantemente usado en este lenguaje</h3>

Si bien quiero enseñar un poco de los lenguajes de programación es dificil empezar en esto, lo se porque yo lo viví en la universidad pero...
no es algo de predecir el siguiente paso es mas de la <b>Constancia</b> la cual te va a permitir poco a poco saber como programar ya que este mundo
es bastante grande y tiene muchas ramificaciones puedes ser back-end front-end full-stack, programar IA, Automatización o ciberseguridad, son muchas areas!
pero eso ya es elección de cada quien escoger en que enfocarce al momento de aprender a programar

Para ello tengo que comenzar con codigos sencillos que logren permitirles enteder un poco el concepto de una función por que algunas funciones
llegan a tener algunas caracteristicas que lo hacen mas util comforme a otra, así que comencemos con el entorno para hacerlo

<h1>
  VS CODE y Python
</h1>
Uff Visual Studio Code donde empece a programar y pronto ustedes si es que lo quieren usar, tambien existen otras alternativas como JetBrains Atom incluso Bloc de notas si eres muy habilidoso jajaja.
pero con VS esta bien es multiproposito, customizable y muy conocido hecho por Microsoft https://code.visualstudio.com --> Este es el link para poder instalarlo dentro de el usaremos las recomendaciones
de instalacion si quieres usar alguna distinta adelante. y dentro de la misma sigue el Get Started para hacerlo a tu gusto despues te vas a la izquierda en extensiones son 4 cuadrados con uno volteado,
tienes que buscar phyton por Microsoft y lo instalas, luego en tu navegador buscas python y en el boton amarillo le das clic para instalar, puedes instalar con las recomendaciones pero es mejor
dar en la casilla de PATH y Administrador, para no tener problemas con eso listo podemos empezar a hacer codigo.

<h1>
  Mi primer !hola mundo¡
</h1>
Es muy comun esto el usar como primera base, tenemos que aprender algunas bases si queremos hacer algo funcional o aprender como funcionan ciertas cosas como los frameworks o algunos programas, entonces si queremos llegar a tener un poco de conocmiento como poder desarrollar una calculadora basica tenemos que hacernos algunas preguntas para responder esto en este caso ¿Cuales son los componentes que conforman una calculadora? el primero sería una pantalla donde podemos ver lo que ingresamos y el resultado.
Entonces tenemos el principal requisito, proyectar lo que vemos.

Para eso tenemos el "print()" esta función sirve para imprimir en pantalla lo que queremos hacer para ello puede ver el codigo de python "01_Primer_Print.py"
como recomendación deberías de hacer algunas practicas como imprimir tu nombre realizar una suma, división, variable y tu nombre o algun dato. para poder reproducir el codigo usa:
<img width="170" height="33" alt="{9F15A276-439F-4317-8D2E-498A5C5B60D1}" src="https://github.com/user-attachments/assets/53d14d58-99ca-41af-8e49-2181f7937656" /> 
El boton de play sirve para correr codigo en la terminal se encuentra posicionado en la parte superior del archivo de python pero como creamos un archivo python facil:
<img width="2557" height="1119" alt="{CED31962-1291-49AA-A6F3-82D9B2AD598D}" src="https://github.com/user-attachments/assets/0e5005ec-7d25-4d1d-afb5-789974de5284" />
Tenemos una GUI con distintas cosas para usar usaremos el explorador <img width="49" height="52" alt="{3B487FAE-CEC5-4961-ADD4-A22C560281D4}" src="https://github.com/user-attachments/assets/5f063a19-1330-46c0-a0db-6c6d3b5967dd" /> y usaremos File > Open Folder y escogeremos el folder que deseamos usar para guardar nuestros codigos siempre evitando usar caracteres especiales o espacios en los folders y archivos
Tenemos que crear nuestro primer archivo dentro del explorer en el texto con el nombre de la carpeta donde guardaremos nuestros proyectos le daremos clic a:
<img width="294" height="28" alt="{DF8187C0-428D-45FA-9A8F-8633A74C8DD8}" src="https://github.com/user-attachments/assets/9150cb49-483a-4545-9a81-764758f3c434" />
El documento justo se creara un cuadro de texto donde colocaremos "NombreDelArchivo".py esto creara un archivo .py que es un archivo python el cual podremos usar para crear nuestro software.

<h1>
  Mi primer saludo!
</h1>
Ahora viene algo interesante, la calculadora no solo muestra el resultado, si no, también logra guardar los datos de entrada, entonces ¿Como capturamos información y los guardamos en python? facíl.
Primero tienes que conocer 2 cosas.
<h3>
  Variables y Constantes
</h3>
Estos datos son muy importantes, son objetos que permiten almacenar un valor dentro de las mismas las <b>Variables</b> guardan datos que cambian constantemente y las <b>Constantes</b> almacenan un valor que permanece igual a lo largo del tiempo. Dentro de ambas existen distintas maneras de almacenarce de momento solo seran 5: Int, float, char, string, boolean.
Este tipo de "etiqueta" permite guardar datos dentro de el programa que sean especificos si quieres que solo se ocupen enteros, caracteres, verdadero o falso, etc.
<h3>
  input()
</h3>
Muy bien esta <b>Función</b> permite "capturar" un dato de entrada en si misma, para despues guardarla en una variable, puede usar distintas cosas pero en este caso sera la entrada del teclado, aunque se puede usar tambien para obtener ciertas cosas como la posición de tu raton.
Las funciones son importantes permiten realizar diversas operaciones dentro de una sola palabra por ejemplo input la cual puede ser modificada o usada dentro de otra función como print ejemplo claro sería:
print(input())
Que es una impresion de la entrada del input
Para poder tener alguna idea que se puede hacer para la calculadora descargue "02_Primer_Input.py"
<h3>
  Primer sumador
</h3>
Felicidades ahora tienes los conocimientos basicos para hacer una función desde la terminal de VScode asi que comencemos primero con ciertas cosas que uno requiere tener al momento de hacer algun codigo existen algo llamado buenas practicas esto se refiere a la manera de documentar el código y la estructura del mismo, si bien, uno puede hacer el programa como uno le guste es verdad que si debe de llevar un formato para evitar problemas al modificar el codigo o saber que hace cada parte para poder saber que se tiene que modificar en especifico asi que cuales son esa practicas que nesecitamos bueno son las siguientes:

1.- Las variables deben de tener un nombre simple y sin una estructura dificil de entender, un ejemplo sería declarar una variable como la gravedad de la tierra, donde g = 9.81 mt/s2, entonces podemos nombrar nuestra variable como "g" o "gravedad" en casos donde se utilicen muchas variables podemos usar tecnicas de como declarar las variables en este caso a mi me gusta hacerlo en PascalCase pero existe camelCase o Snake_Case y muchas otras pero cada quien escoge la que uno quiere
2.- Añadir comentarios para añadir comentarios muchos lenguajes utilizan las // o # para declara que esa linea no debe de tomarse encuenta al ejecutar el código. En estos comentarios siempre se añaden al principio para declarar el autor del código y en ciertas partes para describir el como funcionan las funciones dentro del programa así como su nombre lo dice comentarios hacerca de ciertas lineas que requieren atención.
3.- Jerarquía del código, si bien estamos programando en el segundo lenguaje mas facil de aprender en todos los lenguajes uno requiere llevar la jerarquia del código la cual en especifico son la manera en la cual se agrupa el codigo la cual es la siguiente
Comentario Principal -> Importaciones -> Constantes y Variables -> Funcion Principal -> Funcion Secundaria
*Las importaciones y exportaciones se veran mas adelante.

Ahora como se hace una suma bueno si viste lo anterior podemos hacerlo como función o directamente insertar casi todo en un print, pero en este caso empezaremos suave para despues avanzar a algo mas dificil como las condicionales y loops. para ver como se hace la suma checa 03_Primer_Funcion

<h3>
  Estructuras de control
</h3>

Muy bien toca pasar a la mayor parte de codigo que se encuentra en todos lados, Las estructuras de control las cuales tienen distintos operadores como if,for,while,switch,case,etc.
Pero en este caso comenzaremos con el if es una funcion la cual ejecuta ciertas lineas bajo una condicion. su estructura es la siguiente
if(condicion)
{
Funcion
}
Esto nos permitira hacer un selector mas adelante sera recomendable el uso de switch

Ahora para las repetitivas son aquellas que estan en bucle como lo son el while o for los cuales tienen distintas condiciones como while se ejecutara constantemente hasta que x condicion deje de ser cierta este seguira ejecutandoce igual con el for sin embargo este tiene "Un Tiempo de vida" que es mas o menos decir que se repite ciertas veces y despues se detiene.

<h3>
  Condicionales
</h3>
Esto lo explico rapido son "<" mayor que y ">" menorque tambien existen menor o igual y mayor o igual que solo se añade el "=" y para el igual "==" y el distinto que "!=", existen otras pero estas son las que estaremos usando para este caso de la calculadora

<h3>
  Calculadora
</h3>
Si bien todo esto nos permite crear una calculadora esta claculadora es basica a difencia de la calculadora de tu computadora esta nunca la usarias tenemos que seguir avanzando y crear una aplicación
Para ver la primer calculadora es 04_Test_Calculadora
