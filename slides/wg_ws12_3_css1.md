CSS Basics
==========

---

CSS: Cascading Style Sheets
------------
- CSS ist eine Sprache zum formatieren von HTML Dokumenten
- Formatierung geht weit über Textformatierung hinaus 
	- Beispiel: Mit CSS - ohne CSS
	- <a href="http://www.1stwebdesigner.com/css/50-awesome-css3-animations/">CSS3 Beispiele</a>
- 


---
Was kann CSS?
-------------
<img src="images/css-ohnecss.png" width="800" />


---
Was kann CSS?
-------------
<img src="images/css-mitcss.png" width="800" /> // TODO: Image Zoom



---

Verhalten von HTML-Elementen: Block
------------------------

	!html
	<div>
		<h1>Überschrift</h1>
		<p>Etwas Text</p>
		Nur <b>Text</b> ohne p...
	</div>


<div class="demo border">
	<h1>Überschrift</h1>
	<p>Etwas Text</p>
	Nur <b>Text</b> ohne p...
</div>


- Block-Elemente
	- Erzeugen einen eigenen Absatz im Textfluss
	- Können i.d.R. enthalten
		-Text (#PCDATA)
		- Block-Elemente
		- Inline-Elemente
		- Beispiele: &lt;h1&gt;, &lt;div&gt;, &lt;table&gt;



---
Verhalten von HTML-Elementen: Inline
--------------------------------
- Inline-Elemente
	- Erzeugen keinen Absatz im Textfluss
	- Können i.d.R. enthalten
		-Text (#PCDATA)
		- Inline-Elemente
	- Beispiele: &lt;br&gt;, &lt;i&gt;, &lt;span&gt;, ...

- Unsichtbare-Elemente
	- Beispiele: &lt;meta&gt;, &lt;style&gt;, &lt;script&gt;

- Steuerbar mit CSS  
	<pre><span class="lineno">1</span> <span class="nt"><a href="http://www.css4you.de/display.html" target="_blank" style="border: none;">display</a></span><span class="o">:</span> <span class="nt">none</span> | <span class="nt">block</span> | <span class="nt">inline</span> | ...</pre>


<div class="rightbox">
	<ul>
		<li><a href="http://www.w3schools.com/cssref/playit.asp?filename=playcss_display&preval=inline" target="_blank">Demo</a></li>
		<li><a href="http://www.w3.org/TR/CSS2/sample.html">W3C: Default Style HTML4</a></li>
	</ul>
</div>
---

