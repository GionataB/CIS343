/*******************************************************************
 Main method to run the Game Of Life program.
 @author Gionata Bonazzi
 @author Marshal Brummel
 @version 29 January 2018
 *******************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include "game_utilities.h"

int main(int argc, char** argv){

    /**The status for the game to load a blank world**/
    unsigned int loadWorld = 0;

    /**The number of rows in the world**/
    unsigned int rows;

    /**The number of columns in the world**/
    unsigned int cols;

    /**the world as represented by arrays**/
    int** world;

    //Prompts the user for an input
    printf("Insert a number between 1-7 to select an initial world: ");
    char buffer[1024];
    fgets(buffer, 1024, stdin);

    //Scans in the user input
    sscanf(buffer, "%u", &loadWorld);

    //Populates the world per the user input
    world = fillWorld(loadWorld, &rows, &cols);

    /**The main will never stop the game.
     * The game can only be closed by inputting 'q' when prompted. **/
    while(1){

        //First prints the world
        printWorld(rows, cols, world);

        //Then asks what to do next. it can be: save, load, proceed, quit.
        world = pause(&rows, &cols, world);
    }
}
