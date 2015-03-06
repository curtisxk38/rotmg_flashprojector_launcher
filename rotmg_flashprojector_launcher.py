import urllib.request
import subprocess
import sys

# pass location of flash projector as argument
def main():
    url = "http://www.realmofthemadgod.com/version.txt"
    file = urllib.request.urlopen(url)
    version = file.read()
    file.close()
    flash_url = "https://realmofthemadgodhrd.appspot.com/AssembleeGameClient"
    flash_url += version.decode("utf-8") + ".swf"
    try:
        subprocess.call([sys.argv[1], flash_url])
    except IndexError:
        print("Pass location of the flash projector as an argument")
    except FileNotFoundError:
        print("%s file not found" % sys.argv[1])

if __name__ == "__main__":
    main()
