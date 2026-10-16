#include "genetic.h"
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

char* encoding(int a, int b, int precision, double number) {

    int length = ceil(log2((b - a) * pow(10, precision)));
    double total_intervals = pow(2, length);
    int index = (int)floor((number - a) / (b - a) * total_intervals);

    char *code = malloc(sizeof(char) * (length + 1));
    for (int j = length - 1; j >= 0; j--) {
        code[j] = (index % 2 == 1) ? '1' : '0';
        index /= 2; 
    }

    code[length] = '\0';
    return code;

}

double decoding(int a, int b, int precision, char *bitstring){

        long long index = 0;
        int length = ceil(log2((b - a) * pow(10, precision)));
        double total_intervals = pow(2, length);

        for (int i = 0; i < length; i++) {
            index = (index << 1) | (bitstring[i] - '0');
        }
        
        double result = (double)a + (double)index * (b - a) / total_intervals;

        return result;
}


double fitness(int a, int b, int c, double x){
    return a * pow(x, 2) + b * x + c;
}

double* selection(int a, int b, int c, int n, double *chromosomes){ //polinomial coefictients, size of array and chromosome array
    
    double total_fitness = 0;
    for (int i = 0; i < n; i++)
    {
        double fit = fitness(a, b, c, chromosomes[i]);
        total_fitness += fit;
    }

    double start = 0;
    double end, length;
    double *intervals = malloc(sizeof(double) * (n+1));
    intervals[0] = start;
    for (int i = 1; i < n + 1; i++)
    {
        length = fitness(a, b, c, chromosomes[i - 1]) / total_fitness;
        end = start + length;
        intervals[i] = end;
        start = end;
    }

    return intervals;
}

char **crossover(int length, int position, char * chromosome1, char * chromosome2){
    char * chromosome3 = malloc(sizeof(char) * (length + 1));
    char * chromosome4 = malloc(sizeof(char) * (length + 1));
    char ** result = malloc(sizeof(char*) * 2);

    for (int i = 0; i < length; i ++)
    {
        if( i < position)
        {
            chromosome3[i] = chromosome1[i];
            chromosome4[i] = chromosome2[i];
        }
        else
        {
            chromosome3[i] = chromosome2[i];
            chromosome4[i] = chromosome1[i];
        }
    }

    chromosome3[length] = '\0';
    chromosome4[length] = '\0';

    result[0] = chromosome3;
    result[1] = chromosome4;

    return result;
}

char not(char c){
    if( c == '1')
        return '0';
    else
        return '1';
}

char * mutation(int length, int position, char *chromosome, int * positions){

    char * result = malloc(sizeof(char) * (length + 1));

    for (int i = 0; i < length; i ++)
    {
        result[i] = chromosome[i];
    }
    result[length] = '\0';

    for( int i = 0; i < position; i++){
        result[positions[i]] = not(result[positions[i]]);
    }

    return result;
}
