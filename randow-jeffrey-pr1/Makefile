CFLAGS := -Wall --std=gnu99 -g

ARCH := $(shell uname)
ifneq ($(ARCH),Darwin)
  LDFLAGS += -lpthread
endif

default: webserver webclient
webserver: webserver.o
webclient: webclient.o

.PHONY: clean

clean:
	rm -fr *.o webserver webclient