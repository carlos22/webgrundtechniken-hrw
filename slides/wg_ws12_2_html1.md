HTML Basics
===========

## Presenter Notes
Praktischer Einstieg, theorie später!

---

HTML Bascis: Inhalt / Ziel
--------------------

- Was ist HTML?
- HTML Grundgerüst
- Textformatierung
- Links
- Listen
- Weitere Textauszeichungen (physisch und logisch)
- Allgemeine HTML Elemente
- Bilder einbinden

=> Vertiefung der Kentnisse in Übung 1 (nächste Woche).

---

Das HTML Format
---------------

- HTML Dateien sind Text-Dateien
- Bearbeitbar mit einfachem Texteditor (z. B. Notepad, gedit, TextMate)
- Spezialisierte HTML Editoren
	- Windows: PSPad / Notepad++
	- Linux: gEdit / Kate / Geany
	- OSX:  TextMate
- Dateiendung *.html oder *.htm
- Programm zum Anzeigen einer HTML-Datei: Browser
	- Chrome, Firefox, Safari, Opera, IE

.notes: Es gibt sogenannte WYSIWYG Editoren, verwendet kein Profi ⇒ Wir also auch nicht!!

---
Aufgabe von HTML
-----------------
- Idealisiert:
	- Textauszeichnung
		- Bedeutung von Textelementen festlegen (Semantik)
	- NICHT Textpräsentation, Layout, Design
		- CSS
- Realität:
	- Bau von Webseiten im Zusammenspiel mit CSS und JavaScript

---
Der HTML-Editor PSPad
---------------------
<img src="images/pspad.png" alt="PSPad HTML Editor Screenshot">

---

Entwicklertools im Browser
-------------

<img src="images/firebug.png">

- Firefox: Addon <a href="https://addons.mozilla.org/de/firefox/addon/firebug/" target="_blank">Firebug</a>
- Chrome:  Schraubenschlüssel => Tools => Entwicklertools | UMSCHALT+STRG+I | F12
- Safari:  ALT+CONTROL+I
- Opera:   Tools => Advanced => Opera Dragonfly

Aktuelle Versionen vom Internet Explorer bieten ebenfalls Entwicklertools.

---

HTML4-Datei Aufbau
-----------------

	!html
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" 
	"http://www.w3.org/TR/html4/loose.dtd">
	<html>
	  <head>
	    <title>Titel der Seite</title>
	  </head>
	  <body>
		<h1>Überschrift der Seite</h1>
		<p>Ein Absatz mit Etwas Text</p>
	  </body>
	</html> 

- Dokumenttyp-Deklaration: Deklariert die verwendete Auszeichnungssprache, d.h. das vereinbarte „Regelwerk“
- HTML 4.01 Sprachvarianten
	- Strict: Keine Verwendung unerwünschter Elemente
	- Transitional: Verwendung aller Elemente
	- Frameset: Definition von Framesets

---

HTML5-Datei Aufbau
-----------------

	!html
	<!DOCTYPE HTML>
	<html>
	  <head>
	    <title>Titel der Seite</title>
	  </head>
	  <body>
	  </body>
	</html>

.fx: html5

- HTML5 kennt keine verschiedenen Varianten mehr
	- Keine Frames mehr!
	- Kein DTD nötig, da HTML5 formell keine SMGL Sprache mehr ist.
	- Im nicht-HTML5 Browser: Standards Mode
---
HTML Tags
---------

- Tags sind immer in spitzen Klammern eingeschlosse  
	<pre><span class="nt">&lt;tagname&gt;</span></pre>
- Tags werden (fast) immer geschlossen  
	<pre><span class="nt">&lt;tagname&gt;&lt;/tagname&gt;</span></pre>
- Zwischen den Tags kann (meist) Text und/oder weitere Tags stehen  
	<pre><span class="nt">&lt;b&gt;</span>Text<span class="nt">&lt;/b&gt;</span></pre>
- Tags können (beliebig viele) Attriube haben  
	<pre><span class="nt">&lt;b <span class="na">class=</span><span class="s">"test"</span>&gt;</span>Text<span class="nt">&lt;/b&gt;</span></pre>

---
Text formatierung
-----------------

.fx: column2

	!html
	<p>Das ist etwas Text</p>

<p class="demo">Das ist etwas Text</p>

P steht für Paragraph und bildet einen Absatz

	!html
	<p>Das ist etwas Text<br>mit einem 
	Umbruch im Text</p>

<p class="demo">Das ist etwas Text<br>mit einem Umbruch im Text</p>

br erzeugt (weiche) Umbrüche im Text (in Word/Writer: STRG+ENTER)

