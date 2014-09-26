# A Logic of Vector Lattices

Daoud Clarke, University of Sussex

2nd-3rd October, University of Edinburgh



## Overview

 - A new logic
 - Relation to Fuzzy logic



# A New Logic



## What if vector spaces had a logic?



$$\Huge{x \lor y \qquad\qquad x \land y}$$
# <br>
$$\Huge{x \rightarrow y \qquad\qquad \neg x}$$



## Why?



## Combine logical and distributional semantics



## &ldquo;I like Fidel Castro and his beard&rdquo;



## But vector spaces are too boring&hellip;



## We need extra structure



<pre>
end some medicine for her, but she will need fruit and  milk, and some other special things that
our own. Here we give you ideas for foliage, fruit and  various festive trimmings that you can i
part II). However, other strategies can bear fruit  and are described under three sections which
       supper  tomatoes, potato chips, dried fruit and cake. And  they drank water out of tea-cu
erent days, as  the East Berliners queue for fruit and cheap stereos, a Turkish  beggar sleeps i
dening; and  Pests -- how to control them on fruit and vegetables. Both are  produced by the Hen
me,"Silver Queen" is male so will never bear fruit    At the opposite end of the prickliness sca
 lifted away    Like an orange lifted from a fruit-bowl    And darkness, blacker    Than an oil-
ed in your  wreath. Christmas ribbon and wax fruit can be added for colour.  Essentials are scis
e you need to start developing your very own fruit  collection    KEEPING OUT THE COLD    Need e
ly with Jeyes fluid    THE KITCHEN GARDEN    FRUIT    Cut out cankers on fruit trees, except tho
wn and watered    AUTUMN HUES    Foliage and fruit enrich the autumn garden, whether glowing  th
- have forgotten  the maxim: " tel arbre tel fruit ". If I were  willing  to  unstitch the past 
 of three children of Alfred Roger Ackerley, fruit importer  of London, and his mistress, Janett
rful didactic spirit, much that was to  bear fruit in his years as a mature artist. Although thi
e all made with natural vegetable, plant and fruit ingredients  such as chamomile, kukai nut and
ack in the soup.    He re-visits the Copella fruit juice farm in Suffolk, the  business he told 
rategic relationship" with Lotus, the first  fruit of which is a mail gateway between Office and
, choose your plants  carefully to enjoy the fruit of your labour all year round.    PLACES TO V
 and I love chips.  Otherwise I'll nibble on fruit or something to convince myself  that I'm eat
 tone and felt the  softness and warmth of a fruit ripening against a wall? If she  had she migh
ol place to set. Calories per  slice: 395    Fruit Scones with cinnamon Butter    (makes 12)    
ought me water. Another monster gave me some fruit  to eat. A few monsters lay against my body a
ney fungus.    Cut out diseased wood on most fruit trees    VEGETABLES    Continue winter diggin
age and chafing.    Remove old, unproductive fruit trees by cutting them down to  shoulder heigh
ITCHEN GARDEN    FRUIT    Cut out cankers on fruit trees, except those on peaches, plums  and ch
ps  remain, then stir in the sugar and dried fruit. Using a round-  ended knife, stir in the mil
 of a homeland, well others dream too,    De fruit was forbidden an now yu can't chew,    How ca
onnoisseurs. We take a bite from an unusual  fruit. We come away neither nourished nor ravished,
</pre>



## Basis $\Rightarrow$ Structure



$$\Huge{\widehat{\mathit{orange}}\lor \widehat{\mathit{fruit}}}$$
# <br>
$$\Huge{\widehat{\mathit{orange}}\land \widehat{\mathit{fruit}}}$$



<div class="disjunction-title">$\widehat{\mathit{orange}}$</div>
<div class="disjunction"></div>



## Is that it?



## Give up standard propositional calculus



## Look more like a fuzzy logic



## Accept negative values



$$\Huge{{\mathit{orange}}\rightarrow {\mathit{fruit}}}$$
# <br>
$$\Huge{\neg{\mathit{orange}}}$$



