/*******************************************************************
 This header declares functions to save and load a file.
 @author Gionata Bonazzi
 @author Marshal Brummel
 @version 10 February 2018
 *******************************************************************/

#ifndef GAMEOFLIFE_GAME_UTILITIES_H
#define GAMEOFLIFE_GAME_UTILITIES_H


/*******************************************************************
A support function that creates the memory allocation for the array
 of integers and returns it as the world.
@param buffer a pointer to an array of information about the world
@param rowNum number of rows in the world
@param colNum number of columns in the world.
@return a pointer to a pointer containing the world
*******************************************************************/
int** makeWorld(char* buffer, unsigned int* rowNum, unsigned int* colNum);

/*******************************************************************
Takes a size of and a premade world and creates a copy.
@param rowNum number of rows in the world
@param colNum number of columns in the world.
@param world a double pointer containing the world information
@return a double pointer to the world information
*******************************************************************/
int** copyWorld(unsigned int rowNum, unsigned int colNum, int** world);

/*******************************************************************
Loads a board from a number of presets.
@param state an int that indicates what file to be loaded
@param rowNum number of rows in the world
@param colNum number of columns in the world.
@return the result of the function makeWorld given the file information
*******************************************************************/
int** fillWorld(unsigned int state, unsigned int* rowNum, unsigned int* colNum);

/*******************************************************************
Prints the board to the screen
@param rowNum number of rows in the world
@param colNum number of columns in the world.
@param world a double pointer that points to the board
*******************************************************************/
void printWorld(unsigned int rowNum, unsigned int colNum, int** world);

/*******************************************************************
Determines the state of each cell.
@param interations unused at the moment
@param rowNum number of rows in the world
@param colNum number of columns in the world.
@param world a double pointer that points to the board
*******************************************************************/
void forward(unsigned int iterations, unsigned int rowNum, unsigned int colNum, int** world);


/*******************************************************************
Creates a string with all the world information in it.
@param bufferSize the size of the array plus two for the size of r+c
@param rowNum number of rows in the world
@param colNum number of columns in the world.
@param world a double pointer that points to the board
*******************************************************************/
char* worldToString(int* bufferSize, unsigned int rowNum, unsigned int colNum, int** world);


/*******************************************************************
A method that stops the game engine and prompts the user
 for instructions for how to continue
@param rowNum number of rows in the world
@param colNum number of columns in the world.
@param world a double pointer that points to the board
*******************************************************************/
int** pause(unsigned int* rowNum, unsigned int* colNum, int** world);


#endif //GAMEOFLIFE_GAME_UTILITIES_H
