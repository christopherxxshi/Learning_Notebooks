interface Person{
    name: string;
    age: number;
}

// the shape of variable has to be same as the interface
let chris: Person = {
    name: 'Chirs',
    age: 25
}

interface Person2{
    name: string;
    age: number;
    birthday?: string; // optional property
}

let tom: Person2 = {
    name: 'Tom',
    age: 26
}

// property with any type
interface Person3 {
    name: string;
    age?: number;
    [propName: string]: any;
}

let tom3: Person3 = {
    name: 'Tom',
    gender: 'male'
};
// use readonlu key word

interface Person4 {
    readonly id: number;
    name: string;
    age?: number;
    [propName: string]: any;
}

let tom4: Person4 = {
    id: 89757,
    name: 'Tom',
    gender: 'male'
};
// wrong: readonly property cannot be changed 
//tom4.id = 9527;