## What is truth?



## Assertions assert positivity



$$\large{\mathit{orange}\rightarrow \mathit{fruit}}$$
## <br>
$$\large{\widehat{\mathit{fruit}} - \widehat{\mathit{orange}}} \ge 0$$
## <br>
$$\large{\widehat{\mathit{orange}}} \le \widehat{\mathit{fruit}}$$



$$\Huge{\neg\mathit{orange}}$$
## <br>
$$\Huge{-\widehat{\mathit{orange}}}$$



<div class="disjunction-title">$\widehat{\mathit{orange}}$</div>
<div class="disjunction"></div>



# Riesz Logic



## Modus Ponens
### <br>
$$\huge{\frac{\phi,\ \phi \rightarrow \psi}{\psi}}$$



## RI
### <br>
$$\huge{\frac{\phi \rightarrow \psi}{\phi \lor \chi \rightarrow \psi \lor \chi}}$$



## Axioms

\begin{align}
&\textrm{R1a} && (\phi \rightarrow \psi) \rightarrow ((\psi \rightarrow \chi) \rightarrow (\phi \rightarrow \chi)) \\\\
&\textrm{R1b} && ((\psi \rightarrow \chi) \rightarrow (\phi \rightarrow \chi)) \rightarrow (\phi \rightarrow \psi) \\\\
&\textrm{R2} && \phi \rightarrow \phi \lor \psi\\\\
&\textrm{R3} && \phi \lor \psi \rightarrow \psi \lor \phi\\\\
&\textrm{R4} && (\phi \lor \psi)\lor \psi \rightarrow \phi \lor \psi\\\\
&\textrm{R5a} && 0 \rightarrow (\phi \rightarrow \phi)\\\\
&\textrm{R5b} && (\phi \rightarrow\phi) \rightarrow 0\\\\
&\textrm{R6a} && ((\phi \rightarrow \psi)\lor 0 \rightarrow (\psi \rightarrow \phi) \lor 0) \rightarrow (\psi \rightarrow \phi)\\\\
&\textrm{R6b} &&  (\psi \rightarrow \phi) \rightarrow ((\phi \rightarrow \psi)\lor 0 \rightarrow (\psi \rightarrow \phi) \lor 0)
\end{align}



## Soundness
$\Rightarrow$ Abelian lattice ordered groups



## Completeness
$\Rightarrow$ The Logic of Equilibrium (Galli et al.)



### A Proof

