/*******************************************************************
 Implementation of the functions declared in 'game_utilities.h'
 @author Gionata Bonazzi
 @author Marshal Brummel
 @version 29 January 2018
 *******************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "file_utilities.h"
#include "game_utilities.h"

//Takes a string and makes a matrix from it.
int** makeWorld(char* buffer, unsigned int* rowNum, unsigned int* colNum){

    //buffer[0] is the number of rows.
    *rowNum = (int) (buffer[0] - '0');

    //buffer[1] is the number of columns.
    *colNum = (int) (buffer[1] - '0');

    int scan = 2;
    int** world = (int**) malloc (*rowNum * sizeof(int*));

    for(int i = 0; i < *rowNum; i++)
        world[i] = (int*) malloc (*colNum * sizeof(int));

    for(int i = 0; i < *rowNum; i++){
        for(int j = 0; j < *colNum; j++){

        /**Explicit casting from char to int, to improve code's readability.
         World is equal to the relative position of the char from the ascii value of the char 0 (zero).
         Currently the ascii value of 0 is 48, the value of 9 is 57; **/

        //The 2 accounts for the first 2 positions in buffer, rowNum and colNum.
        world[i][j] = (int) (buffer[scan] - '0');
        scan++;
      }
    }

    //The memory space was allocated in the read_file() function.
    free(buffer);

    return world;
}

//Copies the contents of a matrix in a new matrix, with different memory addresses.
int** copyWorld(unsigned int rowNum, unsigned int colNum, int** world){

    //Creates an array with the size of the world
    int** copy = (int**) malloc(rowNum * sizeof(int*));

    //Adds the "2d" part to the array
    for(int i = 0; i < rowNum; i++)
        copy[i] = (int*) malloc (colNum * sizeof(int));

    //Copies in each element of the array
    for(int i = 0; i < rowNum; i++){
        for(int j = 0; j < colNum; j++)
            copy[i][j] = world[i][j];
    }

    return copy;
}

//takes an initial state and load the appropriate file.
//The code supports three states for each cell in the matrix: live cell, dead cell, empty space.
//However, especially to show the blinkers, the seven preloaded files do not have any empty space.
int** fillWorld(unsigned int state, unsigned int* rowNum, unsigned int* colNum){
    char* world_buffer;
    char* name = (char*) malloc(50 * sizeof(char));

    //No case 0. 7 cases total + a default one.
    switch(state){
        //call the load method with different file names, one for each case.
        case 1: strcpy(name, "Default saves/One_block.txt");
                break;
        case 2: strcpy(name, "Default saves/Two_boat.txt");
                break;
        case 3: strcpy(name, "Default saves/Three_loaf.txt");
                break;
        case 4: strcpy(name, "Default saves/Four_beehive.txt");
                break;
        case 5: strcpy(name, "Default saves/Five_blinker.txt");
                break;
        case 6: strcpy(name, "Default saves/Six_beacon.txt");
                break;
        case 7: strcpy(name, "Default saves/Seven_toad.txt");
                break;
        default: printf("File does not exist\n");
                 printf("Possible values are between 1 and 7.\n");
                 free(name);
                 exit(1);
    }

    read_file(name, &world_buffer);
    free(name);

    return makeWorld(world_buffer, rowNum, colNum);
}

void printWorld(unsigned int rowNum, unsigned int colNum, int** world){
    char ch = 'E';
    for(int i = 0; i < rowNum; i++){
    printf("\t| ");
        for(int j = 0; j < colNum; j++){

            //If an 'E' gets printed, it's a sign that something is not working.
            ch = 'E';

            //A live cell is represented by 'o'
            if(world[i][j] == 1) ch = 'o';

            //A dead cell is represented by 'x'
            if(world[i][j] == 2) ch = 'x';

            //An empty space is represented by '~'
            if(world[i][j] == 3) ch = '~';

            printf(" %c |", ch);
        }
        printf("\n");
    }
    printf("\n");
}

