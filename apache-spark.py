import apt, apt.debfile
import pathlib, stat, shutil, urllib.request, subprocess, getpass, time
import secrets, json, re
import IPython.utils.io

def _installPkg(cache, name):
  pkg = cache[name]
  if pkg.is_installed:
    print(f"{name} is already installed")
  else:
    print(f"Install {name}")
    pkg.mark_install()

def _installPkgs(cache, *args):
  for i in args:
    _installPkg(cache, i)

def _download(url, path):
  try:
    with urllib.request.urlopen(url) as response:
      with open(path, 'wb') as outfile:
        shutil.copyfileobj(response, outfile)
  except:
    print("Failed to download ", url)
    raise
	
def installSpark():

  java_ver = "1.8"
  spark_ver = "2.4.4"
  turboVNC_ver = "2.2.3"

  #libjpeg_url = "https://svwh.dl.sourceforge.net/project/libjpeg-turbo/{0}/libjpeg-turbo-official_{0}_amd64.deb".format(java_ver)
  spark_ver_url = "http://apache.crihan.fr/dist/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz".format(spark_ver)
  turboVNC_url = "https://svwh.dl.sourceforge.net/project/turbovnc/{0}/turbovnc_{0}_amd64.deb".format(turboVNC_ver)

  _download(spark_ver_url, "libjpeg-turbo.deb")
  #_download(virtualGL_url, "virtualgl.deb")
  #_download(turboVNC_url, "turbovnc.deb")
  cache = apt.Cache()
  apt.debfile.DebPackage("libjpeg-turbo.deb", cache).install()
  apt.debfile.DebPackage("virtualgl.deb", cache).install()
  apt.debfile.DebPackage("turbovnc.deb", cache).install()
  _installPkgs(cache, "openjdk-8-jdk-headless")
  _installPkgs(cache, "findspark", "spark-nlp")
  cache.commit()	

#apt-get install openjdk-8-jdk-headless
#wget http://apache.crihan.fr/dist/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
#tar xf spark-2.4.4-bin-hadoop2.7.tgz
#pip install -q findspark
#pip install spark-nlp

#export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
#export SPARK_HOME=/content/spark-2.4.4-bin-hadoop2.7