<div style='zoom:0.5;'>
\begin{align}
& (1) && \alpha \rightarrow 0 & \text{(assumption)}\\\\
& (2) && \phi \rightarrow ((\phi \rightarrow \psi) \rightarrow \psi) & \text{(MP, R1b, R1b)}\\\\
& (3) && \phi \lor \psi \rightarrow (\phi \lor \chi) \lor \psi & \text{(RI, R2)}\\\\
& (4) && (\phi \lor \psi) \lor \chi \rightarrow (\psi \lor \phi) \lor \chi & \text{(RI, R3)}\\\\
& (5) && (\phi \lor \psi \rightarrow \chi) \rightarrow (\psi \lor \phi \rightarrow \chi) & \text{(MP, R3, R1a)}\\\\
& (6) && (\phi \lor \psi \rightarrow \chi) \rightarrow ((\phi \lor \psi) \lor \psi \rightarrow \chi) & \text{(MP, R4, R1a)}\\\\
& (7) && 0 & \text{(MP, R3, R5b)}\\\\
& (8) && ((\phi \rightarrow \psi) \rightarrow \chi) \rightarrow (((\psi \rightarrow \phi) \lor 0 \rightarrow (\phi \rightarrow \psi) \lor 0) \rightarrow \chi) & \text{(MP, R6a, R1a)}\\\\
& (9) && \alpha \lor \phi \rightarrow 0 \lor \phi & \text{(RI, 1)}\\\\
& (10) && (0 \rightarrow \phi) \rightarrow \phi & \text{(MP, 7, 2)}\\\\
& (11) && (0 \rightarrow \phi) \lor \psi \rightarrow \phi \lor \psi & \text{(RI, 10)}\\\\
& (12) && (0 \lor \phi \rightarrow \psi) \rightarrow (\alpha \lor \phi \rightarrow \psi) & \text{(MP, 9, R1a)}\\\\
& (13) && ((\phi \lor \psi) \lor \chi \rightarrow \omega) \rightarrow (\phi \lor \chi \rightarrow \omega) & \text{(MP, 3, R1a)}\\\\
& (14) && ((\phi \lor \psi) \lor \chi \rightarrow \omega) \rightarrow ((\psi \lor \phi) \lor \chi \rightarrow \omega) & \text{(MP, 4, R1a)}\\\\
& (15) && ((\phi \rightarrow \psi \lor \chi) \lor 0 \rightarrow (\psi \lor \chi \rightarrow \phi) \lor 0) \rightarrow (\chi \lor \psi \rightarrow \phi) & \text{(MP, 5, 8)}\\\\
& (16) && (\phi \lor \psi \rightarrow \chi) \rightarrow ((0 \rightarrow \phi) \lor \psi \rightarrow \chi) & \text{(MP, 11, R1a)}\\\\
& (17) && (\phi \lor \psi) \lor \phi \rightarrow \psi \lor \phi & \text{(MP, R4, 14)}\\\\
& (18) && \phi \lor \phi \rightarrow \psi \lor \phi & \text{(MP, 17, 13)}\\\\
& (19) && \alpha \lor 0 \rightarrow \phi \lor 0 & \text{(MP, 18, 12)}\\\\
& (20) && (\alpha \lor 0) \lor 0 \rightarrow \phi \lor 0 & \text{(MP, 19, 6)}\\\\
& (21) && (0 \lor \alpha) \lor 0 \rightarrow \phi \lor 0 & \text{(MP, 20, 14)}\\\\
& (22) && (0 \rightarrow 0 \lor \alpha) \lor 0 \rightarrow \phi \lor 0 & \text{(MP, 21, 16)}\\\\
& (23) && \alpha \lor 0 \rightarrow 0 & \text{(MP, 22, 15)}
\end{align}
</div>



# Riesz Logic and Fuzzy Logic



## Fuzzy Axioms

\begin{align}
&\textrm{R1a} && (\phi \rightarrow \psi) \rightarrow ((\psi \rightarrow \chi) \rightarrow (\phi \rightarrow \chi)) \\\\
&\textrm{R2} && \phi \rightarrow \phi \lor \psi\\\\
&\textrm{R3} && \phi \lor \psi \rightarrow \psi \lor \phi\\\\
&\textrm{R4} && (\phi \lor \psi)\lor \psi \rightarrow \phi \lor \psi
\end{align}



## Fuzzy logic semantics:
## <br>
$$\huge{[0,1]}$$




## Logistic function
<embed src="Logistic-curve.svg"/>



## T-norm



\begin{align}
T(a, b) &= T(b, a) \\\\
T(a, b) &\le T(c, d) \text{ if } a \le c  \text{ and } b \le d\\\\
T(a, T(b, c)) &= T(T(a, b), c)\\\\
T(a, 1) &= a
\end{align}



## Łukasiewicz T-norm
## <br>
$$\huge{T_L(a,b) = \max\\{0, a + b - 1\\}}$$



<embed src="lukasiewicz.svg"/>



## Riesz T-norm?



## Logistic addition



$$\huge{T_R(a, b) = \frac{ab}{ab + (1-a)(1-b)}}$$



<!-- $$\huge{\neg x := 1 - x}$$ -->
<!-- $$T(a,b) := a \oplus b$$ -->
<embed src="vector-add.svg"/>



\begin{align}
T(a, b) &= T(b, a) \\\\
T(a, b) &\le T(c, d) \text{ if } a \le c  \text{ and } b \le d\\\\
T(a, T(b, c)) &= T(T(a, b), c)\\\\
\color{red}{T(a, 1)} &\color{red}{= a}
\end{align}
