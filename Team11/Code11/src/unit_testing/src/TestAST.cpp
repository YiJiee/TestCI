
#include "TNode.h"

#include "catch.hpp"
#include <fstream>
#include <iostream>
using namespace std;

TEST_CASE("1st Test") {

    TNode T;
    string myText;

	ifstream myfile;
	myfile.open("../../../../tests/prototype_sample_SIMPLE_source.txt");
	while (getline(myfile, myText)) {
		// Output the text from the file
		cout << myText << endl;
	}
	myfile.close();
	
    REQUIRE(1 == 1);
}


