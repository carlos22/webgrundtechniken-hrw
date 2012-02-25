# Übung 4: Tabellen, Forms & JavaScript

## 4.1 Vorbereitung

Laden sie von <http://up.frubar.net/1279/index.html> das Grundgerüst herunter.
Es soll ein Formular zur Pizza Bestellung angelegt werden. Die ausgewählten Pizzen werden in einen Einkaufswagen hinzugefügt. Dieser wird als Tabelle dargestellt.

## 4.2 Formular

Die Datei enthält bereits einen Form-Tag.
Innerhalb soll das Auswahl Formular erstellt werden.
Die einzelnen Eingabeelemente sollen zu einem <code>fieldset</code> zusammengefasst werden. In der Legende soll "Was wollen Sie essen?" stehen.

Der Anwender muss drei Angaben machen:

- Pizza
- Größe
- Extras

Für jede dieser Angaben soll es ein <code>label</code> geben was auf das entsprechende Eingabefeld verweist.

Die Pizza-Auswahl soll über Radio-Buttons realisiert werden.
Zur Auswahl stehen: Margherita, Salami, Prosciutto, Hawaii und Diavolo.
Beim Laden der Seite ist keine Pizza ausgewählt.
Der Name für die Form-Elemente soll "pizza" lauten.

Die Größe soll ein Dropdown Feld mit den Optionen "26 cm", "28 cm" und "Party-Pizza (45x35 cm)" sein. Beim Laden der Seite ist "28 cm" eingestellt.
Der Name für das Form-Element soll "size" lauten.

Es gibt drei Extras, welche als Checkboxen umgesetzt werden sollen.
Es kann "Doppelt Käse", "Oliven" und "Pilze" gebucht werden.
Die Form-Elemente sollen über den Namen "extra" angesprochen werden können.

Wurden alle Angaben gemacht kann der Anwender die Pizza zum Einkaufswagen hinzufügen.
Dazu wird ein Submit-Button benötigt. Der <code>onclick</code>-Event Handler soll die JavaScript Funktion "<code>addPizza();</code>" aufrufen.

## 4.3 Tabelle

Der Einkaufswagen soll eine Tabelle mit der id "einkaufswagen" sein.
Der <code>thead</code> besteht aus einer Zeile mit 5 Spalten.
Die Kopfzellen haben die Beschriftungen "Pizza", "Größe", "Doppelt Käse", "Oliven" und "Pilze".
Der <code>tbody</code> bekommt die id "einkaufswagen_body".
Wurde noch keine Pizza hinzugefügt soll ein Text angezeigt werden.
Fügen sie dazu eine Zelle, welche über 5 Spalten geht, in eine Table-Row mit der Klasse "empty" in den <code>tbody</code> ein.
Der Text dieser Zelle soll wie folgt lauten:

	Der Einkaufswagen ist leer.
	Fügen Sie oben ein paar Pizzen hinzu…

Ihre Seite sollte nun wie auf dem Screenshot aussehen.

<img src="http://up.frubar.net/1278/pizzaservice.png" alt="pizzaservice screenshot"
style="box-shadow: 0px 0px 15px #888; margin: 1em;">

## 4.4 JavaScript

Für diese Aufgabe sollen keine JS-Libraries oder Frameworks (z.B. jquery) verwendet werden.
Die <code>addPizza()</code> Funktion soll um diese Punkte vervollständigt werden:

#### Validierung der Eingabe

Wurde noch keine Pizza ausgewählt soll nur eine Nachricht mit dem Text "Bitte eine Pizza auswählen." angezeigt werden. Um eine Nachricht anzuzeigen kann die <code>alert()</code> Funktion verwendet werden.

Um herauszufinden welcher Radio-Button ausgewählt ist wurde die Hilfs-Funktion <code>radioValue(radio)</code> mitgeliefert. Diese erwartet als Parameter ein Radio-Button-Form Element und gibt den ausgewählten Wert zurück. Wurde keine Wert gewählt gibt die Funktion <code>false</code> zurück.

Um auf Form-Elemente zuzugreifen können sie <code>document.[formname].[elementname]</code> verwenden.
Die Form hat in diesem Fall den Namen "pizzaform" und das Element heisst "pizza".
Übergeben sie der <code>radioValue</code> Funktion also <code>document.pizzaform.pizza</code>.

#### Platzhalter Entfernen

Wird die erste Pizza hinzugefügt ist der Einkaufswagen natürlich nicht mehr leer.
Die Zeile mit der Klasse "empty" soll also entfernt werden.

Über die ID wird mit <code>getElementById</code> der "einkaufswagen_body" aufgelöst und in die Variable <code>ek_body</code> geschrieben. Über DOM Funktionen wie <code>children</code> und <code>removeChild()</code> können die Kind-Elemente manipuliert werden.

Mit der classList API können sie Prüfen ob ein Element teil einer Klasse ist: <code>[e].classList.contains('foo')</code>.

Prüfen sie ob das erste Kind von <code>ek_body</code> in der Klasse "empty" ist.
Falls dies der Fall ist entfernen sie dieses Element.

#### Neue Zeile zur Tabelle hinzufügen

Um eine neue Zeile zur Tabelle hinzuzufügen müssen die einzelnen Elemente via JavaScript angelegt und mit Text gefüllt werden.

Hierzu benötigen sie die Funktionen <code>document.createElement()</code> bzw. <code>document.createTextNode()</code> und <code>[e].appendChild()</code>.

Angenommen sie haben ein div mit der ID "mydiv" und möchten den Code <code>&lt;h1>Hallo Welt&lt;/h1></code> einfügen:
<pre>
mydiv = document.getElementById('mydiv');
myh1  = document.createElement('h1');
myh1.appendChild(document.createTextNode('Hallo Welt'));
mydiv.appendChild(myh1);
</pre>


Sie müssen so also ein <code>tr</code> und fünf <code>td</code> Tags anlegen.
Die <code>td</code>-Tags dem <code>tr</code>-Tag und diesen <code>ek_body</code> als Kind hinzufügen.

In der erste Spalte soll die Pizza stehen. Verwenden sie dazu wie bei der Validierung die Funktion <code>radioValue</code>.
In der zweiten Spalte soll die Größe stehen. Wie bei Text-Feldern und anderen Eingabe Elementen können sie den aktuellen Wert über das Attribut <code>.value</code> abrufen.

Spalten drei bis fünf enthalten, je nach dem ob die entsprechende Checkbox gesetzt ist, ein "X" oder ein "-". Der Wert einer Checkbox lässt sich über <code>.checked</code> abfragen. Da die drei Checkboxen den selben Namen haben muss der Zugriff als Liste erfolgen. Um zu sehen ob Oliven gefordert wurden kann folgender Code verwendet werden:

	document.pizzaform.extra[1].checked

Der index beginnt bei 0, um also die zweite Checkbox (Oliven) abzufragen wird index 1 verwendet.

## 4.5 jQuery (Optional)

Erstellen sie eine Kopie ihrer Lösung von Aufgabe 4.4.
Binden sie die JavaScript Bibliothek jQuery ein.
Versuchen sie die Funktionalität von 4.4 anstatt mit DOM mit jQuery nachzubilden.

Diese Aufgabe wird nicht gewertet.


