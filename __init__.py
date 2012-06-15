#!/usr/bin/python
# -*- coding: utf-8 -*-
#by SullenLook sullen look@sullenlook.eu

from plugin import *

class itunesfehler(Plugin):

    @register("de-De", ".*Fehler.*1.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Fehler beim Downgrade von iOS 5 auf iOS 4. Verwende entweder eine Custom Firmware von PwnageTool oder sn0wbreeze oder benutze FixRecovery.     Auf einem iPhone 4 Downgrade von iOS 5, verwende in TinyUmbrella die Option, Baseband Upgrade, um den Fehler zu umgehen.    Kann nicht downgraden. Versuchen Sie, den USB-Port zu wechseln und den Computer neu starten.
     Die installierte Version von iTunes kann auch zu alt. aktualisiere iTunes.")
        self.complete_request()

    @register("de-DE", ".*Fehler.*2.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("ASR auf Ramdisk nicht vorhanden oder beschädigt oder ist nicht signiert.")
        self.complete_request()

    @register("de-DE", ".*Fehler.*6.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say(" USB-Port wechseln und den Computer neu starten.")
        self.complete_request()

    @register("de-DE", ".*Fehler.*11.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Entferne die BBFW Datei im Ordner einer entpackten Firmware IPSW.    Das Geraet ist startfähig, nutze "Kick Out of Recovery" in Tiny Umbrella.     Custom Firmware muss immer im DFU Modus wiederhergestellt werden.")
        self.complete_request()

    @register("de-DE", ".*Fehler.*1600.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Dieser Fehler wird bei sn0wbreeze Benutzern, bzw. bei Custom Firmware Benutzern oft zu sehen sein. Der Grund dafuer ist, das eine Custom Firmware nicht einfach mit einem DFU Modus wiederhergestellt werden kann,
sondern weil dafür der PwnDFU Modus benoetigt wird. Das geht ganz einfach, dazu wird das Programm "iReb" benoetigt, mit diesem bringt man sein Geraet in den pwnDFU Modus und stellt das Geraet anschließend wiederher.
Danach sollte die Wiederherstellung kein Problem mehr sein und die Custom Firmware kann problemlos aufgespielt werden.")
        self.complete_request()

    @register("de-DE", ".*Fehler.*2003.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Hierfuer gibt es zwei Moeglichkeiten, warum der Fehler aufgetreten ist.
1. Verbindungsproblem, den USB Port ueberprüfen und wenn verfuegbar, ein anderes Kabel benutzen.
2. (Tritt nur bei sn0wbreeze auf) Sn0wbreeze konnte die Firmware nicht wiederherstellen. Das iPhone oder den iPod touch aus- und wieder anschließen..")
        self.complete_request()

    @register("de-DE", ".*Fehler.*1619.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Dieser Fehler tritt auf, wenn iTunes zu alt ist und das iPhone nicht wiederherstellen kann.
Hierzu iTunes auf die neuste Version updaten und erneut versuchen.")
        self.complete_request()

    @register("de-DE", ".*Fehler.*14.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Hierfuer kann es mehrere Moeglichkeiten geben, entweder wenn man mit einer normalen Firmware das iPhone updaten will (eine Custom Firmware aber benoetigt wird), 
oder das Geraet ist nicht mehr bootbar. Um dieses Problem zu beheben, eine neue Custom Firmware erstellen und damit dann normal wiederherstellen, oder wenn das Geraet nicht mehr bootbar ist,
das Geraet auch mit einer Custom Firmware wiederherstellen. Auch Moegliche Fehlerbehebungen ist einen anderen USB Port zu benutzen, oder den PC/Mac neuzustarten.).")
        self.complete_request()

    @register("de-DE", ".*Fehler.*1015.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Dieser Fehler ist ueblich, beim Downgrade iPhone und 3G-faehigen iPads. Das Problem tritt auf, wenn das Baseband des Geraets eine hoehere Versionsnummer als die Baseband in der Firmware. Stellen Sie einfach auto-boot true in iRecovery oder benutzen Sie iREB/TinyUmbrella/RecBoot. Falls dies nicht funktioniert Nutze Pwnage Tool eine Custom Firmware ohne das iPad Baseband zu erstellen, setzen Sie Ihr Geraet in den DFU-Modus pwned und via iTunes wiederherstellen.
.")
        self.complete_request()

    @register("de-DE", ".*Fehler.*2001.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Das Mac OS X Kernel-Erweiterung "IOUSBFamily", die mit Ende 2008 / Anfang 2009 MacBooks sowie dem 10.5.6 Update gebuendelt wurde, hat einen Bug, bei dem es nicht richtig zu erkennen, ein iDevice in den DFU-Modus. Es kann durch ein Update auf 10.5.7 (oder neuer) oder einen USB-Hub geloest werden..")
        self.complete_request()

    @register("de-DE", ".*Fehler.*2002.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("iTunes kann keine Verbindung herstellen, weil ein anderes Programm benutzen oder es wurde während dem Apple-Server-Check getrennt.")
        self.complete_request()
