/* This is a multi-line comment
   Always comment as you write code*/

// Single line comment

// Provides you with printf() among other functions
// When the program is compiled the code between the brackets
// will be loaded here

#include <stdio.h> // For printf, scanf
#include <string.h> // For strcpy

// You define constants with define
// Tells the compiler to replace MYNAME with what is provided

#define MYNAME "Derek Banas"

// Every program must have a main function
// The main function is where the computer starts executing your code
// If you have any other functions that aren't called from main
// they will never execute

// This is a global variable that is available in every function
// in this program

int globalVar = 100;

int main()
{
	// Variables are boxes in memory that save important data
	// A variable name must start with a letter, but then can
	// contain numbers, letters or underscores

	// A char can hold any of 256 single characters
	// All characters are surrounded by apostrophes '
	// If you save a number as a char it can't be used for calculating

	char firstLetter = 'D';

	// An int can contain any whole number positive or negative
	// Between -32,768 and 32,767

	int age = 38;

	// Use a long int if you need to use a number larger or smaller
	// then is provided by an int

	long int superBigNum = -32767000;

	// A float is a number with a decimal positive or negative

	float piValue = 3.14159265359;


	// A double is used when you need a number bigger then float

	double reallyBigPi = 3.1415926535897932384626433832795028841971;

	printf("this is me");

	return 0;
}
// 	// Most all C function names contain no uppercase letters
// 	// printf() prints to screen the string inside of quotes
// 	// \n tells the screen to skip to the next line
// 	// Escape Sequences: \t - tab, \\ - backslash, \" - Quote
//
// 	printf("This will print to screen\n\n");
//
// 	// %d is a conversion character that inserts an int into your output
//
// 	printf("I am %d years old\n\n", age);
//
// 	// %ld is a conversion character for long ints
//
// 	printf("Big Number %ld\n\n", superBigNum);
//
// 	// %f is a conversion character for floats and doubles
// 	// You can define the number of decimal places as well
// 	// Size goes from -3.4 * 10^38 to 3.4 * 10^38
//
// 	printf("Pi = %.5f\n\n", piValue);
//
// 	// As you can see the computer representation of a float
// 	// is imprecise. If you need precision it is best to store
// 	// decimals as ints
//
// 	printf("Big Pi = %.20f\n\n", reallyBigPi);
//
// 	// %c is the conversion character for chars
//
// 	printf("The first letter of my name is %c\n\n", firstLetter);
//
// 	// %s is used for strings
//
// 	printf("My name is %s\n\n", "Derek");
//
// 	// To create a String you instead create char arrays
// 	// Every char array has a \0 String Terminator as the last
// 	// character, so always make your char arrays at least 1
// 	// character longer then you need
//
// 	char myName[12] = "Derek Banas";
//
// 	// You could also do this char myName[] = "Derek Banas";
//
// 	printf("My name is %s\n\n", myName);
//
// 	// You can't assign a new value to a char array
// 	// You would use strcpy for that
//
// 	strcpy(myName, "Bob Smith");
//
// 	printf("My name is %s\n\n", myName);
//
// 	// scanf() is used to get input from the user
// 	// You must use the & ampersand before the
// 	// variable unless you're using %s
//
// 	char middleInitial;
//
// 	printf("What is your middle initial? ");
//
// 	scanf(" %c", &middleInitial);
//
// 	// You can only except more then one value if you
// 	// define exactly what you expect to get
//
// 	char firstName[30], lastName[30];
//
// 	printf("What is your name? ");
//
// 	scanf(" %s %s", firstName, lastName);
//
// 	printf("Your name is %s %c %s\n\n", firstName, middleInitial, lastName);
//
//
//
// 	// You can also except a / if you know the user will enter it
//
// 	int month, day, year;
//
// 	printf("Whats your birth date? ");
//
// 	scanf(" %d/%d/%d", &month, &day, &year);
//
// 	printf("Birth Date %d/%d/%d\n\n", month, day, year);
//
// 	// C Programming Math
// 	// +, -, *, /, and sometimes % (% only with ints)
//
// 	int num1 = 12, num2 = 15, numAns;
//
// 	float decimal1 = 1.2, decimal2 = 1.5, decimalAns;
//
// 	printf("Integer Calculation %d\n\n", num2 / num1);
//
// 	printf("Float Calculation %f\n\n", decimal2 / decimal1);
//
// 	printf("Modulus %d\n\n", num2 % num1);
//
// 	// Use parentheses when needed
// 	// Order of Operations
// 	// Parentheses
// 	// - Negative Sign, ! Not, ++ Increment, -- Decrement
// 	// * Multiplication, / Division, % Modulus
// 	// + Addition, - Subtraction
// 	// Relational Operators : <, >, <=, >=
//
// 	printf("Without Parentheses %d\n\n", 3 + 6 * 10);
//
// 	printf("With Parentheses %d\n\n", (3 + 6) * 10);
//
// 	int randomNum = 1;
//
// 	// There are shortcut ways to perform calculations
// 	// +=, -=, *=, /=, %=, ++, --
//
// 	printf("1 += 2 : %d\n\n", randomNum, randomNum += 2);
//
// 	// We didn't do it this way because the addition takes
// 	// place first
//
// 	printf("%d += 2 : %d\n\n", randomNum, randomNum += 2);
//
// 	// ++ and -- work differently depending on where they are
//
// 	int exNum = 1;
//
// 	printf("++%d : %d\n\n", exNum, ++exNum);
//
// 	exNum = 1;
//
// 	printf("%d++ : %d\n\n", exNum, exNum++);
//
// 	// If you ever need to cast one data type to another
// 	// just put (dataType) before it to cast
//
// 	int numberEx = 12;
//
// 	float numberEx2 = 1.234;
//
// 	int numberEx3 = numberEx / numberEx2;
//
// 	printf("numberEx / numberEx2 : %f\n\n", (float) numberEx3);
//
// 	return 0;
// }
