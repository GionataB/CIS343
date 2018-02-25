%{
	#include <stdio.h>
%}

%%
	(close) {return END}
	\; 	{return END_STATEMENT}
%%