<ul><li>Überschriften</li></ul>

	!html
	<h1>Überschrift 1</h1>
	<h2>Überschrift 2</h2>
	<h3>Überschrift 3</h3>
	<h4>Überschrift 4</h4>
	<h5>Überschrift 5</h5>
	<h6>Überschrift 6</h6>

<div class="colbreak"></div>

<h1>Überschrift 1</h1>
<h2>Überschrift 2</h2>
<h3>Überschrift 3</h3>
<h4>Überschrift 4</h4>
<h5>Überschrift 5</h5>
<h6>Überschrift 6</h6>



- Überschriften sind nicht nur ein visuelles Mittel!
	- Semantische Auszeichnung
	- Wichtig für maschnielle Verarbeitung, z. B. Suchmaschinenen und Sehbehinderte

---
Zeilenumbruch
-------------
- Zeilenumbruch erzwingen
	- &lt;br&gt; (Standalone-Element)
- Zeilenumbruch verhindern
	- &amp;nbsp; erzeugt ein geschütztes Leerzeichen
	- An einer solchen Stelle erfolgt kein Umbruch
	- Alternative Schreibweise: &amp;#160;
- Bedingter Zeilenumbruch
	- &amp;shy; markiert eine Stelle an der getrennt werden darf Browserunterstützung mangelhaft, daher vermeiden


---
Hyperlinks
----------

	!html
	<a href="http://scooter.de" target="_blank">HYPER HYPER</a>
	<a href="[URI]" target="[ZIEL]">[SICHTBARER TEXT]</a>
	

<a class="demo" href="http://scooter.de" target="_blank">HYPER HYPER</a>

- Herzstück des WWW: Ermöglichen Kontext von Informationen
- Prizip: Weiterentwicklung von Literaturverzeichnissen aus Wissenschaftlichen Publikationen  
- Vordefinierte optionen für `target`
	- `_blank`: Anzeige des Verweisziels in neuem Fenster
	- `_self`: Anzeige des Verweisziels in aktuellem Fenster
	- `_parent`: Anzeige in Vaterfenster bei verschachteltem Frameset
	- `_top`: Anzeige in Hauptfenster bei verschachteltem Frameset


<a href="http://webkompetenz.wikidot.com/html-handbuch:links" target="_blank" title="HTML5 Buch" class="html5hb"><img src="images/html5btn.png" alt="HTML5 Handbuch"></a>

---
URI: Uniform Resource Identifier
--------------------------------
<br>
<blockqoute class="bigqoute">Ein Uniform Resource Identifier (URI) (engl. „einheitlicher Bezeichner für Ressourcen“) ist ein Identifikator und besteht aus einer Zeichenfolge, die zur Identifizierung einer abstrakten oder physischen Ressource dient. URIs werden zur Bezeichnung von Ressourcen (wie Webseiten, sonstigen Dateien, Aufruf von Webservices, aber auch z. B. E-Mail-Empfängern) im Internet und dort vor allem im WWW eingesetzt.</blockqoute>


<a href="http://de.wikipedia.org/wiki/Uniform_Resource_Identifier" target="_blank" title="Wikipedia" class="html5hb"><img src="images/wikipedia.png" alt="HTML5 Handbuch"></a>

### Presenter Notes
- Nicht nur Adressen von Webseiten sondern auch von Resourcen innerhalb der Webseite (Grafiken, CSS etc.)

---
Verweise innerhalb einer Datei
------------------------------
	!html
	<a href="[URI]#[Ankername]">Verweistext</a>

- Regeln für Ankernamen (bzw. IDs):  
	- sollten nur Buchstaben, Ziffern und die Sonderzeichen Unterstrich, Bindestrich, Punkt und Doppelpunkt enthalten
	- Ankernamen und ID-Attribute müssen dateiweit eindeutig sein

Beispiel: <a href="http://de.wikipedia.org/wiki/Html#Syntax">Wikipedia Artikel HTML, Abschnitt Syntax</a>

---
Verweise zu Email-Adressen
--------------------------

	!html
	<a href="mailto:[email-Adresse]">Verweistext</a>
	<a href="mailto:karl.glatz@hs-weingarten.de">Karl</a>
	<a href="mailto:karl.glatz@hs-weingarten.de?cc=karl.glatz@gmail.com">
	Karl Glatz</a>

- Optionen bei Email-Verweisen
	- cc, bcc, subject und body
- Optionen werden als Parameter des href-Attributs übergeben, eingeleitet durch ein ?
- Problem: Spam-Bots durchsuchen internet nach mailto: Adressen!
	- Lösungen: oft wird die Adresse verunstaltet oder mit JS encodiert



