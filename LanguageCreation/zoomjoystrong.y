%{
	#include <stdio.h>
	#include <string.h>
	#include "zoomjoystrong.h"
	void yyerror(const char* msg);
	int yylex();
	int checkBoundaries(int abscissa, int ordinate);
%}

%error-verbose
%start statement_list

%union { int i; double d; }

%token END
%token END_STATEMENT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token <i> INT
%token <d> FLOAT //Not used.
%token HELP //Token to ask for a list of instructions.
%token UNKNOWNWORD
%token UNKNOWNSYMBOL //Keep words and symbols separate to improve: 1. readability 2. Error's communication.

%%

statement_list:	statement end
              |	statement statement_list
;

statement: command
         | helper
;

helper: help_command
      | help_point
      | help_line
      | help_circle
      | help_rectangle
      | help_set_color
;

command: point
       | line
       | circle
       | rectangle
       | set_color
       | end
;

help_command: HELP END_STATEMENT
              {printf("List of commands:\npoint line circle rectangle set_color\nType the name of the command to learn more on how to use them.\n To close the program, type \"end;\"\n");}
;

point: POINT INT INT END_STATEMENT
	     {int stop = checkBoundaries($2, $3);
	      if(stop == 0)
	       point( $2, $3 );
	     }
;

help_point: POINT END_STATEMENT
            {printf("To draw a point, use the syntax: point x y;\nThe x value has to be between 0 and %d, the y value between 0 and %d\n", WIDTH, HEIGHT);}
;

line: LINE INT INT INT INT END_STATEMENT
      {int firstCheck = checkBoundaries($2, $3);
	     if(firstCheck != 0)
		     printf("Please check the values for the first point.\n");
	     int secondCheck = checkBoundaries($4, $5);
	     if(secondCheck != 0)
		     printf("Please check the values for the second point.\n");
	     if(firstCheck + secondCheck == 0) //Used two checks to give a more specific error message.
		     line( $2, $3, $4, $5 );
      }
;

help_line: LINE END_STATEMENT
		       {printf("To draw a line, use the syntax: line x1 y1 x2 y2;\nThe x1 and x2 values have to be between 0 and %d, the y1 and y2 values between 0 and %d\n", WIDTH, HEIGHT);}
;

circle: CIRCLE INT INT INT END_STATEMENT
	      {int stop = checkBoundaries($2, $3);
	       if($2 + $4 > WIDTH){ //Part of the circle will be drawn outside the window
		       printf("The circle will go outside the window.\nPlease, change the abscissa of the center, move the center, or change the radius.\n");
		       stop = 1;
		     }
	       if($3 + $4 > HEIGHT){ //Part of the circle will be drawn outside the window
		       printf("The circle will go outside the window.\nPlease, change the ordinate of the center, move the center, or change the radius.\n");
		       stop = 1;
		     }
	       if(stop == 0)
		       circle( $2, $3, $4 );
	      }
;

help_circle: CIRCLE END_STATEMENT
		         {printf("To draw an empty circle, use the syntax: circle x y r;\nMake sure that the center is in a position that won't let the circle be drawn outside the window.\n");}
;

rectangle: RECTANGLE INT INT INT INT END_STATEMENT
           {int stop = checkBoundaries($2, $3); //Check that the initial point is in the window
		        if($2 + $4 > WIDTH){ //Part of the rectangle will be drawn outside the window
			printf("The rectangle is too wide.\n Please change the starting point or the width.\n");
			stop = 1;
			}
		 if($3 + $5 > HEIGHT){ //Part of the rectangle will be drawn outside the window
			printf("The rectangle is too tall.\n Please change the starting point or the height.\n");
			stop = 1;
			}
		 if(stop == 0)
		  	rectangle( $2, $3, $4, $5 );
		}
;

help_rectangle: RECTANGLE END_STATEMENT
		{printf("To draw a rectangle, use the syntax: rectangle x y w h;\nMake sure that there is enough space for the rectangle to not be drawn outside the window.\n");}
;

set_color: 	SET_COLOR INT INT INT END_STATEMENT
	 	{int stop = 0;
		 if($2 > 255){
			printf("The red value is too high.\n");
			stop = 1;
			}
		 if($3 > 255){
		 	printf("The green value is too high.\n");
			stop = 1;
			}
		 if($4 > 255){
			printf("The blue value is too high.\n");
			stop = 1;
			}
		 if(stop == 0) //Checks that the colors are between 0 and 255
		 	set_color( $2, $3, $4 );
		 else
			printf("Acceptable values for each color are between 0 and 255 (inclusive)\n");
		}
;

help_set_color: SET_COLOR END_STATEMENT
 		{printf("To change the drawing color, use the syntax: set_color r g b;\nEach color's value has to be between 0 and 255\n");}
;

end: 	END END_STATEMENT
	{finish(); exit(1);}

%%

/*******************************************************************************
* The main method. It invokes the setup() function to create the drawing window,
* a welcome message, and starts the parser.
* @param argc the size of argv
* @param argv array of strings passed from the command line.
* @return 0 if the program ends succesfully.
*******************************************************************************/
int main(int argc, char** argv){
	setup();
	printf("Welcome to Zoomjoystrong!\nType \"help;\" for a list of commands.\nAuthor: Gionata Bonazzi\t Date: 3/7/2018\n");
	yyparse();
	return 0;
}

/*******************************************************************************
* The method checks if the point defined by the coordinates (abscissa, ordinate)
* is inside the window or not.
* @param abscissa the x-coordinate of the point
* @param ordinate the y-coordinate of the point
* @return 0 if the point is inside the window, 1 otherwise.
*******************************************************************************/
int checkBoundaries(int abscissa, int ordinate){
	int result = 0;
	if(abscissa < 0 || abscissa > WIDTH){ //the x value is outside the window
		printf("The point's abscissa has to be between 0 and %d\n", WIDTH);
		result = 1;
		}
	if(ordinate < 0 || ordinate > HEIGHT){ //the y value is outside the window
		printf("The point's ordinate has to be between 0 and %d\n", HEIGHT);
		result = 1;
		}
	return result;
}

/*******************************************************************************
* The method prints an error message in case there are unexpected tokens.
* Simply put, if the statement is not a valid statement, the function
* will print what token is wrong, and will restart parsing without closing
* the program.
* @param msg the error message returned by the parser.
*******************************************************************************/
void yyerror(const char* msg){
	fprintf(stderr, "ERROR! %s\n", msg);
	yyparse(); //Prevent the program from crashing after a syntax error.
}
