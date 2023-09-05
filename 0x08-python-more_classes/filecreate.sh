#!/bin/bash
echo "file >"
read file
touch $file
echo "#include <stdio.h>" > $file
echo "/**
* main - Entry point
*
* Description: A program 
*
* Return: 0(success)
*/

int main(void)
{
	return (0);		
}" >> $file
chmod 764 $file
bash dirgit.sh
gedit $file