---
Listen: Aufzählungslisten (unordered list)
-----------------------------

	!html
	<h2>Einkaufsliste</h2>
	<ul>
		<li>Milch</li>
		<li>Eier</li>
		<ul>
			<li>3x Bio</li>
			<li>2x Freiland</li>
		</ul>
		<li>Spagetti</li>
	</ul>

<div class="demo">
<h2>Einkaufsliste</h2>
<ul>
	<li>Milch</li>
	<li>Eier</li>
	<ul>
		<li>3x Bio</li>
		<li>2x Freiland</li>
	</ul>
	<li>Spagetti</li>
</ul>
</div>

<b>ul</b>: <b>u</b>norderd <b>l</b>ist | <b>li</b>: <b>l</b>ist <b>i</b>tem

### Presenter Notes
Kind-Elemente ul: li-Elemente  
Eltern-Elemente li: ul- oder ol-Elemente  
Kind-Elemente li: Block-Elemente und Inline-Elemente  
Beliebige Verschachtelungen von Listen sind möglich  

---
Nummerierte Listen (ordered list)
----------------------------------
	!html
	<h2>Anleitung</h1>
	<ol>
		<li>Download</li>
		<li>Entpacken</li>
		<li>Starten ...</li>
	</ol>
<div class="demo">
<h2>Anleitung</h1>
<ol>
	<li>Download</li>
	<li>Entpacken</li>
	<li>Starten ...</li>
</ol>
</div>

<b>Achtung:</b> Verschachtelung nummerierter Listen bewirkt keine Nummerierungshierarchie (<a href="http://aktuell.de.selfhtml.org/artikel/css/nummerierung/">Mit CSS möglich</a>)

---
Präformatierter Text
--------------------
	!html
	<pre>präformatierter 
		<b>Text</b> mit ein paar
	Umbrüchen und
	        Einrückungen!</pre>

<pre class="demo">präformatierter 
		<b>Text</b> mit ein paar
	Umbrüchen und
	        Einrückungen!</pre>

Anzeige mit Formatierungen in dichtengleicher Schrift  
Aber: HTML-Zeichen werden interpretiert

- Verwendung
	- Anzeige von Quellcode
	- vordefinierten Tabellen, etc.

---
Zitate und Adressen
-------------------
	!html
	<blockquote><p>there are only two hard problems in computing: caching, 
	concurrency and off-by-one errors</p></blockquote>
<blockquote class="demo"><p>there are only two hard problems in computing: caching, concurrency and off-by-one errors</p></blockquote>

- Zitate
	- Kind-Elemente: Block-Elemente
	- Attribut cite: URI der zitierten Quelle (ohne Visualisierung)
	- &lt;blockquote cite="http://www.hs-weingarten.de/"&gt; ...
- Adressen
	Kind-Elemente: Inline-Elemente

	!html
	<address>Hochschule Ravensburg-Weingarten<br>
	Doggenried Str.<br>
	88250 Weingarten</address>

---
Logische Textauszeichnung
---------------------------------------
.fx: column2

- Logische Auszeichnungen im Text
	- Elemente definieren logische Bedeutung unabhängig von einer konkreten Darstellung
	- Logische Auszeichnungen sind Inline-Elemente
- Elemente zur logischen Textauszeichnung
	- <span class="nt">em</span> – empathisch, betont
	- <span class="nt">strong</span> – stark betont
	- <span class="nt">code</span> – Quelltext
	- <span class="nt">samp</span> – Beispiel
	- <span class="nt">kbd</span> – Benutzereingaben
	- <span class="nt">var</span> – Variable
	- <span class="nt">cite</span> – Quelle oder Autor
	- <span class="nt">dfn</span> – Definition
	- <span class="nt">abbr</span> – Abkürzung
	- <span class="nt">acronym</span> – Akronym
	- <span class="nt">q</span> - Zitat
	- <span class="nt">del</span> - gelöschter Text   
	  <span class="nt">ins</span> - eingefügter Text
		- Attribut <span class="na">datetime</span>: Zeitpunkt der Änderung
		- Attribut <span class="na">cite</span>: URI als Grund für Änderung


---
Physische Textauszeichnung
----------------------------------------
.fx: column2

- HTML4: Elemente definieren direkt eine gewünschte Darstellung
- HTML5: Jeweils "schwache" semantische Bedeutung zugeordnet => Styling CSS
- Elemente zur physischen Textauszeichnung
	- <span class="nt">b</span> – fett (bold)
	- <span class="nt">i</span> – kursiv (italic)
	- <del><span class="nt">tt</span> – dichtengleich (teletyper)</del><sup>*</sup>
	- <del><span class="nt">big</span> – größer als normal</del><sup>*</sup>
	- <del><span class="nt">center</span> - zentriert</del><sup>*</sup>
	- <del><span class="nt">strike</span> - durchgestrichen</del><sup>*</sup>
	- <span class="nt">small</span> – kleiner als normal
	- <span class="nt">sup</span> – hochgestellt (superior)
	- <span class="nt">sub</span> – tiefgestellt (subordinate)
