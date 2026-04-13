---
fach: Mathematik
thema: Differenzialrechnung
tags: [analysis, differenzialrechnung]
datum: 2024-04-18
typ: notiz
---
	
**Wiederholung**

Ein Produkt ist genau dann 0 wenn min. einer der Faktoren 0 ist.
$F(x)=ax²+bx+c$
$F(x)=(x+2)(x-3)$

**Fall 1**
$0 = x_{n}+2$ 
$x_{n} = -2$

**Fall 2**
$0 = x_{n}-3$ 
$x_{n} = 3$
Bsp.: 
$0 = (x-\frac{3}{2})(x+1)$
$x_{n_{1}}=\frac{3}{2}$
$x_{n_{2}}=-1$

$h(x) = x (x+2)(x-2)$
$\lim_{ x \to \pm\infty } f(x) = \pm {\infty}$

Für $\lim_{ x \to +\infty } f(x) = g$ sagt man:
g heißt Grenzwert von f 

![[Differenzialrechnung Verhalten im Unendlichen#Ganz rationale Funktionen]]
![[Differenzialrechnung Verhalten im Unendlichen#e-Funktionen]]

![[Pasted image 20230918114659.png]]
f(x)=-1+x^(2)
f ist im gesamten DB stetig 
(Graph kann gezeichnet werden ohne den Stift abzusetzen)
$\lim_{ x \to 2 } f(x)=4$
Es gibt Funktionen die unbestimmten oder keinen Grenzwert haben
$\lim_{ x \to 0 } = + \infty$
$\lim_{ x \to \infty } = + \infty$
unbestimmter Grenzwert

2 Funktionswerte
$\lim_{ x \to 1 } = 4$
$\lim_{ x \to 1 } = 2$
kein Grenzwert

![[Pasted image 20230918114850.png]]

---
### **Differenzen - und Differentialquotient**

Bsp: Geradlinige gleichmäßig beschleunigte Bewegung
$\frac{\nabla{s}}{\nabla{t}}=v_{durch}$
Ist Anstieg von s
Momentangeschwindigkeit zum Zeitpunkt t1
=> $\nabla t$ wird immer kleiner $(\nabla t\to o)$
=> Sekante -> Tangente

**Differenzenquotient**

$m_{s} = \frac{f\left(x_0+h\right)-f\left(x_0\right)}{h}$

$m = \frac{y_{2}-y_{1}}{x_{2}-x_{1}}=\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}$
Durchschnittliche Steigung

Anstieg der Tangente t an K an der Stelle $x_0$?
$\to$ h strebt gegen 0 ($h\to0$)
$\to$ Punkt s bewegt sich auf $P_{0} zu$
$\to$ Sekante $\to$ Tangente

Differenzialquotient
anstieg der Tangente t
$m_{t} = \lim_{ h \to 0 } \frac{f\left(x_0+h\right)-f\left(x_0\right)}{h} = 2x_{0}$

in Kurz: $f´(x_{0})=2x_{0}$
Anleitung von f an der Stelle $x_{0}$
Anstieg von t an K an der Stelle $x_{0} ≘$ Anstieg von f an der Stelle $x_{0}$
![[Pasted image 20230920080535.png]]
geg $f(x)=x^{2}(x\in \mathbb{R})$
$f´(x_{0)=2x_{0}}$
Ges: $m_{f}$

$x_{0} = 3$          $f´(3)=2*3=6$
$x_{0} = - \frac{5}{2}$       $f´(3)=2*\left( - \frac{5}{2} \right)=-5$

2. An Welcher Stelle $x_{0}$ hat f den Anstieg:
- 1/2 
	$f'(x_{0})=\frac{1}{2}$
	$2x_{0}=\frac{1}{2}$
	$x_{0}=\frac{1}{4}$
- 5/3 | -5/6
- -1 | -1/2

### **Geradengleichung**
#### Gleichung der Tangente t

3. Ermitteln sie eine Gleichung der Tangente $t$ an $K$ im Punkt $(3|f(3))$
fx = x²

$y-y_{0} = m(x-x_{0})$
$x_{0}=3$
$y_{0}=f(3)$ = 9
$m = f'(3) = 6$
$y-9=6(x-3)$
$y=6x-9$

$t$ an $K$ im Punkt (-1/2 | f(-1/2))
$y-y_{0} = m(x-x_{0})$
$x_{0}=-\frac{1}{2}$
$y_{0}=f\left( -\frac{1}{2} \right)=0.25$
$m = f'\left( -\frac{1}{2} \right) = 1$
$y-0.25=-1x -0.5$
$y=-x-0.25$


$t_{2}$ an $K$ im Punkt (-3/4 | f(-3/4))
$y-y_{0} = m(x-x_{0})$
$x_{0}=-\frac{3}{4}$
$y_{0}=f\left( -\frac{3}{4} \right)=\frac{9}{16}$
$m = f'\left( -\frac{3}{4} \right) = -1.5$
$y-\frac{9}{16}=-1.5\left(x + \frac{3}{4} \right)$
$y=-1.5x-\frac{9}{16}$

$y=-\frac{3}{2}x-\frac{9}{16}$

4. Ermitteln sie eine Gleichung der Sekante $s$ die $K$ in den Punkten $(1|f(1))$ und $(2|f(2))$ schneidet.

(1|1)
(2|2)

$m_{s}= \frac{y_{2}-y_{1}}{x_{2}-x_{1}}$
$m=\frac{4-1}{2-1}=\frac{1-4}{1-2}=3$

$y-4=3(x-2)$
$y=3x-2$

5. Bestimmen sie eine Gleichung der Tangente an $K$, die parallel zu $s$ verläuft.
1.5|2.25
$3=f'(x_{0})$
$3=2x_{0}$
$x_{0}=1.5$

$y-2.25=3*\left( x-\frac{3}{2} \right)$

$y=3x-2.25$

6. Bestimmen Sie den **Winkel, den t mit der x-Achse einschließt**
$\tan^{-1} 3 = 71.57$ 

y=-2x-5
 = -2
 = -63.4°
 = 116.6°
### Übung Nachhilfe
![[Pasted image 20230928180741.png]]
![[Pasted image 20230928185249.png]]
![[Pasted image 20230928190024.png]]
![[Pasted image 20230928190657.png]]
![[Pasted image 20230928191319.png]]

### Normale an den Graphen einer Funktion
![[Pasted image 20231016113153.png]]

$f(x)=\frac{3}{2}x²-1$
$f'(x)=3x$
Punkt (1|f(1)) = (1|0.5)
$x_{0}=1$
$y_{0}=f(1)=.5$
$m_{t}=f'(1)=3$

t: $y-y_{0}=m_{t}(x-x_{0})$
$y-.5=3(x-1)$
$y=3x-\frac{5}{2}$

n:
$y-y_{0}=m_{n}(x-x_{0})$
$y-.5=-\frac{1}{3}(x-1)$
$y=-\frac{1}{3}x+\frac{5}{6}$

Punkt (-1/2|f(-1/2)) = (-0.5|−0.625)
$x_{0}=-0.5$
$y_{0}=f(1)=−0.625$
$m_{t}=f'(1)=-1.5$

t: $y-y_{0}=m_{t}(x-x_{0})$
$y-(−0.625)=-1.5\left( x-\left( -\frac{1}{2} \right) \right)$
$y=-\frac{3}{2}x-\frac{1}{8}$

n:
$y-y_{0}=m_{n}(x-x_{0})$
$y-(−0.625)=-\frac{1}{3}(x-1)$
$y=\frac{2}{3}x-\frac{7}{24}$

Punkt (0|f(0)) = (0|-1)
$x_{0}=-0$
$y_{0}=f(0)=−1$
$m_{t}=0$

mn = x=0

Steigung der Tangente im Punkt P(x0|y0) entspricht Grenzwert des Sekantenanstieg und ist die erste Ableitung an der Stelle x0.
![[Pasted image 20231106112415.png]]
Ableitungsregeln Tafelwerk S. 34

h(t)=-2t²+16t | Regeln
h(t)=-4t+16

$s(t)=40t-4t²$
b)5s
c)20m/s
$s'(t)=40-8t$
d)40m/s

