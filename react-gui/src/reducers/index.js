
const initialState = {
    network: null,
    visNodes: null,
    initialNodeOptions: null,
    activeNode: null,
    backendUrl: "http://localhost:8000",
    visData: null
}

export default function rootReducer(state = initialState, action){
    switch (action.type){
        case "SET_DATA":
            return{
                ...state,   
                visData: action.payload
            }
        case "INIT_NETWORK":
            return{
                ...state,   
                network: action.payload
            }
        case "NODES_DATASET":
            return{
                ...state,
                visNodes: action.payload
            }
        case "INIT_NODE_OPTIONS":
            return{
                ...state,
                initialNodeOptions: action.payload
            }
        case "SELECT_NODE":
            return{
                ...state,
                activeNode: action.payload
            }
        default:
            return state
    }
}