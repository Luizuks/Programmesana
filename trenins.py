nenodots= input('Vai Jums ir kāds laikā nenodots izdevums? (J,N)')
if nenodots=='J':
    print('Jūs nedrīkstat neko izņemt')
elif nenodots=='N':
    pieprasits=input('Vai šī publikācija ir pieprasīta?')
    if pieprasits=='J':
        print('Izsniedz uz 2 dienān')
    zurnals=input('Vai publikacija ir žurnāls?')
    if zurnals=='J':
        print('Izsniedz uz 7 dienām')