![[Pasted image 20231108074921.png]]
$2\sqrt{ x¹ }=x^{\frac{1}{2}}$
$3\sqrt{ x¹ }=x^{\frac{1}{3}}$
$\frac{1}{x}=x^{-1}$

$9x^5+2x^4+10x^2+8x$
$45x^4+8x^3+20x+8$
c)
d) $-12x^2+2x$
e) -4x+3
f)$3x^2-1$

2.
a)$8x^3-3$
b)$-2x+\frac{2}{3}x$
c)$-1x^2+1.2x+1$
d)$-3.6$
e)$5.2x$
f)$-3.6x^2+0.8x+0.3$


4.
a)$2x+\frac{1}{2\sqrt{ x }}$
d) $6x+\frac{2}{3}x^{-\frac{1}{3}}$
d) $6x+\frac{2}{3\sqrt{x  }}$ (3. Wurzel)
b)$-\frac{3}{x²}+\frac{1}{\sqrt{ x }}$
![[Pasted image 20231113115305.png]]
$f'(x)=-x+3$
x=3
y=4.5

y,x=4
t(x)=-1x+8

P4|4
P8|0
Leiter = 5.656854249 = √((8−4)²+(0−4)²)
### Extrempunkte
![[Pasted image 20231113121429.png]]
lokales relatives Max/Minimum

$f(x)=\frac{1}{3}x³-x²-3x+2$
Notewendige Bedingung: $f'(x)=0$

$f'(x)=x²-2x-3$
Pq formel
x1 = 3 Tiefpunkt
x2 = -1 Hochpunkt

f'(-2) = 5 
f'(1)   = -4
von positiven zu negativen Steigung der Tangente 
$g'(x)=2 x-5$
$h'(x)=((3)/(9)) x^2-3$
$g(x)=x^3-4 x$

