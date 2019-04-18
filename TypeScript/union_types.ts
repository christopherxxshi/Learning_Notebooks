let myFavoriteNumber: string | number;
myFavoriteNumber = 'seven';
myFavoriteNumber = 7;

function getLength(something: string | number): string {
    // console.log(something.length); 
    // length is not common property of string and number
    return something.toString();
}

let myFavoriteNumber2: string | number;
myFavoriteNumber2 = 'seven';
console.log(myFavoriteNumber2.length); // 5
myFavoriteNumber2 = 7;
// wrong
// console.log(myFavoriteNumber.length); 
