WWWDIR = ../www
BINDIR = ../bin
VIRTUAL_ENV = env

all: virtual

virtual:
	@echo "--> Setup and activate virtualenv"
	cd ${WWWDIR}; \
	if test ! -d "$(VIRTUAL_ENV)"; then \
	  pip install --user virtualenv; \
	  virtualenv --no-site-packages $(VIRTUAL_ENV); \
	  . $(VIRTUAL_ENV)/bin/activate; \
	  pip install -r requirements.txt; \
	  deactivate; \
	fi
	@echo ""

install: virtual
	install -D --mode 0755 run_flask.sh ${BINDIR}/run_flask.sh

clean:

distclean: clean
	rm -rf ${WWWDIR}/env \
	       ${BINDIR}/run_flask.sh;
	find ${WWWDIR} -name *.pyc -exec rm {} +
