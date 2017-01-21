//Simple Linked List
class LinkedList{
    constructor(){
        this.value = null;
        this.next = null;
    }

    setNext(next_ptr){
        this.next = next_ptr;
    }

    getNext(){
        return this.next;
    }

    setValue(val){
        this.value = val;
    }

    getValue(){
        return this.value;
    }
}

class Stack{
    constructor(){
        this.top_item = null;
        this.length = 0;
    }
    push(val){
        var new_item = new LinkedList();
        new_item.setValue(val);
        if(this.length == 0){
            this.top_item = new_item;
        }
        else{
            new_item.next = this.top_item;
            this.top_item = new_item;
        }
        this.length++;        
    }
    pop(){
        if(this.length == 0){
            return null;
        }
        else{
            var ret_item = this.top_item;
            this.top_item = ret_item.next;
            this.length--;
            return ret_item.getValue();
        }
    }
    isEmpty(){
        return (this.length==0);
    }
}

class Point{
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
}

//My datastructure to know what points I visited
class VisitHashMap{
    constructor(){
        this.visited_points = {};
    }

    visit(point){
        this.visited_points[point.x + "," + point.y] = true;
    }

    visited(point){
        return (this.visited_points[point.x + "," + point.y] != undefined);
    }
}