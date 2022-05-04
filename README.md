# trainingsplatz
Testumgebung für Halite Agents

Die Datei Trainingsplatz.py beinhaltet den Code zum Ausführen einer Halite Episode gegen "random" Bots. Sie kann so verändert werden,
dass auch andere Bots gegen die submission.py spielen. Sowohl die submission.py, als auch mögliche Gegnerbots müssen sich zusammen in einem
Ordner mit der Trainingsplatz Datei befinden.

Um alle nötigen Packete auf dem FH Rechner zu erhalten, muss folgender Anleitung gefolgt werden.

Falls pip nicht installiert:

- Eingabeaufforderung/cmd
```console
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
- Eingabeaufforderung/cmd
```console
C:
cd C:\Python\Python39\Scripts
pip install requests
pip install kaggle-environments
pip install numpy
```

Um dieses Repository mit Visual Studio code zu Klonen muss folgender Anleitung gefolgt werden.
Installieren Sie in Visual Studio code ```GitHub Pull Requests and Issues```

Drücken Sie: ```strg+shift+p```

Geben Sie ein: ```git: clone``` + eingabe der URL

Erstellen Sie einen Ordner in Ihrem Laufwerk.

Um nun nach Änderungen in ihrem Code einen commit zu erstellen müssen sie sich vorher identifzieren:
```
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```
