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

%%

statement_list:	statement
	            |	statement statement_list
;

statement:	point
         |  line
				 |	circle
				 |	rectangle
				 |	set_color
				 |	end
;

point: POINT INT INT END_STATEMENT
			 {point( $2, $3 );}
;

line: LINE INT INT INT INT END_STATEMENT
			{line( $2, $3, $4, $5 );}
;

circle: CIRCLE INT INT INT END_STATEMENT
				{circle( $2, $3, $4 );}
;

rectangle: RECTANGLE INT INT INT INT END_STATEMENT
					 {rectangle( $2, $3, $4, $5 );}
;

set_color: SET_COLOR INT INT INT END_STATEMENT
					 {set_color( $2, $3, $4 );}
;

end: END
		 {finish();}
;

%%

int main(int argc, char** argv){
	setup();
	yyparse();
	return 0;
}

void yyerror(const char* msg){
	fprintf(stderr, "ERROR! %s\n", msg);
}
