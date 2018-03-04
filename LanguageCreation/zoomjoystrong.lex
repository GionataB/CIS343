%{
	#include <stdio.h>
	#include "zoomjoystrong.tab.h"
%}

%option noyywrap

%%

(end) 					{return END;}
;								{return END_STATEMENT;}
(help)					{return HELP;}
(point) 				{return POINT;}
(line) 					{return LINE;}
(circle) 				{return CIRCLE;}
(rectangle) 		{return RECTANGLE;}
(set_color) 		{return SET_COLOR;}
[0-9]+ 					{yylval.i = atoi(yytext); return INT;}
[0-9]+\.[0-9]+ 	{yylval.d = atof(yytext); return FLOAT;}
[ \t\n]   			;
[\./,]+ 				{printf("Command Unknown\n");}
[.]+						{printf("TEST");}

%%
