CC=gcc
LDFLAGS=-lm -lpthread -pthread
CFLAGS=-Wall -Werror -g

obj-m += ue.o

all: ue

ue: ue.c ue_service.c
	$(CC) ue.c -o ue $(CFLAGS) $(LDFLAGS)
	$(CC) ue_service.c -o ue_service $(CFLAGS) $(LDFLAGS)

clean:
	rm -f ue ue_service



