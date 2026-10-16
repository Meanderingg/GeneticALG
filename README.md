# Pasi de executie

1. Compilarea librariei : gcc -c -Wall -Werror -fpic genetic.c
                          gcc -shared -o genetic.so libgenetic.o
2. Adaugarea librariei in path: sudo cp ./libgenetic.so /usr/lib
                                chmod 777 /usr/lib/libgenetic.so
                                ldconfig
3. Introducera parametrilor in parameters.in
4. Rularea cu python3 algorithm.py