//Applies the game's rules.
//States: 1 = alive, 2 = dead, 3 = empty
void forward(unsigned int iterations, unsigned int rowNum, unsigned int colNum, int** world){
    while(iterations > 0){

        int neighbors = 0;
        int** copy = copyWorld(rowNum, colNum, world);

        //Since the world is a matrix, a single cell can have at most 8 neighbors, or 8 if cases.
        for(int i = 0; i < rowNum; i++){
            for(int j = 0; j < colNum; j++){

                neighbors = 0;

                // The cell in the matrix is empty
                if(copy[i][j] == 3) continue;

                if(i - 1 >= 0 && j - 1 >= 0){

                    //Top left cell
                    if(copy[i-1][j-1] == 1) neighbors++;
                }
                if(i - 1 >= 0){

                    //Top mid cell
                    if(copy[i-1][j] == 1) neighbors++;
                }
                if(i - 1 >= 0 && j + 1 < colNum){

                    //Top right cell
                    if(copy[i-1][j+1] == 1) neighbors++;
                }
                if(j - 1 >= 0){

                    //Mid left cell
                    if(copy[i][j-1] == 1) neighbors++;
                }
                if(j + 1 < colNum){

                    //Mid right cell
                    if(copy[i][j+1] == 1) neighbors++;
                }
                if(i + 1 < rowNum && j - 1 >= 0){

                    //Bottom left cell
                    if(copy[i+1][j-1] == 1) neighbors++;
                }
                if(i + 1 < rowNum){

                    //Bottom mid cell
                    if(copy[i+1][j] == 1) neighbors++;
                }
                if(i + 1 < rowNum && j + 1 < colNum){

                    //Bottom right cell
                    if(copy[i+1][j+1] == 1) neighbors++;
                }

                //Now that all the neighbors have been checked, decide if the cell lives or dies.
                if(copy[i][j] == 1){

                    //The cell dies if it has less than 2 or more than 3 neighboring cells.
                    if(neighbors < 2 || neighbors > 3) world[i][j] = 2;
                }
                else if( copy[i][j] == 2 && neighbors == 3) world[i][j] = 1;
            }
        }
        free(copy);
        iterations--;
    }
}

char* worldToString(int* bufferSize, unsigned int rowNum, unsigned int colNum, int** world){

    *bufferSize = rowNum * colNum + 2;

    //accounts for the two dimensions, every entry in the matrix. It won't have a '\0' at the end.
    char* buffer = (char*) malloc(*bufferSize * sizeof(char));
    int pos = 2;
    buffer[0] = (char) ('0' + rowNum);
    buffer[1] = (char) ('0' + colNum);
    for(int i = 0; i < rowNum; i++){
        for(int j = 0; j < colNum; j++){
            buffer[pos] = (char) ('0' + world[i][j]);
            pos++;
        }
    }
    return buffer;
}

int** pause(unsigned int *rowNum, unsigned int *colNum, int** world){

    char* buffer = malloc(1024 * sizeof(char));

    //Used to save or load a file.
    char* filename;

    //used when saving or loading a file.
    char* world_buffer;
    char choice;

    //Used to tell how many generations the world has to go through.
    unsigned int gen = 0;

    //Prompts user for an input
    printf("Type (s) to save the current game, (l) to load another game, (c) to continue the game or (q) to quit.\n");

    //Scans input
    fgets(buffer, 1024, stdin);
    sscanf(buffer, "%c", &choice);

    //Reallocate the memory, to clean the buffer.
    buffer = (char*) realloc(buffer, 1024*sizeof(char));
    choice = tolower(choice);
    switch(choice){

        //The file's name will be at maximum 16 characters long.

        case 's':   filename = (char*) malloc(17 * sizeof(char));
                    printf("File name: ");
                    fgets(buffer, 1024, stdin);

                    //Fill only 16 chars in name, the 17th is the '\0' character.
                    sscanf(buffer, "%16s", filename);
                    int bSize;

                    //Prints the world and writes to file
                    world_buffer = worldToString(&bSize, *rowNum, *colNum, world);
                    write_file(filename, world_buffer, bSize);

                    //Frees un-needed memory.
                    free(world_buffer);
                    free(filename);
                    free(buffer);
                    break;
        case 'l':   filename = (char*) malloc(17 * sizeof(char));
                    printf("File name: ");
                    fgets(buffer, 1024, stdin);

                    //Fill only 16 chars in name, the 17th is the '\0' character.
                    sscanf(buffer, "%16s", filename);

                    read_file(filename, &world_buffer);

                    //Frees un-needed memory.
                    free(filename);
                    free(buffer);
                    free(world);

                    //Begin from a clean state.
                    world = makeWorld(world_buffer, rowNum, colNum);
                    break;
        case 'c':   while(gen < 1){
                        printf("How many generations?\n");
                        fgets(buffer, 1024, stdin);
                        sscanf(buffer, "%u", &gen);
                        free(buffer);
                        if(gen < 1){
                            printf("Please insert a positive integer\n");
                            buffer = malloc(1024 * sizeof(char));
                        }
                        else{
                            forward(gen, *rowNum, *colNum, world);
                        }
                    }
                    break;
        case 'q':   printf("The game will close without saving, are you sure? (y/n)\n");
                    fgets(buffer, 1024, stdin);
                    char ch;
                    sscanf(buffer, "%c", &ch);

                    //Free the buffer
                    free(buffer);

                    if(ch == 'y')
                    {
                      //Free the game world.
                      free(world);
                      exit(1);
                    }
                    //This way if it is neither y or n it will go to the default block giving a 'Command Unknown' message.
                    else if(ch == 'n') break;
        default:    printf("Command Unknown\n");
    }
    //Return the address of the world, used in case an user loads a file. if a file is not loaded, it simply returns the same address of the already existing world
    return world;
}
