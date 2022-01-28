import './css/App.css';
import React from 'react';

// import components
import Graph from './components/graph/Graph';
import HUD from './components/hud/Hud';

function App() {

  return (
    <div className="App">
      <Graph/>
      <HUD/>
    </div>
  );
}

export default App;
