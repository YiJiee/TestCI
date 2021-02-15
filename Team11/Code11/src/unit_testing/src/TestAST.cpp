
#include "TNode.h"

#include "catch.hpp"
#include <fstream>
#include <iostream>
using namespace std;

TEST_CASE("1st Test") {

    TNode T;
	
	myfile.open("../../../../tests/Sample_queries.txt");
	while (getline(myfile, myText)) {
		// Output the text from the file
		cout << myText << endl;
	}
	myfile.close();
	
    require(1 == 1);
}


