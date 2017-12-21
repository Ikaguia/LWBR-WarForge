BUILD = __build_mod.py
COMPILE = compile.py tag %1 %2 %3 %4 %5 %6 %7 %8 %9
#DEST = /home/cristiano/.local/share/Steam/steamapps/common/MountBlade Warband/Modules
DEST = c:/Program Files (x86)/Steam/steamapps/common/MountBlade Warband/Modules

MOD_PATH = mod
CLIENT_V_PATH = $(MOD_PATH)/client
SERVER_V_PATH = $(MOD_PATH)/server
FULL_V_PATH = $(MOD_PATH)/full

PY_FILES = $(wildcard *.py)

CLIENT_FILES = $(wildcard $(CLIENT_V_PATH)/*)
SERVER_FILES = $(wildcard $(SERVER_V_PATH)/*)
FULL_FILES   = $(wildcard $(FULL_V_PATH)/*)

$(CLIENT_V_PATH)/variables.txt: $(PY_FILES)
	# $(COMPILE) clientVersion
	@python $(COMPILE) clientVersion
$(SERVER_V_PATH)/variables.txt: $(PY_FILES)
	#$(COMPILE) serverVersion
	@python $(COMPILE) serverVersion
$(FULL_V_PATH)/variables.txt: $(PY_FILES)
	#$(COMPILE)
	@python $(COMPILE)
$(MOD_PATH)/client.zip : $(CLIENT_V_PATH)/variables.txt
	#python $(BUILD) client
	@python $(BUILD) client
$(MOD_PATH)/server.zip : $(SERVER_V_PATH)/variables.txt
	#python $(BUILD) server
	@python $(BUILD) server
$(MOD_PATH)/full.zip   : $(FULL_V_PATH)/variables.txt
	#python $(BUILD) full
	@python $(BUILD) full

_backup:
	@if [ -d "$(DEST)/Native/" ]; then \
		if [ -d "$(DEST)/Native_backup/" ]; then \
			echo "backup already exists"; \
			rm -r  "$(DEST)/Native/"; \
		else \
			echo "native module backup created"; \
			mv "$(DEST)/Native/" "$(DEST)/Native_backup/"; \
		fi \
	fi

_move_cl:     $(MOD_PATH)/client.zip _backup
	@unzip -q $(MOD_PATH)/client.zip -d "$(DEST)/"
	@echo "finished moving client version"
_move_sv:     $(MOD_PATH)/server.zip _backup
	@unzip -q $(MOD_PATH)/server.zip -d "$(DEST)/"
	@echo "finished moving server version"
_move_full:   $(MOD_PATH)/full.zip   _backup
	@unzip -q $(MOD_PATH)/full.zip   -d "$(DEST)/"
	@echo "finished moving full version"



cmp_cl:   _clear $(CLIENT_V_PATH)/variables.txt _clean
cmp_sv:   _clear $(SERVER_V_PATH)/variables.txt _clean
cmp_full: _clear $(FULL_V_PATH)/variables.txt _clean
cmp_all:  _clear cmp_cl cmp_sv cmp_full _clean

build_cl:   _clear $(MOD_PATH)/client.zip _clean
build_sv:   _clear $(MOD_PATH)/server.zip _clean
build_full: _clear $(MOD_PATH)/full.zip _clean
build_all:  _clear build_cl build_sv build_full _clean

cl:   _clear _move_cl
sv:   _clear _move_sv
full: _clear _move_full


_clear:
	@#clear
_clean:
	@rm -f cur_compilation.py
	@rm -f *.pyc

debug: _clear
	@echo "MOD_PATH = $(MOD_PATH)"
	@echo "CLIENT_V_PATH = $(CLIENT_V_PATH)"
	@echo "SERVER_V_PATH = $(SERVER_V_PATH)"
	@echo "FULL_V_PATH = $(FULL_V_PATH)"
	@echo " "

	@echo " "
	@echo "PY_FILES = $(PY_FILES)"
	@echo " "

	@echo " "
	@echo "CLIENT_FILES = $(CLIENT_FILES)"
	@echo " "
	@echo "SERVER_FILES = $(SERVER_FILES)"
	@echo " "
	@echo "FULL_FILES = $(FULL_FILES)"
	@echo " "