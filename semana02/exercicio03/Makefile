

all:
	
	cd UFU

run:
	echo "Rodando um programa"

clean:
	rm ./bin/* ./obj/*


hello:
	echo "Hello!"
	ls .

sist:
	cd UFU

	
all:
	gcc -c ./src/float_vector.c -I ./include -o ./obj/float_vector.o
	gcc -c ./src/mytime.c -I ./include -o ./obj/mytime.o
	gcc ./apps/app.c ./obj/*.o -I ./include -o ./bin/app
	gcc ./apps/app_com_mytime.c ./obj/*.o -I ./include -o ./bin/app_com_mytime

run:
	./bin/app

clean:
	rm ./bin/* ./obj/*


PPS = ./apps
BIN = ./bin
OBJ = ./obj
SRC = ./src
INCLUDE = ./include

all: libed myapps

libed:
	gcc -c $(SRC)/float_vector.c -I $(INCLUDE) -o $(OBJ)/float_vector.o
	gcc -c $(SRC)/mytime.c -I $(INCLUDE) -o $(OBJ)/mytime.o

myapps:
	gcc $(APPS)/app.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app
	gcc $(APPS)/app_com_mytime.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app_com_mytime

run:
	./bin/app

clean:
	rm ./bin/* ./obj/*


APPS = ./apps
BIN = ./bin
INCLUDE = ./include
OBJ = ./obj
SRC = ./src

all: libed myapps

libed: \
	float_vector.o \
	mytime.o

myapps:
	gcc $(APPS)/app.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app
	gcc $(APPS)/app_com_mytime.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app_com_mytime


%.o: $(SRC)/%.c $(INCLUDE)/%.h
	gcc -c $< -I $(INCLUDE) -o $(OBJ)/$@

run:
	./bin/app

clean:
	rm -rf ./bin/* ./obj/*