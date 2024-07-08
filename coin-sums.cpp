int pennies = 0;
while(cents > 0) {
    if (cents >= 25) {
        quarters++;
        cents -= 25;
    } else if (cents >= 10) {
        dimes++;
        cents -= 10;
    } else if (cents >= 5) {
        nickles++;
        cents -= 5;
    } else {
        pennies += cents;
        break;
    }
}

cout << quarters << endl;  
cout << nickles << endl;   
cout << dimes << endl;      
cout << pennies << endl;