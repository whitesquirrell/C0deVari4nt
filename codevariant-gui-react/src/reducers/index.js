
const initialState = {
    activeNode: null
}

export default function rootReducer(state = initialState, action){
    switch (action.type){
        case "SELECT_NODE":
            return{
                ...state,
                activeNode: action.payload
            }
        default:
            return state
    }
}