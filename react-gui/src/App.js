import './css/App.css';
import React from 'react';

// import components
import Graph from './components/graph/Graph';
import NodeProps from './components/hud/NodeProps';
import CodeQLOptions from './components/hud/CodeQLOptions';

function App() {

  return (
    <div className="App">
      <Graph/>
      <NodeProps/>
      <CodeQLOptions/>
    </div>
  );
}

export default App;
