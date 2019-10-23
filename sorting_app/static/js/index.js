function populateList(list){
    element_block_code = (value='') => { return '<div id="element">' + value + '</div>'};
    
    // contains the code to populate list
    code = '';

    for(var i=0;i < LIST_LENGTH;i++){
        if(i < list.length){
            console.log(list[i].toString())
            code += element_block_code(list[i].toString())
        
        }else{
            code += element_block_code();

        }
    }

    LIST_ELEMENT.innerHTML = code;

}

function upload(){
    list_str = INPUT_LIST_ELEMENT.value;

    // convert list string to list
    num_list = list_str.split(' ').slice(0,10);

    //slice the list before sending to the backend


    // sets the hidden field
    HIDDEN_INPUT_ELEMENT.value = list_str;

    // converts list string to list
    list = list_str.split(' ');

    // populates the grid
    populateList(num_list);
}

const LIST_LENGTH = 10;
const LIST_ELEMENT = document.getElementById('list');
const INPUT_LIST_ELEMENT = document.getElementById('input_list');
const HIDDEN_INPUT_ELEMENT = document.getElementById('hidden_list');

populateList([])