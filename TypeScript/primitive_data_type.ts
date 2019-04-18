// boolean
let isDone: boolean = false;
//speically variable created by Boolean consstructor is Boolean Object
let createdByNewBoolean: Boolean = new Boolean(1);
// or 
let createdByBoolean: boolean = Boolean(1);

// number
let decLiteral : number = 6;
let hexLiteral: number = 0xf00d;
let binaryLiteral: number = 0b1010;  // will be compiled to decimal
let octalLiteral: number = 0o744; // will be compiled to decimal
let notANumber: number = NaN;
let infinityNumber: number = Infinity;


//string
let myName: string = 'Chris';

//void
function alertName():void{
    alert('My name is Chris');
}
let unusable: void  = undefined; // only can be undefined or null

// null and undefined
let u: undefined = undefined;
let n: null = null;

// void vs. null and undefined
// null and undefined are subtype of other type
// void is not.
let num: number = undefined;


