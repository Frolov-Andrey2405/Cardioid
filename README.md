# Cardioid

In geometry, a cardioid is a plane curve traced by a point on the perimeter of a circle that is rolling around a fixed circle of the same radius. It can also be defined as an epicycloid having a single cusp. It is also a type of sinusoidal spiral, and an inverse curve of the parabola with the focus as the center of inversion. A cardioid can also be defined as the set of points of reflections of a fixed point on a circle through all tangents to the circle.

## Cardioid as Envelope of a Pencil of Lines

![Cardioid as envelope of a pencil of lines](https://upload.wikimedia.org/wikipedia/commons/9/97/Kardioide-sehnen.svg)

**Cardioid as envelope of a pencil of lines**

A similar and simple method to draw a cardioid uses a pencil of lines. It is due to L. Cremona:

1. Draw a circle, divide its perimeter into equally spaced parts with $2N$ points (see the picture) and number them consecutively.
2. Draw the chords: $(1,2),(2,4),\dots ,(n,2n),\dots ,(N,2N),(N+1,2),(N+2,4),\dots $ (That is, the second point is moved by double velocity.)
3. The envelope of these chords is a cardioid.

### Proof

![Cremona's generation of a cardioid](https://upload.wikimedia.org/wikipedia/commons/6/6b/Cycloid-cremona-pr.svg)

**Cremona's generation of a cardioid**

The following consideration uses trigonometric formulae for $\cos \alpha + \cos \beta$, $\sin \alpha + \sin \beta$, $1 + \cos 2\alpha$, $\cos 2\alpha$, and $\sin 2\alpha$. In order to keep the calculations simple, the proof is given for the cardioid with polar representation $r = 2(1 + \cos \phi)$.

### Equation of the Tangent of the Cardioid with Polar Representation $r = 2(1 + \cos \phi)$

From the parametric representation:

$$
\begin{align*}
x(\phi) &= 2(1 + \cos \phi)\cos \phi, \\
y(\phi) &= 2(1 + \cos \phi)\sin \phi
\end{align*}
$$

one gets the normal vector $\vec{n} = \left(\dot{y}, -\dot{x}\right)^{\mathsf{T}}$. The equation of the tangent $\dot{y}(\phi)\cdot(x - x(\phi)) - \dot{x}(\phi)\cdot(y - y(\phi)) = 0$ is:

$$
(\cos 2\phi + \cos \phi)\cdot x + (\sin 2\phi + \sin \phi)\cdot y = 2(1 + \cos \phi)^2.
$$

With help of trigonometric formulae and subsequent division by $\cos \frac{1}{2}\phi$, the equation of the tangent can be rewritten as:

$$
\cos\left(\frac{3}{2}\phi\right)\cdot x + \sin\left(\frac{3}{2}\phi\right)\cdot y = 4\left(\cos \frac{1}{2}\phi\right)^3 \quad 0 < \phi < 2\pi, \phi \neq \pi.
$$

### Equation of the Chord of the Circle with Midpoint $(1, 0)$ and Radius $3$

For the equation of the secant line passing through the two points $\left(1 + 3\cos \theta, 3\sin \theta\right)$, $\left(1 + 3\cos 2\theta, 3\sin 2\theta\right)$ one gets:

$$
(\sin \theta - \sin 2\theta)x + (\cos 2\theta - \sin \theta)y = -2\cos \theta - \sin(2\theta).
$$

With help of trigonometric formulae and subsequent division by $\sin \frac{1}{2}\theta$, the equation of the secant line can be rewritten by:

$$
\cos\left(\frac{3}{2}\theta\right)\cdot x + \sin\left(\frac{3}{2}\theta\right)\cdot y = 4\left(\cos \frac{1}{2}\theta\right)^3 \quad 0 < \theta < 2\pi.
$$

## Python Implementation

The `main.py` script implements the generation of a cardioid using the pencil segment method.

### Functionality

- The code utilizes the Pygame library for graphics.
- It defines classes for Drawable objects and the Cardioid itself, along with an application class to manage the game loop.
- The Cardioid class implements the pencil segment method to draw the cardioid curve on the screen.
- The App class initializes the Pygame window and manages the game loop.

### How to Run

1.  Install the required libraries using pip:
```
pip install -r requirements.txt
```
2. Run the `main.py` file:
```
python main.py
```
3. The Pygame window will open, displaying the animated cardioid curve.
