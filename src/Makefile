WWWDIR = ../www
VIRTUAL_ENV = env

all: virtual

virtual:
	@echo "--> Setup and activate virtualenv"
	cd ${WWWDIR}; \
	@. /etc/environ.sh; \
		use -e -r anaconda-4.1; \
		if test ! -d "$(VIRTUAL_ENV)"; then \
		  pip install --user virtualenv; \
		  virtualenv --no-site-packages $(VIRTUAL_ENV); \
		  . $(VIRTUAL_ENV)/bin/activate; \
		  pip install -r requirements.txt; \
		  deactivate; \
		fi
	@echo ""

install: virtual

clean:

distclean: clean
	rm -rf ${WWWDIR}/env;
