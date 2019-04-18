// boolean
var isDone = false;
//speically variable created by Boolean consstructor is Boolean Object
var createdByNewBoolean = new Boolean(1);
// or 
var createdByBoolean = Boolean(1);
// number
var decLiteral = 6;
var hexLiteral = 0xf00d;
var binaryLiteral = 10; // will be compiled to decimal
var octalLiteral = 484; // will be compiled to decimal
var notANumber = NaN;
var infinityNumber = Infinity;
//string
var myName = 'Chris';
//void
function alertName() {
    alert('My name is Chris');
}
var unusable = undefined; // only can be undefined or null
// null and undefined
var u = undefined;
var n = null;
// void vs. null and undefined
// null and undefined are subtype of other type
// void is not.
var num = undefined;
