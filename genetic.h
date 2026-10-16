#ifndef ENCODING 
#define ENCODING 

//encodes a floating point number in a fixed precision binary string, representing the left boundry of an intreval
//a and b are the interval limits, precision is the decimal precition and number is the floating point number to encode

char* encoding(int a, int b, int precision, double number);


//decodes a binary string to a floating point number
//the bitstring is the left boundry of a intreval in between a and b, precision is the number of decimals

double decoding(int a, int b, int precision, char *bitstring);


//generates the an n+1 array of floating point numbers representing intervals to be used with roulette selection
//a b and c represent the coeficients of a polinomial
//chromosomes an array of length n with the current generation of chromosomes

double* selection(int a, int b, int c, int n, double *chromosomes);

//crosses over two chromosomes of length lengh at the bit on the position position
//return a two element array pointing to the resulting chromosomes

char **crossover(int length, int position, char * chromosome1, char * chromosome2);


//flips position bits in a length size chromosome
//positions is an array of positions to be flipped

char * mutation(int length, int position, char *chromosome, int * positions);

#endif // ENCODING
