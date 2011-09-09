HTML Basics
===========

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
Der HTML-Editor PSPad
---------------------
<img src="images/pspad.png" alt="PSPad HTML Editor Screenshot">

---

Browser Tools
-------------

<img src="images/firebug.png">

- Firefox: <a href="https://addons.mozilla.org/de/firefox/addon/firebug/" target="_blank">Firebug</a>
- Chrome: Eingebaute Entwicklertools: F12
- Safari: Eingebaute Entwicklertools: ALT+CONTROL+I


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

- HTML5 kennt keine verschiedenen Varianten mehr
	- Keine Frames mehr!
	- Kein DTD nötig, da HTML5 formell keine SMGL Sprache mehr ist.
	- Im nicht-HTML5 Browser: Standards Mode

---
Text formatierung
-----------------

.fx: column2

	!html
	<p>Das ist etwas Text</p>

<p class="demo">Das ist etwas Text</p>

P steht für Paragraph und bildet einen Absatz

	!html
	<p>Das ist etwas Text<br>mit einem Umbruch im Text</p>

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
Hyperlinks
------
- Herzstück des WWW
- Ermöglichen Kontext von Informationen
- Prizip: Weiterentwicklung von Literaturverzeichnissen aus Wissenschaftlichen Publikationen

	!html
	<a href="http://scooter.de" target="_blank">HYPER HYPER</a>

<a href="http://scooter.de" target="_blank">HYPER HYPER</a>



<a href="http://webkompetenz.wikidot.com/html-handbuch:links" target="_blank" class="html5hb"><img src="images/html5btn.png" alt="HTML5 Handbuch"></a>

---

---
CSS Basics
==========

---


