<h1>🐍 Python: un buen comienzo</h1>

Python es, sin duda, uno de los mejores lenguajes para empezar a programar.
Es práctico, sencillo y tiene una enorme comunidad con toneladas de contenido que puedes consultar cuando te atoras en algo.

Yo sé que empezar en el mundo de la programación no es fácil.
Cuando comencé en la universidad, también me costó entender por dónde arrancar. Pero con el tiempo entendí que aprender a programar no se trata de adivinar el siguiente paso, sino de tener constancia.
Poco a poco vas entendiendo cómo pensar en código, y eso es lo que realmente importa.

La programación es un universo enorme: puedes ser backend, frontend, full-stack, desarrollar IA, automatización o ciberseguridad.
Son muchas áreas, y cada persona decide hacia dónde quiere enfocar su camino.
Pero para llegar ahí, primero hay que entender las bases.

Y por eso empezamos aquí, con Python.

<h2>💻 Preparando el entorno</h2>

Vamos a trabajar con Visual Studio Code (VS Code), que fue el primer entorno donde empecé a programar (y el que más recomiendo).
Es versátil, liviano, fácil de personalizar y muy conocido.
Puedes descargarlo desde 👉 https://code.visualstudio.com

Una vez instalado, abre la pestaña de extensiones (el ícono de cuatro cuadritos) y busca “Python” por Microsoft. Instálala.
Luego, ve al sitio oficial de Python 👉 https://www.python.org

Descarga la versión más reciente, marca las casillas “Add to PATH” y “Run as administrator”, e instálalo normalmente.
Con eso ya tendrás todo listo para escribir tu primer código.

<h2>👋 Mi primer “¡Hola Mundo!”</h2>

El clásico de los clásicos.
Antes de hacer proyectos más grandes, hay que entender las bases.
Para esto usaremos la función print(), que nos permite mostrar texto o resultados en pantalla.

Puedes ver un ejemplo en el archivo 01_Primer_Print.py.

Te recomiendo practicar cosas simples:

Imprimir tu nombre.

Hacer operaciones básicas (suma, división).

Probar con variables.

Para ejecutar tu código en VS Code, abre el archivo .py y presiona el botón de ▶ (Play) en la parte superior.
Así verás los resultados directamente en la terminal.

<h2>🗣️ Mi primer saludo</h2>

Una calculadora no solo muestra el resultado, también recibe datos.
Y para eso necesitamos aprender a capturar información.

🔹 Variables y constantes

Son los contenedores de datos de nuestro programa.

Variables: guardan valores que cambian.

Constantes: guardan valores fijos.

Los tipos más comunes son:
int, float, char, string, y boolean.

🔹 input()

La función input() nos permite recibir datos del teclado.
Por ejemplo:

<pre>
    ```python
    print(input("Escribe tu nombre: "))
    ```
</pre>
    
Esto mostrará lo que el usuario escriba.
Puedes ver un ejemplo en 02_Primer_Input.py.

<h2>➕ Mi primer sumador</h2>

Ahora que ya conoces las bases, es momento de crear nuestra primera función simple.
Pero antes, hablemos de algo muy importante: las buenas prácticas.

Nombres claros: usa nombres simples y descriptivos para tus variables.

<pre>
    Ejemplo: gravedad = 9.81
</pre>
    
Comentarios: usa # para anotar ideas, explicaciones o recordatorios.

Estructura: sigue un orden lógico en tu código:

Comentarios principales

Importaciones

Constantes y variables

Función principal

Funciones secundarias

Con eso en mente, revisa el archivo 03_Primer_Funcion.py, donde aprenderás cómo realizar una suma básica paso a paso.

<h2>🔄 Estructuras de control</h2>

Aquí empieza lo divertido: las estructuras de control, que son la base de toda lógica en programación.

Condicionales (if) → ejecutan algo solo si se cumple una condición.

Bucles (for, while) → repiten una acción hasta que se cumpla cierta regla.

Ejemplo:

<pre>
    ```python
    if x > 0:
        print("El número es positivo")
    ```
</pre>


Y los operadores más comunes son:
<, >, <=, >=, ==, !=

Puedes encontrar ejemplos en los siguientes archivos para practicar.

<h2>🧮 Mi primera calculadora</h2>

Con todo lo anterior ya tienes lo necesario para crear tu primera calculadora básica.
No será tan avanzada como la del sistema operativo, pero es el primer paso para entender cómo funcionan los programas reales.

Dale un vistazo al archivo 04_Test_Calculadora.py, donde juntamos todo lo aprendido: entrada de datos, operaciones y salida de resultados.

<h2>🚀 Conclusión</h2>

Y así comenzamos este viaje con Python.
No te preocupes si algo se te complica al principio; todos pasamos por eso.
La clave es practicar, equivocarte y volver a intentarlo.
Con el tiempo, el código deja de parecer extraño y empieza a tener sentido.

¡Sigue adelante, y recuerda que cada línea escrita te acerca a ser mejor programador! 💪