- Sonstige Elemente: <span class="nt">hr</span> – trennlinie

<div style="-webkit-break-before: column;-moz-break-before: column">
<sup>*</sup>nicht in HTML5: <a href="http://www.w3.org/TR/html5-diff/#absent-elements">W3C: HTML5 vs HTML4</a>
</div>

---
Allgemeine Elemente für Textbereiche
------------------------
- Allgemeines Block-Element
	- <span class="nt">div</span>
	- Kind-Elemente: Block-Elemente und Inline-Elemente
- Allgemeines Inline-Element
	- <span class="nt">span</span>
	- Kind-Elemente: Inline-Elemente
- Formatierung allgemeiner Elemente mit CSS
	- Allgemeine Elemente ermöglichen die logische Auszeichnung von	Abschnitten oder Blöcken
	- Formatierung mit CSS


---
Allgemeine Elemente HTML5
------------------------

.fx: html5

- HTML5 biete neue allgemeine Elemente
	- <span class="nt">article</span> – Artikel z. B. in einem Blog
	- <span class="nt">section</span> – Abschnitt eines Textes
	- <span class="nt">nav</span> – Navigation, Menü
	- <span class="nt">header</span> – Kopf einer Seite
	- <span class="nt">footer</span> – Fuß einer Seite
	- <span class="nt">aside</span> – z.B. Sidebar bei einem Blog

- Alle Elemente verhalten sich wie das <span class="nt">div</span>, bieten jedoch die möglichkeit das HTML-Dokument besser zu strukturieren.

---
Grafikformate: Vektor und Pixel
-------------------------------
.fx: column2

- Pixel:
	- <b>JPEG</b>: Joint Photographic Experts Group
		- Verlustbehaftetes Format
		- Einsatzzweck: Fotos von Personen, Landschaften etc.
	- <b>PNG</b>: Portable Network Graphics
		- Verlustfreies Format
		- Echte Transparenz: Alpha Kanal
		- Animierte Varianten: APNG, MNG (fehlender Browser Support)
		- Einsatz: Alle Grafiken wie Verläufe, Comics, Zeichnungen, Buttons etc.
	- <b>GIF</b>: Graphics Interchange Format
		- Verlustfreies Format
		- Limitierter Farbraum
		- Einfache Transparenz (1-Bit)
		- Einsatzzweck: Animation
		- <b>Veraltetes Format!</b>
- Vektor:
	- <b>SVG</b>: Scalable Vector Graphics
		- Einsatzzweck: Grafiken wie Karten, Logos, Wappen, Zeichnungen, usw.
	- <a href="http://diveintohtml5.org/canvas.html" target="_blank"><b>Canvas</b></a>: Generierte Vektorgrafik
		- Einsatzzweck: Interaktive Spiele, Animationen etc.
		- Grafik muss programmiert werden in JavaScript

<a href="http://webkompetenz.wikidot.com/html-handbuch:canvas-vektorgrafik" target="_blank" title="HTML5 Buch: Grafiken" class="html5hb"><img src="images/html5btn.png" alt="HTML5 Handbuch"></a>

## Presenter Notes

- SVG Tools: Inkscape, Adobe Illustrator
- Pixel Tools: Photoshop, Gimp etc.

---
Einbinden von Bildern
---------------------
	!html
	<img src="[URI]" alt="[Alternativtext]">

- Referenz auf eine Graphik
	- img-Element ist Standalone-Element
- Attribut `src` bestimmt die Graphikdatei
	Beachten Sie die Möglichkeiten zur Referenzierung von Dateien in HTML
- Attribut `alt` definiert alternativen Text 
	- IE: Tooltip
		- Tooltips normalerweise via Universalattribute `title`
	- Alle: Falls Bild nicht angezeigt werden kann; Screenreader

---
(Veraltete) Attribute für Bilder
-------------------------------
- Größe der Grafik: `width`, `height`
	- Bei langsamen Verbindungen führt angabe zur schnelleren Seitendarstellung
	- Abweichende Größen zum Original sind nicht empfehlenswert:
		- Schlechte Skalierungsalgorithmen der Browser
		- Höhere Ladezeiten bei verkleinerung der Grafiken
- Ausrichtung:
	- `align`, `vspace`, `hspace`
- <span class="important">Für beides sollte heute CSS verwendet werden! (HTML4 Strict/HTML5)</span>

- <a href="http://webkompetenz.wikidot.com/html-handbuch:image-maps" target="_blank">Image Maps</a>: Verweissensitive Grafiken



