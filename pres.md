# A Logic for Vector Space Semantics

Daoud Clarke, University of Sussex

14th January 2015

Artificial Intelligence Group Seminar, University of York



## Overview

 - A Logic for Vector Space Semantics
 - Abelian Logic
 - Relation to other logics



## What if vector spaces had a logic?



$$\Huge{x \lor y \qquad\qquad x \land y}$$
# <br>
$$\Huge{x \rightarrow y \qquad\qquad \neg x}$$



## Why?



## Combine logical and distributional semantics



## &ldquo;I like Fidel Castro and his beard&rdquo;



## king - man + woman = queen

(Mikolov et al)



## But vector spaces have too little structure &hellip;



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
$\Rightarrow$ Vector Lattice (Riesz Space)



$$\Huge{\widehat{\mathit{orange}}\lor \widehat{\mathit{fruit}}}$$
# <br>
$$\Huge{\widehat{\mathit{orange}}\land \widehat{\mathit{fruit}}}$$



<div class="disjunction-title">$\widehat{\mathit{orange}}$</div>
<div class="disjunction"></div>



## Is that it?



$$\Huge{{\mathit{orange}}\rightarrow {\mathit{fruit}}}$$
# <br>
$$\Huge{\neg{\mathit{orange}}}$$



## What is truth?



## Give up standard propositional calculus



## Look more like a fuzzy logic



## Accept negative values



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



## Vector lattices are abelian lattice ordered groups

$\Rightarrow$ Abelian Logic (Meyer and Slaney)



## Abelian lattice ordered group

 - Abelian group: $\ \ \quad x - x = 0$
 - Lattice ordered: $\quad x \land y + z = (x + z) \land (y + z)$ 



## Abelian Logic (from A to Z)

Paraconsistent Logic: Essays on the Inconsistent (1989) 

## A, Still Adorable

Paraconsistency: the Logical Way to the Inconsistent (2000)



## Axioms (Part I)

<div style='zoom:1;'>
\begin{align}
&\textrm{identity} && (\phi \rightarrow \phi) \\\\
&\textrm{weak permutation} && (\phi \rightarrow ((\psi \rightarrow \chi) \rightarrow \delta)) \rightarrow ((\psi \rightarrow \chi) \rightarrow (\phi \rightarrow \delta)) \\\\
&\textrm{suffixing} && (\phi \rightarrow \psi) \rightarrow ((\psi \rightarrow \chi) \rightarrow (\phi \rightarrow \chi)) \\\\
&\textrm{contraposition} && (\phi \rightarrow \lnot \psi) \rightarrow (\psi \rightarrow \lnot \phi)\\\\
&\textrm{double negation} && \lnot\lnot \phi \rightarrow \phi\\\\
&\textrm{assertion} && \phi \rightarrow ((\phi \rightarrow \psi) \rightarrow \psi)\\\\
&\textrm{relativization} && ((\phi \rightarrow \psi) \rightarrow \psi) \rightarrow \phi\\\\
\end{align}
</div>
<!-- &\textrm{unit} && 1\\\\ -->
<!-- &\textrm{unit implication} && 1 \rightarrow (\phi \rightarrow \phi)\\\\ -->



## Axioms (Part II)

<div style='zoom:1;'>
\begin{align}
&\land\rightarrow && (\phi \land \psi) \rightarrow \phi \\\\
&\land\rightarrow && (\phi \land \psi) \rightarrow \psi \\\\
&\rightarrow\land && ((\phi \rightarrow \psi) \land (\phi \rightarrow \chi)) \rightarrow (\phi \rightarrow (\psi \land \chi))\\\\
&\rightarrow\lor && \phi \rightarrow (\phi \lor \psi) \\\\
&\rightarrow\lor && \psi \rightarrow (\phi \lor \psi) \\\\
&\lor\rightarrow && ((\phi \rightarrow \chi) \land (\psi \rightarrow \chi)) \rightarrow ((\phi \lor \psi) \rightarrow \chi)\\\\
&\textrm{distributivity} && (\phi \land (\psi \lor \chi)) \rightarrow ((\phi \land \psi) \lor (\phi \land \chi))\\\\
\end{align}
</div>



## Rules
###<br>
$$\huge{\frac{\phi,\ \phi \rightarrow \psi}{\psi}} \quad\quad \huge{\frac{\phi,\ \psi}{\phi \land \psi}}$$



## Abelian Logic is sound and complete w.r.t. abelian lattice ordered groups



## Relevance logics: reject
 
$\phi \rightarrow (\psi \rightarrow \phi)$

 - If 2 + 2 = 4, then the fact the Moon is made of Camembert implies that 2 + 2 = 4.
 - But 2 + 2 = 4. Therefore, by modus ponens, the fact that the Moon
   is made of Camembert implies that 2 + 2 = 4



# Relation to Other Logics



## Residuated Lattices: an Algebraic Glimpse at Substructural Logics

(Galatos et al, 2007)



<embed src="logic-hierarchy.svg"/>



## $\mathrm{FL}_{eo}$ algebras:
$0 \le x$



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



# Conclusion



## Vector spaces in CL have a logic



## Future work: higher order logic



# Thanks!
