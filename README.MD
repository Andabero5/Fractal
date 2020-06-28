# **Programa graficador de fractales**

- [**Integrantes**](#integrantes)
- [**Turtle**](#turtle)
- [**L-Systems**](#l-systems)
- [**Main**](#main)
- [**Ejemplos**](#ejemplos)

## **Integrantes**

- Laura Catalina Torres Gallego: 20182020056
- Andrés David Beltran Rojas: 20182020090
- Josué Daniel Rodríguez Siatama: 20191020109
- Kenner Alejandro Buitrago Castillo: 20191020095
- Steffany Johana Rojas Comas: 20181020002
- Sebastian David Peñuela Guerrero: 20191020081

## **Turtle**

Se hizo uso del módulo turtle para la graficación de los fractales debido a que permite graficar con instrucciones como lo son el moverse hacia adelante y girar en cierto angulo a cada lado.

```python
import turtle
```

## **L-Systems**

Bajo el principio de L-Systems funciona **_logic_** definiendo a:

- **_alphabet_** como el conjunto de símbolos que el logica va a utilizar.
  - 'F': Mover hacia adelante (del inglés Fowards).
  - '+': Girar a la derecha.
  - '-': Girar a la izquierda.

```python
    def drawLogic(t, instructions, angle, distance):
    for i in instructions:
        if i == 'F':
            t.forward(distance)
        elif i == '+':
            t.right(angle)
        elif i == '-':
            t.left(angle)
```

- **_axiom_** como la cadena original que se utiliza en la generación.
- **_rules_** que indica como debe ser reemplazado cada uno de los símbolos en la siguiente iteración.

> para conocer mas del principio de L-Systems de click [aquí](https://www.youtube.com/watch?v=f6ra024-ASY&feature=emb_title)

## **Main**

La funcion main es la que recibe todos los parametros, tanto axiomas como tamaños de le ventana grosor de trasado entre otros.

```python
def main(iterations, axiom, rules, angle, length=10, size=1, y_offset=0,
         x_offset=0, offset_angle=0, width=500, height=500)
```

lo primero que se hara es cargar nuestros axiomas, reglas y numero de iteraciones al metodo **_logic_**.

```python
inst = logic(iterations, axiom, rules)
```

posteriormente se creara la _ventana_ y el _"lapiz"_ proporcionandoles el tamaño.

```python

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(10)
    t.pensize(size)
```

ya definida nuestra _ventana_ y _lapiz_ se pasan lo parametros al metodo **_drawLogic_** que interpretara el axioma, las reglas y guiara el trazado de la linea en pantalla

```python
drawLogic(t, inst, angle, length)
```

```python
def drawLogic(t, instructions, angle, distance):
    for i in instructions:
        if i == 'F':
            t.forward(distance)
        elif i == '+':
            t.right(angle)
        elif i == '-':
            t.left(angle)
```

## **Ejemplos**

Estos con algunos ejemplos que se pueden introducir al metodo **_main_**.

```python
axiom = "F+F+F+F"
rules = {"F":"F-F+F+FFF-F-F+F"}
iterations = 2
angle = 90
```

![fractal 1](fractal1.PNG)

```python
axiom = "F+F+F+F"
rules = {"F":"FF+F++F+F"}
iterations = 2
angle = 90
```

![fractal 1](fractal2.PNG)

```python
axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 2
angle = 60
```

![fractal 1](fractal3.PNG)
