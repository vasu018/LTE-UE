CC=gcc
LDFLAGS=-lm -lpthread -pthread
CFLAGS=-Wall -Werror -g

#obj-m += ue.o

all: ue ue_no_write

ue: ue.c 
	$(CC) ue.c -g -o ue $(CFLAGS) $(LDFLAGS)

ue_no_write: ue.c
	$(CC) ue.c -o ue_no_write $(CFLAGS) -DNOWRITE $(LDFLAGS)

clean:
	rm -f ue ue_no_write