![[Pasted image 20231115081415.png]]

2x/5
3/9x2 

$1 / 3 x³ + 1 / 2 x² - 3x$
![[Pasted image 20231204113311.png]]
![[Pasted image 20231204113236.png]]
![[Pasted image 20231204113252.png]]

6x²-12x

x⁵-x²

Die Kurvendiskussion einer Funktion

Schrittfolge einer Kurvendiskussion
1) Definitionsbereich  (D)
2) Verhalten an den Rändern des Definitionsbereichs (D)
3) Shnitctpunkt mit dem Koordinatenachsen
4) Extrempunkte
5) Wendepunkte
6) Monotonie
7) Symmetrie
8) Wertebereich (W)
9) Graph der Funktion
$f(x)=x⁴-2x²-6$
$f'(x)=4x^3-4x$
$f''(x)=12x^2-4$
$f(x)=x⁴-2x²-6$
1) D= Reelle Zahlen
2) lim $x⁴-2x²-6 - + unendlich$
3) Nullstellen 
4) F'(x) 0 setzen und ausrechnen mit z=x² 
5) 
6) kä

g(x)=x³-6 x²+9 x
g'(x)=3x²-12x+9 | :3
g(x)=x²-4x

g(x)=6x-12

      u     v
f(x)=e^x(x²-2x)
u'        v      +   u   v'
e^x(x²-2x) + e^x(2x-2)
e^x(x²-2x+2x-2)
e^x(x²-2)
0=e^x(x²-2)
Extrempunkte: +- sqrt(2)

+1.41 -3.41
-1.41  1.17

WP:
1+- sqrt(3) = 
2.732050808 1
0.73 -3


1. 
a)
$0=(1-x)e^x$
$x=1$
y-2/e=1e⁻¹(x+1) 
y=1/ex+3/e 

WP: -1 | 2e⁻¹/2/e

f'(x)=e^x*(-1)+e^x*(1-x)
f'(x)=-xe^x

1e⁻¹


![[Pasted image 20240212113902.png]]


2|6
f'(2)=4
f(x)=ax²+bx+c
f'(x)=2ax+b
f(2)=4a+2b=6
f'(2)=4a+b=4

4a+2b=6
4a+b=4 |* -1
-4a-b=-4
b=2
a=0.5


0|4
-3|0
3|0
Abstand = 5
Umfang = 16

Extremum 0.5 | 1.25

s r: 0 | 1
orthogonale von y=4 am Extremum | y des Extrempunkts bestimmen und -4
2.75
Winkel?

5.
a = -1/4
d = 4
e = 2
$ax⁴+bx²+c$
$2=ax⁴+bx²+c$

$f(x)=ax³+bx²+cx+3$
$2a+1b+3$
b=1 a=-1 c=5


16a+8b+4c+8 = 0
32a+12b+4c+4=0
48a+12b+2c  = 0

$f(x)=ax³+bx²+cx$
$f'(x)=3ax²+2bx+c$
$f''(x)=6ax+2b$


$f(-2)=8a+4b-2c+d=6$
f'(-4)=48a-8b+c=0
f''(x)=-12a+2b = 0 
f'(-2)=12a-4b+c = -12 

a = 1
b = 6
c = 0
z = -26

$f(x)=ax³+bx²+cx + d$
$f'(x)=3ax²+2bx+c$
f(-1)=-a+b-c+d=-2
f(0)= d = -6
f(-2)=-8a+4b-2c+d = 0
f'(-2)=-4b+c = -30

1 
-a+b-c=4
-8a+4b-2c=6
12a-4b+c      +
4a-c=6
8a-3c=16
-c=4
c=-4
a=0.5
b=0.5


$f(x)=ax³+bx²+cx + d$
$f'(x)=3ax²+2bx+c$
$f''(x)=6ax+2b$
f''(2)=12a+2b=0


mn=1/2 negatives reziproke 
mE= -2
f'(2)=12a+4b+c=-2
f'(3)=27a+6b+c= 0
f(3)=27a+9b+3c+d=2

1
f'(2)=12a+4b+c=-2
f'(3)=27a+6b+c= 0 +
15a+2b=2
12a+2b=0
a= 2/3
b=-4
c=6
d=2

$f(x)=ax⁵+bx³+cx$
$f'(x)=5ax⁴+3bx²+c$
$f''(x)=20ax³+6bx$
f(1)=a+b+c=1
f''(1)=20a+6b=0
f'(1)=5a+3b+c=9



1.4
2.8571429%
b)ab 12  ab 15

y 475
x 1-7

steig

d)
t = y + 350 als 6h später

1.
![[Pasted image 20240318095156.png]]
2.![[Pasted image 20240318100543.png]]
100m Zaun um 200m erweitert werden maximaler Flächeninhalt


$f(x) = 4a²-6a*3x²-12x$
$f'(x) = 6x-12=0$
$x=2$
$f(2)=4a²-6a-12$

$f(a)=8a-6=0$
$a=\frac{6}{8}=\frac{3}{4}$
