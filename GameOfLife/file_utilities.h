/*******************************************************************
 This header declares functions to save and load a file.
 @author Gionata Bonazzi
 @author Marshal Brummel
 @version 29 January 2018
 *******************************************************************/

#ifndef file_utilities_h
#define file_utilities_h

/*******************************************************************
Returns the size in bytes of a file.
@param file the file to get the size
@return the size of the file (in bytes).
*******************************************************************/
int file_size(FILE* file);

/*******************************************************************
 Creates a file at the address 'filename'
 and copies the content of 'buffer' in it.
 @param filename the address of the file to open or create.
 @param buffer a string containing the information to save.
 @param size the size of buffer.
 @return the size of the file created.
 *******************************************************************/
int write_file( char* filename, char* buffer, int size);//size is the size for the buffer array.

/*******************************************************************
 Opens the 'filename' file and copies its content
 to the char* 'buffer' is pointing to.
 @param filename the address of the file to open.
 @param buffer the pointer to a string used to save filename's content.
 @return the size of the file loaded in.
 *******************************************************************/
int read_file( char* filename, char** buffer );

#endif /* file_utilities_h */
