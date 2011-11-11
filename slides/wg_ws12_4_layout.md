Layout
==========

---
Das Box Modell
--------------

<img src="images/boxmodell_sh.png" alt="Boxmodell" />


<small> Quelle: <a href="http://de.selfhtml.org/css/formate/box_modell.htm">SelfHTML</a> </small>

---
Aussen-Abstand: Margin
------------------------------

Aussen-Abstand oben/rechts/unten/links

`margin-[top|right|bottom|left]: [Abstandsangabe|auto|inherit]`

Abstände rechts/links aneinandergrenzender Elemente werden addiert
Abstände oben/unten aneinandergrenzender Elemente werden nicht addiert sondern der größere Abstand gilt 

`auto` oben/unten bewirkt Abstand `0`
`auto` links bewirkt rechtsbündige Position
`auto` rechts und links bewirkt Zentrierung

`margin-top:10px; margin-bottom:10px`

---
Aussen-Abstand: Margin
----------------------------

	!css
	margin:10px
	margin:10px 5px 10px 5px

Außenrand/Abstand oben/rechts/unten/links

`margin:[Angabe 1] ... [Angabe 4]`

* Eine Angabe für alle 4 Ränder
* Angabe für oben/unten und rechts/links
* Angabe für oben, rechts/links und unten
* Angabe für oben, rechts, unten und links


---
Innenabstand: Padding
-------------------

Innenabstand oben/rechts/unten/links

	!css
	padding-[top|right|bottom|left]:[Abstand]
	padding-top:10px; padding-bottom:10px
	padding:[Abstand 1] ... [Abstand 4]

* Eine Angabe für alle 4 Ränder
* Angabe für oben/unten und rechts/links
* Angabe für oben, rechts/links und unten
* Angabe für oben, rechts, unten und links

---
Rahmen: Border
------------
Rahmentyp
	
	!css
	border-[top|right|bottom|left]-style: [none|hidden|dotted|dashed|solid|double| groove|ridge|inset|outset]
	border-style:[Angabe 1] ... [Angabe 4]
	border-style:solid
	border-top-style:solid

Rahmenbreite

	!css
	border-[top|right|bottom|left]-width: [Rahmenbreite|thin|medium|thick]
	border-width:5px; border-top-width:5px
---
Rahmen: Border
------------
###Rahmenfarbe

	!css
	border-[top|right|bottom|left]-color: [Rahmenfarbe]
	border-color:blue; border-top-color:blue

###Rahmen gesamt

	!css
	border-[top|right|bottom|left]: [border-width border-style border-color]

Reihenfolge der Angaben ist egal

	!css
	border:5px solid red
	border-top:5px solid red

---
Rahmen: Border
-------------
Outline (Kontur)

Rahmen für nicht rechteckige Bereiche (Textfluss) Unterschied zu `border`: Konturen werdenüber dem Element gezeichnet, daher keinen eigenen Platz Outline-Rahmen können nur vollständig geschlossen gezeichnet werden

	!css
	outline-width: [Rahmenbreite]
	outline-style: [Rahmentyp]
	outline-color: [Rahmenfarbe]
	outline: [width style color]
---
Hintergrundfarben und -bilder
-----------------------------------------

Hintergrundfarbe

	!css
	background-color:[Farbe]

Hintergrundbild

	!css
	background-image:url([URI])

Wiederholung Hintergrundbild

	!css
	background-repeat:[repeat|repeat-x|repeat-y|no-repeat]

Wasserzeichen-Effekt

	!css
	background-attachment:[scroll|fixed]

---
Hintergrundfarben und -bilder
------------------------------------------

Hintergrundposition

	!css
	background-position:[left|center|right] [top|center|bottom]
	background-position: left top;

Hintergrund gesamt

	!css
	background:[background-color	background-image	background-repeat	
	   background-attachment	background-position]
	
	background:url(wi-team-1.jpg) no-repeat fixed center;

---
Größe von Elementen
--------------------------------
Angabe von Breite und Höhe

`width:[Breite|auto]` Breite des Elements  
`min-width:[Breite]` Mindestbreite des Elements  
`max-width:[Breite]` Maximalbreite des Elements  


`height:[Höhe|auto]` Höhe des Elements  
`min-height:[Breite]` Mindesthöhe des Elements  
`max-height:[Breite]` Maximalhöhe des Elements  

---
Position von Elementen
----------------------------------

Art der Positionierung

	!css
	position: [static|relative|absolute|fixed]

`static` normaler Elementfluss (Normalposition)  
`relative` relativ zur Normalposition (Verschieb.)  
`absolute` absolute Position (zum nächsthöheren _nicht static_ positionierten Element)  
`fixed` absolute Position (zum Browserfenster) bleibt beim Scrollen stehen  

Mit `absolute` oder `fixed` positionierte Elemente sind nicht Teil des Elementflusses  

Angabe der Position

`top:[Abstand|auto]` Position von oben  
`left:[Abstand|auto]` Position von links  
`bottom:[Abstand|auto]` Position von unten  
`right:[Abstand|auto]` Position von rechts  

---
Anzeige von Elementen
----------------------------------

### Anzeige von übergroßem Inhalt

	!css
	overflow:[visible|hidden|scroll|auto]

`visible` Inhalt ragt aus Element heraus   
`hidden` Inhalt wird abgeschnitten   
`scroll` abschneiden + scrollen   
`auto` Web-Browser entscheidet  

### Textfluss

	!css
	float:[left|right|none]

Element steht links/rechts und wird von nachfolgendem Text umflossen

	!css
	clear:[left|right|both|none]

Textumfluss wird abgebrochen und nachfolgender Text beginnt unterhalb des Elements

---
Anzeige von Elementen
----------------------------------

###Ebene bei Überlappung

	!css
	z-index:[Ebene];
	z-index:3;


###Art der Anzeige
	
	!css
	display:[block|inline|inline-block|list-item|run-in|none]

> `block` Anzeige als Block  
> `inline` Anzeige im Textfluss  
> `inline-block` Block im Textfluss  
> `list-item` Block mit Bullet  
> `run-in` kontextabhängig  
> `none` Keine Anzeige  
---
Anzeige von Elementen
----------------------------------

	!css
	visibility:[visible|hidden|collapse]

> `visible` 		sichtbar  
> `hidden`		versteckt (Platzhalter)  
> `collapse`	Tabelle gibt Platz frei  

Unterschied zwischen `visibility: hidden` und `display: none`: Berechnung der Position anderer Elemente!

---
Positionierung Beispiel
---------------------------------

TODO


---
Layout Methoden
-------------------------

### Veraltete Methoden des Seitenlayouts

* Frames  
	* „Deprecated“: kein gültiges HTML in der Variante Strict
* Tabellenbasiertes Seitenlayout   
	* Verletzt die Trennung zwischen Inhalt und Layout

Beide Varianten ermöglichen keine Anpassung an Smartphones/Tablets!!

### CSS-basiertes Seitenlayout  
> ➔ Flexible Definition der Anordnung der Elemente einer Seite  
> ➔ Erleichtert die Pflege der Seiten  
> ➔ Ermöglicht alternative Layouts  
> ➔ Reduziert den Umfang des HTML-Codes  


---
Layout Best-Practise
------------------------------

TODO


