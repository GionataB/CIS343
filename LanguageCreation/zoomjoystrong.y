%{
	#include <stdio.h>
	#include "zoomjoystrong.h"
	void yyerror(const char* msg);
	int yylex();
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
%token <d> FLOAT
%token HELP

%%

statement_list:	statement
	            |	statement statement_list
;

statement: modifier
				 | helper
;

helper: help_modifier
			| help_point
			| help_line
			| help_circle
			| help_rectangle
			| help_set_color
			| help_end
;

modifier:	point
        | line
				|	circle
			 	|	rectangle
			 	|	set_color
			 	|	end
;

help_modifier: HELP END_STATEMENT
						 	 {printf("List of commands:\npoint line circle rectangle set_color\nType the name of the command to learn more on how to use them.\n");}
;

point: POINT INT INT END_STATEMENT
			 {point( $2, $3 );}
;

help_point: POINT END_STATEMENT
						{printf("To draw a point, use the syntax: point x y;\n");}
;


line: LINE INT INT INT INT END_STATEMENT
			{line( $2, $3, $4, $5 );}
;

help_line: LINE END_STATEMENT
				 	 {printf("To draw a line, use the syntax: line x1 y1 x2 y2;\n");}
;

circle: CIRCLE INT INT INT END_STATEMENT
				{circle( $2, $3, $4 );}
;

help_circle: CIRCLE END_STATEMENT
				 	 	 {printf("To draw an empty circle, use the syntax: circle x y r;\n");}
;

rectangle: RECTANGLE INT INT INT INT END_STATEMENT
					 {rectangle( $2, $3, $4, $5 );}
;

help_rectangle: RECTANGLE END_STATEMENT
				 				{printf("To draw a rectangle, use the syntax: rectangle x y w h;\n");}
;

set_color: SET_COLOR INT INT INT END_STATEMENT
					 {set_color( $2, $3, $4 );}
;


help_set_color: SET_COLOR END_STATEMENT
				 		 		{printf("To change the drawing color, use the syntax: set_color r g b;\n");}
;

end: END END_STATEMENT
		 {finish(); exit(1);}

help_end: END
	 		 		{printf("To exit the program, use the syntax: end;\n");}
;

%%

int main(int argc, char** argv){
	setup();
	printf("Welcome to Zoomjoystrong!\nType help for a list of commands.\nAuthor: Gionata Bonazzi\t Date: 3/4/2018\n");
	yyparse();
	return 0;
}

void yyerror(const char* msg){
	fprintf(stderr, "ERROR! %s\n", msg);
}
