/*******************************************************************
 Implementation of the functions declared in 'file_utilities.h'
 @author Gionata Bonazzi
 @author Marshal Brummel
 @version 7 February 2018
 *******************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include "file_utilities.h"

int file_size(FILE* file){
  fseek(file, 0L, SEEK_END); //go to the end of the file.
  int fsize = ftell(file); //get the size of the file.
  rewind(file); //go to the beginning of the file.
  return fsize; //return the size of the file.
}

int write_file( char* filename, char* buffer, int size){
  FILE* save = fopen(filename, "w");
  for( int i = 0; i < size; i++){ //copies all the elements in buffer inside the file.
    fprintf(save, "%c", buffer[i]);
  }
  int fsize = file_size(save);
  fclose(save); //finally, close the file.
  return fsize;
}

int read_file(char* filename, char** buffer){
  FILE* load = fopen(filename, "r");
  int fsize = file_size(load); //get the size of the file first to allocate an appropriate amount of heap memory.
  *buffer = (char*)malloc(fsize * sizeof(char)); //reserve as much heap memory as the size of the file opened.
  char ch; //the scanned character.
  int pos = 0; //the position where to save the scanned character.
  while(fscanf(load, "%c", &ch) != EOF)
  {
    *(*buffer + pos) = ch; //this is a call to the array the pointer is pointing to.
    pos++;
  }
  *(*buffer + pos) = '\0';
  fclose(load); //finally, close the file.
  return fsize; //return the size of the loaded file.
}
