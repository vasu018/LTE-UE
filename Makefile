CC=gcc
LDFLAGS=-lm -lpthread -pthread
CFLAGS=-Wall -Werror -g

obj-m += ue.o

all: ue

ue: ue.c 
	$(CC) ue.c -o ue $(CFLAGS) $(LDFLAGS)

clean:
	rm -f ue 



