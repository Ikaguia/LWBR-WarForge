import os,sys,zipfile

if "full" in sys.argv: versions = ["full"]
else: versions = ["client","server","full"]

def dirToZipFile(path,zf,folderName):
	for dirname, subdirs, files in os.walk(path):
		for filename in files:
			zf.write(os.path.join(dirname, filename),os.path.join(dirname, filename).replace(path,folderName))


path = "mod/"
commonPath = "mod/common/"
defPath = "mod/def/"

for version in versions:

	print "\ncompiling",version,"version..."

	os.system("python compile.py tag %%1 %%2 %%3 %%4 %%5 %%6 %%7 %%8 %%9 %sVersion" %version)
	os.system("rm cur_compilation.py")

	zipName = path + version + ".zip"
	curPath = path + version + "/"

	print "making",zipName,"..."

	with zipfile.ZipFile(zipName,'w') as zf:
		zf.write(curPath,"Native/")
		dirToZipFile(defPath,zf,"Native/")
		dirToZipFile(commonPath,zf,"Native/")
		dirToZipFile(curPath,zf,"Native/")
		zf.close()

	print "done...\n"
print "\nall done"
