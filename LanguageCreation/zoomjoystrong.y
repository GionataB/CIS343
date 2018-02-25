%{
	#include <stdio.h>
	void yyerror(const char* msg);
	int yylex();
	int num_contacts = 0;
%}

%error-verbose
%start statement_list

%union {int i, char* str, double d};

%token END
%token END_STATEMENT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token INT
%token FLOAT
%token SPACE
%token UNDEFINED

%%

statement_list:	statement
	            |	statement statement_list

statement:    instruction
         |    instruction END_STATEMENT

instruction:
;


%%
